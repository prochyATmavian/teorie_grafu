# Dokumentace rozpoznávače grafů

## Obsah
1. [Přehled](#přehled)
2. [Instalace a spuštění](#instalace-a-spuštění)
3. [Struktura projektu](#struktura-projektu)
4. [Moduly a funkce](#moduly-a-funkce)
5. [Formát vstupního souboru](#formát-vstupního-souboru)
6. [Příklady použití](#příklady-použití)

---

## Přehled

Rozpoznávač grafů je nástroj pro analýzu grafů zadaných v textovém formátu. Program:
- Načítá grafy z textových souborů
- Analyzuje vlastnosti grafů
- Počítá charakteristiky uzlů
- Sestavuje různé matice a seznamy
- Vizualizuje grafy (textově nebo graficky)

---

## Instalace a spuštění

### Základní použití (bez grafické vizualizace)
```bash
python3 run.py <soubor_s_grafem.tg>
```

### S grafickou vizualizací (volitelné)
```bash
# Instalace knihoven pro vizualizaci
pip install matplotlib networkx
# nebo
pip install graphviz

# Spuštění
python3 run.py <soubor_s_grafem.tg>
```

---

## Struktura projektu

```
rozeznavac_grafu/
├── run.py              # Hlavní program
├── parser.py           # Parser pro načítání grafů
├── graph.py            # Třída Graph - reprezentace grafu
├── analyzer.py         # Analýza vlastností grafu
├── matrices.py         # Sestavování matic a seznamů
├── visualizer.py       # Vizualizace grafů
├── READ_ME             # Zadání úkolu
└── DOKUMENTACE.md      # Tento soubor
```

---

## Moduly a funkce

### 1. parser.py

#### Třída `Node`
Reprezentace uzlu v grafu.

**Atributy:**
- `identifier` (str): Identifikátor uzlu
- `weight` (float|None): Ohodnocení uzlu

#### Třída `Edge`
Reprezentace hrany v grafu.

**Atributy:**
- `node1` (str): První uzel
- `node2` (str): Druhý uzel
- `directed` (bool): True pokud je hrana orientovaná
- `reverse` (bool): True pro operátor `<`
- `weight` (float|None): Váha hrany
- `label` (str|None): Označení hrany

**Vlastnosti:**
- `source`: Zdrojový uzel (pro orientované hrany)
- `target`: Cílový uzel (pro orientované hrany)

#### Třída `GraphParser`
Parser pro zpracování textového formátu.

**Metody:**
- `parse_file(filepath)`: Načte a parsuje soubor
  - **Parametry:** 
    - `filepath` (str): Cesta k souboru
  - **Vrací:** tuple (nodes, edges, is_binary_tree)

- `parse_content(content)`: Parsuje textový obsah
  - **Parametry:** 
    - `content` (str): Textový obsah
  - **Vrací:** tuple (nodes, edges, is_binary_tree)

---

### 2. graph.py

#### Třída `Graph`
Reprezentace grafu s uzly a hranami.

**Atributy:**
- `nodes` (dict): Slovník uzlů {identifier: Node}
- `edges_list` (list): Seznam hran
- `is_binary_tree` (bool): True pro binární strom
- `adjacency_list` (dict): Seznam sousednosti
- `in_neighbors` (dict): Vstupní sousedé (orientované)
- `out_neighbors` (dict): Výstupní sousedé (orientované)

**Metody:**

##### Základní informace
- `get_node_count()`: Počet uzlů
- `get_edge_count()`: Počet hran
- `has_node(node_id)`: Kontrola existence uzlu

##### Sousedé (k-m)
- `get_neighbors(node_id)`: Sousedé uzlu
- `get_successors(node_id)`: **U+(node_id)** - Následníci uzlu
- `get_predecessors(node_id)`: **U-(node_id)** - Předchůdci uzlu
- `get_all_neighbors(node_id)`: **U(node_id)** - Všichni sousedé

##### Hrany (n-p)
- `get_outgoing_edges(node_id)`: **H+(node_id)** - Výstupní hrany
- `get_incoming_edges(node_id)`: **H-(node_id)** - Vstupní hrany
- `get_incident_edges(node_id)`: **H(node_id)** - Všechny incidentní hrany

##### Stupně (q-s)
- `get_out_degree(node_id)`: **d+(node_id)** - Výstupní stupeň
- `get_in_degree(node_id)`: **d-(node_id)** - Vstupní stupeň
- `get_degree(node_id)`: **d(node_id)** - Celkový stupeň

##### Vlastnosti
- `is_directed()`: Je graf orientovaný?
- `is_weighted()`: Je graf ohodnocený?
- `has_self_loop()`: Obsahuje smyčky?
- `has_multiple_edges()`: Obsahuje vícenásobné hrany?

##### Prohledávání
- `bfs(start_node)`: BFS - množina dosažitelných uzlů
- `bfs_undirected(start_node)`: BFS ignorující směry

---

### 3. analyzer.py

#### Třída `GraphAnalyzer`
Analýza vlastností grafů.

**Metody:**

##### Vlastnosti grafu (a-j)
- `is_weighted()`: **a) Ohodnocený** - má hrany váhy?
- `is_directed()`: **b) Orientovaný** - mají hrany směr?
- `is_connected()`: **c) Souvislý** - existuje cesta mezi všemi uzly?
  - Vrací: `{'connected': bool, 'type': 'strongly'/'weakly'/None}`
  - Silně souvislý: ze všech uzlů do všech
  - Slabě souvislý: z nějakého uzlu do všech (ignoruje směry)
  
- `is_simple()`: **d) Prostý** - bez smyček a vícenásobných hran?
- `is_loop_free()`: **e) Jednoduchý** - bez smyček?
- `is_planar()`: **f) Rovinný** - lze nakreslit bez křížení hran?
  - Používá Eulerovu formulu: m ≤ 3n - 6
  - Vrací: `{'planar': bool, 'method': str, 'note': str}`
  
