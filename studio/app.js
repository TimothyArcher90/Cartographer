// Cartographer · Estudio: navegar, buscar en el acervo, superponer, editar, 3D, animar y exportar.
const $ = (id) => document.getElementById(id);
const norm = (t) => t.normalize('NFKD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/\s+/g, ' ').trim();
const MAX_RESULTADOS = 400;

let NOMBRES = {}, PAISES = {}, GEO = null;
let proyecto = { capas: [], dibujos: [], pintados: {}, claves: [], epoca: '', camara: null };
let herramienta = 'navegar', trazo = [];

const map = new maplibregl.Map({
  container: 'mapa', center: [20, 30], zoom: 2, maxPitch: 85,
  canvasContextAttributes: { preserveDrawingBuffer: true }, preserveDrawingBuffer: true,
  style: { version: 8, sources: {}, layers: [{ id: 'mar', type: 'background', paint: { 'background-color': '#a9c3c8' } }] },
});
map.addControl(new maplibregl.NavigationControl({ visualizePitch: true }));
map.addControl(new maplibregl.ScaleControl());

async function json(url) { const r = await fetch(url); if (!r.ok) throw new Error(url + ' ' + r.status); return r.json(); }
async function jsonlGz(url) {
  const r = await fetch(url); if (!r.ok) return [];
  const buf = new Uint8Array(await r.arrayBuffer());
  let texto;
  if (buf[0] === 0x1f && buf[1] === 0x8b) {
    const s = new Blob([buf]).stream().pipeThrough(new DecompressionStream('gzip'));
    texto = await new Response(s).text();
  } else texto = new TextDecoder().decode(buf);
  return texto.split('\n').filter(Boolean).map((l) => JSON.parse(l));
}

// ---------- Base ----------
map.on('load', async () => {
  [NOMBRES, PAISES, GEO] = await Promise.all([json('datos/nombres.json'), json('datos/paises.json'), json('datos/paises.geojson')]);
  map.addSource('paises', { type: 'geojson', data: GEO, promoteId: 'iso' });
  map.addLayer({ id: 'tierra', type: 'fill', source: 'paises', paint: { 'fill-color': ['coalesce', ['feature-state', 'color'], '#efe6cf'], 'fill-opacity': 1 } });
  map.addLayer({ id: 'bordes', type: 'line', source: 'paises', paint: { 'line-color': '#8a7a5c', 'line-width': 0.6 } });
  map.addSource('epoca', { type: 'geojson', data: { type: 'FeatureCollection', features: [] } });
  map.addLayer({ id: 'epoca-relleno', type: 'fill', source: 'epoca', paint: { 'fill-color': '#c0703a', 'fill-opacity': 0.18 } });
  map.addLayer({ id: 'epoca-linea', type: 'line', source: 'epoca', paint: { 'line-color': '#7a2e12', 'line-width': 1.4 } });
  map.addSource('dibujos', { type: 'geojson', data: { type: 'FeatureCollection', features: [] } });
  map.addLayer({ id: 'd-area', type: 'fill', source: 'dibujos', filter: ['==', '$type', 'Polygon'], paint: { 'fill-color': ['get', 'color'], 'fill-opacity': 0.35 } });
  map.addLayer({ id: 'd-area-3d', type: 'fill-extrusion', source: 'dibujos', filter: ['==', '$type', 'Polygon'], layout: { visibility: 'none' },
    paint: { 'fill-extrusion-color': ['get', 'color'], 'fill-extrusion-height': ['coalesce', ['get', 'altura'], 60000], 'fill-extrusion-opacity': 0.8 } });
  map.addLayer({ id: 'd-linea', type: 'line', source: 'dibujos', filter: ['!=', '$type', 'Point'], layout: { 'line-cap': 'round', 'line-join': 'round' }, paint: { 'line-color': ['get', 'color'], 'line-width': 3 } });
  map.addLayer({ id: 'd-punto', type: 'circle', source: 'dibujos', filter: ['all', ['==', '$type', 'Point'], ['!has', 'texto']], paint: { 'circle-color': ['get', 'color'], 'circle-radius': 6, 'circle-stroke-color': '#fff', 'circle-stroke-width': 2 } });
  map.addSource('trazo', { type: 'geojson', data: { type: 'FeatureCollection', features: [] } });
  map.addLayer({ id: 'trazo', type: 'line', source: 'trazo', paint: { 'line-color': '#222', 'line-width': 2, 'line-dasharray': [2, 2] } });
  map.addSource('dem', { type: 'raster-dem', tiles: ['https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{z}/{x}/{y}.png'], encoding: 'terrarium', tileSize: 256, maxzoom: 12 });
  map.addLayer({ id: 'sombras', type: 'hillshade', source: 'dem', layout: { visibility: 'none' }, paint: { 'hillshade-exaggeration': 0.5 } }, 'bordes');
  llenarSugerencias();
  for (let s = 1; s <= 21; s++) $('siglo').add(new Option('s. ' + romano(s), s));
  for (const t of ['portulano', 'carta náutica', 'ptolemaico', 'mapamundi', 'plano urbano', 'topográfico', 'militar', 'ferroviario/viario', 'histórico/temático', 'general']) $('tipo').add(new Option(t, t));
  try { const g = localStorage.getItem('cartographer-proyecto'); if (g) cargarProyecto(JSON.parse(g)); } catch (e) {}
  pintarEtiquetas();
});

function romano(n) { const v = [[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]; let r = ''; for (const [k, s] of v) while (n >= k) { r += s; n -= k; } return r; }

// Etiquetas HTML (sin servidor de tipografías).
const capaEtq = document.createElement('div'); $('mapa').appendChild(capaEtq);
function pintarEtiquetas() {
  if (!GEO) return;
  capaEtq.innerHTML = '';
  const z = map.getZoom(), b = map.getBounds();
  if ($('actuales').checked) for (const f of GEO.features) {
    const p = f.properties; if (z < 2.5 && (PAISES[p.iso]?.total || 0) < 3000) continue;
    if (!b.contains([p.lon, p.lat])) continue;
    etiqueta(p.nombre, [p.lon, p.lat], '');
  }
  for (const d of proyecto.dibujos) if (d.properties.texto) etiqueta(d.properties.texto, d.geometry.coordinates, 'libre', d.properties.color);
}
function etiqueta(texto, lnglat, clase, color) {
  const pt = map.project(lnglat); const e = document.createElement('div');
  e.className = 'etq ' + clase; e.textContent = texto; e.style.left = pt.x + 'px'; e.style.top = pt.y + 'px'; if (color) e.style.color = color;
  capaEtq.appendChild(e);
}
map.on('move', pintarEtiquetas);
$('actuales').onchange = () => { map.setLayoutProperty('bordes', 'visibility', $('actuales').checked ? 'visible' : 'none'); pintarEtiquetas(); };

// ---------- Búsqueda ----------
function llenarSugerencias() {
  const dl = $('sugerencias');
  for (const iso of Object.keys(PAISES).sort((a, b) => PAISES[b].total - PAISES[a].total)) dl.appendChild(new Option(PAISES[iso].nombre));
}
function resolver(q) {
  const n = norm(q); if (!n) return { iso: [], region: [] };
  if (NOMBRES[n]) return { iso: NOMBRES[n].iso || [], region: NOMBRES[n].region || [] };
  const iso = Object.keys(PAISES).filter((k) => norm(PAISES[k].nombre) === n || k.toLowerCase() === n);
  if (iso.length) return { iso, region: [] };
  const parcial = Object.keys(NOMBRES).find((k) => k.startsWith(n));
  return parcial ? { iso: NOMBRES[parcial].iso || [], region: NOMBRES[parcial].region || [] } : { iso: [], region: [] };
}
let ultimos = [];
async function buscar() {
  const q = $('q').value; const r = resolver(q);
  const isos = [...new Set([...r.iso, ...r.region.map((x) => x[1])])];
  if (!isos.length) { $('estado').textContent = `No reconozco «${q}». Prueba con el nombre del país o región.`; $('resultados').innerHTML = ''; return; }
  $('estado').textContent = 'Cargando…';
  let todos = [];
  for (const iso of isos) todos = todos.concat(await jsonlGz(`biblioteca/paises/${iso}.jsonl.gz`));
  const regiones = new Set(r.region.map((x) => x[0]));
  if (regiones.size && !r.iso.length) todos = todos.filter((m) => (m.regiones || []).some((x) => regiones.has(x)));
  const siglo = +$('siglo').value, tipo = $('tipo').value;
  if (siglo) todos = todos.filter((m) => (m.siglos || []).includes(siglo));
  if (tipo) todos = todos.filter((m) => m.tipo === tipo);
  if ($('solobbox').checked) todos = todos.filter((m) => m.bbox && m.bbox[0] !== m.bbox[2]);
  todos.sort((a, b) => (b.relevancia || 0) - (a.relevancia || 0) || (a.anio || 9999) - (b.anio || 9999));
  ultimos = todos.slice(0, MAX_RESULTADOS);
  const nombre = r.iso.length ? r.iso.map((i) => PAISES[i]?.nombre || i).join(', ') : r.region.map((x) => x[2]).join(', ');
  $('estado').textContent = `${nombre}: ${todos.length.toLocaleString('es')} mapas` + (todos.length > MAX_RESULTADOS ? ` (muestro ${MAX_RESULTADOS}; filtra por siglo o tipo)` : '');
  $('resultados').innerHTML = '';
  ultimos.forEach((m, i) => {
    const d = document.createElement('div'); d.className = 'ficha';
    d.title = `${m.t}\n${m.anio || 'sin fecha'} · ${m.tipo} · ${m.lic}\nClic: superponer · Doble clic: abrir en el archivo`;
    d.innerHTML = `<img loading="lazy" alt=""><div></div>`;
    d.querySelector('img').src = m.th || '';
    d.querySelector('div').textContent = `${m.anio || 's/f'} · ${m.t.slice(0, 60)}`;
    d.onclick = () => superponer(m);
    d.ondblclick = () => window.open(m.url, '_blank', 'noopener');
    $('resultados').appendChild(d);
  });
  const bb = unirBbox(isos);
  if (bb) map.fitBounds(bb, { padding: 30, duration: 1200 });
}
function unirBbox(isos) {
  let b = null;
  for (const f of GEO.features) if (isos.includes(f.properties.iso)) {
    const cs = f.geometry.coordinates.flat(f.geometry.type === 'MultiPolygon' ? 2 : 1);
    for (const [x, y] of cs) b = b ? [Math.min(b[0], x), Math.min(b[1], y), Math.max(b[2], x), Math.max(b[3], y)] : [x, y, x, y];
  }
  return b && [[b[0], b[1]], [b[2], b[3]]];
}
$('buscar').onclick = buscar; $('q').onkeydown = (e) => e.key === 'Enter' && buscar();
$('siglo').onchange = $('tipo').onchange = $('solobbox').onchange = () => $('q').value && buscar();

// ---------- Capas superpuestas ----------
function urlImagen(m) {
  if (m.iiif) return m.iiif.replace(/\/info\.json$/, '') + '/full/2000,/0/default.jpg';
  return (m.th || '').replace(/\/(\d+)px-([^/]+)$/, '/2000px-$2');
}
function superponer(m) {
  let bb = m.bbox && m.bbox[0] !== m.bbox[2] ? m.bbox : null;
  let aprox = false;
  if (!bb) { const c = map.getBounds(); bb = [c.getWest() + (c.getEast() - c.getWest()) * 0.2, c.getSouth() + (c.getNorth() - c.getSouth()) * 0.2, c.getEast() - (c.getEast() - c.getWest()) * 0.2, c.getNorth() - (c.getNorth() - c.getSouth()) * 0.2]; aprox = true; }
  const capa = { id: 'c' + Date.now(), t: m.t, anio: m.anio, url: m.url, lic: m.lic, img: urlImagen(m), bbox: bb, opacidad: 0.8, aprox };
  proyecto.capas.push(capa); montarCapa(capa); listarCapas(); guardarLocal();
  if (!aprox) map.fitBounds([[bb[0], bb[1]], [bb[2], bb[3]]], { padding: 30 });
}
function montarCapa(c) {
  const [w, s, e, n] = c.bbox;
  if (map.getSource(c.id)) return;
  map.addSource(c.id, { type: 'image', url: c.img, coordinates: [[w, n], [e, n], [e, s], [w, s]] });
  map.addLayer({ id: c.id, type: 'raster', source: c.id, paint: { 'raster-opacity': c.opacidad, 'raster-fade-duration': 0 } }, 'epoca-relleno');
}
function quitarCapa(c) { if (map.getLayer(c.id)) map.removeLayer(c.id); if (map.getSource(c.id)) map.removeSource(c.id); }
function listarCapas() {
  const ul = $('capas'); ul.innerHTML = '';
  if (!proyecto.capas.length) ul.innerHTML = '<li class="nota">Haz clic en un resultado para superponerlo.</li>';
  proyecto.capas.forEach((c, i) => {
    const li = document.createElement('li');
    li.innerHTML = `<span></span><input type="range" min="0" max="1" step="0.05" style="width:70px"><button title="Subir">↑</button><button title="Quitar">✕</button>`;
    li.querySelector('span').textContent = `${c.anio || 's/f'} ${c.aprox ? '(ubicación aproximada) ' : ''}${c.t}`;
    li.querySelector('span').title = `${c.t}\nLicencia: ${c.lic}\n${c.url}`;
    const r = li.querySelector('input'); r.value = c.opacidad;
    r.oninput = () => { c.opacidad = +r.value; map.setPaintProperty(c.id, 'raster-opacity', c.opacidad); guardarLocal(); };
    const [sub, x] = li.querySelectorAll('button');
    sub.onclick = () => { map.moveLayer(c.id, 'epoca-relleno'); proyecto.capas.push(proyecto.capas.splice(i, 1)[0]); listarCapas(); };
    x.onclick = () => { quitarCapa(c); proyecto.capas.splice(i, 1); listarCapas(); guardarLocal(); };
    ul.appendChild(li);
  });
}

// ---------- Épocas ----------
$('epoca').onchange = async () => {
  proyecto.epoca = $('epoca').value;
  map.getSource('epoca').setData(proyecto.epoca ? await json(`epocas/anio-${proyecto.epoca}.geojson`) : { type: 'FeatureCollection', features: [] });
  guardarLocal();
};
map.on('click', 'epoca-relleno', (e) => {
  if (herramienta !== 'navegar') return;
  const p = e.features[0].properties;
  new maplibregl.Popup().setLngLat(e.lngLat).setText((p.nombre_es || p.nombre_original || 'sin nombre') + ' · fronteras aproximadas (' + p.fuente + ')').addTo(map);
});

// ---------- Edición ----------
document.querySelectorAll('#herramientas button').forEach((b) => b.onclick = () => {
  terminarTrazo(); herramienta = b.dataset.h;
  document.querySelectorAll('#herramientas button').forEach((x) => x.classList.toggle('activo', x === b));
  map.getCanvas().style.cursor = herramienta === 'navegar' ? '' : 'crosshair';
});
const color = () => $('color').value;
function refrescarDibujos() { map.getSource('dibujos').setData({ type: 'FeatureCollection', features: proyecto.dibujos }); pintarEtiquetas(); guardarLocal(); }
map.on('click', (e) => {
  const p = [+e.lngLat.lng.toFixed(5), +e.lngLat.lat.toFixed(5)];
  if (herramienta === 'punto') { proyecto.dibujos.push({ type: 'Feature', properties: { color: color() }, geometry: { type: 'Point', coordinates: p } }); refrescarDibujos(); }
  else if (herramienta === 'texto') { const t = prompt('Texto:'); if (t) { proyecto.dibujos.push({ type: 'Feature', properties: { color: color(), texto: t }, geometry: { type: 'Point', coordinates: p } }); refrescarDibujos(); } }
  else if (herramienta === 'ruta' || herramienta === 'area') { trazo.push(p); map.getSource('trazo').setData({ type: 'Feature', geometry: { type: 'LineString', coordinates: trazo.length > 1 ? trazo : [p, p] } }); }
  else if (herramienta === 'pintar') {
    const f = map.queryRenderedFeatures(e.point, { layers: ['tierra'] })[0]; if (!f) return;
    const iso = f.properties.iso;
    if (proyecto.pintados[iso] === color()) { delete proyecto.pintados[iso]; map.removeFeatureState({ source: 'paises', id: iso }, 'color'); }
    else { proyecto.pintados[iso] = color(); map.setFeatureState({ source: 'paises', id: iso }, { color: color() }); }
    guardarLocal();
  }
});
map.on('dblclick', (e) => { if (trazo.length) { e.preventDefault(); terminarTrazo(); } });
function terminarTrazo() {
  if (herramienta === 'ruta' && trazo.length > 1) proyecto.dibujos.push({ type: 'Feature', properties: { color: color() }, geometry: { type: 'LineString', coordinates: trazo } });
  if (herramienta === 'area' && trazo.length > 2) proyecto.dibujos.push({ type: 'Feature', properties: { color: color() }, geometry: { type: 'Polygon', coordinates: [[...trazo, trazo[0]]] } });
  trazo = []; if (map.getSource('trazo')) map.getSource('trazo').setData({ type: 'FeatureCollection', features: [] }); if (map.getSource('dibujos')) refrescarDibujos();
}
$('terminar').onclick = terminarTrazo;
$('deshacer').onclick = () => { if (trazo.length) { trazo.pop(); return; } proyecto.dibujos.pop(); refrescarDibujos(); };
$('extruir').onchange = () => map.setLayoutProperty('d-area-3d', 'visibility', $('extruir').checked ? 'visible' : 'none');

// ---------- 3D ----------
function relieve() {
  const on = $('relieve').checked;
  map.setTerrain(on ? { source: 'dem', exaggeration: +$('exag').value } : null);
  map.setLayoutProperty('sombras', 'visibility', on ? 'visible' : 'none');
}
$('relieve').onchange = $('exag').oninput = relieve;
$('pitch').oninput = () => map.setPitch(+$('pitch').value);
$('bearing').oninput = () => map.setBearing(+$('bearing').value);
map.on('pitchend', () => $('pitch').value = map.getPitch()); map.on('rotateend', () => $('bearing').value = map.getBearing());

// ---------- Animación ----------
function camara() { const c = map.getCenter(); return { center: [+c.lng.toFixed(4), +c.lat.toFixed(4)], zoom: +map.getZoom().toFixed(2), pitch: Math.round(map.getPitch()), bearing: Math.round(map.getBearing()) }; }
$('clave').onclick = () => { proyecto.claves.push({ ...camara(), dur: +$('dur').value || 3 }); listarClaves(); guardarLocal(); };
function listarClaves() {
  const ul = $('claves'); ul.innerHTML = '';
  proyecto.claves.forEach((k, i) => {
    const li = document.createElement('li');
    li.innerHTML = `<span>${i + 1}. zoom ${k.zoom} · incl. ${k.pitch}° · ${k.dur}s</span><button>ir</button><button>✕</button>`;
    const [ir, x] = li.querySelectorAll('button');
    ir.onclick = () => map.jumpTo(k); x.onclick = () => { proyecto.claves.splice(i, 1); listarClaves(); guardarLocal(); };
    ul.appendChild(li);
  });
}
async function reproducir() {
  if (!proyecto.claves.length) { alert('Añade al menos un fotograma clave.'); return; }
  map.jumpTo(proyecto.claves[0]);
  await new Promise((r) => setTimeout(r, 400));
  for (const k of proyecto.claves.slice(1)) {
    map.flyTo({ ...k, duration: k.dur * 1000, essential: true, curve: 1.2 });
    await new Promise((r) => map.once('moveend', r));
  }
}
$('reproducir').onclick = reproducir;
$('grabar').onclick = async () => {
  if (!window.MediaRecorder) { alert('Tu navegador no permite grabar vídeo.'); return; }
  const contenedor = $('mapa'), fmt = $('formato').value;
  const antes = [contenedor.style.width, contenedor.style.height];
  if (fmt) { const [w, h] = fmt.split('x').map(Number); const k = Math.min(1, (window.innerHeight - 20) / h, (contenedor.parentElement.clientWidth - 360) / w); contenedor.style.width = w * k + 'px'; contenedor.style.height = h * k + 'px'; map.resize(); }
  const stream = map.getCanvas().captureStream(30);
  const tipo = ['video/mp4;codecs=avc1', 'video/webm;codecs=vp9', 'video/webm'].find((t) => MediaRecorder.isTypeSupported(t));
  const rec = new MediaRecorder(stream, { mimeType: tipo, videoBitsPerSecond: 12e6 }); const trozos = [];
  rec.ondataavailable = (e) => e.data.size && trozos.push(e.data);
  const listo = new Promise((r) => rec.onstop = r);
  $('rec').style.display = 'block'; rec.start();
  // Fuerza repintado continuo para que el vídeo no se congele en los tramos quietos.
  let vivo = true; (function bucle() { if (vivo) { map.triggerRepaint(); requestAnimationFrame(bucle); } })();
  await reproducir(); await new Promise((r) => setTimeout(r, 600));
  vivo = false; rec.stop(); await listo; $('rec').style.display = 'none';
  contenedor.style.width = antes[0]; contenedor.style.height = antes[1]; map.resize();
  descargar(new Blob(trozos, { type: tipo }), 'cartographer.' + (tipo.includes('mp4') ? 'mp4' : 'webm'));
};

// ---------- Proyecto ----------
function descargar(blob, nombre) { const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = nombre; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 5000); }
function guardarLocal() { proyecto.camara = camara(); try { localStorage.setItem('cartographer-proyecto', JSON.stringify(proyecto)); } catch (e) {} }
function cargarProyecto(p) {
  proyecto.capas.forEach(quitarCapa);
  for (const iso of Object.keys(proyecto.pintados)) map.removeFeatureState({ source: 'paises', id: iso }, 'color');
  proyecto = Object.assign({ capas: [], dibujos: [], pintados: {}, claves: [], epoca: '' }, p);
  proyecto.capas.forEach(montarCapa); listarCapas(); listarClaves();
  for (const [iso, c] of Object.entries(proyecto.pintados)) map.setFeatureState({ source: 'paises', id: iso }, { color: c });
  $('epoca').value = proyecto.epoca || ''; $('epoca').onchange();
  refrescarDibujos(); if (proyecto.camara) map.jumpTo(proyecto.camara);
}
$('guardar').onclick = () => { guardarLocal(); descargar(new Blob([JSON.stringify(proyecto, null, 1)], { type: 'application/json' }), 'proyecto-cartographer.json'); };
$('abrir').onchange = async (e) => { const f = e.target.files[0]; if (f) cargarProyecto(JSON.parse(await f.text())); };
$('nuevo').onclick = () => confirm('¿Empezar un proyecto vacío?') && cargarProyecto({});
$('png').onclick = () => map.getCanvas().toBlob((b) => descargar(b, 'cartographer.png'));
map.on('moveend', guardarLocal);
