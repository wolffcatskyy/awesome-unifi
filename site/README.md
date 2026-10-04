# Awesome UniFi companion site

Static, dependency-free HTML/CSS/JS that renders the list from `data.json`
(same dark theme stack as wolffcatskyy.dev - plain static files, no build step).

## Local preview

```bash
python3 -m http.server 8000 --directory site
# open http://localhost:8000
```

`app.js` loads `./data.json` first and falls back to the canonical
`data.json` on `main` via raw.githubusercontent.com.

## Deploy

Option A - GitHub Pages (preview): repo Settings > Pages > deploy from branch
`main`, folder `/site`. The site appears at
`https://wolffcatskyy.github.io/awesome-unifi/`.

Option B - unifi.wolffcatskyy.dev (production): wolffcatskyy.dev is hosted on
Cloudflare as static files, so either
1. set the Pages custom domain to `unifi.wolffcatskyy.dev` and add a CNAME in
   Cloudflare DNS pointing at `wolffcatskyy.github.io` (DNS-only or proxied), or
2. upload `site/` as a subpath/second site in the same Cloudflare setup as
   wolffcatskyy.dev.

Both options need repo/admin or Cloudflare access, so they are owner steps.
