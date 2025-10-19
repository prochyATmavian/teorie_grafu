# Použití analyzátoru grafů

Program pro analýzu grafů byl rozdělen na **dva samostatné spouštěcí soubory**:

## 1. Analýza vlastností grafu a uzlů

**Soubor:** `analyze_properties.py`

**Co program dělá:**
- Načítá a parsuje graf ze souboru
- Vytváří **textovou a grafickou vizualizaci** grafu
- Analyzuje **vlastnosti grafu** (a-j):
  - a) Ohodnocený
  - b) Orientovaný
  - c) Souvislý
  - d) Prostý
  - e) Jednoduchý
  - f) Rovinný
  - g) Konečný
  - h) Úplný
  - i) Regulární
  - j) Bipartitní
- Zobrazuje **detailní informace o vybraných uzlech** (k-s):
  - k) Následníci U+(v)
  - l) Předchůdci U-(v)
  - m) Sousedé U(v)
  - n) Výstupní hrany H+(v)
  - o) Vstupní hrany H-(v)
  - p) Okolí H(v)
  - q) Výstupní stupeň d+(v)
  - r) Vstupní stupeň d-(v)
  - s) Stupeň d(v)

### Použití:

```bash
# Základní použití - zobrazí vlastnosti grafu, bez detailů uzlů
./venv/bin/python analyze_properties.py <soubor_grafu>

# Příklad:
./venv/bin/python analyze_properties.py grafy/02.tg

# S detaily o vybraných uzlech
./venv/bin/python analyze_properties.py <soubor_grafu> [uzel1] [uzel2] ...

# Příklady:
./venv/bin/python analyze_properties.py grafy/02.tg A
./venv/bin/python analyze_properties.py grafy/02.tg A B C
./venv/bin/python analyze_properties.py grafy/01.tg A E F
```

### Výstup:
- Textová vizualizace grafu
- Seznam sousednosti
- Grafický obrázek (uložen do `vykreslene_grafy/graf_<jmeno>.png`)
- Vlastnosti grafu (a-j)
- Detaily o zadaných uzlech (k-s) - pouze pokud jsou uzly specifikovány

---

## 2. Analýza matic a seznamů

**Soubor:** `analyze_matrices.py`

**Co program dělá:**
- Načítá a parsuje graf ze souboru
- Vytváří různé **matice** grafu:
  - a) Matice sousednosti
  - b) Znaménková matice
  - c) Mocniny matice sousednosti (^2, ^3) - pro grafy do 10 uzlů
  - d) Matice incidence
  - e) Matice délek (Floyd-Warshall)
- Vytváří **seznam sousedů** (h)

### Použití:

```bash
# Základní použití
./venv/bin/python analyze_matrices.py <soubor_grafu>

# Příklady:
./venv/bin/python analyze_matrices.py grafy/02.tg
./venv/bin/python analyze_matrices.py grafy/01.tg
```

### Výstup:
- Matice sousednosti
- Znaménková matice
- Mocniny matice sousednosti (pro menší grafy)
- Matice incidence
- Matice délek (nejkratší cesty mezi všemi páry uzlů)
- Seznam sousedů

---

## Původní program (run.py)

**Poznámka:** Původní soubor `run.py` stále existuje a obsahuje **obě analýzy dohromady**. Pokud chcete spustit kompletní analýzu najednou, použijte:

```bash
./venv/bin/python run.py <soubor_grafu> [uzly...]
```

---

## Formát vstupního souboru

Grafy se zadávají v textovém formátu `.tg`:

```
u A;           # Definice uzlu A
u B;           # Definice uzlu B
u C 5;         # Definice uzlu C s ohodnocením 5

h A - B;       # Neorientovaná hrana A-B
h A > B;       # Orientovaná hrana A→B
h A < B;       # Orientovaná hrana A←B (= B→A)
h A - B 10;    # Neorientovaná hrana s váhou 10
h A > B 5 :h1; # Orientovaná hrana s váhou 5 a označením h1
```

---

## Příklady použití

### Příklad 1: Kompletní analýza neorientovaného grafu
```bash
# Vlastnosti + uzly A, B, F
./venv/bin/python analyze_properties.py grafy/02.tg A B F

# Matice
./venv/bin/python analyze_matrices.py grafy/02.tg
```

### Příklad 2: Analýza orientovaného grafu
```bash
# Vlastnosti + uzly A, E (zobrazí předchůdce/následníky)
./venv/bin/python analyze_properties.py grafy/01.tg A E

# Matice (včetně znaménkové)
./venv/bin/python analyze_matrices.py grafy/01.tg
```

### Příklad 3: Pouze vlastnosti, bez detailů uzlů
```bash
# Zobrazí pouze vlastnosti grafu (a-j), žádné detaily o uzlech
./venv/bin/python analyze_properties.py grafy/02.tg
```

---

## Tipy

1. **Vizualizace:** Graf se automaticky vykreslí do složky `vykreslene_grafy/`
2. **Výběr uzlů:** Můžete zadat 0 až N uzlů pro detailní analýzu
3. **Malé grafy:** Pro grafy do 10 uzlů se zobrazí i mocniny matic
4. **Velké grafy:** Pro větší grafy se některé výpočty přeskočí (např. mocniny matic)

---

## Systémové požadavky

- Python 3.10+
- Virtual environment (venv) s nainstalovanými knihovnami:
  - matplotlib
  - networkx
  - numpy

Pro aktivaci prostředí:
```bash
source venv/bin/activate  # Linux/Mac
# nebo
venv\Scripts\activate     # Windows
```

