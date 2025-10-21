# NamedMatrix - Přístup k maticím pomocí názvů

## Přehled

Nové API `NamedMatrix` umožňuje přistupovat k prvkům matic pomocí **názvů uzlů a hran** místo číselných indexů. To činí kód čitelnější a méně náchylný k chybám.

## Základní použití

### Starý způsob (číselné indexy)

```python
from src.matrices import MatrixBuilder

builder = MatrixBuilder(graph)
adj_matrix, nodes = builder.adjacency_matrix()

# Musíte vědět, že A je na indexu 0 a B na indexu 1
value = adj_matrix[0][1]  # Hrana z A do B?
```

### Nový způsob (názvy uzlů)

```python
from src.matrices import MatrixBuilder

builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()  # Vrací NamedMatrix

# Přímočaré a jasné!
value = adj_matrix['A']['B']  # Hrana z A do B
```

## Podporované matice

Všechny matice nyní vracejí `NamedMatrix`:

| Metoda                       | Typ řádků | Typ sloupců |
|------------------------------|-----------|-------------|
| `adjacency_matrix()`         | Uzly      | Uzly        |
| `weighted_adjacency_matrix()`| Uzly      | Uzly        |
| `signed_matrix()`            | Uzly      | Uzly        |
| `adjacency_matrix_powers()`  | Uzly      | Uzly        |
| `incidence_matrix()`         | Uzly      | Hrany       |
| `distance_matrix()`          | Uzly      | Uzly        |
| `predecessor_matrix()`       | Uzly      | Uzly        |

## Příklady použití

### 1. Matice sousednosti

```python
from src.parser import GraphParser
from src.graph import Graph
from src.matrices import MatrixBuilder

# Načtení grafu
parser = GraphParser()
nodes, edges, _ = parser.parse_file("data/grafy/01.tg")
graph = Graph(nodes, edges)

# Vytvoření matice
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Přístup pomocí názvů
print(adj_matrix['A']['B'])  # Počet hran z A do B
print(adj_matrix['C']['D'])  # Počet hran z C do D

# Stále můžete použít indexy
print(adj_matrix[0][1])  # Stejné jako adj_matrix['A']['B']

# Kombinace
print(adj_matrix['A'][1])  # Z uzlu A k druhému uzlu
```

### 2. Matice incidence

```python
inc_matrix = builder.incidence_matrix()

# Přístup pomocí názvu uzlu a hrany
print(inc_matrix['A']['h1'])  # Je uzel A incidentní s hranou h1?
print(inc_matrix['B']['h5'])  # Je uzel B incidentní s hranou h5?
```

### 3. Matice délek (Floyd-Warshall)

```python
dist_matrix = builder.distance_matrix()

# Vzdálenost mezi uzly
distance = dist_matrix['A']['F']
if distance == float('inf'):
    print("Uzel F není dosažitelný z A")
else:
    print(f"Vzdálenost z A do F: {distance}")
```

### 4. Mocniny matice sousednosti

```python
powers = builder.adjacency_matrix_powers(3)  # A^2, A^3

# Počet cest délky 2 z A do B
paths_2 = powers[2]['A']['B']
print(f"Počet cest délky 2 z A do B: {paths_2}")

# Počet cest délky 3 z C do D
paths_3 = powers[3]['C']['D']
print(f"Počet cest délky 3 z C do D: {paths_3}")
```

## Užitečné metody

### `matrix.get(row, col)`

Alternativní syntaxe pro přístup k prvkům:

```python
value = adj_matrix.get('A', 'B')  # Stejné jako adj_matrix['A']['B']
```

### `matrix.raw()`

Získání surových dat jako 2D seznam:

```python
raw_data = adj_matrix.raw()  # [[0, 1, 0, ...], [0, 0, 1, ...], ...]
```

### `matrix.row_labels()` a `matrix.col_labels()`

Získání popisků řádků a sloupců:

```python
nodes = adj_matrix.row_labels()      # ['A', 'B', 'C', ...]
edges = inc_matrix.col_labels()      # ['h1', 'h2', 'h3', ...]
```

### `len(matrix)`

Počet řádků:

```python
num_nodes = len(adj_matrix)  # Počet uzlů
```

## Chybové stavy

### Neexistující uzel/hrana

