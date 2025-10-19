# Změny ve struktuře projektu

## 📋 Přehled reorganizace

Projekt byl kompletně restrukturalizován pro lepší organizaci a údržbu kódu.

## 🔄 Provedené změny

### 1. Vytvoření logické souborové struktury

```
PŘED:                           PO:
rozeznavac_grafu/              rozeznavac_grafu/
├── parser.py                  ├── src/               (zdrojové kódy)
├── graph.py                   ├── scripts/           (spouštěcí skripty)
├── analyzer.py                ├── docs/              (dokumentace)
├── matrices.py                ├── data/              (vstupní data)
├── visualizer.py              ├── output/            (výstupy)
├── run.py                     ├── tools/             (pomocné nástroje)
├── analyze_*.py               └── venv/              (virtuální prostředí)
├── README.md
├── DOKUMENTACE.md
├── grafy/
└── vykreslene_grafy/
```

### 2. Moduly přesunuty do `src/`

Všechny zdrojové Python moduly jsou nyní v `src/`:
- ✅ `parser.py` → `src/parser.py`
- ✅ `graph.py` → `src/graph.py`
- ✅ `analyzer.py` → `src/analyzer.py`
- ✅ `matrices.py` → `src/matrices.py`
- ✅ `visualizer.py` → `src/visualizer.py`
- ✅ Nový `src/__init__.py` pro export tříd

### 3. Skripty přesunuty do `scripts/`

- ✅ `run.py` → `scripts/run.py`
- ✅ `analyze_properties.py` → `scripts/analyze_properties.py`
- ✅ `analyze_matrices.py` → `scripts/analyze_matrices.py`

### 4. Dokumentace přesunuta do `docs/`

Všechna dokumentace je nyní centralizována:
- ✅ `README.md` → `docs/README.md` (původní)
- ✅ `DOKUMENTACE.md` → `docs/DOKUMENTACE.md`
- ✅ `INSTALACE_VENV.md` → `docs/INSTALACE_VENV.md`
- ✅ `POUZITI.md` → `docs/POUZITI.md`
- ✅ `READ_ME` → `docs/READ_ME`
- ✅ Nový `docs/STRUKTURA.md` (popis struktury)

### 5. Data přesunuta do `data/`

- ✅ `grafy/` → `data/grafy/`

### 6. Výstupy přesunuty do `output/`

- ✅ `vykreslene_grafy/` → `output/vykreslene_grafy/`

### 7. Nástroje přesunuty do `tools/`

- ✅ `install_libs.py` → `tools/install_libs.py`
- ✅ `test_venv.py` → `tools/test_venv.py`
- ✅ `setup_venv.sh` → `tools/setup_venv.sh`
- ✅ `run_with_venv.sh` → `tools/run_with_venv.sh`
- ✅ `vykresli_graf.py` → `tools/vykresli_graf.py`

### 8. Aktualizace importů

Všechny skripty byly aktualizovány pro import z `src/`:
```python
# PŘED:
from parser import GraphParser

# PO:
from src.parser import GraphParser
```

### 9. Aktualizace cest

Všechny cesty byly aktualizovány:
- Testovací grafy: `grafy/01.tg` → `data/grafy/01.tg`
- Výstupy: `vykreslene_grafy/` → `output/vykreslene_grafy/`

### 10. Nové soubory

- ✅ `README.md` (nový hlavní README)
- ✅ `QUICKSTART.md` (rychlý návod)
- ✅ `ZMENY.md` (tento soubor)
- ✅ `analyze.sh` (interaktivní spouštěcí skript)
- ✅ `.gitignore` (pravidla pro git)

## 🚀 Jak používat novou strukturu

### Základní použití

**Interaktivní režim:**
```bash
./analyze.sh
```

**Analýza vlastností:**
```bash
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg A B
```

**Analýza matic:**
```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/02.tg
```

**Kompletní analýza:**
```bash
./venv/bin/python scripts/run.py data/grafy/02.tg A B
```

### Import modulů v novém kódu

```python
from src.parser import GraphParser
from src.graph import Graph
from src.analyzer import GraphAnalyzer
from src.matrices import MatrixBuilder
from src.visualizer import visualize_graph
```

## 📁 Výhody nové struktury

### 1. **Čitelnost**
- Jasné oddělení zdrojových kódů, skriptů a dokumentace
- Snadná navigace v projektu

### 2. **Údržba**
- Moduly jsou logicky seskupeny
- Snadnější najít a upravit kód

### 3. **Škálovatelnost**
- Struktura připravena pro růst projektu
- Snadné přidávání nových modulů a skriptů

### 4. **Profesionalita**
- Standardní struktura Python projektů
- Připraveno pro případnou distribuci (PyPI)

### 5. **Bezpečnost**
- `.gitignore` chrání před commitováním nežádoucích souborů
- Oddělení výstupů od zdrojových kódů

## 🔍 Zpětná kompatibilita

Původní funkčnost zůstala **plně zachována**:
- ✅ Všechny funkce fungují stejně
- ✅ Stejné vstupy a výstupy
- ✅ Žádné změny v API

Jediné změny:
- Cesty k souborům (data/, output/)
- Import cesty (src/)

## 📚 Dokumentace

Aktualizovaná dokumentace:
- `README.md` - Hlavní přehled projektu
- `QUICKSTART.md` - Rychlý start
- `docs/POUZITI.md` - Detailní návod
- `docs/STRUKTURA.md` - Popis struktury
- `docs/DOKUMENTACE.md` - Technická dokumentace

## 🧪 Testování

Všechny funkce byly otestovány po reorganizaci:
- ✅ analyze_properties.py - Funguje
- ✅ analyze_matrices.py - Funguje
- ✅ run.py - Funguje
- ✅ Vizualizace - Funguje
- ✅ Výstupní soubory - Ukládají se správně

## 🎯 Další kroky (volitelné)

Pro budoucí vylepšení:
1. Vytvoření unit testů v `tests/`
2. Přidání CI/CD konfigurace
3. Vytvoření setup.py pro instalaci jako balíček
4. Dokumentace API pomocí Sphinx

## 📝 Poznámky

- Virtual environment (`venv/`) zůstal na stejném místě
- Všechny grafy v `data/grafy/` jsou zachovány
- Vykreslené grafy v `output/vykreslene_grafy/` jsou zachovány
- Žádné funkce nebyly odebrány nebo změněny

---

**Datum reorganizace:** 19. října 2025
**Verze:** 2.0 (restrukturalizovaná)

