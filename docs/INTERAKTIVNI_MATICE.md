# Interaktivní výběr matic

Program `analyze_matrices.py` nyní podporuje **interaktivní režim**, kde si můžete vybrat konkrétní matici a volitelně i konkrétní index.

## 🎯 Režimy použití

### 1. Interaktivní režim (výchozí)

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg
```

Program se vás **postupně zeptá**:

1. **Která matice?**
   - a) Matice sousednosti
   - b) Znaménková matice
   - c) Mocniny matice sousednosti (A^2, A^3)
   - d) Matice incidence
   - e) Matice délek (Floyd-Warshall)
   - h) Seznam sousedů
   - *) Všechny matice

2. **Chcete konkrétní index?** (a/n)
   - Pokud ANO: zadejte řádek a sloupec (od 0)
   - Pokud NE: zobrazí se celá matice

### 2. Režim --all (všechny matice najednou)

```bash
# Všechny matice
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg --all

# Všechny matice, konkrétní index [0][1]
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg --all 0 1
```

## 📝 Ukázky použití

### Příklad 1: Matice sousednosti, celá matice

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

============================================================
INTERAKTIVNÍ VÝBĚR MATICE
============================================================

Vyberte matici k sestavení:
  a) Matice sousednosti
  b) Znaménková matice
  c) Mocniny matice sousednosti (A^2, A^3)
  d) Matice incidence
  e) Matice délek (Floyd-Warshall)
  h) Seznam sousedů
  *) Všechny matice

Vaše volba (a/b/c/d/e/h/*): a    <-- VSTUP

Načítám graf ze souboru: data/grafy/01.tg
Načteno: 8 uzlů, 14 hran

------------------------------------------------------------
Chcete zobrazit konkrétní index matice? (a/n): n    <-- VSTUP

============================================================
VÝSLEDKY
============================================================

a) Matice sousednosti:
Rozměry: 8 řádků × 8 sloupců
------------------------------------------------------------
       A    B    C    D    E    F    G    H
  A:   0    1    0    1    0    0    0    0
  B:   0    0    1    0    0    0    0    0
  ...
```

