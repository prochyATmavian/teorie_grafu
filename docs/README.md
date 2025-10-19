# Rozpoznávač grafů

Nástroj pro analýzu grafů v textovém formátu.

## 🚀 Rychlý start

### Bez virtuálního prostředí (textová vizualizace)
```bash
python3 run.py <soubor_s_grafem.tg>
```

### S virtuálním prostředím (grafická vizualizace)
```bash
# 1. Vytvořte a aktivujte venv
python3 -m venv venv
source venv/bin/activate

# 2. Nainstalujte knihovny
pip install -r requirements.txt

# 3. Spusťte program
python3 run.py <soubor_s_grafem.tg>
```

**Nebo použijte automatický instalační skript:**
```bash
bash setup_venv.sh
bash run_with_venv.sh <soubor.tg>
```

📖 Podrobné instrukce: [INSTALACE_VENV.md](INSTALACE_VENV.md)

## 📋 Co program dělá

Program analyzuje graf a vypíše:

### ✅ Vlastnosti grafu (a-j)
- **a)** Ohodnocený
- **b)** Orientovaný  
- **c)** Souvislý (silně/slabě)
- **d)** Prostý
- **e)** Jednoduchý
- **f)** Rovinný
- **g)** Konečný
- **h)** Úplný
- **i)** Regulární
- **j)** Bipartitní

### 📊 Charakteristiky uzlů (k-s)
- **k)** U+(v) - následníci
- **l)** U-(v) - předchůdci
- **m)** U(v) - sousedé
- **n)** H+(v) - výstupní hrany
- **o)** H-(v) - vstupní hrany
- **p)** H(v) - okolí
- **q)** d+(v) - výstupní stupeň
- **r)** d-(v) - vstupní stupeň
- **s)** d(v) - stupeň

### 🔢 Matice a seznamy
- **a)** Matice sousednosti
- **b)** Znaménková matice
- **c)** Mocniny matice sousednosti
- **d)** Matice incidence
- **e)** Matice délek (Floyd-Warshall)
- **f)** Matice předchůdců
- **g)** Tabulka incidentních hran
- **h)** Seznam sousedů
- **i)** Seznam uzlů a hran

## 📝 Formát vstupního souboru

### Uzly
```
u A;           # Uzel A
u B 5;         # Uzel B s váhou 5
u *;           # Vynechaný uzel (binární strom)
```

### Hrany
```
h A > B;       # Orientovaná A → B
h A < B;       # Orientovaná A ← B
h A - B;       # Neorientovaná A — B
h A > B 5 :h1; # S váhou a označením
```

## 📁 Struktura projektu

```
rozeznavac_grafu/
├── run.py              # ← HLAVNÍ PROGRAM
├── parser.py           # Parser vstupního formátu
├── graph.py            # Reprezentace grafu
├── analyzer.py         # Analýza vlastností
├── matrices.py         # Matice a seznamy
├── visualizer.py       # Vizualizace
├── READ_ME             # Zadání úkolu
├── DOKUMENTACE.md      # Podrobná dokumentace
└── README.md           # Tento soubor
```

## 🎨 Vizualizace (volitelné)

Pro grafické vykreslení grafu:

```bash
pip install matplotlib networkx
# nebo
pip install graphviz
```

Bez těchto knihoven program funguje a zobrazuje textovou vizualizaci.

## 📖 Dokumentace

Podrobná dokumentace všech funkcí je v souboru **[DOKUMENTACE.md](DOKUMENTACE.md)**

## 🧪 Příklad použití

```bash
python3 run.py /Users/prochy/Downloads/grafy/01.tg
```

Výstup:
- Textová vizualizace grafu
- Analýza vlastností (a-j)
- Informace o uzlech (k-s)  
- Všechny matice a seznamy
- (Volitelně) Grafické vykreslení

## ⚙️ Požadavky

- **Python 3.6+** (bez dalších závislostí)
- **Volitelně:** matplotlib, networkx nebo graphviz pro grafickou vizualizaci

## 🎯 Funkce bez externích knihoven

Program je navržen tak, aby fungoval **bez externích knihoven**:
- ✅ Parsování grafů
- ✅ Analýza všech vlastností
- ✅ Sestavení všech matic
- ✅ Textová vizualizace

Grafická vizualizace je pouze **volitelný bonus**.

