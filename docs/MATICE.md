# Práce s maticemi

Rozšířená funkcionalita pro analýzu matic grafů.

## 🎯 Funkce

Program `analyze_matrices.py` nyní podporuje:

1. **Zobrazení rozměrů matic** (řádky × sloupce)
2. **Přístup k jednotlivým prvkům matic** podle indexu
3. **Indexování od 0** (jako ve většině programovacích jazyků)

## 📊 Podporované matice

### a) Matice sousednosti
- **Rozměry:** n × n (kde n je počet uzlů)
- **Význam:** `A[i][j]` = počet hran z uzlu i do uzlu j
- **Index:** `[řádek_uzlu][sloupec_uzlu]`

### b) Znaménková matice
- **Rozměry:** n × n
- **Význam:** `S[i][j]` = orientace hrany (1, 0, -1)
- **Index:** `[řádek_uzlu][sloupec_uzlu]`

### c) Mocniny matice sousednosti
- **Rozměry:** n × n
- **Význam:** `A^k[i][j]` = počet cest délky k z i do j
- **Index:** `[řádek_uzlu][sloupec_uzlu]`

### d) Matice incidence
- **Rozměry:** n × m (n uzlů × m hran)
- **Význam:** `I[i][j]` = incidence uzlu i s hranou j
- **Index:** `[řádek_uzlu][sloupec_hrany]`

### e) Matice délek (Floyd-Warshall)
- **Rozměry:** n × n
- **Význam:** `D[i][j]` = délka nejkratší cesty z i do j
- **Index:** `[řádek_uzlu][sloupec_uzlu]`

## 🚀 Použití

### Zobrazení celých matic s rozměry

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg
```

**Výstup:**
```
a) Matice sousednosti:
Rozměry: 8 řádků × 8 sloupců
------------------------------------------------------------
       A    B    C    D    E    F    G    H
  A:   0    1    0    1    0    0    0    0
  B:   0    0    1    0    0    0    0    0
  ...
```

### Přístup k jednotlivým prvkům

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg [řádek] [sloupec]
```

**Indexování od 0!**

#### Příklad 1: Prvek [0][1] (A→B)

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 1
```

**Výstup:**
```
🔍 Režim přístupu k prvkům - Index [0][1]

============================================================
PŘÍSTUP K PRVKŮM MATIC - Index [0][1]
============================================================

a) Matice sousednosti[A][B] = 1
   (index: [0][1])

b) Znaménková matice[A][B] = 1
   (index: [0][1])

c) Matice sousednosti^2[A][B] = 0
   (index: [0][1])

c) Matice sousednosti^3[A][B] = 1
   (index: [0][1])

d) Matice incidence[A][e1] = 0
   (index: [0][1])

e) Matice délek (Floyd-Warshall)[A][B] = 1.0
   (index: [0][1])
```

#### Příklad 2: Prvek [2][4] (C→E)

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 2 4
```

**Výstup:**
```
a) Matice sousednosti[C][E] = 1
   (index: [2][4])

e) Matice délek (Floyd-Warshall)[C][E] = 3.0
   (index: [2][4])
```

**Interpretace:**
- `[C][E] = 1` znamená: existuje hrana z C do E
- Nejkratší cesta z C do E má délku 3.0

#### Příklad 3: Neplatný index

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 10 10
```

**Výstup:**
```
❌ Neplatný index [10][10] - mimo rozsah matice!
```

## 📋 Mapování indexů na uzly

Pro graf se 8 uzly (A, B, C, D, E, F, G, H):

| Index | Uzel |
|-------|------|
| 0     | A    |
| 1     | B    |
| 2     | C    |
| 3     | D    |
| 4     | E    |
| 5     | F    |
| 6     | G    |
| 7     | H    |

Uzly jsou **seřazeny abecedně**!

## 💡 Praktické příklady

### Zjištění, zda existuje hrana A→B

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 1
```

Podívej se na `Matice sousednosti[A][B]`:
- `= 1` → existuje hrana A→B
- `= 0` → neexistuje hrana A→B

