#!/usr/bin/env python3
"""
Hlavní interaktivní program pro analýzu grafů.

Program načte graf a pak v cyklu nabízí různé operace.
"""

import sys
from pathlib import Path

# Přidání src do sys.path
sys.path.insert(0, str(Path(__file__).parent))

from src.parser import GraphParser
from src.graph import Graph
from src.matrices import MatrixBuilder
from src.analyzer import GraphAnalyzer


class GraphInteractive:
    """Interaktivní rozhraní pro práci s grafem."""
    
    def __init__(self):
        self.graph = None
        self.builder = None
        self.analyzer = None
        self.filepath = None
        
        # Cache pro matice
        self.cached_matrices = {}
    
    def nacti_graf(self):
        """Načtení grafu ze souboru."""
        print("\n" + "=" * 70)
        print("NAČTENÍ GRAFU")
        print("=" * 70)
        
        while True:
            filepath = input("\nZadejte cestu k souboru s grafem (nebo 'q' pro ukončení): ").strip()
            
            if filepath.lower() == 'q':
                return False
            
            if not Path(filepath).exists():
                print(f"CHYBA: Soubor '{filepath}' neexistuje!")
                continue
            
            try:
                parser = GraphParser()
                nodes, edges, is_binary_tree = parser.parse_file(filepath)
                self.graph = Graph(nodes, edges, is_binary_tree)
                self.builder = MatrixBuilder(self.graph)
                self.analyzer = GraphAnalyzer(self.graph)
                self.filepath = filepath
                self.cached_matrices = {}  # Vyčištění cache
                
                print(f"\nGraf úspěšně načten!")
                print(f"Soubor: {filepath}")
                print(f"Uzly: {len(self.graph.nodes)} - {sorted(self.graph.nodes.keys())}")
                print(f"Hrany: {len(self.graph.edges_list)}")
                
                return True
                
            except Exception as e:
                print(f"CHYBA při načítání grafu: {e}")
                continue
    
    def zobraz_menu(self):
        """Zobrazí hlavní menu."""
        print("\n" + "=" * 70)
        print("HLAVNÍ MENU")
        print("=" * 70)
        print("\nANALÝZA:")
        print("  1) Vlastnosti grafu")
        print("  2) Vlastnosti uzlu (nebo všech uzlů)")
        print("  3) Vlastnosti hrany")
        print("\nMATICE:")
        print("  4) Matice sousednosti")
        print("  5) N-tá mocnina matice sousednosti")
        print("  6) Matice incidence")
        print("  7) Matice délek")
        print("  8) Matice předchůdců")
        print("\nOSTATNÍ:")
        print("  9) Načíst jiný graf")
        print("  0) Ukončit program")
        print("=" * 70)
    
    def vlastnosti_grafu(self):
        """Zobrazí vlastnosti grafu."""
        # ANSI barvy
        GREEN = '\033[92m'
        RED = '\033[91m'
        RESET = '\033[0m'
        
        print("\n" + "=" * 70)
        print("VLASTNOSTI GRAFU")
        print("=" * 70)
        
        props = self.analyzer.analyze_all()
        
        print(f"\nGraf: {self.filepath}")
        print(f"Uzlů: {len(self.graph.nodes)}")
        print(f"Hran: {len(self.graph.edges_list)}")
        print()
        
        # Překlad vlastností do češtiny
        nazvy_vlastnosti = {
            'a_weighted': 'a) Ohodnocený',
            'b_directed': 'b) Orientovaný',
            'c_connected': 'c) Souvislý',
            'd_simple': 'd) Prostý',
            'e_loop_free': 'e) Jednoduchý (bez smyček)',
            'f_planar': 'f) Rovinný',
            'g_finite': 'g) Konečný',
            'h_complete': 'h) Úplný',
            'i_regular': 'i) Regulární',
            'j_bipartite': 'j) Bipartitní'
        }
        
        print("Vlastnosti:")
        for key, value in props.items():
            cesky_nazev = nazvy_vlastnosti.get(key, key)
            
            if isinstance(value, dict):
                # Složitější vlastnosti (souvislost, regularita, bipartitnost)
                if key == 'c_connected':
                    is_connected = value.get('connected', False)
                    conn_type = value.get('type', '')
                    color = GREEN if is_connected else RED
                    status = "ano" if is_connected else "ne"
                    if is_connected and conn_type:
                        type_cz = "silně" if conn_type == "strongly" else "slabě"
                        print(f"  {color}{cesky_nazev}: {status} ({type_cz}){RESET}")
                    else:
                        print(f"  {color}{cesky_nazev}: {status}{RESET}")
                
                elif key == 'f_planar':
                    is_planar = value.get('planar', False)
                    color = GREEN if is_planar else RED
                    status = "ano" if is_planar else "ne"
                    print(f"  {color}{cesky_nazev}: {status}{RESET}")
                    if 'note' in value:
                        print(f"    Poznámka: {value['note']}")
                
                elif key == 'i_regular':
                    is_regular = value.get('regular', False)
                    degree = value.get('degree', None)
                    color = GREEN if is_regular else RED
                    status = "ano" if is_regular else "ne"
                    if is_regular and degree is not None:
                        print(f"  {color}{cesky_nazev}: {status} (stupeň {degree}){RESET}")
                    else:
                        print(f"  {color}{cesky_nazev}: {status}{RESET}")
                
                elif key == 'j_bipartite':
                    is_bipartite = value.get('bipartite', False)
                    color = GREEN if is_bipartite else RED
                    status = "ano" if is_bipartite else "ne"
                    print(f"  {color}{cesky_nazev}: {status}{RESET}")
                    if is_bipartite and 'partition' in value and value['partition']:
                        part = value['partition']
                        print(f"    Partice: {part[0]} | {part[1]}")
            else:
                # Jednoduché boolean vlastnosti
                color = GREEN if value else RED
                status = "ano" if value else "ne"
                print(f"  {color}{cesky_nazev}: {status}{RESET}")
    
    def vlastnosti_uzlu(self):
        """Zobrazí vlastnosti uzlu nebo všech uzlů."""
        print("\n" + "=" * 70)
        print("VLASTNOSTI UZLU")
        print("=" * 70)
        
        nodes = sorted(self.graph.nodes.keys())
        print(f"\nDostupné uzly: {nodes}")
        
        node_input = input("\nZadejte název uzlu (nebo 'vse' pro všechny uzly): ").strip()
        
        if node_input.lower() == 'vse':
            nodes_to_show = nodes
        else:
            if node_input not in self.graph.nodes:
                print(f"CHYBA: Uzel '{node_input}' neexistuje!")
                return
            nodes_to_show = [node_input]
        
        # Získáme matici délek pro vzdálenosti
        dist_matrix = self._get_cached_matrix('distance')
        
        for node in nodes_to_show:
            print(f"\n{'=' * 70}")
            print(f"UZEL: {node}")
            print('=' * 70)
            
            # Základní informace
            node_obj = self.graph.nodes[node]
            print(f"Ohodnocení: {node_obj.weight if node_obj.weight is not None else 'bez ohodnocení'}")
            
            # Stupně
            print(f"\nStupně:")
            print(f"  Stupeň d({node}): {self.graph.get_degree(node)}")
            if self.graph.is_directed():
                print(f"  Vstupní d-({node}): {self.graph.get_in_degree(node)}")
                print(f"  Výstupní d+({node}): {self.graph.get_out_degree(node)}")
            
            # Předchůdci
            predecessors = self.graph.get_predecessors(node)
            all_neighbors = self.graph.get_all_neighbors(node)
            successors = self.graph.get_successors(node)
            
            # Získáme hrany pro každé okolí
            in_edges = self.graph.get_incoming_edges(node)
            out_edges = self.graph.get_outgoing_edges(node)
            incident_edges_all = self.graph.get_incident_edges(node)
            
            print(f"\nPředchůdci U-({node}) ({len(predecessors)}):")
            if predecessors:
                for pred in sorted(predecessors):
                    if self.graph.is_weighted():
                        distance = dist_matrix[pred][node]
                        if distance == float('inf'):
                            print(f"  - {pred} (vzdálenost: ∞)")
                        else:
                            print(f"  - {pred} (vzdálenost: {distance})")
                    else:
                        print(f"  - {pred}")
                print(f"  Hrany vstupního okolí:")
                for edge in in_edges:
                    edge_str = f"{edge.node1} → {edge.node2}" if edge.directed else f"{edge.node1} - {edge.node2}"
                    if edge.weight is not None:
                        edge_str += f" (váha: {edge.weight})"
                    print(f"    {edge_str}")
            else:
                print("  (žádní)")
            
            # Následníci
            print(f"\nNásledníci U+({node}) ({len(successors)}):")
            if successors:
                for succ in sorted(successors):
                    if self.graph.is_weighted():
                        distance = dist_matrix[node][succ]
                        if distance == float('inf'):
                            print(f"  - {succ} (vzdálenost: ∞)")
                        else:
                            print(f"  - {succ} (vzdálenost: {distance})")
                    else:
                        print(f"  - {succ}")
                print(f"  Hrany výstupního okolí:")
                for edge in out_edges:
                    edge_str = f"{edge.node1} → {edge.node2}" if edge.directed else f"{edge.node1} - {edge.node2}"
                    if edge.weight is not None:
                        edge_str += f" (váha: {edge.weight})"
                    print(f"    {edge_str}")
            else:
                print("  (žádní)")
            
            # Všichni sousedé (pro přehled)
            print(f"\nVšichni sousedé U({node}) ({len(all_neighbors)}):")
            if all_neighbors:
                for neighbor in sorted(all_neighbors):
                    if self.graph.is_weighted():
                        # Zjistíme vzdálenost (může být z obou směrů)
                        dist1 = dist_matrix[node][neighbor]
                        dist2 = dist_matrix[neighbor][node]
                        distance = min(dist1, dist2)
                        if distance == float('inf'):
                            print(f"  - {neighbor} (vzdálenost: ∞)")
                        else:
                            print(f"  - {neighbor} (vzdálenost: {distance})")
                    else:
                        print(f"  - {neighbor}")
                print(f"  Hrany okolí:")
                for edge in incident_edges_all:
                    edge_str = f"{edge.node1} → {edge.node2}" if edge.directed else f"{edge.node1} - {edge.node2}"
                    if edge.weight is not None:
                        edge_str += f" (váha: {edge.weight})"
                    print(f"    {edge_str}")
            else:
                print("  (žádní)")
            
            # Incidentní hrany
            incident_edges = self.graph.get_incident_edges(node)
            print(f"\nIncidentní hrany ({len(incident_edges)}):")
            for edge in incident_edges:
                edge_str = f"{edge.node1} → {edge.node2}" if edge.directed else f"{edge.node1} - {edge.node2}"
                if edge.weight is not None:
                    edge_str += f" (váha: {edge.weight})"
                if edge.label:
                    edge_str += f" [{edge.label}]"
                print(f"  - {edge_str}")
    
    def vlastnosti_hrany(self):
        """Zobrazí vlastnosti hrany."""
        print("\n" + "=" * 70)
        print("VLASTNOSTI HRANY")
        print("=" * 70)
        
        print(f"\nCelkem hran: {len(self.graph.edges_list)}")
        print("\nDostupné hrany:")
        for i, edge in enumerate(self.graph.edges_list):
            label = edge.label if edge.label else f"e{i}"
            edge_type = "→" if edge.directed else "-"
            print(f"  {label}: {edge.node1} {edge_type} {edge.node2}")
        
        edge_input = input("\nZadejte označení hrany (např. h1): ").strip()
        
        # Najdeme hranu podle labelu
        found_edge = None
        for edge in self.graph.edges_list:
            if edge.label == edge_input:
                found_edge = edge
                break
        
        if not found_edge:
            print(f"CHYBA: Hrana '{edge_input}' nenalezena!")
            return
        
        print(f"\n{'=' * 70}")
        print(f"HRANA: {edge_input}")
        print('=' * 70)
        
        print(f"\nKoncové uzly: {found_edge.node1}, {found_edge.node2}")
        print(f"Typ: {'orientovaná' if found_edge.directed else 'neorientovaná'}")
        
        if found_edge.directed:
            print(f"Směr: {found_edge.source} → {found_edge.target}")
        
        print(f"Váha: {found_edge.weight if found_edge.weight is not None else 'bez ohodnocení'}")
        print(f"Označení: {found_edge.label if found_edge.label else 'bez označení'}")
        
        # Je to smyčka?
        if found_edge.node1 == found_edge.node2:
            print("POZOR: Jedná se o smyčku!")
    
    def _get_cached_matrix(self, matrix_type):
        """Získá matici z cache nebo ji vytvoří."""
        if matrix_type not in self.cached_matrices:
            if matrix_type == 'adjacency':
                self.cached_matrices[matrix_type] = self.builder.adjacency_matrix()
            elif matrix_type == 'incidence':
                self.cached_matrices[matrix_type] = self.builder.incidence_matrix()
            elif matrix_type == 'distance':
                self.cached_matrices[matrix_type] = self.builder.distance_matrix()
            elif matrix_type == 'predecessor':
                self.cached_matrices[matrix_type] = self.builder.predecessor_matrix()
        
        return self.cached_matrices[matrix_type]
    
    def zobraz_matici(self, matrix, title):
        """Zobrazí matici v čitelném formátu."""
        print(f"\n{title}")
        print("=" * 70)
        
        row_labels = matrix.row_labels()
        col_labels = matrix.col_labels()
        raw_data = matrix.raw()
        
        print(f"Rozměry: {len(raw_data)} řádků × {len(raw_data[0]) if raw_data else 0} sloupců")
        print(f"Řádky: {row_labels}")
        print(f"Sloupce: {col_labels}")
        print()
        
        # Hlavička
        header = "    " + " ".join(f"{label:>4}" for label in col_labels)
        print(header)
        
        # Řádky
        for i, row in enumerate(raw_data):
            label = f"{row_labels[i]:>3}:"
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
    
    def dotaz_na_hodnotu_matice(self, matrix, matrix_name):
        """Interaktivní dotazování na hodnoty v matici."""
        while True:
            print(f"\n{'=' * 70}")
            print(f"DOTAZ NA HODNOTU - {matrix_name}")
            print('=' * 70)
            
            row_labels = matrix.row_labels()
            col_labels = matrix.col_labels()
            
            print(f"\nDostupné řádky: {row_labels}")
            print(f"Dostupné sloupce: {col_labels}")
            
            row_input = input("\nZadejte název řádku (nebo 'zpet' pro návrat): ").strip()
            if row_input.lower() == 'zpet':
                break
            
            if row_input not in row_labels:
                print(f"CHYBA: Řádek '{row_input}' neexistuje!")
                continue
            
            col_input = input("Zadejte název sloupce: ").strip()
            if col_input not in col_labels:
                print(f"CHYBA: Sloupec '{col_input}' neexistuje!")
                continue
            
            # Získání hodnoty pomocí názvů
            value = matrix[row_input][col_input]
            
            # Formátování hodnoty
            if value == float('inf'):
                value_str = "∞"
            elif isinstance(value, float):
                value_str = f"{value:.1f}"
            elif value is None:
                value_str = "-"
            else:
                value_str = str(value)
            
            print(f"\n{matrix_name}[{row_input}][{col_input}] = {value_str}")
    
    def matice_sousednosti(self):
        """Zobrazí matici sousednosti."""
        matrix = self._get_cached_matrix('adjacency')
        self.zobraz_matici(matrix, "MATICE SOUSEDNOSTI")
        
        dotaz = input("\nChcete zjistit konkrétní hodnotu? (a/n): ").strip().lower()
        if dotaz in ['a', 'ano', 'y', 'yes']:
            self.dotaz_na_hodnotu_matice(matrix, "Matice sousednosti")
    
    def mocnina_matice(self):
        """Zobrazí n-tou mocninu matice sousednosti."""
        print("\n" + "=" * 70)
        print("MOCNINA MATICE SOUSEDNOSTI")
        print("=" * 70)
        
        try:
            n = int(input("\nZadejte mocninu (např. 2, 3, 4): ").strip())
            if n < 1:
                print("CHYBA: Mocnina musí být alespoň 1!")
                return
            
            if n == 1:
                # A^1 = A
                matrix = self._get_cached_matrix('adjacency')
            else:
                # Vypočítáme mocninu
                adj_matrix = self._get_cached_matrix('adjacency')
                power_matrix_data = self.builder.matrix_power(adj_matrix.raw(), n)
                
                # Vytvoříme NamedMatrix
                from src.matrices import NamedMatrix
                matrix = NamedMatrix(power_matrix_data, adj_matrix.row_labels(), adj_matrix.col_labels())
            
            self.zobraz_matici(matrix, f"MATICE SOUSEDNOSTI^{n}")
            print(f"\nInterpretace: A^{n}[i][j] = počet cest délky {n} z uzlu i do uzlu j")
            
            dotaz = input("\nChcete zjistit konkrétní hodnotu? (a/n): ").strip().lower()
            if dotaz in ['a', 'ano', 'y', 'yes']:
                self.dotaz_na_hodnotu_matice(matrix, f"Matice sousednosti^{n}")
                
        except ValueError:
            print("CHYBA: Neplatné číslo!")
    
    def matice_incidence(self):
        """Zobrazí matici incidence."""
        matrix = self._get_cached_matrix('incidence')
        self.zobraz_matici(matrix, "MATICE INCIDENCE")
        
        print("\nInterpretace:")
        print("  Pro neorientovaný graf:")
        print("    1 = uzel je incidentní s hranou")
        print("    2 = hrana je smyčka na uzlu")
        print("  Pro orientovaný graf:")
        print("    1 = hrana vychází z uzlu")
        print("   -1 = hrana vstupuje do uzlu")
        print("    2 = hrana je smyčka na uzlu")
        
        dotaz = input("\nChcete zjistit konkrétní hodnotu? (a/n): ").strip().lower()
        if dotaz in ['a', 'ano', 'y', 'yes']:
            self.dotaz_na_hodnotu_matice(matrix, "Matice incidence")
    
    def matice_delek(self):
        """Zobrazí matici délek."""
        matrix = self._get_cached_matrix('distance')
        self.zobraz_matici(matrix, "MATICE DÉLEK (Floyd-Warshall)")
        
        print("\nInterpretace: D[i][j] = nejkratší vzdálenost z uzlu i do uzlu j")
        print("              ∞ = uzel není dosažitelný")
        
        dotaz = input("\nChcete zjistit konkrétní hodnotu? (a/n): ").strip().lower()
        if dotaz in ['a', 'ano', 'y', 'yes']:
            self.dotaz_na_hodnotu_matice(matrix, "Matice délek")
    
    def matice_predchudcu(self):
        """Zobrazí matici předchůdců."""
        matrix = self._get_cached_matrix('predecessor')
        self.zobraz_matici(matrix, "MATICE PŘEDCHŮDCŮ")
        
        print("\nInterpretace: P[i][j] = předchůdce uzlu j na nejkratší cestě z i do j")
        
        dotaz = input("\nChcete zjistit konkrétní hodnotu? (a/n): ").strip().lower()
        if dotaz in ['a', 'ano', 'y', 'yes']:
            self.dotaz_na_hodnotu_matice(matrix, "Matice předchůdců")
    
    def run(self):
        """Hlavní smyčka programu."""
        print("=" * 70)
        print("INTERAKTIVNÍ ANALYZÁTOR GRAFŮ")
        print("=" * 70)
        
        # Načtení grafu na začátku
        if not self.nacti_graf():
            print("\nUkončuji program.")
            return
        
        # Hlavní smyčka
        while True:
            self.zobraz_menu()
            
            volba = input("\nVaše volba: ").strip()
            
            if volba == '1':
                self.vlastnosti_grafu()
            elif volba == '2':
                self.vlastnosti_uzlu()
            elif volba == '3':
                self.vlastnosti_hrany()
            elif volba == '4':
                self.matice_sousednosti()
            elif volba == '5':
                self.mocnina_matice()
            elif volba == '6':
                self.matice_incidence()
            elif volba == '7':
                self.matice_delek()
            elif volba == '8':
                self.matice_predchudcu()
            elif volba == '9':
                if not self.nacti_graf():
                    print("\nUkončuji program.")
                    break
            elif volba == '0':
                print("\nUkončuji program. Nashledanou!")
                break
            else:
                print("Neplatná volba! Zkuste to znovu.")
            
            input("\nStiskněte Enter pro pokračování...")


def main():
    """Spuštění programu."""
    try:
        app = GraphInteractive()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram přerušen uživatelem.")
        sys.exit(0)
    except Exception as e:
        print(f"\nChyba: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

