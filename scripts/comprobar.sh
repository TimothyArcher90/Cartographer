#!/usr/bin/env bash
# Ejecuta toda la cadena y las validaciones. Sale con error si algo falla.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PYTHON:-python3}
$PY scripts/normalizar_epocas.py
# Prueba interna del código (sintética, fuera de mapas/ y del paquete).
$PY pruebas/generar_prueba_sintetica.py
$PY scripts/georreferenciar.py pruebas/salida/prueba-sintetica
# Mapas históricos reales.
for d in mapas/*/; do [ -f "$d/ficha.json" ] || continue; $PY scripts/georreferenciar.py "$d"; done
$PY pruebas/comprobar_sintetica.py
$PY scripts/empaquetar.py
$PY scripts/validar.py
if [ "${CAPTURAS:-1}" = "1" ]; then node scripts/capturas.mjs; fi
echo "TODO CORRECTO"