### Zjištění nejkratší cesty mezi uzly

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 7
```

Podívej se na `Matice délek[A][H]`:
- Hodnota = délka nejkratší cesty
- `= ∞` → neexistuje cesta

### Zjištění počtu cest délky 3

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 4
```

Podívej se na `Matice sousednosti^3[A][E]`:
- Hodnota = počet různých cest délky 3 z A do E

### Zjištění incidence uzlu s hranou

```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 5
```

Podívej se na `Matice incidence[A][e5]`:
- `= 1` → hrana e5 vychází z A
- `= -1` → hrana e5 vchází do A
- `= 0` → hrana e5 není incidentní s A

## 🔢 Formát výstupu

### Režim celých matic

```
a) Matice sousednosti:
Rozměry: 8 řádků × 8 sloupců
------------------------------------------------------------
       A    B    C    D    E    F    G    H
  A:   0    1    0    1    0    0    0    0
  ...
```

### Režim přístupu k prvkům

```
a) Matice sousednosti[A][B] = 1
   (index: [0][1])
```

**Formát:**
- `Matice[Uzel_řádek][Uzel_sloupec] = hodnota`
- `(index: [číselný_řádek][číselný_sloupec])`

## ⚠️ Důležité poznámky

1. **Indexování od 0** - první řádek/sloupec má index 0
2. **Seřazení uzlů** - uzly jsou abecedně seřazeny
3. **Matice incidence** - sloupce jsou hrany (e0, e1, e2, ...)
4. **Neplatné indexy** - program zobrazí chybovou hlášku
5. **Mocniny matic** - pouze pro grafy do 10 uzlů

## 📚 Související dokumentace

- [POUZITI.md](POUZITI.md) - Obecný návod k použití
- [DOKUMENTACE.md](DOKUMENTACE.md) - Technická dokumentace
- [STRUKTURA.md](STRUKTURA.md) - Struktura projektu

## 🔧 Technické detaily

### Funkce v kódu

```python
# Získání prvku matice
get_matrix_element(matrix, row, col, row_labels, col_labels)

# Výpis prvku matice
print_matrix_element(matrix, row, col, row_labels, col_labels, matrix_name)

# Výpis celé matice s rozměry
print_matrix(matrix, row_labels, col_labels, title, show_dimensions=True)
```

### Návratová hodnota `get_matrix_element`

```python
{
    'value': 1,           # Původní hodnota
    'value_str': '1',     # Formátovaná hodnota
    'row_index': 0,       # Číselný index řádku
    'col_index': 1,       # Číselný index sloupce
    'row_label': 'A',     # Popisek řádku
    'col_label': 'B'      # Popisek sloupce
}
```

## 🎓 Příklady úloh

### Úloha 1: Kolik je hran z A do všech ostatních uzlů?

```bash
# Zobraz celý řádek A (index 0)
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 0
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 1
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 0 2
# ... atd
```

### Úloha 2: Jaká je nejkratší cesta z C do všech uzlů?

```bash
# Zobraz celý řádek C (index 2) v matici délek
# Pro 8 uzlů (0-7):
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 2 0  # C→A
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 2 1  # C→B
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 2 2  # C→C
# ... atd
```

### Úloha 3: Které hrany jsou incidentní s uzlem E?

```bash
# Zobraz celý řádek E (index 4) v matici incidence
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 4 0  # E a e0
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg 4 1  # E a e1
# ... atd
```

## 🆘 Řešení problémů

### "❌ Neplatný index [x][y] - mimo rozsah matice!"

- Zkontroluj, že index je v rozsahu 0 až (n-1)
- Pro matici 8×8 jsou platné indexy 0-7
- Nejprve zobraz celou matici pro zjištění rozměrů

### Jak zjistím, jaký uzel má jaký index?

Spusť bez indexu:
```bash
./venv/bin/python scripts/analyze_matrices.py data/grafy/01.tg
```

V hlavičce matice vidíš popisky uzlů v pořadí indexů (0, 1, 2, ...).

