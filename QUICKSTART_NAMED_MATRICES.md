# 🚀 Rychlý průvodce: Přístup k maticím pomocí názvů

## 📝 TL;DR

Nyní můžete používat názvy uzlů/hran místo číselných indexů:

```python
# ✨ NOVÉ - Názvy uzlů
value = matrix['A']['B']

# ✅ STARÉ - Číselné indexy (stále funguje)
value = matrix[0][1]
```

## 🎯 Základní příklady

### Příklad 1: Jednoduchý přístup

```python
from src.parser import GraphParser
from src.graph import Graph
from src.matrices import MatrixBuilder

# Načtení grafu
parser = GraphParser()
nodes, edges, _ = parser.parse_file("data/grafy/01.tg")
graph = Graph(nodes, edges)

# Vytvoření matic
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Přístup pomocí názvů - NOVĚ!
print(adj_matrix['A']['B'])  # Hrana z A do B
print(adj_matrix['C']['D'])  # Hrana z C do D
```

### Příklad 2: Kontrola existence hrany

```python
adj_matrix = builder.adjacency_matrix()

# Existuje hrana z A do B?
if adj_matrix['A']['B'] > 0:
    print("✅ Hrana A→B existuje")
else:
    print("❌ Hrana A→B neexistuje")
```

### Příklad 3: Vzdálenost mezi uzly

```python
dist_matrix = builder.distance_matrix()

# Jaká je nejkratší cesta z A do F?
distance = dist_matrix['A']['F']

if distance == float('inf'):
    print("❌ F není dosažitelný z A")
else:
    print(f"✅ Vzdálenost z A do F: {distance}")
```

### Příklad 4: Matice incidence

```python
inc_matrix = builder.incidence_matrix()

# Je uzel A incidentní s hranou h1?
if inc_matrix['A']['h1'] != 0:
    print("✅ Uzel A je incidentní s hranou h1")
```

## 🔄 Migrace z číselných indexů

### Před (složité)

```python
builder = MatrixBuilder(graph)
adj_matrix, nodes = builder.adjacency_matrix()

# Musíte vytvořit mapování
node_index = {node: i for i, node in enumerate(nodes)}

# Složité vyhledání indexů
i = node_index['A']
j = node_index['B']
value = adj_matrix[i][j]
```

### Po (jednoduché)

```python
builder = MatrixBuilder(graph)
adj_matrix = builder.adjacency_matrix()

# Přímočaré!
value = adj_matrix['A']['B']
```

## 💡 Užitečné metody

```python
adj_matrix = builder.adjacency_matrix()

# Získání popisků
nodes = adj_matrix.row_labels()     # ['A', 'B', 'C', ...]
edges = inc_matrix.col_labels()     # ['h1', 'h2', 'h3', ...]

# Alternativní syntaxe
value = adj_matrix.get('A', 'B')    # Stejné jako adj_matrix['A']['B']

# Surová data (2D seznam)
raw = adj_matrix.raw()              # [[0, 1, 0, ...], ...]

# Počet řádků
num_nodes = len(adj_matrix)
```

## 🎓 Praktické příklady

### Najít všechny sousedy uzlu

```python
adj_matrix = builder.adjacency_matrix()
nodes = adj_matrix.row_labels()

node = 'A'
neighbors = [n for n in nodes if adj_matrix[node][n] > 0]
print(f"Sousedé uzlu {node}: {neighbors}")
```

### Matice vzdáleností jako tabulka

```python
dist_matrix = builder.distance_matrix()
nodes = dist_matrix.row_labels()

print("Matice vzdáleností:")
for node1 in nodes:
    for node2 in nodes:
        d = dist_matrix[node1][node2]
        if d == float('inf'):
            print(f"{node1}→{node2}: ∞")
        else:
            print(f"{node1}→{node2}: {d}")
```

### Kontrola souvislosti

```python
dist_matrix = builder.distance_matrix()
nodes = dist_matrix.row_labels()

disconnected = []
for i, node1 in enumerate(nodes):
    for node2 in nodes[i+1:]:
        if dist_matrix[node1][node2] == float('inf'):
            disconnected.append((node1, node2))

if disconnected:
    print("❌ Graf není souvislý. Nedosažitelné páry:")
    for n1, n2 in disconnected:
        print(f"  {n1} ↔ {n2}")
else:
    print("✅ Graf je souvislý")
```

## 🚀 Ukázková aplikace

Spusťte interaktivní demo:

```bash
python3 demo_named_matrices.py
```

Tato aplikace ukazuje:
- Přístup pomocí názvů vs. indexů
- Různé typy matic
- Chybové stavy
- Užitečné metody

## 📚 Další informace

- **Kompletní dokumentace:** [docs/NAMED_MATRICES.md](docs/NAMED_MATRICES.md)
- **Changelog:** [docs/CHANGELOG_V2.md](docs/CHANGELOG_V2.md)
- **Hlavní README:** [README.md](README.md)

## ❓ FAQ

**Q: Musím upravit svůj starý kód?**  
A: Ne! Číselné indexy stále fungují. Můžete přejít postupně.

**Q: Mohu kombinovat názvy a indexy?**  
A: Ano! `matrix['A'][1]` i `matrix[0]['B']` funguje.

**Q: Co se stane, když zadám neexistující uzel?**  
A: Dostanete `KeyError` s užitečnou chybovou hláškou:
```
KeyError: "Řádek 'X' neexistuje v matici. Dostupné: ['A', 'B', 'C']"
```

**Q: Jak získám surová data pro NumPy?**  
A: Použijte metodu `.raw()`:
```python
import numpy as np
matrix_np = np.array(adj_matrix.raw())
```

## ✅ Checklist pro přechod

- [ ] Přečetl jsem [NAMED_MATRICES.md](docs/NAMED_MATRICES.md)
- [ ] Spustil jsem `demo_named_matrices.py`
- [ ] Vyzkoušel jsem nové API na svém kódu
- [ ] Rozumím rozdílu mezi `.raw()` a `NamedMatrix`
- [ ] Vím, jak získat popisky pomocí `.row_labels()` a `.col_labels()`

## 🎉 Hotovo!

Nyní víte, jak používat nové API pro přístup k maticím pomocí názvů uzlů a hran.

Užijte si čitelnější a intuitivnější kód! 🚀

