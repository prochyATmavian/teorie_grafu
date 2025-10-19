#!/bin/bash
# Test skript pro testování interaktivního výběru matic

TESTS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$TESTS_DIR")"

echo "╔══════════════════════════════════════════════════════════╗"
echo "║          TESTY INTERAKTIVNÍHO VÝBĚRU MATIC               ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

echo "=== TEST 1: Interaktivní režim - Matice sousednosti, celá matice ==="
echo -e "a\nn\n" | "$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/data/grafy/01.tg"

echo ""
echo "=== TEST 2: Interaktivní režim - Matice délek, index [0][1] ==="
echo -e "e\na\n0\n1\n" | "$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/data/grafy/01.tg"

echo ""
echo "=== TEST 3: Všechny matice, index [2][4] ==="
echo -e "*\na\n2\n4\n" | "$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/data/grafy/01.tg"

echo ""
echo "=== TEST 4: Režim --all (všechny matice) ==="
"$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/data/grafy/01.tg" --all | head -30

echo ""
echo "=== TEST 5: Režim --all s indexem [2][4] ==="
"$PROJECT_DIR/venv/bin/python" "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/data/grafy/01.tg" --all 2 4

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                    TESTY DOKONČENY                       ║"
echo "╚══════════════════════════════════════════════════════════╝"

