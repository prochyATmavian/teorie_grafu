#!/usr/bin/env python3
"""
Ukázka použití NamedMatrix - přístup k prvkům matic pomocí názvů uzlů/hran.

Tento skript ukazuje nové API pro práci s maticemi, kde můžete používat
názvy uzlů místo číselných indexů.
"""

import sys
from pathlib import Path

# Přidání src do sys.path
sys.path.insert(0, str(Path(__file__).parent))

from src.parser import GraphParser
from src.graph import Graph
from src.matrices import MatrixBuilder


def demo_named_matrices():
    """Ukázka použití NamedMatrix."""
    
    print("=" * 70)
    print("UKÁZKA: Přístup k maticím pomocí názvů uzlů/hran")
    print("=" * 70)
    
    # Načteme ukázkový graf
    filepath = "data/grafy/01.tg"
    
    if not Path(filepath).exists():
        print(f"❌ Soubor {filepath} neexistuje!")
        return
    
    print(f"\n📂 Načítám graf: {filepath}")
    parser = GraphParser()
    nodes, edges, is_binary_tree = parser.parse_file(filepath)
    graph = Graph(nodes, edges, is_binary_tree)
    
    print(f"✅ Načteno: {len(graph.nodes)} uzlů, {len(graph.edges_list)} hran")
    print(f"   Uzly: {sorted(graph.nodes.keys())}")
    
    # Vytvoříme matice
    builder = MatrixBuilder(graph)
    
    print("\n" + "=" * 70)
    print("1. MATICE SOUSEDNOSTI")
    print("=" * 70)
    
    adj_matrix = builder.adjacency_matrix()
    print(f"\n📊 Typ: {type(adj_matrix)}")
    print(f"📐 Rozměry: {adj_matrix}")
    print(f"   Řádky (uzly): {adj_matrix.row_labels()}")
    print(f"   Sloupce (uzly): {adj_matrix.col_labels()}")
    
    # Ukázka přístupu pomocí číselných indexů (staré API - stále funguje)
    print("\n🔢 Přístup pomocí ČÍSELNÝCH INDEXŮ:")
    if len(adj_matrix.row_labels()) > 1:
        print(f"   adj_matrix[0][1] = {adj_matrix[0][1]}")
        print(f"   adj_matrix[1][0] = {adj_matrix[1][0]}")
    
    # Ukázka přístupu pomocí názvů uzlů (nové API!)
    print("\n✨ Přístup pomocí NÁZVŮ UZLŮ:")
    node_list = adj_matrix.row_labels()
    
    if len(node_list) >= 2:
        node1, node2 = node_list[0], node_list[1]
        
        print(f"   adj_matrix['{node1}']['{node2}'] = {adj_matrix[node1][node2]}")
        print(f"   adj_matrix['{node2}']['{node1}'] = {adj_matrix[node2][node1]}")
        
        # Můžeme také použít metodu get()
        value = adj_matrix.get(node1, node2)
        print(f"\n   Alternativně: adj_matrix.get('{node1}', '{node2}') = {value}")
    
    # Kombinace - jeden index číselný, druhý název
    print("\n🔀 KOMBINACE indexů a názvů:")
    if len(node_list) >= 2:
        print(f"   adj_matrix[0]['{node_list[1]}'] = {adj_matrix[0][node_list[1]]}")
        print(f"   adj_matrix['{node_list[0]}'][1] = {adj_matrix[node_list[0]][1]}")
    
    print("\n" + "=" * 70)
    print("2. MATICE INCIDENCE")
    print("=" * 70)
    
    inc_matrix = builder.incidence_matrix()
    print(f"\n📊 Typ: {type(inc_matrix)}")
    print(f"📐 Rozměry: {inc_matrix}")
    print(f"   Řádky (uzly): {inc_matrix.row_labels()}")
    print(f"   Sloupce (hrany): {inc_matrix.col_labels()}")
    
    if len(inc_matrix.row_labels()) > 0 and len(inc_matrix.col_labels()) > 0:
        node = inc_matrix.row_labels()[0]
        edge = inc_matrix.col_labels()[0]
        
        print(f"\n✨ Přístup pomocí názvu uzlu a hrany:")
        print(f"   inc_matrix['{node}']['{edge}'] = {inc_matrix[node][edge]}")
    
    print("\n" + "=" * 70)
    print("3. MATICE DÉLEK (Floyd-Warshall)")
    print("=" * 70)
    
    dist_matrix = builder.distance_matrix()
    print(f"\n📊 Typ: {type(dist_matrix)}")
    
    if len(node_list) >= 2:
        node1, node2 = node_list[0], node_list[1]
        
        distance = dist_matrix[node1][node2]
        print(f"\n✨ Vzdálenost z '{node1}' do '{node2}':")
        if distance == float('inf'):
            print(f"   dist_matrix['{node1}']['{node2}'] = ∞ (nedosažitelný)")
        else:
            print(f"   dist_matrix['{node1}']['{node2}'] = {distance}")
    
    print("\n" + "=" * 70)
    print("4. CHYBOVÉ STAVY")
    print("=" * 70)
    
    print("\n❌ Pokus o přístup k neexistujícímu uzlu:")
    try:
        value = adj_matrix['NEEXISTUJICI_UZEL']['A']
        print(f"   Hodnota: {value}")
    except KeyError as e:
        print(f"   Chyba: {e}")
    
    print("\n" + "=" * 70)
    print("5. PŘÍSTUP K SUROVÝM DATŮM")
    print("=" * 70)
    
    print("\n🔧 Pokud potřebujete surová data (2D seznam):")
    raw_data = adj_matrix.raw()
    print(f"   Typ: {type(raw_data)}")
    print(f"   První řádek: {raw_data[0] if raw_data else 'prázdné'}")
    
    print("\n" + "=" * 70)
    print("✅ UKÁZKA DOKONČENA")
    print("=" * 70)
    print("\nNové API umožňuje:")
    print("  ✓ Použití názvů uzlů/hran místo číselných indexů")
    print("  ✓ Číselné indexy stále fungují (zpětná kompatibilita)")
    print("  ✓ Kombinace obou přístupů")
    print("  ✓ Lepší čitelnost a menší náchylnost k chybám")
    print("\nPříklady použití:")
    print("  matrix['A']['B']     - přístup pomocí názvů")
    print("  matrix[0][1]         - přístup pomocí indexů") 
    print("  matrix.get('A', 'B') - alternativní syntaxe")
    print("  matrix.raw()         - získání surových dat")
    print()


if __name__ == "__main__":
    try:
        demo_named_matrices()
    except Exception as e:
        print(f"\n❌ Chyba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

