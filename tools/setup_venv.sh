#!/bin/bash
# Skript pro nastavení virtuálního prostředí a instalaci knihoven

echo "🔧 Vytváření virtuálního prostředí..."
python3 -m venv venv

echo "✓ Virtuální prostředí vytvořeno"
echo ""

echo "📦 Aktivace venv a instalace knihoven..."
source venv/bin/activate

echo "Aktualizace pip..."
pip install --upgrade pip

echo ""
echo "Instalace knihoven pro vizualizaci..."
pip install matplotlib networkx graphviz

echo ""
echo "✓ Knihovny nainstalovány"
echo ""

echo "📋 Seznam nainstalovaných knihoven:"
pip list | grep -E "matplotlib|networkx|graphviz"

echo ""
echo "✅ Hotovo!"
echo ""
echo "Pro aktivaci venv v budoucnu použijte:"
echo "  source venv/bin/activate"
echo ""
echo "Pro spuštění programu ve venv:"
echo "  ./venv/bin/python3 run.py <soubor.tg>"

