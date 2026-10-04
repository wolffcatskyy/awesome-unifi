/* Awesome UniFi directory - renders data.json with search + filters. No dependencies. */
(function () {
  const DATA_URLS = [
    'data.json',
    'https://raw.githubusercontent.com/wolffcatskyy/awesome-unifi/main/data.json',
  ];
  const state = { q: '', os: '', deploy: '', cat: '', sort: 'stars', archived: false };
  let data = null;
  let catIndex = {};

  const $ = (id) => document.getElementById(id);
  const esc = (s) => String(s == null ? '' : s).replace(/[&<>"']/g,
    (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  async function load() {
    for (const url of DATA_URLS) {
      try {
        const r = await fetch(url, { cache: 'no-cache' });
        if (r.ok) return await r.json();
      } catch (e) { /* try next source */ }
    }
    throw new Error('could not load data.json');
  }

  function fmtDate(iso) {
    if (!iso) return 'n/a';
    const d = new Date(iso);
    return d.toLocaleDateString(undefined, { year: 'numeric', month: 'short', day: 'numeric' });
  }

  function osBadge(e) {
    const u = e.unifi_os || { status: 'unknown', versions: [] };
    if (u.status === 'unknown') return '<span class="badge">UniFi OS: unknown</span>';
    const cls = { works: 'os-works', partial: 'os-partial', broken: 'os-broken' }[u.status] || '';
    const vers = (u.versions || []).map((v) => esc(v) + '.x').join(' ');
    return `<span class="badge ${cls}">UniFi OS ${u.status}${vers ? ' · ' + vers : ''}</span>`;
  }

  function catLabel(id) {
    const c = catIndex[id];
    return c ? c.path.join(' › ') : id;
  }

  function card(e) {
    const gh = e.github || {};
    const bits = [];
    if (gh.stars != null) bits.push(`<span class="badge stars">★ ${gh.stars.toLocaleString()}</span>`);
    if (gh.last_push) bits.push(`<span class="badge">updated ${fmtDate(gh.last_push)}</span>`);
    if (gh.license && gh.license !== 'NOASSERTION') bits.push(`<span class="badge">${esc(gh.license)}</span>`);
    bits.push(osBadge(e));
    if (e.deployment && e.deployment !== 'unknown')
      bits.push(`<span class="badge">${esc(e.deployment)}${e.deployment_source === 'inferred' ? '?' : ''}</span>`);
    if (gh.archived) bits.push('<span class="badge arch">archived</span>');
    if (gh.renamed_from) bits.push(`<span class="badge renamed">renamed from ${esc(gh.renamed_from)}</span>`);
    const title = esc(e.name);
    return `<article class="card">
      <div class="card-head"><h2><a href="${esc(e.url)}">${title}</a></h2>
        <span class="cat">${esc(catLabel(e.category))}</span></div>
      <p class="desc">${esc(e.description)}</p>
      <div class="meta">${bits.join('')}</div>
    </article>`;
  }

  function matches(e) {
    if (!state.archived && e.github && e.github.archived) return false;
    if (state.os) {
      const u = e.unifi_os || { status: 'unknown' };
      if (state.os === 'unknown') { if (u.status !== 'unknown') return false; }
      else if (!(u.versions || []).includes(state.os)) return false;
    }
    if (state.deploy && (e.deployment || 'unknown') !== state.deploy) return false;
    if (state.cat && !e.category.id.startsWith(state.cat)) return false;
    if (state.q) {
      const hay = `${e.name} ${e.description} ${e.url} ${catLabel(e.category)}`.toLowerCase();
      if (!hay.includes(state.q)) return false;
    }
    return true;
  }

  function sortEntries(list) {
    const by = {
      stars: (a, b) => ((b.github || {}).stars || -1) - ((a.github || {}).stars || -1),
      updated: (a, b) => String((b.github || {}).last_push || '').localeCompare(String((a.github || {}).last_push || '')),
      name: (a, b) => a.name.toLowerCase().localeCompare(b.name.toLowerCase()),
    }[state.sort];
    return list.sort(by);
  }

  function render() {
    const list = sortEntries(data.entries.filter(matches));
    $('list').innerHTML = list.length
      ? list.map(card).join('')
      : '<p class="empty">No entries match these filters.</p>';
    const shown = list.length;
    $('stats').innerHTML = [
      `<span class="chip"><b>${shown}</b> of ${data.stats.entries} tools</span>`,
      `<span class="chip"><b>${data.stats.categories}</b> categories</span>`,
      `<span class="chip">data generated <b>${fmtDate(data.generated_at)}</b></span>`,
    ].join('');
  }

  function fillCategories() {
    const sel = $('f-cat');
    const seen = new Set();
    for (const c of data.categories) {
      if (!c.entries || seen.has(c.id)) continue;
      seen.add(c.id);
      const opt = document.createElement('option');
      opt.value = c.id;
      opt.textContent = `${c.path.join(' › ')} (${c.entries})`;
      sel.appendChild(opt);
    }
  }

  function bind() {
    $('q').addEventListener('input', (ev) => { state.q = ev.target.value.trim().toLowerCase(); render(); });
    $('f-os').addEventListener('change', (ev) => { state.os = ev.target.value; render(); });
    $('f-deploy').addEventListener('change', (ev) => { state.deploy = ev.target.value; render(); });
    $('f-cat').addEventListener('change', (ev) => { state.cat = ev.target.value; render(); });
    $('f-sort').addEventListener('change', (ev) => { state.sort = ev.target.value; render(); });
    $('f-archived').addEventListener('change', (ev) => { state.archived = ev.target.checked; render(); });
  }

  load().then((d) => {
    data = d;
    for (const c of d.categories) catIndex[c.id] = c;
    fillCategories(); bind(); render();
  })
    .catch((err) => { $('list').innerHTML = `<p class="empty">Failed to load data: ${esc(err.message)}</p>`; });
})();
