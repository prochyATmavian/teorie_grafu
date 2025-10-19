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


def print_matrix(matrix, row_labels=None, col_labels=None, title="Matice", show_dimensions=True):
    """Vypíše matici v čitelném formátu."""
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    
    print(f"\n{title}:")
    if show_dimensions:
        print(f"Rozměry: {rows} řádků × {cols} sloupců")
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


def get_matrix_element(matrix, row, col, row_labels=None, col_labels=None):
    """
    Vrátí prvek matice na pozici [řádek][sloupec].
    
    Args:
        matrix: Matice
        row (int): Index řádku (od 0)
        col (int): Index sloupce (od 0)
        row_labels: Seznam popisků řádků (volitelné)
        col_labels: Seznam popisků sloupců (volitelné)
        
    Returns:
        Hodnota prvku nebo None pokud index není platný
    """
    if row < 0 or row >= len(matrix):
        return None
    if col < 0 or col >= len(matrix[row]):
        return None
    
    value = matrix[row][col]
    
    # Formátování hodnoty
    if value == float('inf'):
        value_str = "∞"
    elif isinstance(value, float):
        value_str = f"{value:.1f}"
    elif value is None:
        value_str = "-"
    else:
        value_str = str(value)
    
    row_label = row_labels[row] if row_labels and row < len(row_labels) else str(row)
    col_label = col_labels[col] if col_labels and col < len(col_labels) else str(col)
    
    return {
        'value': value,
        'value_str': value_str,
        'row_index': row,
        'col_index': col,
        'row_label': row_label,
        'col_label': col_label
    }


def print_matrix_element(matrix, row, col, row_labels=None, col_labels=None, matrix_name="Matice"):
    """Vypíše konkrétní prvek matice."""
    result = get_matrix_element(matrix, row, col, row_labels, col_labels)
    
    if result is None:
        print(f"❌ Neplatný index [{row}][{col}] - mimo rozsah matice!")
        return
    
    print(f"\n{matrix_name}[{result['row_label']}][{result['col_label']}] = {result['value_str']}")
    print(f"   (index: [{result['row_index']}][{result['col_index']}])")


