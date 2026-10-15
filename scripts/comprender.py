"""Comprende el catálogo: asigna a cada mapa sus PAÍSES, su ESCALA, su TIPO y su SIGLO,
y construye la biblioteca por país.

Uso: python scripts/comprender.py
Entrada:  catalogo/indice/mapas-*.jsonl.gz
          catalogo/geo/paises.geojson        (Natural Earth 1:50m, dominio público; nombres en 25+ idiomas)
          catalogo/nombres_historicos.json   (nombres antiguos/latinos por país)
Salida:   catalogo/biblioteca/paises/<ISO3>.jsonl.gz  (mapas de cada país, orden cronológico)
          catalogo/biblioteca/paises.json              (por país: nombre, total, por siglo, por tipo, por vía)
          catalogo/biblioteca/resumen.json
          BIBLIOTECA.md                                (documento legible: todos los países y cifras)

Cómo se asigna un país (cada asignación guarda su 'via'):
  - nombre:      el título, los lugares o las categorías nombran el país (nombre actual en cualquier idioma)
  - historico:   nombran un nombre histórico/latino del país (catalogo/nombres_historicos.json)
  - coordenadas: la cobertura geográfica del mapa (bbox) cae sobre el país: el país ocupa >=10 % del
                 mapa o el mapa cubre >=30 % del país. Los mapamundis (>150° de ancho) no se asignan
                 por coordenadas, para no meter todos los países en cada mapamundi.
Se usa la coincidencia más larga (p. ej. 'Nueva Granada' gana a 'Granada'; 'New Mexico' gana a 'Mexico').
Si el mapa tiene coordenadas, un país nombrado solo se acepta si cae dentro de su cobertura (margen 2°):
así 'Smyrna, DE' (Delaware) no se asigna a Turquía. Los mapas de continente solo se asignan por
coordenadas a países que ocupen >=15 % del mapa. Un país pequeño solo entra por coordenadas si ocupa
>=2 % del mapa. Cada asignación lleva 'relevancia' (1 = nombrado; si no, fracción del mapa que ocupa).
"""
import gzip
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

from shapely.geometry import box, shape
from shapely.strtree import STRtree

RAIZ = Path(__file__).resolve().parent.parent
CAT = RAIZ / "catalogo"
IDIOMAS = ["NAME", "NAME_LONG", "NAME_EN", "NAME_ES", "NAME_FR", "NAME_DE", "NAME_IT", "NAME_PT", "NAME_NL",
           "NAME_PL", "NAME_SV", "NAME_HU", "NAME_TR", "NAME_EL", "NAME_RU", "NAME_UK", "NAME_ID", "NAME_VI",
           "NAME_AR", "NAME_FA", "NAME_HE", "NAME_ZH", "NAME_JA", "NAME_KO", "FORMAL_EN", "NAME_ALT"]

TIPOS = [
    ("portulano", r"portolan|portulan|portolano|portulano"),
    ("carta náutica", r"\bchart\b|nautical|carte marine|marine chart|sea chart|hydrograph|zeekaart|coast pilot|carta n[aá]utica"),
    ("ptolemaico", r"ptolem|tabula (?:prima|secunda|tertia|quarta|quinta|sexta|septima|octava|nona|decima|undecima|duodecima)|(?:europae|asiae|africae|aphricae) tab"),
    ("mapamundi", r"mappa ?mundi|orbis terrarum|world map|mapamundi|mappemonde|planisph|weltkarte|\bthe world\b|hemispher"),
    ("plano urbano", r"\bplan (?:of|de|du|von)\b|\bplano\b|\bpianta\b|stadtplan|city map|town plan|\bplattegrond"),
    ("topográfico", r"1\s*:\s*\d[\d,. ]{3,}|topograph|\bsheet\b|\bblatt\b|\bfeuille\b|\bhoja\b|ordnance survey"),
    ("militar", r"battle|siege|bataille|schlacht|batalla|campaign|fortif|military|war\b"),
    ("ferroviario/viario", r"railroad|railway|chemin de fer|eisenbahn|ferrocarril|road map|route"),
    ("histórico/temático", r"historical|ancient|antiqu|veteris|vetus|imperium|empire|geology|geolog|ethnograph|population"),
]


