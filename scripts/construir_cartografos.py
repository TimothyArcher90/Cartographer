"""Índice por cartógrafo para la galería: studio/datos/cartografos/<clave>.json y cartografos.json.

Busca el nombre del cartógrafo en autor y título (variantes latinas incluidas). Solo registros con imagen.
"""
import glob
import gzip
import json
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARTOGRAFOS = {
    "mercator": ("Gerardus Mercator", r"mercator"),
    "ortelius": ("Abraham Ortelius", r"ortel(?:ius|ii)"),
    "blaeu": ("Blaeu (Willem y Joan)", r"blaeu|blaev|blaeuw"),
    "hondius": ("Hondius", r"hondius|hondii"),
    "janssonius": ("Jan Janssonius", r"jans+on(?:ius|ii)"),
    "ptolomeo": ("Claudio Ptolomeo (ediciones)", r"ptolem|ptolom|ptolomeo"),
    "munster": ("Sebastian Münster", r"m[uü]nster(?:us)?\b(?!.*abbey)"),
    "waldseemuller": ("Martin Waldseemüller", r"waldseem"),
    "sanson": ("Nicolas Sanson", r"\bsanson\b"),
    "delisle": ("Guillaume de L'Isle", r"de ?l'?isle|delisle"),
    "danville": ("Jean-Baptiste d'Anville", r"d'?anville"),
    "homann": ("Johann Baptist Homann", r"homann"),
    "seutter": ("Matthäus Seutter", r"seutter"),
    "visscher": ("Nicolaes Visscher", r"visscher"),
    "dewit": ("Frederik de Wit", r"\bde wit\b|\bf\. de wit"),
    "speed": ("John Speed", r"\bjohn speed\b|\bspeed, john"),
    "cassini": ("Cassini", r"cassini"),
    "coronelli": ("Vincenzo Coronelli", r"coronelli"),
    "bellin": ("Jacques-Nicolas Bellin", r"\bbellin\b"),
    "vaugondy": ("Robert de Vaugondy", r"vaugondy"),
    "arrowsmith": ("Aaron Arrowsmith", r"arrowsmith"),
    "cary": ("John Cary", r"\bcary,? john|\bjohn cary\b|cary's"),
    "lopez": ("Tomás López", r"tom[aá]s l[oó]pez|lopez de vargas"),
    "codazzi": ("Agustín Codazzi", r"codazzi"),
    "humboldt": ("Alexander von Humboldt", r"humboldt"),
    "piri-reis": ("Piri Reis", r"piri re[iï]s"),
    "delacosa": ("Juan de la Cosa", r"juan de la cosa"),
    "mitchell": ("Samuel Augustus Mitchell", r"\bmitchell, s|s\. augustus mitchell|samuel augustus mitchell"),
    "colton": ("Colton", r"\bcolton\b"),
    "stieler": ("Adolf Stieler", r"stieler"),
}


def main():
    pats = {k: re.compile(v[1], re.I) for k, v in CARTOGRAFOS.items()}
    salida = {k: [] for k in CARTOGRAFOS}
    for p in sorted(glob.glob(str(RAIZ / "catalogo/indice/mapas-*.jsonl.gz"))):
        for l in gzip.open(p, "rt", encoding="utf-8"):
            r = json.loads(l)
            if not (r.get("th") or r.get("iiif")):
                continue
            texto = f"{r.get('autor') or ''} {r.get('t') or ''}"
            for k, pat in pats.items():
                if pat.search(texto):
                    salida[k].append({x: r.get(x) for x in ("t", "anio", "th", "iiif", "url", "lic", "autor", "fuente")})
    destino = RAIZ / "studio/datos/cartografos"
    destino.mkdir(parents=True, exist_ok=True)
    resumen = {}
    for k, lista in salida.items():
        lista.sort(key=lambda r: (r["anio"] or 9999))
        (destino / f"{k}.json").write_text(json.dumps(lista[:4000], ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        resumen[k] = {"nombre": CARTOGRAFOS[k][0], "total": len(lista)}
    (RAIZ / "studio/datos/cartografos.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=0), encoding="utf-8")
    for k, v in sorted(resumen.items(), key=lambda t: -t[1]["total"]):
        print(v["total"], v["nombre"])


if __name__ == "__main__":
    main()
