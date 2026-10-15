#!/usr/bin/env bash
# Ejecuta toda la cadena y las validaciones. Sale con error si algo falla.
set -euo pipefail
cd "$(dirname "$0")/.."
PY=${PYTHON:-python3}
$PY scripts/normalizar_epocas.py
$PY pruebas/generar_prueba_sintetica.py
for d in mapas/*/; do [ -f "$d/ficha.json" ] && $PY scripts/georreferenciar.py "$d"; done
$PY pruebas/comprobar_sintetica.py
$PY scripts/empaquetar.py
$PY scripts/validar.py
if [ "${CAPTURAS:-1}" = "1" ]; then node scripts/capturas.mjs; fi
echo "TODO CORRECTO"