# Palabras comunes que coinciden con nombres de país en algún idioma (p. ej. "Island" = Islandia en alemán).
EXCLUIR_TERMINOS = {"island", "chad", "jordan", "niger", "georgia", "jersey", "guinea", "turkey red", "china clay",
                    "india rubber", "dominica", "panama canal zone", "cook islands", "christmas island"}
# Nombres de Estados Unidos que contienen nombres de país: al ser más largos, ganan la coincidencia.
EEUU = ["New Mexico", "New Jersey", "New York", "New Hampshire", "New England", "New Orleans", "New Holland, PA",
        "Lebanon, PA", "Lebanon, OH", "Lebanon, TN", "Lebanon, IN", "Lebanon, MO", "Lebanon, NH", "Lebanon, KY",
        "Mexico, MO", "Mexico, NY", "Mexico, ME", "Peru, IN", "Peru, IL", "Peru, NY", "Poland, ME", "Poland, OH",
        "Norway, ME", "Denmark, SC", "Denmark, WI", "Canton, OH", "Canton, MS", "Canton, GA", "Athens, GA",
        "Athens, OH", "Athens, TN", "Paris, TX", "Paris, TN", "Paris, KY", "Rome, GA", "Rome, NY", "Cairo, IL"]


def norm(t):
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", t).strip()


def cargar_paises():
    datos = json.loads((CAT / "geo/paises.geojson").read_text(encoding="utf-8"))
    paises, geoms, codigos, terminos = {}, [], [], {}
    hist = {k: v for k, v in json.loads((CAT / "nombres_historicos.json").read_text(encoding="utf-8")).items()
            if not k.startswith("_")}
    for f in datos["features"]:
        p = f["properties"]
        iso = p.get("ISO_A3") if p.get("ISO_A3") not in (None, "-99") else p.get("ADM0_A3")
        if not iso:
            continue
        g = shape(f["geometry"])
        if iso in paises:
            paises[iso]["geom"] = paises[iso]["geom"].union(g)
        else:
            paises[iso] = {"iso": iso, "nombre_es": p.get("NAME_ES") or p.get("NAME"), "geom": g,
                           "continente": p.get("CONTINENT"), "region": p.get("SUBREGION")}
        for c in IDIOMAS:
            v = p.get(c)
            if v and len(norm(v)) >= 4:
                terminos.setdefault(norm(v), set()).add((iso, "nombre"))
    for v in EEUU:
        terminos.setdefault(norm(v), set()).add(("USA", "nombre"))
    for t in EXCLUIR_TERMINOS:
        terminos.pop(t, None)
    for iso, lista in hist.items():
        for v in lista:
            if len(norm(v)) >= 4:
                terminos.setdefault(norm(v), set()).add((iso, "historico"))
    for iso, d in paises.items():
        geoms.append(d["geom"])
        codigos.append(iso)
    # Expresión única: términos más largos primero (gana la coincidencia más larga).
    orden = sorted(terminos, key=len, reverse=True)
    patron = re.compile(r"(?<![a-z0-9])(" + "|".join(re.escape(t) for t in orden) + r")(?![a-z0-9])")
    return paises, STRtree(geoms), geoms, codigos, terminos, patron


def escala(b):
    if not b or None in b:
        return "desconocida"
    ancho = abs(b[2] - b[0])
    if ancho > 150:
        return "mundo"
    if ancho > 40:
        return "continente"
    if ancho > 8:
        return "región o país"
    if ancho > 1:
        return "provincia o comarca"
    return "local o ciudad"


def tipo_de(texto, esc):
    t = norm(texto)
    for nombre, rx in TIPOS:
        if re.search(rx, t):
            return nombre
    if esc == "mundo":
        return "mapamundi"
    return "general"


