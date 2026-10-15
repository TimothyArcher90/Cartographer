"""Genera el paquete exportable en paquetes/cartographer/ (formato descrito en paquetes/FORMATO.md).

Uso: python scripts/empaquetar.py
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun import AVISO_FRONTERAS, RAIZ, escribir_json, fuente, leer_json  # noqa: E402

FORMATO = "cartographer-paquete"
VERSION_FORMATO = 1


def main():
    destino = RAIZ / "paquetes/cartographer"
    if destino.exists():
        shutil.rmtree(destino)
    (destino / "epocas").mkdir(parents=True)
    (destino / "mapas").mkdir()

    epocas = []
    for e in leer_json(RAIZ / "epocas/indice.json")["epocas"]:
        nombre = Path(e["archivo"]).name
        shutil.copy(RAIZ / e["archivo"], destino / "epocas" / nombre)
        f = fuente(e["fuente"])
        epocas.append({
            "id": e["id"], "anio": e["anio"], "titulo": e["titulo"], "nota": e.get("nota"),
            "archivo": f"epocas/{nombre}", "entidades": e["entidades"],
            "aviso": AVISO_FRONTERAS,
            "fuente": {"id": f["id"], "nombre": f["nombre"], "url": f["url"], "commit": f.get("commit")},
            "licencia": f["licencia"],
        })

    mapas = []
    for ficha_ruta in sorted((RAIZ / "mapas").glob("*/ficha.json")):
        m = leer_json(ficha_ruta)
        if m.get("modo") != "superpuesto" or "salida" not in m:
            continue
        nombre = f"{m['id']}.png"
        shutil.copy(ficha_ruta.parent / m["salida"]["vista"], destino / "mapas" / nombre)
        mapas.append({
            "id": m["id"], "titulo": m["titulo"], "autor": m["autor"], "anio": m["anio"],
            "imagen": f"mapas/{nombre}", "esquinas": m["limites"],
            "esquinas_orden": "noroeste, noreste, sureste, suroeste (lon, lat)",
            "error_medio_km": m["error_medio_km"], "modo": m["modo"],
            "licencia": m["licencia"], "licencia_verificada": m["licencia_verificada"],
            "uso_en_video": m["uso_en_video"], "url": m["url"], "calidad": m["calidad"],
        })

    escribir_json(destino / "catalogo.json", {
        "formato": FORMATO, "version_formato": VERSION_FORMATO,
        "aviso_fronteras": AVISO_FRONTERAS,
        "epocas": epocas, "mapas": mapas,
    })
    shutil.copy(RAIZ / "fuentes/historical-basemaps.LICENSE.txt", destino / "LICENSE-historical-basemaps.txt")
    print(f"Paquete: {len(epocas)} épocas, {len(mapas)} mapas -> {destino}")


if __name__ == "__main__":
    main()
