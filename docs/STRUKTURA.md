# Struktura projektu

Tento dokument popisuje logickou organizaci projektu Rozpoznávač grafů.

## 📂 Přehled struktury

```
rozeznavac_grafu/
│
├── src/                         Zdrojové kódy knihoven
│   ├── __init__.py             Inicializace balíčku + exporty
│   ├── parser.py               Parser grafů z .tg souborů
│   ├── graph.py                Třída Graph a operace s grafy
│   ├── analyzer.py             Analýza vlastností grafů
│   ├── matrices.py             Vytváření matic
│   └── visualizer.py           Vizualizace grafů
│
├── scripts/                     Spouštěcí skripty
│   ├── analyze_properties.py  Analýza vlastností + uzly
│   ├── analyze_matrices.py    Analýza matic
│   └── run.py                  Kompletní analýza
│
├── data/                        Vstupní data
│   └── grafy/                  Grafové soubory .tg
│       ├── 01.tg
│       ├── 02.tg
│       └── ...                 Všechny testovací grafy
│
├── output/                      Výstupní soubory
│   └── vykreslene_grafy/       PNG obrázky grafů
│
├── docs/                        Dokumentace
│   ├── README.md               Základní dokumentace
│   ├── POUZITI.md              Návod k použití
│   ├── DOKUMENTACE.md          Technická dokumentace
│   ├── INSTALACE_VENV.md       Instalační návod
│   ├── STRUKTURA.md            Tento soubor
│   └── READ_ME                 Původní poznámky
│
├── tools/                       Pomocné nástroje
│   ├── install_libs.py         Instalátor knihoven
│   ├── test_venv.py            Test virtuálního prostředí
│   ├── setup_venv.sh           Vytvoření venv
│   └── run_with_venv.sh        Wrapper pro spuštění s venv
│
├── venv/                        Virtuální prostředí Python
├── analyze.sh                   Interaktivní spouštěcí skript
├── requirements.txt             Python závislosti
├── .gitignore                   Git ignore pravidla
└── README.md                    Hlavní README
```

## 📦 Moduly (src/)

### `__init__.py`
Inicializační soubor balíčku, který exportuje hlavní třídy a funkce:
- `GraphParser`, `Node`, `Edge`
- `Graph`
- `GraphAnalyzer`
- `MatrixBuilder`
- `visualize_graph`, `TextVisualizer`

### `parser.py`
**Účel:** Parsování grafů z textových souborů formátu `.tg`

**Třídy:**
- `Node` - Reprezentace uzlu
- `Edge` - Reprezentace hrany
- `GraphParser` - Parser pro načítání grafů

**Formát vstupních souborů:**
```
u A;              # Uzel
u B 5;            # Uzel s ohodnocením
h A - B;          # Neorientovaná hrana
h A > B 10 :h1;   # Orientovaná hrana s váhou a označením
```

### `graph.py`
**Účel:** Reprezentace grafu a základní operace

**Třída `Graph`:**
- `get_neighbors()` - Získání sousedů
- `get_successors()` - Následníci (U+)
- `get_predecessors()` - Předchůdci (U-)
- `get_degree()` - Stupeň uzlu
- `bfs()` - Prohledávání do šířky

### `analyzer.py`
**Účel:** Analýza vlastností grafů

**Třída `GraphAnalyzer`:**
- `is_weighted()` - a) Ohodnocený
- `is_directed()` - b) Orientovaný
- `is_connected()` - c) Souvislý
- `is_simple()` - d) Prostý
- `is_loop_free()` - e) Jednoduchý
- `is_planar()` - f) Rovinný
- `is_finite()` - g) Konečný
- `is_complete()` - h) Úplný
- `is_regular()` - i) Regulární
- `is_bipartite()` - j) Bipartitní

### `matrices.py`
**Účel:** Vytváření matic a seznamů

**Třída `MatrixBuilder`:**
- `adjacency_matrix()` - Matice sousednosti
- `signed_matrix()` - Znaménková matice
- `adjacency_matrix_powers()` - Mocniny matice
- `incidence_matrix()` - Matice incidence
- `distance_matrix()` - Matice délek (Floyd-Warshall)
- `neighbor_list()` - Seznam sousedů

### `visualizer.py`
**Účel:** Vizualizace grafů

**Třídy a funkce:**
- `TextVisualizer` - Textová vizualizace
- `visualize_graph()` - Univerzální funkce
- `try_matplotlib_visualization()` - Matplotlib/NetworkX
- `try_graphviz_visualization()` - Graphviz

