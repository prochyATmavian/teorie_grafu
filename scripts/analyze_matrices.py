#!/usr/bin/env python3
"""
Rozpoznávač grafů - analýza matic a seznamů.

Načítá graf z textového souboru a provádí:
- Sestavení matice sousednosti
- Sestavení znaménkové matice
- Mocniny matice sousednosti
- Matice incidence
- Matice délek (Floyd-Warshall)
- Seznam sousedů
"""

import sys
from pathlib import Path

# Přidání rodičovského adresáře do sys.path pro import src modulů
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import GraphParser
from src.graph import Graph
from src.matrices import MatrixBuilder


def print_matrix(matrix, row_labels=None, col_labels=None, title="Matice"):
    """Vypíše matici v čitelném formátu."""
    print(f"\n{title}:")
    print("-" * 60)
    
    # Hlavička se sloupci
    if col_labels:
        header = "    " + " ".join(f"{label:>4}" for label in col_labels)
        print(header)
    
    # Řádky matice
    for i, row in enumerate(matrix):
        if row_labels:
            label = f"{row_labels[i]:>3}:"
        else:
            label = f"{i:>3}:"
        
        # Formátování čísel
        formatted_row = []
        for val in row:
            if val == float('inf'):
                formatted_row.append("  ∞ ")
            elif isinstance(val, float):
                formatted_row.append(f"{val:>4.1f}")
            elif val is None:
                formatted_row.append("  - ")
            else:
                formatted_row.append(f"{val:>4}")
        
        print(label + " ".join(formatted_row))
    print()


def analyze_matrices(filepath):
    """
    Načte graf a vytvoří jeho matice a seznamy.
    
    Args:
        filepath (str): Cesta k souboru s grafem
    """
    print(f"\nNačítám graf ze souboru: {filepath}")
    print("=" * 60)
    
    # 1. Parsování
    parser = GraphParser()
    nodes, edges, is_binary_tree = parser.parse_file(filepath)
    
    print(f"Načteno: {len(nodes)} uzlů, {len(edges)} hran")
    if is_binary_tree:
        print("Typ: Binární strom")
    else:
        print("Typ: Obecný graf")
    
    # 2. Vytvoření grafu
    graph = Graph(nodes, edges, is_binary_tree)
    
    # 3. Matice
    print("\n" + "=" * 60)
    print("MATICE A SEZNAMY")
    print("=" * 60)
    
    builder = MatrixBuilder(graph)
    
    # Matice sousednosti
    adj_matrix, nodes_list = builder.adjacency_matrix()
    print_matrix(adj_matrix, nodes_list, nodes_list, "a) Matice sousednosti")
    
    # Znaménková matice
    sign_matrix, _ = builder.signed_matrix()
    print_matrix(sign_matrix, nodes_list, nodes_list, "b) Znaménková matice")
    
    # Mocniny matice sousednosti
    if len(nodes_list) <= 10:  # Pouze pro menší grafy
        powers = builder.adjacency_matrix_powers(3)
        for power, (matrix, _) in powers.items():
            print_matrix(matrix, nodes_list, nodes_list, f"c) Matice sousednosti^{power}")
    else:
        print(f"\nc) Matice sousednosti^n: Vynecháno (graf má {len(nodes_list)} uzlů > 10)")
    
    # Matice incidence
    inc_matrix, nodes_inc, edges_inc = builder.incidence_matrix()
    edge_labels = [f"e{i}" for i in range(len(edges_inc))]
    print_matrix(inc_matrix, nodes_inc, edge_labels, "d) Matice incidence")
    
    # Matice délek
    dist_matrix, _ = builder.distance_matrix()
    print_matrix(dist_matrix, nodes_list, nodes_list, "e) Matice délek (Floyd-Warshall)")
    
    # Seznam sousedů
    print("\nh) Seznam sousedů:")
    neighbors = builder.neighbor_list()
    for node, neighs in neighbors.items():
        print(f"   {node}: {neighs}")
    
    print("\n" + "=" * 60)
    print("ANALÝZA MATIC DOKONČENA")
    print("=" * 60)
    
    return graph


def main():
    """Hlavní funkce programu."""
    if len(sys.argv) < 2:
        print("Použití: python analyze_matrices.py <soubor_s_grafem>")
        print("Příklad: python analyze_matrices.py graph.tg")
        
        # Pokud je spuštěno bez parametrů, zkusíme testovací soubor
        test_file = str(Path(__file__).parent.parent / "data" / "grafy" / "01.tg")
        print(f"\nZkouším testovací soubor: {test_file}")
        try:
            analyze_matrices(test_file)
        except FileNotFoundError:
            print(f"Testovací soubor nenalezen: {test_file}")
            sys.exit(1)
    else:
        filepath = sys.argv[1]
        
        try:
            analyze_matrices(filepath)
        except FileNotFoundError:
            print(f"Soubor nenalezen: {filepath}")
            sys.exit(1)
        except Exception as e:
            print(f"Chyba při zpracování: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


if __name__ == "__main__":
    main()

