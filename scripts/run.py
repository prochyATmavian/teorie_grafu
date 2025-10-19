#!/usr/bin/env python3
"""
Rozpoznávač grafů - hlavní program.

Načítá graf z textového souboru a provádí jeho analýzu:
- Detekce vlastností grafu
- Výpočty pro uzly
- Sestavení matic a seznamů
- Vizualizace
"""

import sys
import os
from pathlib import Path

# Přidání rodičovského adresáře do sys.path pro import src modulů
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parser import GraphParser
from src.graph import Graph
from src.analyzer import GraphAnalyzer
from src.matrices import MatrixBuilder
from src.visualizer import visualize_graph, TextVisualizer


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


def print_properties(properties):
    """Vypíše vlastnosti grafu."""
    print("\n" + "=" * 60)
    print("VLASTNOSTI GRAFU")
    print("=" * 60)
    
    print(f"\na) Ohodnocený: {'ANO' if properties['a_weighted'] else 'NE'}")
    print(f"b) Orientovaný: {'ANO' if properties['b_directed'] else 'NE'}")
    
    conn = properties['c_connected']
    if conn['connected']:
        if conn['type']:
            print(f"c) Souvislý: ANO ({conn['type']} - {conn['type']})")
        else:
            print(f"c) Souvislý: ANO")
    else:
        print(f"c) Souvislý: NE")
    
    print(f"d) Prostý: {'ANO' if properties['d_simple'] else 'NE'}")
    print(f"e) Jednoduchý (bez smyček): {'ANO' if properties['e_loop_free'] else 'NE'}")
    
    planar = properties['f_planar']
    print(f"f) Rovinný: {'ANO' if planar['planar'] else 'NE'} ({planar['note']})")
    
    print(f"g) Konečný: {'ANO' if properties['g_finite'] else 'NE'}")
    print(f"h) Úplný: {'ANO' if properties['h_complete'] else 'NE'}")
    
    regular = properties['i_regular']
    if regular['regular']:
        print(f"i) Regulární: ANO (stupeň {regular['degree']})")
    else:
        print(f"i) Regulární: NE")
    
    bipartite = properties['j_bipartite']
    if bipartite['bipartite']:
        p1, p2 = bipartite['partition']
        print(f"j) Bipartitní: ANO")
        print(f"   Partition 1: {{{', '.join(sorted(p1))}}}")
        print(f"   Partition 2: {{{', '.join(sorted(p2))}}}")
    else:
        print(f"j) Bipartitní: NE")


def print_node_info(graph, node_id):
    """Vypíše informace o uzlu."""
    if not graph.has_node(node_id):
        print(f"Uzel '{node_id}' neexistuje!")
        return
    
    print(f"\nINFORMACE O UZLU: {node_id}")
    print("-" * 40)
    
    print(f"k) U+({node_id}) - Následníci: {{{', '.join(graph.get_successors(node_id))}}}")
    print(f"l) U-({node_id}) - Předchůdci: {{{', '.join(graph.get_predecessors(node_id))}}}")
    print(f"m) U({node_id}) - Sousedé: {{{', '.join(sorted(graph.get_all_neighbors(node_id)))}}}")
    
    out_edges = graph.get_outgoing_edges(node_id)
    print(f"n) H+({node_id}) - Výstupní hrany: {len(out_edges)}")
    for edge in out_edges:
        print(f"     {edge}")
    
    in_edges = graph.get_incoming_edges(node_id)
    print(f"o) H-({node_id}) - Vstupní hrany: {len(in_edges)}")
    for edge in in_edges:
        print(f"     {edge}")
    
    incident = graph.get_incident_edges(node_id)
    print(f"p) H({node_id}) - Okolí (všechny hrany): {len(incident)}")
    
    print(f"q) d+({node_id}) - Výstupní stupeň: {graph.get_out_degree(node_id)}")
    print(f"r) d-({node_id}) - Vstupní stupeň: {graph.get_in_degree(node_id)}")
    print(f"s) d({node_id}) - Stupeň: {graph.get_degree(node_id)}")


def analyze_graph(filepath, visualize=True, nodes_to_display=None):
    """
    Načte a analyzuje graf ze souboru.
    
    Args:
        filepath (str): Cesta k souboru s grafem
        visualize (bool): Zda vizualizovat graf
        nodes_to_display (list): Seznam uzlů, pro které zobrazit detaily. None = nezobrazovat.
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
    
    # 3. Vizualizace
    if visualize:
        print("\n" + "=" * 60)
        print("VIZUALIZACE")
        print("=" * 60)
        visualizer = TextVisualizer(graph)
        print(visualizer.draw_text())
        print(visualizer.draw_adjacency_list())
        
        # Vytvoříme složku pro výstupy, pokud neexistuje
        output_dir = Path(__file__).parent.parent / "output" / "vykreslene_grafy"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Vytvoříme název souboru z cesty vstupního grafu
        input_name = Path(filepath).stem
        output_path = output_dir / f"graf_{input_name}"
        
        # Pokus o grafickou vizualizaci
        print("\nPokouším se vykreslit graf graficky...")
        result = visualize_graph(graph, method='auto', output_file=str(output_path))
        if not result.endswith('.png'):
            print(result)  # Textová vizualizace jako fallback
    
    # 4. Analýza vlastností
    analyzer = GraphAnalyzer(graph)
    properties = analyzer.analyze_all()
    print_properties(properties)
    
    # 5. Informace o uzlech
    if nodes_to_display is not None and len(nodes_to_display) > 0:
        print("\n" + "=" * 60)
        print("INFORMACE O UZLECH (k-s)")
        print("=" * 60)
        
        # Zobrazíme pouze zadané uzly
        for node_id in nodes_to_display:
            if graph.has_node(node_id):
                print_node_info(graph, node_id)
            else:
                print(f"\nVarování: Uzel '{node_id}' neexistuje v grafu!")
        
        print(f"\n(Zobrazeno {len([n for n in nodes_to_display if graph.has_node(n)])} z {len(graph.nodes)} uzlů)")
    
    # 6. Matice
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
    
    # Matice incidence
    inc_matrix, nodes_inc, edges_inc = builder.incidence_matrix()
    edge_labels = [edge.label if edge.label else f"e{i}" for i, edge in enumerate(edges_inc)]
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
    print("ANALÝZA DOKONČENA")
    print("=" * 60)
    
    return graph


def main():
    """Hlavní funkce programu."""
    if len(sys.argv) < 2:
        print("Použití: python run.py <soubor_s_grafem> [uzel1] [uzel2] ...")
        print("Příklad: python run.py graph.tg A B C")
        print("         python run.py graph.tg          (bez uzlů = nezobrazovat detaily uzlů)")
        
        # Pokud je spuštěno bez parametrů, zkusíme testovací soubor
        test_file = str(Path(__file__).parent.parent / "data" / "grafy" / "01.tg")
        print(f"\nZkouším testovací soubor: {test_file}")
        try:
            analyze_graph(test_file, nodes_to_display=None)
        except FileNotFoundError:
            print(f"Testovací soubor nenalezen: {test_file}")
            sys.exit(1)
    else:
        filepath = sys.argv[1]
        # Uzly jsou všechny parametry od druhého dál
        nodes_to_display = sys.argv[2:] if len(sys.argv) > 2 else None
        
        try:
            analyze_graph(filepath, nodes_to_display=nodes_to_display)
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

