# 🔍 Rozpoznávač grafů

Profesionální nástroj pro **analýzu grafů** - detekci vlastností, výpočet charakteristik uzlů a vytváření matic.

> 📚 **Projekt pro předmět Teorie grafů**

## 📁 Struktura projektu

```
rozeznavac_grafu/
│
├── 📂 src/                   Zdrojové kódy (6 modulů)
│   ├── __init__.py          Export tříd a funkcí
│   ├── parser.py            Parser .tg souborů
│   ├── graph.py             Třída Graph
│   ├── analyzer.py          Analýza vlastností (a-j)
│   ├── matrices.py          Vytváření matic (a-e, h)
│   └── visualizer.py        Vizualizace grafů
│
├── 📂 scripts/               Python programy (3 skripty)
│   ├── analyze_properties.py  Vlastnosti + uzly
│   ├── analyze_matrices.py    Matice (interaktivní)
│   └── run.py                 Kompletní analýza
│
├── 📂 bin/                   Spouštěcí wrappery
│   ├── *.sh                 Linux/Mac (3 soubory)
│   └── *.bat                Windows (3 soubory)
│
├── 📂 data/                  Vstupní data
│   └── grafy/               21 grafových souborů .tg
│
├── 📂 output/                Výstupy
│   └── vykreslene_grafy/    PNG obrázky grafů
│
├── 📂 docs/                  Dokumentace (9+ souborů)
│   ├── README.md, POUZITI.md
│   ├── INTERAKTIVNI_MATICE.md, MATICE.md
│   ├── WINDOWS.md, STRUKTURA.md
│   └── ...
│
├── 📂 tests/                 Testovací skripty
│   ├── test_interactive_matrix.sh
│   └── test_interactive_matrix.bat
│
├── 📂 tools/                 Pomocné nástroje
│   ├── install_libs.py, test_venv.py
│   ├── setup_venv.sh, run_with_venv.sh
│   └── vykresli_graf.py
│
├── 📂 venv/                  Virtual environment
│
├── 📄 analyze.sh            🚀 Hlavní spouštěč (Linux/Mac)
├── 📄 analyze.bat           🚀 Hlavní spouštěč (Windows)
├── 📄 README.md             📖 Tento soubor
└── 📄 requirements.txt      📦 Python závislosti
```

## 🚀 Rychlý start

### 🆕 Hlavní interaktivní program (DOPORUČENO)

#### Linux / Mac
```bash
# 1. Instalace
bash tools/setup_venv.sh

# 2. Spuštění
./start.sh
```

#### Windows
```cmd
REM 1. Instalace
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
deactivate

REM 2. Spuštění
start.bat
```

**Nový program `main.py`** nabízí:
- Jeden while cyklus s menu
- Analýza vlastností grafu, uzlů a hran
- Všechny matice s dotazováním pomocí názvů
- Vzdálenosti u sousedů/předchůdců/následníků
- Vlastnosti v češtině s barevným kódováním (zelená/červená)

**Dokumentace:** [docs/MAIN_PROGRAM.md](docs/MAIN_PROGRAM.md)

---

### Původní skripty

#### Linux / Mac
```bash
./analyze.sh
```

#### Windows
```cmd
analyze.bat
```

**Podrobnosti:** [QUICKSTART.md](QUICKSTART.md) | [docs/WINDOWS.md](docs/WINDOWS.md)

### 2. Použití

#### Linux / Mac

```bash
# Vlastnosti + uzly
./bin/analyze_properties.sh data/grafy/02.tg A B C

# Matice (interaktivní)
./bin/analyze_matrices.sh data/grafy/02.tg

# Matice (všechny)
./bin/analyze_matrices.sh data/grafy/02.tg --all

# Matice (index [0][1])
./bin/analyze_matrices.sh data/grafy/02.tg --all 0 1

# Kompletní analýza
./bin/run.sh data/grafy/02.tg A B
```

#### Windows

```cmd
REM Vlastnosti + uzly
bin\analyze_properties.bat data\grafy\02.tg A B C

REM Matice (interaktivní)
bin\analyze_matrices.bat data\grafy\02.tg

REM Matice (všechny)
bin\analyze_matrices.bat data\grafy\02.tg --all

REM Matice (index [0][1])
bin\analyze_matrices.bat data\grafy\02.tg --all 0 1

REM Kompletní analýza
bin\run.bat data\grafy\02.tg A B
```

## ✨ Nová funkce: Přístup k maticím pomocí názvů

Od verze 2.0 můžete přistupovat k prvkům matic pomocí **názvů uzlů a hran**:

