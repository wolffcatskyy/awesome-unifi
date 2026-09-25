#!/usr/bin/env python3
"""Generate data.json for awesome-unifi from README.md.

Deterministic companion metadata: parses every list entry out of README.md,
enriches GitHub repo entries with stars / last push / license via the GitHub
API, and merges manual annotations from data/overrides.json (UniFi OS
compatibility, deployment mode, flags) that survive regeneration.

Usage:
    python3 scripts/generate_data.py [--readme README.md] [--out data.json]
                                     [--site-out site/data.json]
                                     [--overrides data/overrides.json]

GITHUB_TOKEN (optional) raises API rate limits; CI passes secrets.GITHUB_TOKEN.
No third-party dependencies.
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

ENTRY_RE = re.compile(r"^- \[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\) - (?P<desc>.*\S)\s*$")
HEADING_RE = re.compile(r"^(#{2,3})\s+(.*?)\s*$")
GH_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+?)(?:\.git)?/?$")

SCHEMA_VERSION = 1
UNIFI_OS_VERSIONS = ["3", "4", "5"]

# Deployment inference from the top-level category, marked source=inferred.
CATEGORY_DEPLOYMENT = {
    "API Libraries": "library",
    "Docker Images": "self-hosted",
    "Guides & Documentation": "docs",
    "Official Resources": "official",
    "MCP Servers": "library",
}


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s or "item"


def parse_readme(path):
    """Return (entries, categories) parsed from the awesome list README."""
    entries = []
    categories = []
    cat_stack = {}  # depth -> (title, id)
    in_contents = False
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.rstrip("\n")
            m = HEADING_RE.match(line)
            if m:
                depth = len(m.group(1))
                title = m.group(2).strip()
                in_contents = title.lower() == "contents"
                if in_contents:
                    continue
                if title.lower() in ("contributing", "footnotes"):
                    cat_stack = {}
                    continue
                cid = slugify(title)
                cat_stack = {d: v for d, v in cat_stack.items() if d < depth}
                cat_stack[depth] = (title, cid)
                path_titles = [cat_stack[d][0] for d in sorted(cat_stack)]
                path_ids = [cat_stack[d][1] for d in sorted(cat_stack)]
                categories.append({
                    "id": "/".join(path_ids),
                    "title": title,
                    "path": path_titles,
                })
                continue
            if in_contents or not cat_stack:
                continue
            m = ENTRY_RE.match(line.strip())
            if not m:
                continue
            name, url, desc = m.group("name").strip(), m.group("url").strip(), m.group("desc").strip()
            path_titles = [cat_stack[d][0] for d in sorted(cat_stack)]
            path_ids = [cat_stack[d][1] for d in sorted(cat_stack)]
            gh = GH_RE.match(url)
            entry = {
                "name": name,
                "url": url,
                "description": desc,
                "category": "/".join(path_ids),
                "github": None,
            }
            if gh and gh.group(1).lower() not in ("sindresorhus", "topics", "features", "settings"):
                entry["github"] = {"owner_repo": f"{gh.group(1)}/{gh.group(2)}"}
            entries.append(entry)
    return entries, categories


def assign_ids(entries):
    seen = {}
    for e in entries:
        base = e["github"]["owner_repo"].lower() if e["github"] else slugify(e["name"])
        n = seen.get(base, 0)
        seen[base] = n + 1
        e["id"] = base if n == 0 else f"{base}-{n}"


def batched(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


def fetch_repo_metadata(repos, token, sleep_s, batch_size=8):
    """Fetch stars/pushed_at/license/archived via the search API (batches repos).

    The search endpoint accepts several repo: qualifiers per query, which keeps
    us far under rate limits versus one request per repo.
    """
    meta = {}
    if not repos:
        return meta
    queries = []
    for chunk in batched(sorted(repos), batch_size):
        q = " ".join(f"repo:{r}" for r in chunk)
        queries.append((chunk, q))
    for idx, (chunk, q) in enumerate(queries):
        url = ("https://api.github.com/search/repositories?q="
               + urllib.parse.quote(q) + "&per_page=" + str(batch_size))
        req = urllib.request.Request(url, headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "awesome-unifi-data-generator",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        })
        for attempt in range(3):
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    payload = json.load(resp)
                break
            except urllib.error.HTTPError as exc:
                if exc.code in (403, 429) and attempt < 2:
                    reset = exc.headers.get("X-RateLimit-Reset")
                    wait = max(10, int(reset) - int(time.time()) + 2) if reset else 30 * (attempt + 1)
                    print(f"rate limited, waiting {wait}s", file=sys.stderr)
                    time.sleep(wait)
                    continue
                raise
        else:
            raise RuntimeError(f"search failed for {chunk}")
        for item in payload.get("items", []):
            meta[item["full_name"].lower()] = {
                "owner_repo": item["full_name"],
                "stars": item["stargazers_count"],
                "last_push": item["pushed_at"],
                "license": (item.get("license") or {}).get("spdx_id"),
                "archived": item["archived"],
                "language": item.get("language"),
            }
        missing = [r for r in chunk if r.lower() not in meta]
        for r in missing:
            time.sleep(1.0)
            meta[r.lower()] = fetch_single_repo(r, token)
        if idx < len(queries) - 1:
            time.sleep(sleep_s)
    return meta


def fetch_single_repo(repo, token):
    """Fallback for repos the search index misses (renamed repos redirect to
    their canonical name, which we record so stale README links surface)."""
    req = urllib.request.Request(f"https://api.github.com/repos/{repo}", headers={
        "Accept": "application/vnd.github+json",
        "User-Agent": "awesome-unifi-data-generator",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            item = json.load(resp)
    except urllib.error.HTTPError as exc:
        return {"owner_repo": repo, "stars": None, "last_push": None, "license": None,
                "archived": None, "language": None, "error": f"GitHub API {exc.code}"}
    out = {
        "owner_repo": item["full_name"],
        "stars": item["stargazers_count"],
        "last_push": item["pushed_at"],
        "license": (item.get("license") or {}).get("spdx_id"),
        "archived": item["archived"],
        "language": item.get("language"),
    }
    if item["full_name"].lower() != repo.lower():
        out["renamed_from"] = repo
    return out


def empty_unifi_os():
    return {"status": "unknown", "versions": [], "min": None, "max": None,
            "notes": None, "source": None, "verified_at": None}


def apply_annotations(entries, overrides):
    for e in entries:
        top_cat = e["category"].split("/")[0] if e["category"] else ""
        deployment = CATEGORY_DEPLOYMENT.get(top_cat, "unknown")
        dep_source = "inferred" if deployment != "unknown" else None
        unifi_os = empty_unifi_os()
        ov = overrides.get(e["id"]) or (overrides.get(e["github"]["owner_repo"].lower())
                                        if e["github"] else None)
        flags = []
        if ov:
            if "deployment" in ov:
                deployment, dep_source = ov["deployment"], "manual"
            uo = ov.get("unifi_os") or {}
            if uo:
                unifi_os.update({k: v for k, v in uo.items() if k in unifi_os})
                unifi_os["source"] = unifi_os.get("source") or "manual"
                bad = [v for v in unifi_os["versions"] if v not in UNIFI_OS_VERSIONS]
                if bad:
                    raise SystemExit(f"overrides: {e['id']} has unknown UniFi OS versions {bad}")
            flags = ov.get("flags", [])
        e["deployment"] = deployment
        e["deployment_source"] = dep_source
        e["unifi_os"] = unifi_os
        e["flags"] = flags


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--out", default="data.json")
    ap.add_argument("--site-out", default="site/data.json")
    ap.add_argument("--overrides", default="data/overrides.json")
    ap.add_argument("--max-repos", type=int, default=0, help="testing: cap GitHub API lookups")
    ap.add_argument("--cache", default="", help="optional metadata cache file (read/write)")
    args = ap.parse_args()

    entries, categories = parse_readme(args.readme)
    assign_ids(entries)

    repos = sorted({e["github"]["owner_repo"] for e in entries if e["github"]})
    if args.max_repos:
        repos = repos[:args.max_repos]
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    meta = {}
    if args.cache and os.path.exists(args.cache):
        with open(args.cache, encoding="utf-8") as fh:
            meta = json.load(fh)
    want = [r for r in repos if r.lower() not in meta]
    if want:
        meta.update(fetch_repo_metadata(want, token, sleep_s=2.0 if token else 6.5))
        if args.cache:
            with open(args.cache, "w", encoding="utf-8") as fh:
                json.dump(meta, fh)

    for e in entries:
        if e["github"]:
            m = meta.get(e["github"]["owner_repo"].lower())
            e["github"] = m or {**e["github"], "stars": None, "last_push": None,
                                "license": None, "archived": None, "language": None,
                                "error": "skipped by --max-repos"}

    overrides = {}
    if os.path.exists(args.overrides):
        with open(args.overrides, encoding="utf-8") as fh:
            overrides = json.load(fh).get("entries", {})
    apply_annotations(entries, overrides)

    cat_counts = {}
    for e in entries:
        cat_counts[e["category"]] = cat_counts.get(e["category"], 0) + 1
    for c in categories:
        c["entries"] = cat_counts.get(c["id"], 0)

    def slim(obj):
        if isinstance(obj, dict):
            return {k: slim(v) for k, v in obj.items()
                    if v is not None and v != [] and v != {} and k != "error"}
        return obj
    entries = [slim(e) for e in entries]

    doc = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": {"repository": "wolffcatskyy/awesome-unifi", "readme": "README.md", "ref": "main"},
        "unifi_os_versions": UNIFI_OS_VERSIONS,
        "stats": {
            "entries": len(entries),
            "github_repos": sum(1 for e in entries if e.get("github")),
            "categories": len([c for c in categories if c["entries"]]),
        },
        "categories": categories,
        "entries": entries,
    }
    for out in (args.out, args.site_out):
        if not out:
            continue
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        print(f"wrote {out}: {len(entries)} entries, {doc['stats']['github_repos']} GitHub repos")


if __name__ == "__main__":
    main()