## 🚀 Skripty (scripts/)

### `analyze_properties.py`
**Co dělá:**
- Vizualizace grafu (textová + grafická)
- Analýza vlastností (a-j)
- Detaily o vybraných uzlech (k-s)

**Použití:**
```bash
python scripts/analyze_properties.py data/grafy/02.tg
python scripts/analyze_properties.py data/grafy/02.tg A B C
```

### `analyze_matrices.py`
**Co dělá:**
- Matice sousednosti
- Znaménková matice
- Mocniny matic (pro grafy ≤10 uzlů)
- Matice incidence
- Matice délek
- Seznam sousedů

**Použití:**
```bash
python scripts/analyze_matrices.py data/grafy/02.tg
```

### `run.py`
**Co dělá:**
- Kompletní analýza (vlastnosti + uzly + matice)

**Použití:**
```bash
python scripts/run.py data/grafy/02.tg A B
```

## 📊 Data (data/)

### `grafy/`
Obsahuje testovací grafové soubory ve formátu `.tg`:
- `01.tg` až `20.tg` - Standardní testovací grafy
- `custom*.tg` - Vlastní grafy

## 📤 Výstupy (output/)

### `vykreslene_grafy/`
Automaticky generované PNG obrázky grafů:
- Názvy: `graf_<jmeno_souboru>.png`
- Formát: PNG, 150 DPI
- Používá matplotlib nebo graphviz

## 📚 Dokumentace (docs/)

- **README.md** - Základní přehled
- **POUZITI.md** - Detailní návod k použití s příklady
- **DOKUMENTACE.md** - Kompletní technická dokumentace
- **INSTALACE_VENV.md** - Instalace virtuálního prostředí
- **STRUKTURA.md** - Tento soubor
- **READ_ME** - Původní poznámky k projektu

## 🔧 Nástroje (tools/)

### `install_libs.py`
Python skript pro instalaci závislostí

### `test_venv.py`
Test funkčnosti virtuálního prostředí

### `setup_venv.sh`
Bash skript pro vytvoření a nastavení venv

### `run_with_venv.sh`
Wrapper pro spuštění s aktivovaným venv

## 🎯 Pomocné soubory

### `analyze.sh`
Interaktivní skript pro snadné spouštění analýz.
Poskytuje menu pro výběr typu analýzy.

**Použití:**
```bash
./analyze.sh
./analyze.sh data/grafy/02.tg
```

### `requirements.txt`
Seznam Python závislostí:
- matplotlib
- networkx
- numpy
- graphviz (Python balíček)

### `.gitignore`
Pravidla pro ignorování souborů v git:
- `__pycache__/`
- `venv/`
- `output/vykreslene_grafy/*.png`
- `.DS_Store`, `.vscode/`, atd.

## 🔄 Import struktura

Všechny skripty ve `scripts/` importují z `src/` takto:

```python
import sys
from pathlib import Path

# Přidání kořenového adresáře do sys.path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import GraphParser
from src.graph import Graph
from src.analyzer import GraphAnalyzer
# ...
```

## 📝 Cesty v kódu

Všechny cesty jsou relativní vůči kořenovému adresáři projektu:

```python
# Testovací soubor
test_file = Path(__file__).parent.parent / "data" / "grafy" / "01.tg"

# Výstupní adresář
output_dir = Path(__file__).parent.parent / "output" / "vykreslene_grafy"
```

## 🚀 Spouštění

### Z kořenového adresáře:
```bash
# Použití analyze.sh (doporučeno)
./analyze.sh data/grafy/02.tg

# Přímo přes Python
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg A B
./venv/bin/python scripts/analyze_matrices.py data/grafy/02.tg
./venv/bin/python scripts/run.py data/grafy/02.tg A B

# Přes wrapper
bash tools/run_with_venv.sh data/grafy/02.tg
```

### Z jiného adresáře:
```bash
cd /path/to/rozeznavac_grafu
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg
```

## 🔐 Oprávnění

Spustitelné soubory (.sh) vyžadují execute práva:
```bash
chmod +x analyze.sh
chmod +x tools/*.sh
```

## 📦 Závislosti

**Python 3.10+**
- matplotlib - Vykreslování grafů
- networkx - Práce s grafy
- numpy - Matematické operace
- graphviz - Alternativní vykreslování

**Systémové (volitelné):**
- graphviz (systémový balíček) - Pro graphviz vizualizaci