```python
from src.matrices import MatrixBuilder

builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Nové API - použití názvů uzlů
value = adj_matrix['A']['B']  # Hrana z A do B

# Staré API - stále funguje
value = adj_matrix[0][1]      # Číselné indexy
```

**Více informací:** [docs/NAMED_MATRICES.md](docs/NAMED_MATRICES.md) | `python3 demo_named_matrices.py`

## 📚 Dokumentace

Podrobná dokumentace je k dispozici ve složce `docs/`:

- **[POUZITI.md](docs/POUZITI.md)** - Detailní návod k použití s příklady
- **[DOKUMENTACE.md](docs/DOKUMENTACE.md)** - Kompletní technická dokumentace
- **[INSTALACE_VENV.md](docs/INSTALACE_VENV.md)** - Podrobný návod na instalaci
- **[NAMED_MATRICES.md](docs/NAMED_MATRICES.md)** - 🆕 Přístup k maticím pomocí názvů

## 🔧 Moduly

### `src/parser.py`
Parser pro načítání grafů z textových souborů formátu `.tg`.

### `src/graph.py`
Třída `Graph` pro reprezentaci grafu s metodami pro:
- Přístup k uzlům a hranám
- Výpočet stupňů, sousedů, předchůdců
- BFS prohledávání

### `src/analyzer.py`
Třída `GraphAnalyzer` pro analýzu vlastností:
- Ohodnocený, orientovaný, souvislý
- Prostý, jednoduchý, rovinný
- Úplný, regulární, bipartitní

### `src/matrices.py`
Třída `MatrixBuilder` pro vytváření:
- Matice sousednosti
- Znaménková matice
- Matice incidence
- Matice délek (Floyd-Warshall)

**Nově:** Třída `NamedMatrix` pro přístup pomocí názvů uzlů/hran

### `src/visualizer.py`
Nástroje pro vizualizaci grafů:
- Textová vizualizace
- Grafické vykreslení (matplotlib/networkx)
- Podpora pro vícenásobné hrany

## 📝 Formát vstupních souborů

Grafy se zadávají v textovém formátu `.tg`:

```
u A;           # Uzel A
u B;           # Uzel B
u C 5;         # Uzel C s ohodnocením 5

h A - B;       # Neorientovaná hrana
h A > B;       # Orientovaná hrana A→B
h A < B;       # Orientovaná hrana A←B
h A - B 10;    # Hrana s váhou
h A > B 5 :h1; # Hrana s váhou a označením
```

## 🎯 Vlastnosti grafu

Program detekuje následující vlastnosti:
- **a)** Ohodnocený
- **b)** Orientovaný
- **c)** Souvislý (silně/slabě)
- **d)** Prostý (bez vícenásobných hran)
- **e)** Jednoduchý (prostý + bez smyček)
- **f)** Rovinný
- **g)** Konečný
- **h)** Úplný
- **i)** Regulární
- **j)** Bipartitní

## 📊 Výstupy

Program vytváří:
- Textovou vizualizaci grafu
- Grafické PNG obrázky (uložené v `output/vykreslene_grafy/`)
- Matice sousednosti, incidence, délek
- Detailní informace o uzlech

## 🔧 Spouštěcí soubory

### Hlavní spouštěče (kořenový adresář)
- `analyze.sh` / `analyze.bat` - 🚀 **Interaktivní menu** (doporučeno)

### Přímé spuštění (bin/)

**Linux / Mac:**
- `bin/analyze_properties.sh` - Vlastnosti + uzly
- `bin/analyze_matrices.sh` - Matice (interaktivní)
- `bin/run.sh` - Kompletní analýza

**Windows:**
- `bin\analyze_properties.bat` - Vlastnosti + uzly
- `bin\analyze_matrices.bat` - Matice (interaktivní)
- `bin\run.bat` - Kompletní analýza

### Testy (tests/)
- `tests/test_interactive_matrix.sh` - Testy (Linux/Mac)
- `tests/test_interactive_matrix.bat` - Testy (Windows)

**Windows dokumentace:** [docs/WINDOWS.md](docs/WINDOWS.md)

## 🐛 Řešení problémů

Pokud nefunguje grafické vykreslování:
```bash
pip install --upgrade matplotlib networkx numpy
```

Pro více informací viz:
- [docs/INSTALACE_VENV.md](docs/INSTALACE_VENV.md)
- [docs/WINDOWS.md](docs/WINDOWS.md) - Pro Windows

## 👨‍💻 Autor

Projekt pro předmět Teorie grafů

