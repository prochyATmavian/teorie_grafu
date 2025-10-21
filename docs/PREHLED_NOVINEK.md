# 🎉 Přehled novinek

## Co je nového?

### 🚀 Hlavní interaktivní program (main.py)

Nový hlavní program s intuitivním menu a while cyklem!

**Spuštění:**
```bash
./start.sh          # Linux/Mac
start.bat           # Windows
python3 main.py     # Přímé spuštění
```

**Dokumentace:** [MAIN_PROGRAM.md](MAIN_PROGRAM.md)

### ✨ Klíčové vlastnosti

#### 1. Menu-driven interface

```
================================================================
HLAVNÍ MENU
================================================================

📊 ANALÝZA:
  1) Vlastnosti grafu
  2) Vlastnosti uzlu (nebo všech uzlů)
  3) Vlastnosti hrany

📐 MATICE:
  4) Matice sousednosti
  5) N-tá mocnina matice sousednosti
  6) Matice incidence
  7) Matice délek
  8) Matice předchůdců

🔧 OSTATNÍ:
  9) Načíst jiný graf
  0) Ukončit program
```

#### 2. Přístup k maticím pomocí názvů

**Všechny matice** podporují dotazování pomocí **názvů uzlů/hran**:

```
Zadejte název řádku: A
Zadejte název sloupce: B

✅ Matice sousednosti[A][B] = 1
```

❌ **NE** číselné indexy (matrix[0][1])  
✅ **ANO** názvy uzlů (matrix['A']['B'])

#### 3. Vzdálenosti u sousedů

Pro ohodnocené grafy se zobrazují vzdálenosti:

```
Sousedé (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)

Předchůdci U-(A) (0):
  (žádní)

Následníci U+(A) (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)
```

#### 4. Vlastnosti uzlů a hran

**Vlastnosti uzlu:**
- Ohodnocení
- Stupně (d, d+, d-)
- Sousedé se vzdálenostmi
- Předchůdci se vzdálenostmi
- Následníci se vzdálenostmi
- Incidentní hrany

**Vlastnosti hrany:**
- Koncové uzly
- Orientace
- Váha
- Označení
- Detekce smyček

#### 5. N-tá mocnina matice

Vypočítá libovolnou mocninu matice sousednosti:

```
Zadejte mocninu (např. 2, 3, 4): 3

MATICE SOUSEDNOSTI^3
...

Interpretace: A^3[i][j] = počet cest délky 3 z uzlu i do uzlu j
```

#### 6. Smyčky v matici incidence

Smyčky se označují **hodnotou 2** (podle požadavku):

```
Matice incidence:
      h1   h2   h3
  A:   2    0    0    # h1 je smyčka na A
  B:   0    1   -1
```

## Nové soubory

### Programy
- **`main.py`** - hlavní interaktivní program
- **`start.sh`** - spouštěč pro Linux/Mac
- **`start.bat`** - spouštěč pro Windows

### Dokumentace
- **`docs/MAIN_PROGRAM.md`** - dokumentace k hlavnímu programu
- **`docs/NAMED_MATRICES.md`** - přístup k maticím pomocí názvů
- **`docs/CHANGELOG_V2.md`** - changelog verze 2.0
- **`docs/PREHLED_NOVINEK.md`** - tento soubor
- **`QUICKSTART_NAMED_MATRICES.md`** - rychlý průvodce

### Ukázky
- **`demo_named_matrices.py`** - ukázka NamedMatrix API

## Technické změny

### Nová třída: NamedMatrix

V `src/matrices.py`:

```python
class NamedMatrix:
    """Wrapper pro matice s názvovým indexováním."""
    
    def __getitem__(self, key):
        # Umožňuje matrix['A']['B']
        ...
```

**Výhody:**
- Čitelnější kód
- Lepší chybové hlášky
- Zpětná kompatibilita s indexy

### Aktualizované metody

Všechny metody v `MatrixBuilder` nyní vracejí `NamedMatrix`:

| Metoda | Před | Po |
|--------|------|-----|
| `adjacency_matrix()` | `(matrix, nodes)` | `NamedMatrix` |
| `incidence_matrix()` | `(matrix, nodes, edges)` | `NamedMatrix` |
| `distance_matrix()` | `(matrix, nodes)` | `NamedMatrix` |
| atd. | ... | ... |

