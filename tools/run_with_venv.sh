#!/bin/bash
# Wrapper pro spuštění programu s virtuálním prostředím

# Získání kořenového adresáře projektu (rodič tohoto tools/ adresáře)
TOOLS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_DIR="$(dirname "$TOOLS_DIR")"

# Kontrola, zda venv existuje
if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo "❌ Virtuální prostředí neexistuje!"
    echo ""
    echo "Vytvořte ho pomocí:"
    echo "  python3 -m venv venv"
    echo "  source venv/bin/activate"
    echo "  pip install -r requirements.txt"
    echo ""
    echo "Nebo spusťte:"
    echo "  bash tools/setup_venv.sh"
    exit 1
fi

# Aktivace venv a spuštění programu
source "$PROJECT_DIR/venv/bin/activate"

if [ $# -eq 0 ]; then
    echo "Použití: $0 <soubor_s_grafem.tg>"
    echo ""
    echo "Příklad:"
    echo "  $0 data/grafy/01.tg"
    exit 1
fi

echo "🚀 Spouštím s virtuálním prostředím..."
echo "Python: $(which python3)"
echo ""

python3 "$PROJECT_DIR/scripts/run.py" "$@"

