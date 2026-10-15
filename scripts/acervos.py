"""Recolectores de catálogos de mapas libres (además de Wikimedia Commons).

Uso (en GitHub Actions, que tiene internet):
  python scripts/acervos.py ogm        --minutos 300   # OpenGeoMetadata (bibliotecas universitarias)
  python scripts/acervos.py loc        --minutos 300   # Library of Congress
  python scripts/acervos.py ia         --minutos 300   # Internet Archive
  python scripts/acervos.py europeana  --minutos 300   # Europeana (clave pública de demostración)

Cada fuente escribe catalogo/<fuente>/parte-XXXX.jsonl.gz con el mismo esquema que Commons:
  t, url, th (miniatura), iiif, lic, autor, fecha, anio, siglos, lugares, bbox [O,S,E,N], fuente, id
y guarda su estado en catalogo/<fuente>/estado.json para reanudar.
Solo se guardan registros con licencia libre identificada (dominio público, CC0, CC BY, CC BY-SA,
"sin restricciones conocidas"). Los demás se cuentan en el estado como descartados.
"""
import argparse
import gzip
import json
import re
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
UA = "Cartographer/1.0 (https://github.com/TimothyArcher90/Cartographer; catalogo de mapas libres)"
POR_PARTE = 20000
RE_ANIO = re.compile(r"(?<!\d)(1[0-9]{3}|[5-9][0-9]{2})(?!\d)")


NAVEGADOR = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36",
             "Accept": "application/json,text/html;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.9,es;q=0.8"}


def pedir_json(url, intentos=6, navegador=False):
    for i in range(intentos):
        try:
            cab = dict(NAVEGADOR) if navegador else {"User-Agent": UA, "Accept": "application/json"}
            req = urllib.request.Request(url, headers=cab)
            with urllib.request.urlopen(req, timeout=120) as r:
                return json.load(r)
        except Exception as e:
            print("reintento", i, url[:120], e)
            time.sleep(min(120, 3 * 2 ** i))
    return None


RE_MAPA = re.compile(r"(?i)\b(map|maps|mapa|mapas|mappa|carte|cartes|karte|karten|landkarte|kaart|kaarten|"
                     r"plan|plano|planta|pianta|plattegrond|stadtplan|atlas|chart|portolan\w*|portulan\w*|"
                     r"me(?:ss|ß)tischbl\w*|topograph\w*|cartograph\w*|kartograf\w*|mappemonde|planisph\w*|"
                     r"globus|globe|sheet|blatt|feuille|hoja|1\s*:\s*\d[\d .,]{2,})\b")


RE_NO_MAPA = re.compile(r"(?i)postcard|carte postale|cartes postales|ansichtskarte|postkarte|vykort|"
                        r"\bfa[țt][ăa]\s*:|\bvedere\b|fotograf|photograph|\bphoto\b|portrait|retrato|bildnis")


def es_mapa(*textos):
    texto = " ".join(str(t) for t in textos if t)
    return bool(RE_MAPA.search(texto)) and not RE_NO_MAPA.search(texto)


def lista(v):
    if v is None:
        return []
    return [str(x) for x in v] if isinstance(v, list) else [str(v)]


def por_antiguedad(anio):
    """Obras publicadas antes de 1900: dominio público por antigüedad en casi todos los países.
    Se marca como inferido para que no se confunda con una licencia declarada."""
    return "Dominio público por antigüedad (anterior a 1900; inferido, verificar)" if anio and anio < 1900 else None


def anio_de(*textos):
    for t in textos:
        m = RE_ANIO.search(str(t or ""))
        if m:
            return int(m.group(1))
    return None