## Porovnání: Staré vs. Nové

### Přístup k maticím

**Staré:**
```python
builder = MatrixBuilder(graph)
adj_matrix, nodes = builder.adjacency_matrix()

node_index = {node: i for i, node in enumerate(nodes)}
i = node_index['A']
j = node_index['B']
value = adj_matrix[i][j]
```

**Nové:**
```python
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

value = adj_matrix['A']['B']  # Jednoduché!
```

### Analýza uzlů

**Staré:**
```python
# Museli jste psát vlastní kód
neighbors = graph.get_neighbors('A')
for neighbor in neighbors:
    # Ručně vypočítat vzdálenosti...
```

**Nové:**
```
Zadejte název uzlu: A

================================================================
UZEL: A
================================================================

Sousedé (2):
  - B (vzdálenost: 1.0)
  - D (vzdálenost: 1.0)
```

### Matice

**Staré:**
```bash
# Spustit samostatný skript
./bin/analyze_matrices.sh data/grafy/01.tg --all

# Pak ručně hledat index pro konkrétní uzel
```

**Nové:**
```
Vyberte operaci: 4 (Matice sousednosti)

Chcete zjistit konkrétní hodnotu? a

Zadejte název řádku: A
Zadejte název sloupce: B

✅ Matice sousednosti[A][B] = 1
```

## Zpětná kompatibilita

✅ **Všechny staré skripty fungují!**

- `scripts/analyze_properties.py` ✅
- `scripts/analyze_matrices.py` ✅
- `scripts/run.py` ✅
- `bin/*.sh` a `bin/*.bat` ✅

## Migrace

### Není nutná!

Můžete používat:
- Nový `main.py` pro interaktivní práci
- Staré skripty pro automatizaci/scripting

### Doporučení

Pro interaktivní práci:
```bash
./start.sh  # Nový hlavní program
```

Pro scripting/automatizaci:
```bash
./bin/analyze_properties.sh data/grafy/01.tg A B C
./bin/analyze_matrices.sh data/grafy/01.tg --all
```

## Jak začít?

### 1. Spusťte nový program

```bash
./start.sh
```

### 2. Načtěte graf

```
Zadejte cestu k souboru: data/grafy/01.tg
```

### 3. Vyzkoušejte různé operace

- Volba `1`: Vlastnosti grafu
- Volba `2`: Vlastnosti uzlu (zkuste `vse` pro všechny)
- Volba `4`: Matice sousednosti (pak zkuste dotaz na hodnotu)
- Volba `5`: Mocniny matice (zkuste `2` nebo `3`)

### 4. Přečtěte si dokumentaci

- [MAIN_PROGRAM.md](MAIN_PROGRAM.md) - Kompletní návod
- [NAMED_MATRICES.md](NAMED_MATRICES.md) - Práce s maticemi
- [CHANGELOG_V2.md](CHANGELOG_V2.md) - Detailní změny

## Časté otázky

**Q: Musím přestat používat staré skripty?**  
A: Ne! Všechny staré skripty fungují. Nový `main.py` je alternativa pro interaktivní práci.

**Q: Jak získám hodnotu z matice pomocí názvů v mém kódu?**  
A: Viz [NAMED_MATRICES.md](NAMED_MATRICES.md) nebo spusťte `python3 demo_named_matrices.py`

**Q: Funguje to i na Windows?**  
A: Ano! Použijte `start.bat` místo `start.sh`

**Q: Kde najdu příklady použití?**  
A: V [MAIN_PROGRAM.md](MAIN_PROGRAM.md) a [NAMED_MATRICES.md](NAMED_MATRICES.md)

## Co dál?

1. ✅ Vyzkoušejte nový `main.py`
2. ✅ Přečtěte si [MAIN_PROGRAM.md](MAIN_PROGRAM.md)
3. ✅ Experimentujte s různými grafy
4. ✅ Podívejte se na `demo_named_matrices.py` pro programování

---

**Užijte si nový intuitivní způsob práce s grafy! 🚀**

