#!/usr/bin/env python3
"""
Jednoduchá funkce pro načtení a vykreslení grafu.
"""

from parser import GraphParser
from graph import Graph
from visualizer import visualize_graph, TextVisualizer


def vykresli_graf(soubor_cesta, metoda='auto', vystup='graph_viz'):
    """
    Načte graf ze souboru a vykreslí ho.
    
    Args:
        soubor_cesta (str): Cesta k souboru s grafem (.tg)
        metoda (str): Metoda vizualizace:
            - 'auto': Zkusí matplotlib, pak graphviz, nakonec text
            - 'text': Pouze textová vizualizace
            - 'matplotlib': Grafická vizualizace pomocí matplotlib
            - 'graphviz': Grafická vizualizace pomocí graphviz
        vystup (str): Název výstupního souboru (bez přípony)
    
    Returns:
        Graph: Instance načteného grafu
    """
    print(f"📊 Načítám graf ze souboru: {soubor_cesta}")
    print("=" * 60)
    
    # Načtení grafu
    parser = GraphParser()
    nodes, edges, is_binary_tree = parser.parse_file(soubor_cesta)
    
    print(f"✓ Načteno: {len(nodes)} uzlů, {len(edges)} hran")
    if is_binary_tree:
        print("✓ Typ: Binární strom")
    else:
        print("✓ Typ: Obecný graf")
    
    # Vytvoření grafu
    graph = Graph(nodes, edges, is_binary_tree)
    
    # Vizualizace
    print("\n" + "=" * 60)
    print("🎨 VIZUALIZACE")
    print("=" * 60)
    
    if metoda == 'text':
        # Pouze textová vizualizace
        visualizer = TextVisualizer(graph)
        print(visualizer.draw_text())
        print("\n" + visualizer.draw_adjacency_list())
    else:
        # Pokus o grafickou vizualizaci
        result = visualize_graph(graph, method=metoda, output_file=vystup)
        
        if result.endswith('.png'):
            print(f"\n✓ Graf vykreslen do souboru: {result}")
        else:
            # Textová vizualizace jako fallback
            print("\n" + result)
    
    print("\n" + "=" * 60)
    print("✓ Hotovo!")
    print("=" * 60)
    
    return graph


if __name__ == "__main__":
    # Příklad použití
    
    # 1. Načtení a vykreslení grafu 01.tg
    graf = vykresli_graf('/Users/prochy/Downloads/grafy/01.tg')
    
    # 2. Můžete pracovat s grafem dál
    print("\n📋 Základní informace:")
    print(f"  Počet uzlů: {graf.get_node_count()}")
    print(f"  Počet hran: {graf.get_edge_count()}")
    print(f"  Orientovaný: {graf.is_directed()}")
    print(f"  Ohodnocený: {graf.is_weighted()}")
    
    # 3. Příklad: Informace o uzlu E
    if graf.has_node('E'):
        print("\n🔍 Informace o uzlu E:")
        print(f"  Následníci U+(E): {graf.get_successors('E')}")
        print(f"  Předchůdci U-(E): {graf.get_predecessors('E')}")
        print(f"  Stupeň d(E): {graf.get_degree('E')}")

