# ✨ Nová struktura projektu

## 📊 Přehled změn

Projekt byl **restrukturalizován** pro maximální přehlednost a profesionalitu.

## 📁 Finální struktura

```
rozeznavac_grafu/
│
├── 📄 analyze.sh              🚀 Hlavní spouštěč (Linux/Mac)
├── 📄 analyze.bat             🚀 Hlavní spouštěč (Windows)
├── 📄 README.md               📖 Hlavní dokumentace
├── 📄 requirements.txt        📦 Python závislosti
│
├── 📂 src/                    💻 Zdrojové kódy (6 modulů)
│   ├── __init__.py           Export tříd
│   ├── parser.py             Parser .tg souborů
│   ├── graph.py              Třída Graph
│   ├── analyzer.py           Analýza vlastností
│   ├── matrices.py           Vytváření matic
│   └── visualizer.py         Vizualizace
│
├── 📂 scripts/                🐍 Python programy (3 skripty)
│   ├── analyze_properties.py Vlastnosti + uzly
│   ├── analyze_matrices.py   Matice (interaktivní)
│   └── run.py                Kompletní analýza
│
├── 📂 bin/                    🔧 Spouštěcí wrappery
│   ├── analyze_properties.sh Linux/Mac wrapper
│   ├── analyze_matrices.sh   Linux/Mac wrapper
│   ├── run.sh                Linux/Mac wrapper
│   ├── analyze_properties.bat Windows wrapper
│   ├── analyze_matrices.bat  Windows wrapper
│   └── run.bat               Windows wrapper
│
├── 📂 data/                   📥 Vstupní data
│   └── grafy/                21 grafových souborů .tg
│       ├── 01.tg až 20.tg
│       └── custom*.tg
│
├── 📂 output/                 📤 Výstupní soubory
│   └── vykreslene_grafy/     PNG obrázky grafů
│
├── 📂 docs/                   📚 Dokumentace (13 souborů)
│   ├── QUICKSTART.md         Rychlý start
│   ├── POUZITI.md            Detailní návod
│   ├── INTERAKTIVNI_MATICE.md Interaktivní matice
│   ├── MATICE.md             Technické info o maticích
│   ├── WINDOWS.md            Windows návod
│   ├── WINDOWS_README.txt    Windows quick reference
│   ├── STRUKTURA.md          Původní struktura
│   ├── NOVA_STRUKTURA.md     Tento soubor
│   ├── DOKUMENTACE.md        Technická dokumentace
│   ├── INSTALACE_VENV.md     Instalace
│   ├── ZMENY.md              Historie změn
│   ├── PREHLED_SOUBORU.txt   Přehled souborů
│   ├── DEMO_MATICE.txt       Demo příklady
│   ├── README.md             Původní README
│   └── READ_ME               Původní poznámky
│
├── 📂 tests/                  🧪 Testovací skripty
│   ├── test_interactive_matrix.sh   Linux/Mac testy
│   └── test_interactive_matrix.bat  Windows testy
│
├── 📂 tools/                  🛠️  Pomocné nástroje
│   ├── install_libs.py       Instalace knihoven
│   ├── test_venv.py          Test venv
│   ├── setup_venv.sh         Vytvoření venv
│   ├── run_with_venv.sh      Wrapper s venv
│   └── vykresli_graf.py      Pomocník
│
└── 📂 venv/                   🐍 Virtual environment
    ├── bin/ (Linux/Mac)
    └── Scripts/ (Windows)
```

## ✨ Klíčové zlepšení

### 1. **Čistý kořenový adresář**

**PŘED (20 souborů):**
```
├── analyze.sh
├── analyze.bat  
├── analyze_properties.bat
├── analyze_matrices.bat
├── run.bat
├── test_interactive_matrix.sh
├── test_interactive_matrix.bat
├── README.md
├── QUICKSTART.md
├── WINDOWS_README.txt
├── ZMENY.md
├── PREHLED_SOUBORU.txt
├── requirements.txt
└── ... více souborů
```

**PO (4 soubory + složky):**
```
├── analyze.sh            🚀 Hlavní menu
├── analyze.bat           🚀 Hlavní menu
├── README.md             📖 Dokumentace
├── requirements.txt      📦 Závislosti
│
└── 📂 bin/, scripts/, src/, data/, docs/, tests/, tools/, output/, venv/
```

### 2. **Logické seskupení**

| Složka | Účel | Obsah |
|--------|------|-------|
| `src/` | Zdrojové kódy | 6 Python modulů |
| `scripts/` | Hlavní programy | 3 Python skripty |
| `bin/` | Spouštěcí wrappery | 6 wrapper skriptů (.sh + .bat) |
| `data/` | Vstupní data | 21 .tg souborů |
| `output/` | Výstupy | PNG obrázky |
| `docs/` | Dokumentace | 13 dokumentačních souborů |
| `tests/` | Testy | 2 testovací skripty |
| `tools/` | Nástroje | 5 pomocných nástrojů |
| `venv/` | Python env | Virtuální prostředí |

