#!/bin/bash
# Wrapper pro spuštění analýzy matic (Linux/Mac)

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

"$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$@"

