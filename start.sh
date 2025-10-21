#!/bin/bash
# Spouštěč hlavního interaktivního programu (Linux/Mac)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Aktivace virtual environment (pokud existuje)
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Spuštění programu
python3 main.py "$@"