### 3. **Hierarchie spouštění**

```
Úroveň 1 (nejjednodušší):
  analyze.sh / analyze.bat
    ↓ Interaktivní menu

Úroveň 2 (přímé):
  bin/*.sh / bin/*.bat
    ↓ Rychlé spuštění

Úroveň 3 (pokročilí):
  venv/bin/python scripts/*.py
    ↓ Plná kontrola
```

## 🚀 Jak používat novou strukturu

### Pro běžné uživatele (doporučeno)

```bash
# Linux/Mac
./analyze.sh

# Windows
analyze.bat
```

### Pro pokročilé uživatele

```bash
# Linux/Mac
./bin/analyze_properties.sh data/grafy/02.tg A B
./bin/analyze_matrices.sh data/grafy/02.tg --all 0 1
./bin/run.sh data/grafy/02.tg A B

# Windows
bin\analyze_properties.bat data\grafy\02.tg A B
bin\analyze_matrices.bat data\grafy\02.tg --all 0 1
bin\run.bat data\grafy\02.tg A B
```

### Pro vývojáře

```bash
# Přímý přístup k Python skriptům
./venv/bin/python scripts/analyze_properties.py data/grafy/02.tg A B
./venv/bin/python scripts/analyze_matrices.py data/grafy/02.tg --all
./venv/bin/python scripts/run.py data/grafy/02.tg A B
```

## 📋 Výhody nové struktury

### ✅ Přehlednost
- Kořenový adresář obsahuje pouze **4 soubory**
- Každá složka má **jasně definovaný účel**
- Snadná orientace v projektu

### ✅ Profesionalita
- Standardní struktura Python projektů
- Oddělení executable, zdrojů a dat
- Připraveno pro distribuci

### ✅ Multiplatformnost
- Symetrická struktura pro Linux/Mac i Windows
- Všechny funkce na obou platformách
- Konzistentní naming

### ✅ Testovatelnost
- Testy v samostatné složce `tests/`
- Spustitelné přes menu (volba 4)
- Podpora pro CI/CD

### ✅ Škálovatelnost
- Snadné přidávání nových modulů do `src/`
- Snadné přidávání nových skriptů do `scripts/`
- Oddělené výstupy v `output/`

## 🔄 Migrace

Pokud jste používali starou strukturu:

### PŘED:
```bash
./analyze_properties.py graf.tg A B
./analyze_matrices.py graf.tg
```

### PO:
```bash
./bin/analyze_properties.sh data/grafy/graf.tg A B
./bin/analyze_matrices.sh data/grafy/graf.tg
```

**Změny:**
1. Použití `bin/` prefixu
2. Cesta k grafům: `data/grafy/`
3. Pro Linux/Mac: přípona `.sh`

## 📚 Aktualizovaná dokumentace

Všechna dokumentace byla aktualizována:
- ✅ `README.md` - Nová struktura
- ✅ `docs/QUICKSTART.md` - Odkazy na `bin/`
- ✅ `docs/WINDOWS.md` - Windows cesty
- ✅ `docs/INTERAKTIVNI_MATICE.md` - Nové příklady
- ✅ `docs/NOVA_STRUKTURA.md` - Tento soubor

## 🎯 Současný stav

### Kořenový adresář (4 soubory)
```
✅ analyze.sh          Interaktivní menu (Linux/Mac)
✅ analyze.bat         Interaktivní menu (Windows)
✅ README.md           Hlavní dokumentace
✅ requirements.txt    Python závislosti
```

### 9 specializovaných složek
```
📂 src/       6 Python modulů
📂 scripts/   3 hlavní programy
📂 bin/       6 wrapper skriptů (3 .sh + 3 .bat)
📂 data/      21 grafových souborů
📂 output/    PNG obrázky grafů
📂 docs/      13 dokumentačních souborů
📂 tests/     2 testovací skripty
📂 tools/     5 pomocných nástrojů
📂 venv/      Virtual environment
```

## 🎉 Výsledek

**Projekt je nyní:**
- ✅ **Přehledný** - Čistý kořenový adresář
- ✅ **Profesionální** - Standardní struktura
- ✅ **Multiplatformní** - Linux/Mac/Windows
- ✅ **Dokumentovaný** - 13 dokumentačních souborů
- ✅ **Testovatelný** - Samostatná složka testů
- ✅ **Škálovatelný** - Připraven pro růst

---

**Datum reorganizace:** 19. října 2025  
**Verze:** 3.0 (finální restrukturalizace)

