# Changelog - Verze 2.0

## 🎉 Nová funkce: NamedMatrix - Přístup k maticím pomocí názvů

**Datum:** 21. října 2025

### Co je nového?

Implementováno nové API pro přístup k prvkům matic pomocí **názvů uzlů a hran** místo číselných indexů.

### Motivace

**Před:**
```python
builder = MatrixBuilder(graph)
adj_matrix, nodes = builder.adjacency_matrix()

# Nejasné - který uzel je na indexu 0 a 1?
value = adj_matrix[0][1]
```

**Po:**
```python
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Jasné a čitelné!
value = adj_matrix['A']['B']
```

### Změny v kódu

#### 1. Nové třídy v `src/matrices.py`

- **`NamedMatrix`**: Wrapper třída pro matice s podporou názvového indexování
- **`NamedMatrixRow`**: Helper třída pro druhé indexování

#### 2. Aktualizované metody v `MatrixBuilder`

Všechny metody nyní vracejí `NamedMatrix` místo tuple `(matrix, labels)`:

| Metoda                        | Před (tuple)           | Po (NamedMatrix)        |
|-------------------------------|------------------------|-------------------------|
| `adjacency_matrix()`          | `(matrix, nodes)`      | `NamedMatrix`           |
| `weighted_adjacency_matrix()` | `(matrix, nodes)`      | `NamedMatrix`           |
| `signed_matrix()`             | `(matrix, nodes)`      | `NamedMatrix`           |
| `adjacency_matrix_powers()`   | `{p: (matrix, nodes)}` | `{p: NamedMatrix}`      |
| `incidence_matrix()`          | `(matrix, nodes, edges)`| `NamedMatrix`          |
| `distance_matrix()`           | `(matrix, nodes)`      | `NamedMatrix`           |
| `predecessor_matrix()`        | `(matrix, nodes)`      | `NamedMatrix`           |

#### 3. Aktualizovaný `scripts/analyze_matrices.py`

- Funkce `print_matrix()` nyní podporuje `NamedMatrix`
- Funkce `get_matrix_element()` rozšířena o podporu názvového indexování
- Zpětná kompatibilita s číselným indexováním zachována

#### 4. Nové soubory

- **`demo_named_matrices.py`**: Ukázkový skript demonstrující nové API
- **`docs/NAMED_MATRICES.md`**: Kompletní dokumentace

### Nové funkce třídy NamedMatrix

```python
# Přístup pomocí názvů
value = matrix['A']['B']

# Přístup pomocí indexů (zpětná kompatibilita)
value = matrix[0][1]

# Kombinace
value = matrix['A'][1]
value = matrix[0]['B']

# Alternativní syntaxe
value = matrix.get('A', 'B')

# Získání surových dat
raw_data = matrix.raw()

# Získání popisků
nodes = matrix.row_labels()
edges = matrix.col_labels()

# Počet řádků
num_rows = len(matrix)
```

### Výhody

✅ **Čitelnost**: Kód je self-dokumentující  
✅ **Bezpečnost**: Lepší chybové hlášky s dostupnými uzly/hranami  
✅ **Flexibilita**: Kombinace názvů a indexů  
✅ **Zpětná kompatibilita**: Starý kód funguje beze změn  
✅ **Intuitivnost**: Přirozené použití  

### Zpětná kompatibilita

✅ **Plně zachována**

Všechny existující skripty fungují beze změn:

```python
# Starý kód stále funguje
adj_matrix = builder.adjacency_matrix()
value = adj_matrix[0][1]  # ✅ Funguje
```

Číselné indexy jsou stále podporovány vedle názvového indexování.

### Testování

Všechny testy prošly úspěšně:

```bash
# Ukázkový skript
$ python3 demo_named_matrices.py
✅ Všechny funkce fungují

# Existující skripty
$ python3 scripts/analyze_matrices.py data/grafy/01.tg --all 0 1
✅ Zpětná kompatibilita zachována
```

### Dokumentace

Nová dokumentace přidána:

- **`docs/NAMED_MATRICES.md`**: Kompletní návod s příklady
- **`demo_named_matrices.py`**: Interaktivní ukázka
- **`README.md`**: Aktualizováno s odkazem na nové API

### Příklady použití

#### Matice sousednosti

```python
adj_matrix = builder.adjacency_matrix()

# Existuje hrana z A do B?
if adj_matrix['A']['B'] > 0:
    print("Ano, existuje hrana z A do B")
```

#### Matice incidence

```python
inc_matrix = builder.incidence_matrix()

# Je uzel A incidentní s hranou h1?
if inc_matrix['A']['h1'] != 0:
    print("Ano, uzel A je incidentní s hranou h1")
```

#### Matice délek

```python
dist_matrix = builder.distance_matrix()

# Jaká je vzdálenost z A do F?
distance = dist_matrix['A']['F']
if distance == float('inf'):
    print("F není dosažitelný z A")
else:
    print(f"Vzdálenost z A do F: {distance}")
```

### Migrace starého kódu

Není vyžadována! Starý kód funguje beze změn.

Pro využití nových funkcí můžete postupně upravit:

```python
# Před
matrix, nodes = builder.adjacency_matrix()
node_index = {node: i for i, node in enumerate(nodes)}
value = matrix[node_index['A']][node_index['B']]

# Po
matrix = builder.adjacency_matrix()
value = matrix['A']['B']
```

### Známé problémy

Žádné.

### Budoucí vylepšení

Možná rozšíření:

- [ ] Iterace přes řádky/sloupce podle názvů
- [ ] Slicing pomocí názvů (např. `matrix['A':'C']`)
- [ ] Export do pandas DataFrame
- [ ] NumPy integrace

### Autor změny

Implementováno v rámci vylepšení projektu Rozpoznávač grafů.

---

Pro více informací viz:
- [docs/NAMED_MATRICES.md](NAMED_MATRICES.md)
- [../demo_named_matrices.py](../demo_named_matrices.py)
- [../README.md](../README.md)

