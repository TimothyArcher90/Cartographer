"""Une las partes del catálogo, elimina duplicados y construye índices por lugar y por siglo.

Uso: python scripts/indexar_catalogo.py
Salida:
  catalogo/indice/mapas-NNN.jsonl.gz (un mapa por línea, sin duplicados, en fragmentos)
  catalogo/indice/lugares.json     (lugar -> número de mapas), ordenado por frecuencia
  catalogo/indice/resumen.json     (totales por siglo, licencia, etc.)
"""
import gzip
import json
import re
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "catalogo"


RE_MAPA = re.compile(r"(?i)\b(map|maps|mapa|mapas|mappa|carte|cartes|karte|karten|landkarte|kaart|kaarten|"
                     r"plan|plano|planta|pianta|plattegrond|stadtplan|atlas|chart|portolan\w*|portulan\w*|"
                     r"me(?:ss|ß)tischbl\w*|topograph\w*|cartograph\w*|kartograf\w*|mappemonde|planisph\w*|"
                     r"globus|globe|sheet|blatt|feuille|hoja|1\s*:\s*\d[\d .,]{2,})\b")
RE_NO_MAPA = re.compile(r"(?i)postcard|carte postale|cartes postales|ansichtskarte|postkarte|vykort|"
                        r"\bfa[țt][ăa]\s*:|\bvedere\b|fotograf|photograph|\bphoto\b|portrait|retrato|bildnis")


# Fuentes generalistas: solo se admite el registro si el título indica que es un mapa.
FUENTES_GENERALISTAS = {"europeana", "ia"}


# Allmaps: imágenes de instituciones cuya licencia NO permite uso comercial.
ALLMAPS_EXCLUIR = ("davidrumsey.com", "gallica.bnf.fr")
INSTITUCIONES = {"iiif.nypl.org": "New York Public Library", "iiif.digitalcommonwealth.org": "Leventhal Map Center / Digital Commonwealth",
                 "iiif-server.lib.uchicago.edu": "University of Chicago", "map-view.nls.uk": "National Library of Scotland",
                 "iiif.lib.utexas.edu": "University of Texas", "rosetta.slv.vic.gov.au": "State Library Victoria",
                 "images.uba.uva.nl": "Universiteit van Amsterdam", "objects.library.uu.nl": "Universiteit Utrecht",
                 "iiif.archive.org": "Internet Archive", "iiif.universiteitleiden.nl": "Universiteit Leiden",
                 "tile.loc.gov": "Library of Congress", "stacks.stanford.edu": "Stanford University"}
RE_CLAVES = re.compile(r"(commonwealth(?:-oai)?:[a-z0-9]+)|stacks\.stanford\.edu/image/iiif/([a-z]{2}\d{3}[a-z]{2}\d{4})")


def claves(texto):
    out = []
    for a, b in RE_CLAVES.findall(texto or ""):
        if a:
            out.append(a.replace("commonwealth-oai:", "commonwealth:"))
        if b:
            out.append("stanford-" + b)
    return out


def siglo_de_anio(a):
    return (a - 1) // 100 + 1 if a and a > 0 else None


def main():
    mapas = {}
    for parte in sorted(DIR.glob("*/parte-*.jsonl.gz")):
        fuente = parte.parent.name
        with gzip.open(parte, "rt", encoding="utf-8") as f:
            for linea in f:
                try:
                    r = json.loads(linea)
                except json.JSONDecodeError:
                    continue
                r.setdefault("fuente", fuente)
                if fuente in FUENTES_GENERALISTAS and (not RE_MAPA.search(r.get("t") or "") or RE_NO_MAPA.search(r.get("t") or "")):
                    continue
                if fuente == "commons":
                    r.setdefault("url", "https://commons.wikimedia.org/wiki/File:" + r["t"].replace(" ", "_"))
                clave = (fuente, r.get("pid") or r.get("id") or r["t"])
                if clave in mapas:
                    v = mapas[clave]
                    v["lugares"] = sorted(set(v.get("lugares") or []) | set(r.get("lugares") or []))
                    v["siglos"] = sorted(set(v.get("siglos") or []) | set(r.get("siglos") or []))
                    if r.get("cat") and r["cat"] not in v.setdefault("cats", []):
                        v["cats"].append(r["cat"])
                else:
                    r["cats"] = [r.pop("cat")] if r.get("cat") else []
                    mapas[clave] = r
    # Fusionar Allmaps con la ficha del mismo mapa en otra fuente (gana título/año; suma georreferencia).
    por_clave = {}
    for k, r in mapas.items():
        if r["fuente"] != "allmaps":
            for c in claves(" ".join(str(x) for x in (r.get("id"), r.get("iiif"), r.get("url"), r.get("th")) if x)):
                por_clave[c] = k
    fusionados = excluidos = 0
    for k in [k for k, r in mapas.items() if r["fuente"] == "allmaps"]:
        r = mapas[k]
        dominio = (r.get("iiif") or "").split("/")[2] if "//" in (r.get("iiif") or "") else ""
        if any(x in dominio for x in ALLMAPS_EXCLUIR):
            del mapas[k]
            excluidos += 1
            continue
        destino = next((por_clave[c] for c in claves(r.get("iiif")) if c in por_clave), None)
        if destino:
            d = mapas[destino]
            d["bbox"] = r.get("bbox") or d.get("bbox")
            d["georreferenciado"] = r.get("url")
            del mapas[k]
            fusionados += 1
        else:
            r["proveedor"] = INSTITUCIONES.get(dominio, dominio)
            r["t"] = f"Mapa georreferenciado en Allmaps · {r['proveedor']}"
            r["georreferenciado"] = r.get("url")
    print(f"Allmaps: {fusionados} fusionados con su ficha, {excluidos} excluidos por licencia no comercial")
    salida = DIR / "indice"
    salida.mkdir(parents=True, exist_ok=True)
    lugares, siglos, licencias, fuentes = Counter(), Counter(), Counter(), Counter()
    for viejo in salida.glob("mapas-*.jsonl.gz"):
        viejo.unlink()
    # Fragmentos de 100 000 mapas para no superar el límite de 100 MB por archivo de GitHub.
    f, n, frag = None, 0, 0
    for r in mapas.values():
        if n % 100000 == 0:
            if f:
                f.close()
            f = gzip.open(salida / f"mapas-{frag:03d}.jsonl.gz", "wt", encoding="utf-8")
            frag += 1
        n += 1
        if not r.get("siglos") and siglo_de_anio(r.get("anio")):
            r["siglos"] = [siglo_de_anio(r["anio"])]
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
        lugares.update(x for x in (r.get("lugares") or []) if isinstance(x, str))
        siglos.update(r.get("siglos") or ["sin siglo"])
        licencias[r["lic"]] += 1
        fuentes[r["fuente"]] += 1
    if f:
        f.close()
    (salida / "lugares.json").write_text(json.dumps(dict(lugares.most_common()), ensure_ascii=False, indent=0),
                                        encoding="utf-8")
    (salida / "resumen.json").write_text(json.dumps({
        "mapas": len(mapas), "lugares_distintos": len(lugares), "por_fuente": dict(fuentes),
        "con_cobertura_geografica": sum(1 for r in mapas.values() if r.get("bbox")),
        "por_siglo": {str(k): v for k, v in sorted(siglos.items(), key=lambda t: (isinstance(t[0], str), t[0]))},
        "licencias": dict(licencias.most_common(30)),
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(mapas)} mapas únicos · {len(lugares)} lugares")


if __name__ == "__main__":
    main()
