# Rozpoznávač grafů

Program pro analýzu grafů - detekci vlastností, výpočet charakteristik uzlů a vytváření matic.

## 📁 Struktura projektu

```
rozeznavac_grafu/
├── src/                      # Zdrojové kódy knihoven
│   ├── __init__.py          # Inicializační soubor balíčku
│   ├── parser.py            # Parser pro načítání grafů z .tg souborů
│   ├── graph.py             # Třída Graph pro reprezentaci grafu
│   ├── analyzer.py          # GraphAnalyzer pro analýzu vlastností
│   ├── matrices.py          # MatrixBuilder pro vytváření matic
│   └── visualizer.py        # Nástroje pro vizualizaci grafů
│
├── scripts/                  # Spouštěcí skripty
│   ├── analyze_properties.py  # Analýza vlastností a uzlů
│   ├── analyze_matrices.py    # Analýza matic a seznamů
│   └── run.py                 # Kompletní analýza (původní)
│
├── data/                     # Vstupní data
│   └── grafy/               # Grafové soubory .tg
│       ├── 01.tg
│       ├── 02.tg
│       └── ...
│
├── output/                   # Výstupy
│   └── vykreslene_grafy/    # Vykreslené grafy (.png)
│
├── docs/                     # Dokumentace
│   ├── README.md            # Základní dokumentace
│   ├── POUZITI.md           # Návod k použití
│   ├── DOKUMENTACE.md       # Podrobná dokumentace
│   ├── INSTALACE_VENV.md    # Návod na instalaci
│   └── READ_ME              # Původní poznámky
│
├── tools/                    # Pomocné nástroje
│   ├── install_libs.py      # Instalace knihoven
│   ├── test_venv.py         # Test virtuálního prostředí
│   ├── setup_venv.sh        # Skript pro vytvoření venv
│   └── run_with_venv.sh     # Spuštění s venv
│
├── venv/                     # Virtual environment (Python)
├── requirements.txt          # Závislosti projektu
└── README.md                # Tento soubor
```

## 🚀 Rychlý start

### 1. Instalace závislostí

```bash
# Vytvoření virtuálního prostředí
python3 -m venv venv

# Aktivace prostředí
source venv/bin/activate  # Linux/Mac
# nebo
venv\Scripts\activate     # Windows

# Instalace závislostí
pip install -r requirements.txt
```

Nebo použijte pomocný skript:
```bash
bash tools/setup_venv.sh
```

### 2. Použití

#### Analýza vlastností grafu a uzlů
```bash
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg A B C
```

#### Analýza matic
```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/02.tg
```

#### Kompletní analýza
```bash
./venv/bin/python scripts/run.py data/grafy/02.tg A B
```

## 📚 Dokumentace

Podrobná dokumentace je k dispozici ve složce `docs/`:

- **[POUZITI.md](docs/POUZITI.md)** - Detailní návod k použití s příklady
- **[DOKUMENTACE.md](docs/DOKUMENTACE.md)** - Kompletní technická dokumentace
- **[INSTALACE_VENV.md](docs/INSTALACE_VENV.md)** - Podrobný návod na instalaci

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

## 🐛 Řešení problémů

Pokud nefunguje grafické vykreslování:
```bash
pip install --upgrade matplotlib networkx numpy
```

Pro více informací viz [docs/INSTALACE_VENV.md](docs/INSTALACE_VENV.md)

## 👨‍💻 Autor

Projekt pro předmět Teorie grafů

