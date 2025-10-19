#!/bin/bash
# Wrapper pro spuštění kompletní analýzy (Linux/Mac)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

"$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/run.py" "$@"