def main():
    paises, arbol, geoms, codigos, terminos, patron = cargar_paises()
    salida = CAT / "biblioteca"
    (salida / "paises").mkdir(parents=True, exist_ok=True)
    for viejo in (salida / "paises").glob("*.jsonl.gz"):
        viejo.unlink()
    por_pais = defaultdict(list)
    est = defaultdict(lambda: {"total": 0, "siglos": Counter(), "tipos": Counter(), "vias": Counter(), "fuentes": Counter()})
    total, sin_pais, tipos_glob, escalas_glob, descartes = 0, 0, Counter(), Counter(), Counter()

    for frag in sorted((CAT / "indice").glob("mapas-*.jsonl.gz")):
        with gzip.open(frag, "rt", encoding="utf-8") as f:
            for linea in f:
                r = json.loads(linea)
                total += 1
                texto = " ".join([r.get("t") or ""] + [str(x) for x in (r.get("lugares") or [])]
                                 + [str(x) for x in (r.get("cats") or [])])
                asign, peso = {}, {}
                corregido = False
                for m in patron.finditer(norm(texto)):
                    for iso, via in terminos[m.group(1)]:
                        if via == "nombre" or iso not in asign:
                            asign[iso] = via
                b = r.get("bbox")
                esc = escala(b)
                if b and None not in b and esc != "mundo":
                    o, s, e, n = b
                    caja = box(min(o, e), min(s, n), max(o, e), max(s, n))
                    # 1) Validar los países nombrados: deben caer dentro de la cobertura (margen 2°).
                    margen = caja.buffer(2)
                    cerca = {codigos[i] for i in arbol.query(margen) if geoms[i].intersects(margen)}
                    # 1b) Coordenadas con el signo cambiado en la fuente (p. ej. latitud sur en vez de norte):
                    #     si ningún país nombrado cae en la cobertura pero sí en la cobertura con el signo
                    #     invertido, se corrige la caja y se anota.
                    if asign and not (set(asign) & cerca):
                        for fo, fs in ((1, -1), (-1, 1), (-1, -1)):
                            c2 = box(min(fo * o, fo * e), min(fs * s, fs * n), max(fo * o, fo * e), max(fs * s, fs * n))
                            m2 = c2.buffer(2)
                            cerca2 = {codigos[i] for i in arbol.query(m2) if geoms[i].intersects(m2)}
                            if set(asign) & cerca2:
                                caja, margen, cerca = c2, m2, cerca2
                                b = [round(c2.bounds[0], 4), round(c2.bounds[1], 4), round(c2.bounds[2], 4), round(c2.bounds[3], 4)]
                                corregido = True
                                descartes["coordenadas con signo corregido"] += 1
                                break
                    for iso in list(asign):
                        if iso not in cerca:
                            del asign[iso]
                            descartes["nombre fuera de la cobertura del mapa"] += 1
                    # 2) Añadir países por coordenadas.
                    umbral = 0.15 if esc == "continente" else 0.10
                    for i in arbol.query(caja):
                        g, iso = geoms[i], codigos[i]
                        if iso in asign:
                            continue
                        if caja.area == 0:
                            if g.contains(caja.centroid):
                                asign[iso] = "coordenadas"
                            continue
                        inter = caja.intersection(g).area
                        cuota_mapa = inter / caja.area
                        cuota_pais = inter / g.area if g.area else 0
                        if cuota_mapa >= umbral or (esc != "continente" and cuota_pais >= 0.30 and cuota_mapa >= 0.02):
                            asign[iso] = "coordenadas"
                            peso[iso] = round(cuota_mapa, 3)
                tipo = tipo_de(texto, esc)
                tipos_glob[tipo] += 1
                escalas_glob[esc] += 1
                if not asign:
                    sin_pais += 1
                    continue
                anio = r.get("anio")
                fila = {"t": r.get("t"), "anio": anio, "siglos": r.get("siglos"), "tipo": tipo, "escala": esc,
                        "fuente": r.get("fuente"), "url": r.get("url"), "th": r.get("th"), "iiif": r.get("iiif"),
                        "lic": r.get("lic"), "autor": r.get("autor"), "bbox": b, "paises": sorted(asign)}
                if corregido:
                    fila["bbox_corregido"] = True
                for iso, via in asign.items():
                    # relevancia: nombrado en el mapa = 1; por coordenadas = parte del mapa que ocupa el país
                    por_pais[iso].append(dict(fila, via=via, relevancia=peso.get(iso, 1.0)))
                    x = est[iso]
                    x["total"] += 1
                    for sg in (r.get("siglos") or ["sin siglo"]):
                        x["siglos"][sg] += 1
                    x["tipos"][tipo] += 1
                    x["vias"][via] += 1
                    x["fuentes"][r.get("fuente")] += 1

    for iso, filas in por_pais.items():
        filas.sort(key=lambda r: (r.get("anio") or 9999, r.get("t") or ""))
        with gzip.open(salida / "paises" / f"{iso}.jsonl.gz", "wt", encoding="utf-8") as f:
            for r in filas:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    resumen_paises = {}
    for iso, x in sorted(est.items(), key=lambda t: -t[1]["total"]):
        d = paises.get(iso, {})
        resumen_paises[iso] = {
            "nombre_es": d.get("nombre_es", iso), "continente": d.get("continente"), "total": x["total"],
            "por_siglo": {str(k): v for k, v in sorted(x["siglos"].items(), key=lambda t: (isinstance(t[0], str), t[0]))},
            "por_tipo": dict(x["tipos"].most_common()), "por_via": dict(x["vias"]), "por_fuente": dict(x["fuentes"]),
        }
    (salida / "paises.json").write_text(json.dumps(resumen_paises, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "resumen.json").write_text(json.dumps({
        "mapas_analizados": total, "con_pais": total - sin_pais, "sin_pais": sin_pais,
        "paises_con_mapas": len(resumen_paises), "por_tipo": dict(tipos_glob.most_common()),
        "por_escala": dict(escalas_glob.most_common()), "descartes": dict(descartes),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    escribir_documento(resumen_paises, total, sin_pais, tipos_glob, escalas_glob)
    print(f"{total} mapas · {total - sin_pais} con país · {len(resumen_paises)} países")


def escribir_documento(rp, total, sin_pais, tipos, escalas):
    siglos = ["9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    filas = []
    for iso, d in sorted(rp.items(), key=lambda t: t[1]["nombre_es"] or t[0]):
        ps = d["por_siglo"]
        antes = sum(v for k, v in ps.items() if k.isdigit() and int(k) < 9)
        filas.append(f"| {d['nombre_es']} | {iso} | {d['total']:,} | {antes or ''} | "
                     + " | ".join(f"{ps.get(s, 0):,}" if ps.get(s) else "" for s in siglos) + " |")
    doc = f"""# Biblioteca de Cartographer

Documento generado por `scripts/comprender.py`. No editar a mano.

- Mapas analizados: **{total:,}** · con país asignado: **{total - sin_pais:,}** · sin país: {sin_pais:,}
  (sobre todo mapamundis, cartas oceánicas o registros sin datos de lugar).
- Países con mapas: **{len(rp)}**.
- Tipos: {", ".join(f"{k} {v:,}" for k, v in tipos.most_common())}.
- Escalas: {", ".join(f"{k} {v:,}" for k, v in escalas.most_common())}.

Cómo se asigna un país: por **nombre** actual (25+ idiomas, Natural Earth), por **nombre histórico**
(`catalogo/nombres_historicos.json`) o por **coordenadas** de la cobertura del mapa. Cada mapa guarda
la vía en el campo `via`; las asignaciones por coordenadas de mapas grandes pueden incluir países
vecinos. Los siglos salen del año de los metadatos de cada archivo y pueden tener errores puntuales.

Mapas de un país: `catalogo/biblioteca/paises/<ISO3>.jsonl.gz` o
`python scripts/buscar_lugar.py "<país>"`.

| País | ISO | Total | Antes del s. IX | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XIX | XX |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
""" + "\n".join(filas) + "\n"
    (RAIZ / "BIBLIOTECA.md").write_text(doc, encoding="utf-8")


if __name__ == "__main__":
    main()