def siglo(a):
    return [(a - 1) // 100 + 1] if a and a > 0 else []


def libre(texto):
    """Devuelve una etiqueta de licencia libre o None."""
    l = (texto or "").lower()
    if not l or re.search(r"\bnc\b|by-nc|non-?commercial|\bnd\b|by-nd|no ?deriv", l):
        return None
    if "publicdomain/zero" in l or "cc0" in l:
        return "CC0"
    if "publicdomain/mark" in l or "public domain" in l or "dominio público" in l or "noc-us" in l \
            or "/noc-" in l or "no known copyright" in l or "no known restrictions" in l \
            or "no restrictions on use" in l or "free of known restrictions" in l:
        return "Dominio público / sin restricciones conocidas"
    m = re.search(r"licenses/(by(?:-sa)?)/(\d\.\d)", l)
    if m:
        return f"CC {m.group(1).upper()} {m.group(2)}"
    return None


class Salida:
    def __init__(self, fuente):
        self.dir = RAIZ / "catalogo" / fuente
        self.dir.mkdir(parents=True, exist_ok=True)
        self.ruta_estado = self.dir / "estado.json"
        self.e = json.loads(self.ruta_estado.read_text()) if self.ruta_estado.exists() else \
            {"parte": 0, "en_parte": 0, "guardados": 0, "descartados": 0, "terminado": False}
        self.f = gzip.open(self.dir / f"parte-{self.e['parte']:04d}.jsonl.gz", "at", encoding="utf-8")
        self.fuente = fuente

    def poner(self, r):
        r["fuente"] = self.fuente
        r["siglos"] = r.get("siglos") or siglo(r.get("anio"))
        self.f.write(json.dumps(r, ensure_ascii=False) + "\n")
        self.e["guardados"] += 1
        self.e["en_parte"] += 1
        if self.e["en_parte"] >= POR_PARTE:
            self.f.close()
            self.e["parte"] += 1
            self.e["en_parte"] = 0
            self.f = gzip.open(self.dir / f"parte-{self.e['parte']:04d}.jsonl.gz", "at", encoding="utf-8")

    def cerrar(self):
        self.f.close()
        self.ruta_estado.write_text(json.dumps(self.e, ensure_ascii=False, indent=1))
        print(f"{self.fuente}: guardados {self.e['guardados']} · descartados {self.e['descartados']} · "
              f"terminado {self.e['terminado']}")


# ---------------------------------------------------------------- OpenGeoMetadata
def bbox_envelope(t):
    m = re.search(r"ENVELOPE\(\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*,\s*([-\d.]+)\s*\)", t or "")
    if not m:
        return None
    o, e, n, s = map(float, m.groups())
    return [o, s, e, n]


def ogm(s, fin):
    repos = s.e.get("repos_pendientes")
    if repos is None:
        nombres = []
        for pagina in range(1, 6):
            d = pedir_json(f"https://api.github.com/orgs/OpenGeoMetadata/repos?per_page=100&page={pagina}") or []
            nombres += [r["name"] for r in d if not r.get("archived")]
            if len(d) < 100:
                break
        repos = sorted(x for x in nombres if "." in x)
        s.e["repos_pendientes"] = repos
    while repos and time.time() < fin:
        repo = repos.pop(0)
        with tempfile.TemporaryDirectory() as tmp:
            r = subprocess.run(["git", "clone", "-q", "--depth", "1", f"https://github.com/OpenGeoMetadata/{repo}", tmp])
            if r.returncode != 0:
                continue
            for ruta in Path(tmp).rglob("*.json"):
                if ruta.name != "geoblacklight.json" and "aardvark" not in str(ruta):
                    continue
                try:
                    d = json.loads(ruta.read_text(encoding="utf-8"))
                    if isinstance(d, dict):
                        ogm_registro(s, d)
                except Exception as e:
                    print("registro con formato inesperado:", ruta, e)
        print("repo", repo, "listo; guardados", s.e["guardados"])
    s.e["terminado"] = not repos


def ogm_registro(s, d):
    clases = lista(d.get("gbl_resourceClass_sm"))
    tipo = " ".join(lista(d.get("dc_type_s") or d.get("layer_geom_type_s")))
    if "Maps" not in clases and not (not clases and tipo in ("Image", "Scanned Map")):
        return
    fecha = " ".join(lista(d.get("dct_issued_s"))) or " ".join(lista(d.get("gbl_indexYear_im")))
    anio = anio_de(fecha, " ".join(lista(d.get("dct_temporal_sm"))))
    derechos = " ".join(lista(d.get("dct_license_sm")) + lista(d.get("dct_rights_sm"))
                        + lista(d.get("dct_rightsHolder_sm")) + lista(d.get("dc_rights_s")))
    restringido = re.search(r"(?i)\brestricted|by-nc|non-?commercial|by-nd|all rights reserved", derechos)
    lic = libre(derechos) or (None if restringido else por_antiguedad(anio))
    if not lic:
        s.e["descartados"] += 1
        return
    try:
        refs = json.loads(d.get("dct_references_s") or "{}")
    except Exception:
        refs = {}
    s.poner({
        "id": d.get("id"), "t": " ".join(lista(d.get("dct_title_s") or d.get("dc_title_s")))[:300],
        "url": refs.get("http://schema.org/url") or (lista(d.get("dct_identifier_sm")) or [None])[0],
        "iiif": refs.get("http://iiif.io/api/presentation#manifest") or refs.get("http://iiif.io/api/image"),
        "th": refs.get("http://schema.org/thumbnailUrl"),
        "lic": lic, "autor": "; ".join(lista(d.get("dct_creator_sm") or d.get("dc_creator_sm")))[:150],
        "fecha": fecha[:40], "anio": anio,
        "lugares": lista(d.get("dct_spatial_sm") or d.get("dc_coverage_sm"))[:12],
        "bbox": bbox_envelope(" ".join(lista(d.get("dcat_bbox") or d.get("locn_geometry") or d.get("solr_geom")))),
        "proveedor": " ".join(lista(d.get("schema_provider_s") or d.get("dct_provenance_s"))),
    })


# ---------------------------------------------------------------- Library of Congress
TRAMOS_LOC = [f"{a}/{a + 49}" for a in range(1000, 1800, 50)] + [f"{a}/{a + 9}" for a in range(1800, 2030, 10)]


def loc(s, fin):
    """Recorre loc.gov/maps por tramos de años: la API deja de paginar pasadas ~400 páginas por consulta."""
    if s.e.get("modo") != "tramos":
        s.e.update(modo="tramos", tramo=0, pagina=1, terminado=False)
    while time.time() < fin and s.e["tramo"] < len(TRAMOS_LOC):
        tramo = TRAMOS_LOC[s.e["tramo"]]
        d = pedir_json(f"https://www.loc.gov/maps/?fo=json&c=150&sp={s.e['pagina']}&dates={tramo}&at=results,pagination")
        if not d:
            break
        for r in d.get("results", []):
            derechos = " ".join(r.get("rights") or []) if isinstance(r.get("rights"), list) else str(r.get("rights") or "")
            lic = libre(derechos) or "Sin restricciones conocidas (Library of Congress; comprobar el registro)"
            fecha = r.get("date") or ""
            imgs = r.get("image_url") or []
            s.poner({
                "id": r.get("id"), "t": (r.get("title") or "")[:300], "url": r.get("id"),
                "th": imgs[0] if imgs else None, "iiif": None, "lic": lic,
                "autor": "; ".join(lista(r.get("contributor")))[:150], "fecha": str(fecha)[:40],
                "anio": anio_de(fecha, r.get("dates")), "lugares": lista(r.get("location"))[:12], "bbox": None,
            })
        if (d.get("pagination") or {}).get("next"):
            s.e["pagina"] += 1
        else:
            print("LoC tramo", tramo, "terminado en página", s.e["pagina"])
            s.e["tramo"] += 1
            s.e["pagina"] = 1
        time.sleep(3)
    s.e["terminado"] = s.e["tramo"] >= len(TRAMOS_LOC)


# ---------------------------------------------------------------- Internet Archive
def ia(s, fin):
    q = ('(subject:(maps OR map OR cartography OR "early maps" OR atlases) OR collection:(maps OR mapsandatlases)) '
         'AND mediatype:(image OR texts)')
    cursor = s.e.get("cursor")
    while time.time() < fin:
        p = {"q": q, "fields": "identifier,title,date,year,creator,licenseurl,rights,subject,coverage", "count": 5000}
        if cursor:
            p["cursor"] = cursor
        d = pedir_json("https://archive.org/services/search/v1/scrape?" + urllib.parse.urlencode(p))
        if not d:
            break
        for r in d.get("items", []):
            derechos = " ".join(lista(r.get("licenseurl")) + lista(r.get("rights")))
            anio = anio_de(r.get("year"), r.get("date"), r.get("title"))
            restringido = re.search(r"(?i)by-nc|non-?commercial|by-nd|all rights reserved|copyright \d", derechos)
            lic = libre(derechos) or (None if restringido else por_antiguedad(anio))
            if not lic:
                s.e["descartados"] += 1
                continue
            ident = r["identifier"]
            lugares = r.get("coverage") or []
            s.poner({
                "id": ident, "t": str(r.get("title") or "")[:300], "url": f"https://archive.org/details/{ident}",
                "th": f"https://archive.org/services/img/{ident}", "iiif": f"https://iiif.archive.org/iiif/{ident}/manifest.json",
                "lic": lic, "autor": str(r.get("creator") or "")[:150], "fecha": str(r.get("date") or r.get("year") or "")[:40],
                "anio": anio,
                "lugares": (lugares if isinstance(lugares, list) else [lugares])[:12], "bbox": None,
            })
        cursor = d.get("cursor")
        s.e["cursor"] = cursor
        if not cursor:
            s.e["terminado"] = True
            break


# ---------------------------------------------------------------- Europeana
CONSULTA_EUROPEANA = ("title:(map OR maps OR mapa OR mapas OR mappa OR carte OR karte OR landkarte OR kaart OR "
                      "atlas OR plan OR plano OR pianta OR stadtplan OR plattegrond OR chart OR portolan OR "
                      "messtischblatt OR mappemonde OR planisphere)")


def europeana(s, fin):
    if s.e.get("consulta") != CONSULTA_EUROPEANA:
        s.e["consulta"] = CONSULTA_EUROPEANA
        s.e["cursor"] = "*"
        s.e["terminado"] = False
    cursor = s.e.get("cursor", "*")
    while time.time() < fin and cursor:
        p = [("wskey", "api2demo"), ("query", CONSULTA_EUROPEANA),
             ("qf", "TYPE:IMAGE"), ("reusability", "open"), ("rows", "100"), ("profile", "rich"), ("cursor", cursor)]
        d = pedir_json("https://api.europeana.eu/record/v2/search.json?" + urllib.parse.urlencode(p))
        if not d or not d.get("success", True):
            break
        for r in d.get("items", []):
            if not es_mapa(" ".join(r.get("title") or []), " ".join(lista(r.get("dcTypeLangAware"))),
                           " ".join(lista(r.get("dcType")))):
                s.e["no_mapa"] = s.e.get("no_mapa", 0) + 1
                continue
            lic = libre(" ".join(r.get("rights") or []))
            if not lic:
                s.e["descartados"] += 1
                continue
            lat, lon = r.get("edmPlaceLatitude"), r.get("edmPlaceLongitude")
            bbox = None
            try:
                if lat and lon:
                    la, lo = float(lat[0]), float(lon[0])
                    bbox = [lo, la, lo, la]
            except (TypeError, ValueError):
                pass
            s.poner({
                "id": r.get("id"), "t": " ".join(r.get("title") or [])[:300],
                "url": (r.get("edmIsShownAt") or [r.get("guid")])[0], "th": (r.get("edmPreview") or [None])[0],
                "iiif": None, "lic": lic, "autor": "; ".join(r.get("dcCreator") or [])[:150],
                "fecha": " ".join(r.get("year") or [])[:40], "anio": anio_de(" ".join(r.get("year") or [])),
                "lugares": (r.get("edmPlaceLabel") or [])[:12], "bbox": bbox,
                "proveedor": " ".join(r.get("dataProvider") or [])[:120],
            })
        cursor = d.get("nextCursor")
        s.e["cursor"] = cursor
        time.sleep(0.5)
    if not cursor:
        s.e["terminado"] = True



# ---------------------------------------------------------------- Digital Commonwealth (incluye el Leventhal Map Center)
def dc(s, fin):
    pagina = s.e.setdefault("pagina", 1)
    while time.time() < fin:
        base = s.e.get("base", "https://collections.leventhalmap.org/search.json?")
        url = base + urllib.parse.urlencode([("per_page", "100"), ("page", str(pagina)), ("q", ""),
                                             ("search_field", "all_fields")])
        d = pedir_json(url, navegador=True)
        if not d and pagina == 1 and "leventhal" in base:
            s.e["base"] = base = "https://www.digitalcommonwealth.org/search.json?f%5Bgenre_basic_ssim%5D%5B%5D=Maps&"
            d = pedir_json(base + urllib.parse.urlencode([("per_page", "100"), ("page", "1")]), navegador=True)
        if not d:
            break
        docs = (d.get("response") or {}).get("docs") or d.get("data") or []
        if not docs:
            s.e["terminado"] = True
            break
        for r in docs:
            a = r.get("attributes", r)
            val = lambda k: (a.get(k) or {}).get("attributes", {}).get("value") if isinstance(a.get(k), dict) else a.get(k)
            derechos = " ".join(lista(val("rights_ss")) + lista(val("license_ss")) + lista(val("rightsstatement_ss")))
            fecha = " ".join(lista(val("date_tsim") or val("date_start_dtsi") or val("date_facet_yearly_itim")))
            anio = anio_de(fecha, val("title_info_primary_tsi"))
            restringido = re.search(r"(?i)by-nc|non-?commercial|by-nd|all rights reserved|in copyright", derechos)
            lic = libre(derechos) or (None if restringido else por_antiguedad(anio))
            if not lic:
                s.e["descartados"] += 1
                continue
            ident = r.get("id")
            lugares = lista(val("subject_geographic_sim") or val("subject_geo_city_sim") or val("subject_geo_country_sim"))
            coords = val("subject_coordinates_geospatial") or val("subject_bbox_geospatial")
            dominio = "https://collections.leventhalmap.org" if "leventhal" in s.e.get("base", "leventhal") else "https://www.digitalcommonwealth.org"
            s.poner({
                "id": ident, "t": " ".join(lista(val("title_info_primary_tsi")))[:300],
                "url": f"{dominio}/search/{ident}",
                "th": f"{dominio}/search/{ident}/thumbnail",
                "iiif": f"{dominio}/search/{ident}/manifest.json",
                "lic": lic, "autor": "; ".join(lista(val("name_tsim")))[:150], "fecha": fecha[:40], "anio": anio,
                "lugares": lugares[:12], "bbox": bbox_envelope(" ".join(lista(coords))) if coords else None,
                "proveedor": " ".join(lista(val("institution_name_ssi"))),
            })
        pagina += 1
        s.e["pagina"] = pagina
        if pagina == 2:
            print("ejemplo de registro DC:", json.dumps(docs[0])[:1500])
        time.sleep(1)


# ---------------------------------------------------------------- Biblioteca Nacional de España (datos.gob.es)
def bne_descargar(url, navegador):
    """Intenta la descarga directa, con curl y desde copias del Internet Archive."""
    vias = [("directa", url)] + [(f"Wayback {a}", f"https://web.archive.org/web/{a}id_/{url}")
                                 for a in ("2026", "2025", "2024", "2023")]
    for via, u in vias:
        try:
            datos = urllib.request.urlopen(urllib.request.Request(u, headers=navegador), timeout=300).read()
        except Exception:
            r = subprocess.run(["curl", "-sSL", "--fail", "-A", navegador["User-Agent"], "--max-time", "300", u],
                               capture_output=True)
            datos = r.stdout if r.returncode == 0 else None
        if datos and datos[:2] == b"PK":
            print("BNE:", url.rsplit("/", 1)[-1], "descargado vía", via, len(datos) // 1024, "KB")
            yield via, datos


def bne_filas(nombre, contenido):
    import csv, io
    csv.field_size_limit(10 ** 9)
    if nombre.endswith(".json"):
        d = json.loads(contenido.decode("utf-8", "replace"))
        return d if isinstance(d, list) else next((v for v in d.values() if isinstance(v, list)), [])
    if nombre.endswith(".csv") or nombre.endswith(".txt"):
        texto = contenido.decode("utf-8", "replace") if b"\xef\xbb\xbf" in contenido[:3] or "utf8" in nombre \
            else contenido.decode("cp1252", "replace")
        cab = texto[:5000].splitlines()[0] if texto else ""
        sep = max([";", ",", "\t", "|"], key=cab.count)
        return list(csv.DictReader(io.StringIO(texto), delimiter=sep))
    return []


def bne(s, fin):
    """Conjunto 'BNE Digital: material cartográfico' de datos.gob.es (la BNE bloquea la descarga
    directa desde GitHub; se usa la copia del Internet Archive). Dominio público, reutilización CC BY 4.0."""
    import io, zipfile
    navegador = {"User-Agent": NAVEGADOR["User-Agent"], "Accept": "*/*", "Referer": "https://datos.gob.es/"}
    base = "https://www.bne.es/media/datosgob/bdh/tipodoc/material_cartografico_"
    mejor = []
    for fmt in ("json", "csv-utf8", "txt", "csv-cp1252"):
        for via, datos in bne_descargar(f"{base}{fmt}.zip", navegador):
            try:
                z = zipfile.ZipFile(io.BytesIO(datos))
            except Exception:
                continue
            for n in z.namelist():
                try:
                    filas = bne_filas(n, z.read(n))
                except Exception as e:
                    print("BNE: no se pudo leer", n, e)
                    continue
                print("BNE:", fmt, via, n, len(filas), "filas")
                if len(filas) > len(mejor):
                    mejor = filas
    print("BNE: filas finales", len(mejor))
    for f in mejor:
        g = {str(k).strip().lower(): (str(v) if v is not None else "").strip() for k, v in f.items() if k}
        titulo = g.get("título") or g.get("titulo") or ""
        fecha = g.get("fecha de publicación") or ""
        enlace = g.get("version_digital") or ""
        enlace = enlace.split(" ")[0] if enlace else ""
        lugares = [x.strip() for x in re.split(r"[;|/]", " ; ".join([g.get("lugar relacionado", ""), g.get("tema", "")])) if x.strip()]
        s.poner({
            "id": g.get("idbne") or enlace or titulo, "t": titulo[:300], "url": enlace, "th": None, "iiif": None,
            "lic": "CC BY 4.0 (obras de dominio público de la BNE; citar 'Biblioteca Nacional de España')",
            "autor": (g.get("autor personas") or g.get("autor entidades") or "")[:150], "fecha": fecha[:40],
            "anio": anio_de(fecha, titulo), "lugares": lugares[:12], "bbox": None,
            "escala": g.get("escala del mapa", "")[:60],
        })
    s.e["terminado"] = s.e["guardados"] > 0


# ---------------------------------------------------------------- Allmaps (mapas georreferenciados por la comunidad)
def allmaps(s, fin):
    candidatos = []
    for pagina in ["https://allmaps.org/", "https://allmaps.org/docs/", "https://dev.allmaps.org/",
                   "https://allmaps.org/docs/open-data/", "https://allmaps.org/open-data/"]:
        try:
            html_ = urllib.request.urlopen(urllib.request.Request(pagina, headers={"User-Agent": UA}), timeout=60).read().decode("utf-8", "replace")
        except Exception as e:
            print("Allmaps: no se pudo leer", pagina, e)
            continue
        enlaces = re.findall(r'href="([^"]+\.(?:ndjson|geojsonl|geojson|json)(?:\?[^"]*)?)"', html_)
        print("Allmaps: enlaces en", pagina, enlaces[:30])
        for e in enlaces:
            candidatos.append(urllib.parse.urljoin(pagina, e))
    # Preferir los formatos de una línea por mapa
    candidatos = sorted(set(candidatos), key=lambda u: (not u.split("?")[0].endswith(("ndjson", "geojsonl")), "maps" not in u, u))
    print("Allmaps: candidatos", candidatos)
    for url in candidatos:
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            r = urllib.request.urlopen(req, timeout=600)
        except Exception as e:
            print("Allmaps: no disponible", url, e)
            continue
        print("Allmaps: usando", url)
        n = 0
        for linea in r:
            try:
                d = json.loads(linea)
            except Exception:
                continue
            n += 1
            if n <= 2:
                print("ejemplo Allmaps:", json.dumps(d)[:1500])
            props = d.get("properties", d)
            geom = d.get("geometry") or props.get("geoMask") or props.get("geometry")
            bbox = None
            try:
                from itertools import chain
                cs = list(chain.from_iterable(geom["coordinates"][0:1]))
                if cs and isinstance(cs[0], (list, tuple)):
                    xs, ys = [c[0] for c in cs], [c[1] for c in cs]
                    bbox = [min(xs), min(ys), max(xs), max(ys)]
            except Exception:
                pass
            imagen = props.get("resourceId") or (props.get("resource") or {}).get("id")
            s.poner({
                "id": props.get("id") or imagen, "t": props.get("label") or props.get("title") or imagen or "",
                "url": props.get("id"), "th": None, "iiif": imagen,
                "lic": "Georreferencia CC0 (Allmaps); la imagen conserva la licencia de su institución (verificar)",
                "autor": "", "fecha": "", "anio": None, "lugares": [], "bbox": bbox,
                "proveedor": (imagen or "").split("/")[2] if imagen and "//" in imagen else None,
            })
        break
    s.e["terminado"] = True


# ---------------------------------------------------------------- Europeana por proveedor (BNE y otras bibliotecas)
PROVEEDORES = ["Biblioteca Nacional de España", "Biblioteca Virtual del Patrimonio Bibliográfico",
               "Biblioteca Digital Hispánica", "Institut Cartogràfic i Geològic de Catalunya",
               "Real Academia de la Historia"]
RE_MAPA_ES = re.compile(r"(?i)\b(carta|cartas|mapa|mapas|plano|planos|plan|descripci[oó]n|atlas|portulano|"
                        r"carte|map|karte|kaart|topogr\w*|corograf\w*|hidrogr\w*|geogr\w*)\b")


def proveedores(s, fin):
    i = s.e.setdefault("i", 0)
    cursor = s.e.get("cursor", "*")
    while time.time() < fin and i < len(PROVEEDORES):
        p = [("wskey", "api2demo"), ("query", "*"), ("qf", f'DATA_PROVIDER:"{PROVEEDORES[i]}"'), ("qf", "TYPE:IMAGE"),
             ("reusability", "open"), ("rows", "100"), ("profile", "rich"), ("cursor", cursor)]
        d = pedir_json("https://api.europeana.eu/record/v2/search.json?" + urllib.parse.urlencode(p))
        if d is None:
            break
        for r in d.get("items", []):
            titulo = " ".join(r.get("title") or [])
            tipos = " ".join(lista(r.get("dcTypeLangAware")) + lista(r.get("dcType")))
            if not RE_MAPA_ES.search(titulo + " " + tipos) or RE_NO_MAPA.search(titulo):
                s.e["no_mapa"] = s.e.get("no_mapa", 0) + 1
                continue
            lic = libre(" ".join(r.get("rights") or []))
            if not lic:
                s.e["descartados"] += 1
                continue
            s.poner({
                "id": r.get("id"), "t": titulo[:300], "url": (r.get("edmIsShownAt") or [r.get("guid")])[0],
                "th": (r.get("edmPreview") or [None])[0], "iiif": None, "lic": lic,
                "autor": "; ".join(lista(r.get("dcCreator")))[:150], "fecha": " ".join(lista(r.get("year")))[:40],
                "anio": anio_de(" ".join(lista(r.get("year"))), titulo), "lugares": lista(r.get("edmPlaceLabel"))[:12],
                "bbox": None, "proveedor": PROVEEDORES[i],
            })
        cursor = d.get("nextCursor")
        if not cursor:
            print("Proveedor terminado:", PROVEEDORES[i], "guardados", s.e["guardados"])
            i += 1
            cursor = "*"
        s.e["i"], s.e["cursor"] = i, cursor
        time.sleep(0.5)
    s.e["terminado"] = i >= len(PROVEEDORES)


FUENTES = {"ogm": ogm, "loc": loc, "ia": ia, "europeana": europeana, "dc": dc, "bne": bne, "allmaps": allmaps, "proveedores": proveedores}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fuente", choices=FUENTES)
    ap.add_argument("--minutos", type=float, default=300)
    a = ap.parse_args()
    s = Salida(a.fuente)
    if s.e.get("terminado") and not (a.fuente == "loc" and s.e.get("modo") != "tramos"):
        print(a.fuente, "ya terminado")
        return
    try:
        FUENTES[a.fuente](s, time.time() + a.minutos * 60)
    finally:
        s.cerrar()


if __name__ == "__main__":
    main()
