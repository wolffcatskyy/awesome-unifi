#!/usr/bin/env node
// Flags awesome-list entries whose GitHub repos are archived or stale (no
// commits in 2+ years) and moves them from README.md to archived.md.
// Runs weekly in CI; the workflow opens a PR with the result.

import { readFileSync, writeFileSync } from 'node:fs';

const TOKEN = process.env.GITHUB_TOKEN;
if (!TOKEN) {
  console.error('GITHUB_TOKEN is required');
  process.exit(1);
}

const STALE_YEARS = 2;
const cutoff = Date.now() - STALE_YEARS * 365.25 * 24 * 60 * 60 * 1000;

const readme = readFileSync('README.md', 'utf8').split('\n');
const entryRe = /^(- \[[^\]]+\]\(https:\/\/github\.com\/([A-Za-z0-9_.-]+)\/([A-Za-z0-9_.-]+?)\) - .*)$/;

async function repoInfo(owner, repo) {
  const res = await fetch(`https://api.github.com/repos/${owner}/${repo}`, {
    headers: {
      Authorization: `Bearer ${TOKEN}`,
      Accept: 'application/vnd.github+json',
      'User-Agent': 'awesome-unifi-stale-check',
    },
  });
  if (res.status === 404) return { missing: true };
  if (!res.ok) throw new Error(`GitHub API ${res.status} for ${owner}/${repo}`);
  const data = await res.json();
  return { archived: data.archived, pushedAt: data.pushed_at };
}

// Collect entries with their section.
const entries = []; // {lineIndex, owner, repo, line, section}
let section = 'Uncategorized';
readme.forEach((line, i) => {
  const h = line.match(/^## (.+)/);
  if (h && h[1] !== 'Contents') section = h[1];
  const m = line.match(entryRe);
  if (m) entries.push({ lineIndex: i, owner: m[2], repo: m[3], line: m[1], section });
});

console.log(`Checking ${entries.length} GitHub entries...`);
const flagged = []; // {...entry, reason}
for (const e of entries) {
  let info;
  try {
    info = await repoInfo(e.owner, e.repo);
  } catch (err) {
    console.warn(`skipping ${e.owner}/${e.repo}: ${err.message}`);
    continue;
  }
  if (info.missing) {
    flagged.push({ ...e, reason: 'Repository no longer available.' });
  } else if (info.archived) {
    flagged.push({ ...e, reason: 'Archived by maintainer.' });
  } else if (info.pushedAt && Date.parse(info.pushedAt) < cutoff) {
    const month = info.pushedAt.slice(0, 7);
    flagged.push({ ...e, reason: `No commits since ${month}.` });
  }
}

if (flagged.length === 0) {
  console.log('Nothing flagged. README and archived.md unchanged.');
  process.exit(0);
}

// Remove flagged lines from README (bottom-up to keep indices valid).
const flaggedIdx = new Set(flagged.map((f) => f.lineIndex));
const newReadme = readme.filter((_, i) => !flaggedIdx.has(i));
writeFileSync('README.md', newReadme.join('\n'));

// Append flagged entries to archived.md under matching sections.
const archived = readFileSync('archived.md', 'utf8').split('\n');
for (const f of flagged) {
  const newLine = `${f.line} ${f.reason}`;
  const header = `## ${f.section}`;
  let hi = archived.findIndex((l) => l.trim() === header);
  if (hi === -1) {
    archived.push('', header, '');
    hi = archived.length - 2;
  }
  // Insert after the last entry line of that section.
  let insert = hi + 1;
  while (insert < archived.length && (archived[insert].startsWith('- ') || archived[insert].trim() === '')) {
    if (archived[insert].trim() === '' && archived[insert + 1]?.startsWith('## ')) break;
    insert++;
  }
  archived.splice(insert, 0, newLine);
  console.log(`flagged: ${f.owner}/${f.repo} (${f.reason})`);
}
writeFileSync('archived.md', archived.join('\n'));
console.log(`Moved ${flagged.length} entries to archived.md.`);