- `is_finite()`: **g) Konečný** - konečný počet uzlů a hran?
- `is_complete()`: **h) Úplný** - každý uzel spojen se všemi?
- `is_regular()`: **i) Regulární** - všechny uzly stejný stupeň?
  - Vrací: `{'regular': bool, 'degree': int|None}`
  
- `is_bipartite()`: **j) Bipartitní** - lze rozdělit do dvou disjunktních množin?
  - Vrací: `{'bipartite': bool, 'partition': (set, set)|None}`
  - Používá 2-coloring algoritmus

##### Souhrnná analýza
- `analyze_all()`: Provede všechny analýzy a-j
  - Vrací slovník se všemi vlastnostmi

---

### 4. matrices.py

#### Třída `MatrixBuilder`
Sestavování matic a seznamů.

**Metody:**

##### Matice sousednosti
- `adjacency_matrix()`: **a) Matice sousednosti**
  - A[i][j] = počet hran z uzlu i do uzlu j
  - Vrací: (matrix, node_list)

- `weighted_adjacency_matrix()`: Matice s vahami
  - A[i][j] = váha hrany z uzlu i do uzlu j
  - Vrací: (matrix, node_list)

- `signed_matrix()`: **b) Znaménková matice**
  - A[i][j] = 1 pokud existuje hrana, jinak 0
  - Vrací: (matrix, node_list)

##### Mocniny
- `adjacency_matrix_powers(max_power=3)`: **c) Mocniny matice sousednosti**
  - A^k[i][j] = počet cest délky k z i do j
  - Vrací: {mocnina: (matrix, node_list)}

##### Ostatní matice
- `incidence_matrix()`: **d) Matice incidence**
  - Řádky = uzly, sloupce = hrany
  - Orientovaný: M[i][j] = 1 (výstupní), -1 (vstupní)
  - Neorientovaný: M[i][j] = 1 (incidentní)
  - Vrací: (matrix, nodes, edges)

- `distance_matrix()`: **e) Matice délek**
  - Floyd-Warshallův algoritmus
  - D[i][j] = nejkratší vzdálenost z i do j
  - Vrací: (matrix, node_list)

- `predecessor_matrix()`: **f) Matice předchůdců**
  - P[i][j] = předchůdce j na nejkratší cestě z i do j
  - Vrací: (matrix, node_list)

##### Seznamy
- `incident_edges_table()`: **g) Tabulka incidentních hran**
  - Pro každý uzel seznam incidentních hran
  - Vrací: {node: [edges]}

- `neighbor_list()`: **h) Seznam sousedů**
  - Pro každý uzel seznam sousedů
  - Vrací: {node: [neighbors]}

- `node_and_edge_list()`: **i) Seznam uzlů a hran**
  - Vrací: {'nodes': list, 'edges': list}

##### Souhrnné sestavení
- `build_all_matrices()`: Sestaví všechny matice a seznamy
  - Vrací slovník se všemi výsledky

---

### 5. visualizer.py

#### Třída `TextVisualizer`
Textová vizualizace grafu.

**Metody:**
- `draw_text()`: Vytvoří textovou reprezentaci
  - Seznam uzlů a hran
  
- `draw_adjacency_list()`: Vizualizace seznamu sousednosti
  - Pro každý uzel jeho sousedé

#### Funkce pro grafickou vizualizaci

- `try_matplotlib_visualization(graph, output_file)`: 
  - Vizualizace pomocí matplotlib a networkx
  - Vyžaduje: `pip install matplotlib networkx`
  
- `try_graphviz_visualization(graph, output_file)`: 
  - Vizualizace pomocí graphviz
  - Vyžaduje: `pip install graphviz`
  
- `visualize_graph(graph, method='auto', output_file='graph_output')`: 
  - Univerzální funkce pro vizualizaci
  - **Parametry:**
    - `method`: 'auto', 'text', 'matplotlib', 'graphviz'
    - `output_file`: Název výstupního souboru
  - **Vrací:** Cestu k souboru nebo textovou reprezentaci

---

## Formát vstupního souboru

### Syntaxe

#### Definice uzlu
```
u identifikator [ohodnoceni];
```