def analyze_matrices(filepath, matrix_index=None):
    """
    Načte graf a vytvoří jeho matice a seznamy.
    
    Args:
        filepath (str): Cesta k souboru s grafem
        matrix_index (tuple): (řádek, sloupec) pro zobrazení konkrétního prvku, None = zobrazit celé matice
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
    if matrix_index:
        row, col = matrix_index
        print(f"PŘÍSTUP K PRVKŮM MATIC - Index [{row}][{col}]")
    else:
        print("MATICE A SEZNAMY")
    print("=" * 60)
    
    builder = MatrixBuilder(graph)
    
    # Matice sousednosti
    adj_matrix, nodes_list = builder.adjacency_matrix()
    if matrix_index:
        row, col = matrix_index
        print_matrix_element(adj_matrix, row, col, nodes_list, nodes_list, "a) Matice sousednosti")
    else:
        print_matrix(adj_matrix, nodes_list, nodes_list, "a) Matice sousednosti")
    
    # Znaménková matice
    sign_matrix, _ = builder.signed_matrix()
    if matrix_index:
        row, col = matrix_index
        print_matrix_element(sign_matrix, row, col, nodes_list, nodes_list, "b) Znaménková matice")
    else:
        print_matrix(sign_matrix, nodes_list, nodes_list, "b) Znaménková matice")
    
    # Mocniny matice sousednosti
    if len(nodes_list) <= 10:  # Pouze pro menší grafy
        powers = builder.adjacency_matrix_powers(3)
        for power, (matrix, _) in powers.items():
            if matrix_index:
                row, col = matrix_index
                print_matrix_element(matrix, row, col, nodes_list, nodes_list, f"c) Matice sousednosti^{power}")
            else:
                print_matrix(matrix, nodes_list, nodes_list, f"c) Matice sousednosti^{power}")
    else:
        if not matrix_index:
            print(f"\nc) Matice sousednosti^n: Vynecháno (graf má {len(nodes_list)} uzlů > 10)")
    
    # Matice incidence
    inc_matrix, nodes_inc, edges_inc = builder.incidence_matrix()
    edge_labels = [edge.label if edge.label else f"e{i}" for i, edge in enumerate(edges_inc)]
    if matrix_index:
        row, col = matrix_index
        print_matrix_element(inc_matrix, row, col, nodes_inc, edge_labels, "d) Matice incidence")
    else:
        print_matrix(inc_matrix, nodes_inc, edge_labels, "d) Matice incidence")
    
    # Matice délek
    dist_matrix, _ = builder.distance_matrix()
    if matrix_index:
        row, col = matrix_index
        print_matrix_element(dist_matrix, row, col, nodes_list, nodes_list, "e) Matice délek (Floyd-Warshall)")
    else:
        print_matrix(dist_matrix, nodes_list, nodes_list, "e) Matice délek (Floyd-Warshall)")
    
    if not matrix_index:
        # Seznam sousedů
        print("\nh) Seznam sousedů:")
        neighbors = builder.neighbor_list()
        for node, neighs in neighbors.items():
            print(f"   {node}: {neighs}")
    
    print("\n" + "=" * 60)
    if matrix_index:
        print("PŘÍSTUP K PRVKŮM DOKONČEN")
    else:
        print("ANALÝZA MATIC DOKONČENA")
    print("=" * 60)
    
    return graph


def interactive_matrix_selection(filepath):
    """
    Interaktivní režim pro výběr matice a indexu.
    """
    print("\n" + "=" * 60)
    print("INTERAKTIVNÍ VÝBĚR MATICE")
    print("=" * 60)
    
    # Nabídka matic
    print("\nVyberte matici k sestavení:")
    print("  a) Matice sousednosti")
    print("  b) Znaménková matice")
    print("  c) Mocniny matice sousednosti (A^2, A^3)")
    print("  d) Matice incidence")
    print("  e) Matice délek (Floyd-Warshall)")
    print("  h) Seznam sousedů")
    print("  *) Všechny matice")
    print("")
    
    choice = input("Vaše volba (a/b/c/d/e/h/*): ").strip().lower()
    
    if choice not in ['a', 'b', 'c', 'd', 'e', 'h', '*']:
        print(f"❌ Neplatná volba: '{choice}'")
        sys.exit(1)
    
    # Načtení grafu
    print(f"\nNačítám graf ze souboru: {filepath}")
    parser = GraphParser()
    nodes, edges, is_binary_tree = parser.parse_file(filepath)
    graph = Graph(nodes, edges, is_binary_tree)
    builder = MatrixBuilder(graph)
    
    print(f"Načteno: {len(nodes)} uzlů, {len(edges)} hran")
    
    # Ptáme se, jestli chce konkrétní index
    print("\n" + "-" * 60)
    show_index = input("Chcete zobrazit konkrétní index matice? (a/n): ").strip().lower()
    
    matrix_index = None
    if show_index in ['a', 'ano', 'y', 'yes']:
        try:
            row = int(input("Zadejte řádek (od 0): ").strip())
            col = int(input("Zadejte sloupec (od 0): ").strip())
            matrix_index = (row, col)
            print(f"\n🔍 Zobrazuji index [{row}][{col}]")
        except ValueError:
            print("❌ Neplatný vstup! Použiji celou matici.")
            matrix_index = None
    
    print("\n" + "=" * 60)
    print("VÝSLEDKY")
    print("=" * 60)
    
    nodes_list = sorted(graph.nodes.keys())
    
    # Sestavení a zobrazení vybrané matice
    if choice == 'a' or choice == '*':
        adj_matrix, nodes_list = builder.adjacency_matrix()
        if matrix_index:
            row, col = matrix_index
            print_matrix_element(adj_matrix, row, col, nodes_list, nodes_list, "a) Matice sousednosti")
        else:
            print_matrix(adj_matrix, nodes_list, nodes_list, "a) Matice sousednosti")
    
    if choice == 'b' or choice == '*':
        sign_matrix, _ = builder.signed_matrix()
        if matrix_index:
            row, col = matrix_index
            print_matrix_element(sign_matrix, row, col, nodes_list, nodes_list, "b) Znaménková matice")
        else:
            print_matrix(sign_matrix, nodes_list, nodes_list, "b) Znaménková matice")
    
    if choice == 'c' or choice == '*':
        if len(nodes_list) <= 10:
            powers = builder.adjacency_matrix_powers(3)
            for power, (matrix, _) in powers.items():
                if matrix_index:
                    row, col = matrix_index
                    print_matrix_element(matrix, row, col, nodes_list, nodes_list, f"c) Matice sousednosti^{power}")
                else:
                    print_matrix(matrix, nodes_list, nodes_list, f"c) Matice sousednosti^{power}")
        else:
            print(f"\nc) Matice sousednosti^n: Vynecháno (graf má {len(nodes_list)} uzlů > 10)")
    
    if choice == 'd' or choice == '*':
        inc_matrix, nodes_inc, edges_inc = builder.incidence_matrix()
        edge_labels = [edge.label if edge.label else f"e{i}" for i, edge in enumerate(edges_inc)]
        if matrix_index:
            row, col = matrix_index
            print_matrix_element(inc_matrix, row, col, nodes_inc, edge_labels, "d) Matice incidence")
        else:
            print_matrix(inc_matrix, nodes_inc, edge_labels, "d) Matice incidence")
    
    if choice == 'e' or choice == '*':
        dist_matrix, _ = builder.distance_matrix()
        if matrix_index:
            row, col = matrix_index
            print_matrix_element(dist_matrix, row, col, nodes_list, nodes_list, "e) Matice délek (Floyd-Warshall)")
        else:
            print_matrix(dist_matrix, nodes_list, nodes_list, "e) Matice délek (Floyd-Warshall)")
    
    if choice == 'h' or choice == '*':
        if not matrix_index:
            print("\nh) Seznam sousedů:")
            neighbors = builder.neighbor_list()
            for node, neighs in neighbors.items():
                print(f"   {node}: {neighs}")
    
    print("\n" + "=" * 60)
    print("HOTOVO")
    print("=" * 60)


def main():
    """Hlavní funkce programu."""
    if len(sys.argv) < 2:
        print("Použití: python analyze_matrices.py <soubor_s_grafem> [režim]")
        print("")
        print("Režimy:")
        print("  (bez parametru)  - Interaktivní výběr matice")
        print("  --all            - Zobrazit všechny matice")
        print("  --all <r> <c>    - Zobrazit prvky všech matic na indexu [r][c]")
        print("")
        print("Příklad:")
        print("  python analyze_matrices.py graph.tg")
        print("  python analyze_matrices.py graph.tg --all")
        print("  python analyze_matrices.py graph.tg --all 0 1")
        print("")
        print("Indexování od 0!")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Kontrola existence souboru
    if not Path(filepath).exists():
        print(f"❌ Soubor nenalezen: {filepath}")
        sys.exit(1)
    
    try:
        # Režim --all (původní funkcionalita)
        if len(sys.argv) >= 3 and sys.argv[2] == '--all':
            matrix_index = None
            
            # Kontrola indexů
            if len(sys.argv) >= 5:
                try:
                    row = int(sys.argv[3])
                    col = int(sys.argv[4])
                    matrix_index = (row, col)
                    print(f"\n🔍 Režim přístupu k prvkům - Index [{row}][{col}]")
                except ValueError:
                    print(f"❌ Chyba: Řádek a sloupec musí být celá čísla!")
                    print(f"   Zadáno: řádek='{sys.argv[3]}', sloupec='{sys.argv[4]}'")
                    sys.exit(1)
            
            analyze_matrices(filepath, matrix_index)
        
        # Interaktivní režim (default)
        else:
            interactive_matrix_selection(filepath)
            
    except FileNotFoundError:
        print(f"❌ Soubor nenalezen: {filepath}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n⚠️  Přerušeno uživatelem")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Chyba při zpracování: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