### Příklad 2: Matice délek, konkrétní index [0][1]

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba (a/b/c/d/e/h/*): e    <-- VSTUP (matice délek)

Načítám graf ze souboru: data/grafy/01.tg
Načteno: 8 uzlů, 14 hran

------------------------------------------------------------
Chcete zobrazit konkrétní index matice? (a/n): a    <-- VSTUP (ano)
Zadejte řádek (od 0): 0    <-- VSTUP
Zadejte sloupec (od 0): 1    <-- VSTUP

🔍 Zobrazuji index [0][1]

============================================================
VÝSLEDKY
============================================================

e) Matice délek (Floyd-Warshall)[A][B] = 1.0
   (index: [0][1])

============================================================
HOTOVO
============================================================
```

**Interpretace:** Nejkratší cesta z A do B má délku 1.0

### Příklad 3: Všechny matice, konkrétní index

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba (a/b/c/d/e/h/*): *    <-- VSTUP (všechny)

Chcete zobrazit konkrétní index matice? (a/n): a    <-- VSTUP (ano)
Zadejte řádek (od 0): 2    <-- VSTUP
Zadejte sloupec (od 0): 4    <-- VSTUP

🔍 Zobrazuji index [2][4]

============================================================
VÝSLEDKY
============================================================

a) Matice sousednosti[C][E] = 1
   (index: [2][4])

b) Znaménková matice[C][E] = 1
   (index: [2][4])

c) Matice sousednosti^2[C][E] = 0
   (index: [2][4])

c) Matice sousednosti^3[C][E] = 1
   (index: [2][4])

d) Matice incidence[C][e4] = 0
   (index: [2][4])

e) Matice délek (Floyd-Warshall)[C][E] = 3.0
   (index: [2][4])
```

**Interpretace:**
- Existuje hrana C→E (matice sousednosti = 1)
- Nejkratší cesta C→E má délku 3.0
- Existuje cesta délky 3 z C do E (A^3 = 1)

### Příklad 4: Matice incidence

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba (a/b/c/d/e/h/*): d    <-- VSTUP (matice incidence)

Chcete zobrazit konkrétní index matice? (a/n): n    <-- VSTUP (celá matice)

============================================================
VÝSLEDKY
============================================================

d) Matice incidence:
Rozměry: 8 řádků × 14 sloupců
------------------------------------------------------------
      e0   e1   e2   e3   e4   e5   e6   e7   e8   e9  e10  e11  e12  e13
  A:   1    0    1   -1    0    0    0    0    0    0    0    0    0    0
  B:  -1    1    0    0   -1    0    0    0    0    0    0    0    0    0
  C:   0   -1    0    0    0    1    0    1    0    0    0    0    0    0
  ...
```

## 🎮 Klávesové zkratky

### Výběr matice:
- **a** - Matice sousednosti
- **b** - Znaménková matice
- **c** - Mocniny matice
- **d** - Matice incidence
- **e** - Matice délek
- **h** - Seznam sousedů
- **\*** - Všechny matice

### Potvrzení indexu:
- **a** / **ano** / **y** / **yes** - Ano, chci konkrétní index
- **n** / **ne** / **no** - Ne, zobraz celou matici

## ⚙️ Neinteraktivní použití (automatizace)

Pro skriptování můžete použít režim `--all`:

```bash
# Celé matice
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg --all

# Konkrétní index
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg --all 0 1
```

Nebo použít `echo` pro simulaci vstupu:

```bash
# Matice sousednosti, celá matice
echo -e "a\nn\n" | ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

# Matice délek, index [0][1]
echo -e "e\na\n0\n1\n" | ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

# Všechny matice, index [2][4]
echo -e "*\na\n2\n4\n" | ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg
```

## 📋 Mapování uzlů na indexy

Uzly jsou **seřazeny abecedně**. Pro zjištění mapování nejprve zobrazte celou matici:

```bash
echo -e "a\nn\n" | ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg
```

V hlavičce matice vidíte pořadí:
```
       A    B    C    D    E    F    G    H
       ↑    ↑    ↑    ↑    ↑    ↑    ↑    ↑
       0    1    2    3    4    5    6    7
```

## 💡 Praktické úlohy

### Úloha 1: Existuje hrana z A do B?

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba: a    # Matice sousednosti
Index: a         # Ano
Řádek: 0         # A
Sloupec: 1       # B

Výsledek: [A][B] = 1  → ANO, existuje hrana
```

### Úloha 2: Jaká je nejkratší cesta z C do všech uzlů?

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba: e    # Matice délek
Index: n         # Ne, celá matice

# Podívej se na řádek C (index 2)
```

### Úloha 3: Kolik je cest délky 2 z A do E?

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba: c    # Mocniny matice
Index: a         # Ano
Řádek: 0         # A
Sloupec: 4       # E

# Podívej se na výsledek z A^2[A][E]
```

### Úloha 4: Které hrany jsou incidentní s uzlem E?

```bash
$ ./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg

Vaše volba: d    # Matice incidence
Index: n         # Ne, celá matice

# Podívej se na řádek E (index 4)
# Hodnoty: 1 = hrana vychází, -1 = hrana vchází, 0 = není incidentní
```

## 🆘 Řešení problémů

### Špatná volba matice
```
❌ Neplatná volba: 'x'
```
→ Použijte pouze a, b, c, d, e, h, nebo *

### Neplatný index
```
❌ Neplatný vstup! Použiji celou matici.
```
→ Index musí být celé číslo (0, 1, 2, ...)

### Přerušení programu
Stiskněte `Ctrl+C`:
```
⚠️  Přerušeno uživatelem
```

## 🔗 Související dokumentace

- [MATICE.md](MATICE.md) - Detailní informace o maticích
- [POUZITI.md](POUZITI.md) - Obecný návod k použití
- [DOKUMENTACE.md](DOKUMENTACE.md) - Technická dokumentace

## 🎓 Výhody interaktivního režimu

✅ **Snadné použití** - Nemusíte pamatovat syntaxi  
✅ **Krok za krokem** - Program vás provede  
✅ **Flexibilní** - Vyberte přesně to, co potřebujete  
✅ **Úspora času** - Nezobrazuje nepotřebné matice  
✅ **Vzdělávací** - Vidíte nabídku všech možností  

## 📊 Srovnání režimů

| Režim | Použití | Vhodné pro |
|-------|---------|------------|
| **Interaktivní** | `program.py graf.tg` | Objevování, učení, jednotlivé dotazy |
| **--all** | `program.py graf.tg --all` | Kompletní přehled, dokumentace |
| **--all + index** | `program.py graf.tg --all 0 1` | Rychlý dotaz na konkrétní prvek |
| **echo \|** | `echo "a\nn" \| program.py` | Automatizace, skripty |