**Příklady:**
```
u A;          # Uzel A bez ohodnocení
u B 5;        # Uzel B s ohodnocením 5
u C -3.5;     # Uzel C s ohodnocením -3.5
u *;          # Vynechaný uzel (binární strom)
```

#### Definice hrany
```
h uzel1 (< | - | >) uzel2 [ohodnoceni] [:oznaceni];
```

**Operátory:**
- `>` nebo `->`: Orientovaná hrana uzel1 → uzel2
- `<` nebo `<-`: Orientovaná hrana uzel1 ← uzel2
- `-`: Neorientovaná hrana uzel1 — uzel2

**Příklady:**
```
h A > B;              # Orientovaná hrana A → B
h A > B 5;            # S váhou 5
h A > B 5 :h1;        # S váhou 5 a označením "h1"
h C - D;              # Neorientovaná hrana C — D
h E < F 3.5 :edge2;   # Orientovaná E ← F, váha 3.5, označení "edge2"
```

### Pravidla

1. **Pořadí může být libovolné**, až na:
   - Hrana může být definována až po definici obou uzlů
   - U binárních stromů: uzly jsou zadány chronologicky po úrovních (level-order)

2. **Binární strom:**
   - Pouze příkazy `u` (bez příkazů `h`)
   - Hvězdička `u *;` = vynechaný uzel
   - Struktura odvozena z pořadí: pozice i má děti na 2i+1 a 2i+2

3. **Komentáře:** Řádky začínající `#` jsou ignorovány

### Příklad grafu

```
u A;
u B;
h A > B 1 :h1;
u C;
h B > C 1 :h2;
u D;
h A > D 2 :h3;
```

---

## Příklady použití

### 1. Základní analýza
```bash
python3 run.py graph.tg
```

Program provede:
- Načtení grafu
- Textovou vizualizaci
- Analýzu vlastností (a-j)
- Výpočty pro uzly (k-s)
- Sestavení matic

### 2. V Pythonu

```python
from parser import GraphParser
from graph import Graph
from analyzer import GraphAnalyzer

# Načtení grafu
parser = GraphParser()
nodes, edges, is_binary_tree = parser.parse_file('graph.tg')

# Vytvoření grafu
graph = Graph(nodes, edges, is_binary_tree)

# Analýza
analyzer = GraphAnalyzer(graph)
properties = analyzer.analyze_all()

# Informace o uzlu
successors = graph.get_successors('A')  # U+(A)
degree = graph.get_degree('A')           # d(A)

# Vlastnosti
print(f"Orientovaný: {properties['b_directed']}")
print(f"Souvislý: {properties['c_connected']}")
print(f"Bipartitní: {properties['j_bipartite']}")
```

### 3. Matice

```python
from matrices import MatrixBuilder

builder = MatrixBuilder(graph)

# Matice sousednosti
adj_matrix, nodes = builder.adjacency_matrix()

# Matice délek
dist_matrix, nodes = builder.distance_matrix()

# Seznam sousedů
neighbors = builder.neighbor_list()
```

### 4. Vizualizace

```python
from visualizer import visualize_graph, TextVisualizer

# Textová
viz = TextVisualizer(graph)
print(viz.draw_text())

# Grafická (pokud jsou knihovny)
result = visualize_graph(graph, method='matplotlib', output_file='muj_graf')
```

---

## Výstup programu

Program vypíše:

1. **Základní informace:** počet uzlů, hran, typ grafu
2. **Textová vizualizace:** seznam uzlů a hran
3. **Seznam sousednosti:** pro každý uzel jeho sousedé
4. **Vlastnosti grafu (a-j):**
   - a) Ohodnocený
   - b) Orientovaný
   - c) Souvislý (silně/slabě)
   - d) Prostý
   - e) Jednoduchý
   - f) Rovinný
   - g) Konečný
   - h) Úplný
   - i) Regulární
   - j) Bipartitní

5. **Informace o uzlech (k-s):**
   - k) U+(v) - následníci
   - l) U-(v) - předchůdci
   - m) U(v) - sousedé
   - n) H+(v) - výstupní hrany
   - o) H-(v) - vstupní hrany
   - p) H(v) - okolí
   - q) d+(v) - výstupní stupeň
   - r) d-(v) - vstupní stupeň
   - s) d(v) - stupeň

6. **Matice a seznamy:**
   - a) Matice sousednosti
   - b) Znaménková matice
   - c) Mocniny matice sousednosti
   - d) Matice incidence
   - e) Matice délek
   - f) Matice předchůdců
   - g) Tabulka incidentních hran
   - h) Seznam sousedů
   - i) Seznam uzlů a hran

---

## Poznámky

- Program funguje **bez externích knihoven**
- Grafická vizualizace je **volitelná** (vyžaduje matplotlib/networkx nebo graphviz)
- Pro binární stromy se automaticky používá level-order interpretace
- Podporuje **orientované i neorientované grafy**
- Podporuje **ohodnocené uzly i hrany**
- Podporuje **označení hran**

---

## Autor a licence

Vytvořeno pro předmět Teorie grafů, Mendelu Brno.

