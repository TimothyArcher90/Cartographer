"""Une las partes del catálogo, elimina duplicados y construye índices por lugar y por siglo.

Uso: python scripts/indexar_catalogo.py
Salida:
  catalogo/indice/mapas-NNN.jsonl.gz (un mapa por línea, sin duplicados, en fragmentos)
  catalogo/indice/lugares.json     (lugar -> número de mapas), ordenado por frecuencia
  catalogo/indice/resumen.json     (totales por siglo, licencia, etc.)
"""
import gzip
import json
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DIR = RAIZ / "catalogo"


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
