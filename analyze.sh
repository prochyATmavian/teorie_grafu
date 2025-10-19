#!/bin/bash
# Pomocný skript pro snadné spouštění analýzy grafů

PROJECT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Barvy pro výstup
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}╔══════════════════════════════════════════╗${NC}"
echo -e "${BLUE}║     Rozpoznávač grafů - Quick Start      ║${NC}"
echo -e "${BLUE}╚══════════════════════════════════════════╝${NC}"
echo ""

# Kontrola virtuálního prostředí
if [ ! -d "$PROJECT_DIR/venv" ]; then
    echo "❌ Virtuální prostředí nebylo nalezeno!"
    echo ""
    echo "Vytvořte ho pomocí:"
    echo "  bash tools/setup_venv.sh"
    exit 1
fi

# Aktivace venv
source "$PROJECT_DIR/venv/bin/activate"

# Menu
echo "Vyberte akci:"
echo "  1) Analýza vlastností grafu + uzly"
echo "  2) Analýza matic (interaktivní)"
echo "  3) Kompletní analýza"
echo ""
read -p "Volba (1-3): " choice

if [ -z "$1" ]; then
    echo ""
    echo "Zadejte cestu k souboru s grafem:"
    echo "  (např: data/grafy/02.tg)"
    read -p "Soubor: " filepath
else
    filepath="$1"
fi

# Kontrola existence souboru
if [ ! -f "$PROJECT_DIR/$filepath" ]; then
    echo "❌ Soubor '$filepath' neexistuje!"
    exit 1
fi

echo ""
echo -e "${GREEN}🚀 Spouštím analýzu...${NC}"
echo ""

case $choice in
    1)
        # Analýza vlastností
        if [ -n "$2" ]; then
            # Zadány uzly
            shift
            python3 "$PROJECT_DIR/scripts/analyze_properties.py" "$PROJECT_DIR/$filepath" "$@"
        else
            echo "Zadejte uzly pro detailní analýzu (oddělené mezerou, Enter pro přeskočení):"
            read -p "Uzly: " nodes
            if [ -n "$nodes" ]; then
                python3 "$PROJECT_DIR/scripts/analyze_properties.py" "$PROJECT_DIR/$filepath" $nodes
            else
                python3 "$PROJECT_DIR/scripts/analyze_properties.py" "$PROJECT_DIR/$filepath"
            fi
        fi
        ;;
    2)
        # Analýza matic (interaktivní)
        python3 "$PROJECT_DIR/scripts/analyze_matrices.py" "$PROJECT_DIR/$filepath"
        ;;
    3)
        # Kompletní analýza
        if [ -n "$2" ]; then
            shift
            python3 "$PROJECT_DIR/scripts/run.py" "$PROJECT_DIR/$filepath" "$@"
        else
            echo "Zadejte uzly pro detailní analýzu (oddělené mezerou, Enter pro přeskočení):"
            read -p "Uzly: " nodes
            if [ -n "$nodes" ]; then
                python3 "$PROJECT_DIR/scripts/run.py" "$PROJECT_DIR/$filepath" $nodes
            else
                python3 "$PROJECT_DIR/scripts/run.py" "$PROJECT_DIR/$filepath"
            fi
        fi
        ;;
    *)
        echo "❌ Neplatná volba!"
        exit 1
        ;;
esac