```python
try:
    value = adj_matrix['NEEXISTUJICI']['A']
except KeyError as e:
    print(f"Chyba: {e}")
    # Chyba: "Řádek 'NEEXISTUJICI' neexistuje v matici. 
    #         Dostupné: ['A', 'B', 'C', 'D', ...]"
```

### Nesprávný typ indexu

```python
try:
    value = adj_matrix[1.5]['A']  # Float není povolený
except TypeError as e:
    print(f"Chyba: {e}")
    # Chyba: "Index musí být int nebo str, ne <class 'float'>"
```

## Zpětná kompatibilita

Číselné indexy **stále fungují**:

```python
# Staré API - stále funguje
value = adj_matrix[0][1]

# Nové API
value = adj_matrix['A']['B']

# Kombinace
value = adj_matrix['A'][1]
value = adj_matrix[0]['B']
```

## Migrace starého kódu

### Před

```python
builder = MatrixBuilder(graph)
adj_matrix, nodes = builder.adjacency_matrix()

# Musíte najít index
node_index = {node: i for i, node in enumerate(nodes)}
i = node_index['A']
j = node_index['B']
value = adj_matrix[i][j]
```

### Po

```python
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Jednoduchý a jasný
value = adj_matrix['A']['B']
```

## Interní struktura

`NamedMatrix` je wrapper kolem 2D seznamu, který:

1. Ukládá mapování `název → index` pro rychlý přístup
2. Podporuje indexování pomocí `__getitem__`
3. Vrací `NamedMatrixRow` pro druhé indexování
4. Poskytuje utility metody (`raw()`, `row_labels()`, atd.)

```python
class NamedMatrix:
    def __init__(self, data, row_labels, col_labels):
        self._data = data  # 2D seznam
        self._row_index = {label: i for i, label in enumerate(row_labels)}
        self._col_index = {label: i for i, label in enumerate(col_labels)}
    
    def __getitem__(self, key):
        # Převede název → index a vrátí NamedMatrixRow
        ...
```

## Výhody

✅ **Čitelnost**: `matrix['A']['B']` je jasnější než `matrix[0][1]`  
✅ **Bezpečnost**: Chybové hlášky obsahují dostupné uzly/hrany  
✅ **Flexibilita**: Kombinace názvů a indexů  
✅ **Zpětná kompatibilita**: Starý kód stále funguje  
✅ **Dokumentace**: Self-dokumentující kód  

## Praktické příklady

### Příklad 1: Kontrola souvislosti

```python
dist_matrix = builder.distance_matrix()
nodes = dist_matrix.row_labels()

print("Kontrola souvislosti grafu:")
for i, node1 in enumerate(nodes):
    for node2 in nodes[i+1:]:
        distance = dist_matrix[node1][node2]
        if distance == float('inf'):
            print(f"  {node1} → {node2}: nedosažitelný")
        else:
            print(f"  {node1} → {node2}: {distance}")
```

### Příklad 2: Analýza hran

```python
inc_matrix = builder.incidence_matrix()
nodes = inc_matrix.row_labels()
edges = inc_matrix.col_labels()

print("Incidence uzlů a hran:")
for edge in edges:
    incident_nodes = [node for node in nodes if inc_matrix[node][edge] != 0]
    print(f"  {edge}: {incident_nodes}")
```

### Příklad 3: Vzdálenostní matice v tabulce

```python
dist_matrix = builder.distance_matrix()
nodes = dist_matrix.row_labels()

print("Matice vzdáleností:")
print("     " + "".join(f"{n:>5}" for n in nodes))
for node1 in nodes:
    row = f"{node1:>3}:"
    for node2 in nodes:
        d = dist_matrix[node1][node2]
        if d == float('inf'):
            row += "    ∞"
        else:
            row += f"{d:>5.0f}"
    print(row)
```

## Ukázková aplikace

Spusťte `demo_named_matrices.py` pro interaktivní ukázku:

```bash
python3 demo_named_matrices.py
```

Tento skript demonstruje:
- Přístup pomocí názvů vs. indexů
- Různé typy matic
- Chybové stavy
- Užitečné metody

## Další informace

Pro více informací viz:
- `src/matrices.py` - implementace `NamedMatrix`
- `demo_named_matrices.py` - ukázkový skript
- `scripts/analyze_matrices.py` - použití v praxi

