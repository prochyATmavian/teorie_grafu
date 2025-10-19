"""
Modul pro vizualizaci grafů.
"""


class TextVisualizer:
    """Třída pro textovou vizualizaci grafu."""
    
    def __init__(self, graph):
        """
        Args:
            graph (Graph): Instance grafu
        """
        self.graph = graph
    
    def draw_text(self):
        """
        Vytvoří textovou reprezentaci grafu.
        
        Returns:
            str: Textová vizualizace
        """
        lines = []
        lines.append("=" * 60)
        lines.append("TEXTOVÁ VIZUALIZACE GRAFU")
        lines.append("=" * 60)
        lines.append("")
        
        # Seznam uzlů
        lines.append("UZLY:")
        for node_id in sorted(self.graph.nodes.keys()):
            node = self.graph.nodes[node_id]
            if node.weight is not None:
                lines.append(f"  • {node_id} (váha: {node.weight})")
            else:
                lines.append(f"  • {node_id}")
        lines.append("")
        
        # Seznam hran
        lines.append("HRANY:")
        for edge in self.graph.edges_list:
            parts = []
            
            if edge.directed:
                # Zobrazujeme vždy ve směru toku (source --> target)
                parts.append(f"  {edge.source} --> {edge.target}")
            else:
                parts.append(f"  {edge.node1} --- {edge.node2}")
            
            extras = []
            if edge.weight is not None:
                extras.append(f"váha: {edge.weight}")
            if edge.label:
                extras.append(f"označení: {edge.label}")
            
            if extras:
                parts.append(f" ({', '.join(extras)})")
            
            lines.append(''.join(parts))
        
        lines.append("")
        lines.append("=" * 60)
        
        return '\n'.join(lines)
    
    def draw_adjacency_list(self):
        """
        Vytvoří vizualizaci seznamu sousednosti.
        
        Returns:
            str: Seznam sousednosti
        """
        lines = []
        lines.append("SEZNAM SOUSEDNOSTI:")
        lines.append("")
        
        for node_id in sorted(self.graph.nodes.keys()):
            neighbors = []
            
            # Následníky (orientované)
            successors = self.graph.get_successors(node_id)
            if successors:
                neighbors.append(f"→ {', '.join(sorted(successors))}")
            
            # Předchůdci (orientované)
            predecessors = self.graph.get_predecessors(node_id)
            if predecessors:
                neighbors.append(f"← {', '.join(sorted(predecessors))}")
            
            # Neorientovaní sousedé
            undir_neighbors = [n for n in self.graph.get_neighbors(node_id) 
                              if n not in successors and n not in predecessors]
            if undir_neighbors:
                neighbors.append(f"- {', '.join(sorted(undir_neighbors))}")
            
            if neighbors:
                lines.append(f"  {node_id}: {' | '.join(neighbors)}")
            else:
                lines.append(f"  {node_id}: (izolovaný)")
        
        return '\n'.join(lines)


def try_graphviz_visualization(graph, output_file='graph_output'):
    """
    Pokusí se vytvořit vizualizaci pomocí graphviz (pokud je k dispozici).
    
    Args:
        graph (Graph): Instance grafu
        output_file (str): Název výstupního souboru (bez přípony)
        
    Returns:
        bool: True pokud bylo vykreslení úspěšné
    """
    try:
        import graphviz
        
        # Vytvoříme graf
        if graph.is_directed():
            dot = graphviz.Digraph(comment='Graf')
        else:
            dot = graphviz.Graph(comment='Graf')
        
        # Přidáme uzly
        for node_id, node in graph.nodes.items():
            label = node_id
            if node.weight is not None:
                label = f"{node_id}\n({node.weight})"
            dot.node(node_id, label=label)
        
        # Přidáme hrany
        for edge in graph.edges_list:
            label = ""
            if edge.weight is not None:
                label = str(edge.weight)
            if edge.label:
                label = f"{label} {edge.label}" if label else edge.label
            
            if edge.directed:
                dot.edge(edge.source, edge.target, label=label)
            else:
                dot.edge(edge.node1, edge.node2, label=label)
        
        # Uložíme
        dot.render(output_file, format='png', cleanup=True)
        print(f"Graf vykreslen do souboru: {output_file}.png")
        return True
        
    except ImportError:
        print("Knihovna graphviz není nainstalována.")
        print("Pro instalaci: pip install graphviz")
        return False
    except Exception as e:
        print(f"Graphviz: {e}")
        return False


def try_matplotlib_visualization(graph, output_file='graph_output.png'):
    """
    Pokusí se vytvořit vizualizaci pomocí matplotlib a networkx.
    
    Args:
        graph (Graph): Instance grafu
        output_file (str): Název výstupního souboru
        
    Returns:
        bool: True pokud bylo vykreslení úspěšné
    """
    try:
        import matplotlib.pyplot as plt
        import networkx as nx
        
        # Detekce vícenásobných hran
        has_multiple = graph.has_multiple_edges()
        
        # Vytvoříme NetworkX graf - použijeme Multi* pro grafy s vícenásobnými hranami
        if graph.is_directed():
            G = nx.MultiDiGraph() if has_multiple else nx.DiGraph()
        else:
            G = nx.MultiGraph() if has_multiple else nx.Graph()
        
        # Přidáme uzly
        for node_id in graph.nodes.keys():
            G.add_node(node_id)
        
        # Přidáme hrany
        for edge in graph.edges_list:
            if edge.directed:
                G.add_edge(edge.source, edge.target, weight=edge.weight, label=edge.label)
            else:
                G.add_edge(edge.node1, edge.node2, weight=edge.weight, label=edge.label)
        
        # Vykreslíme
        plt.figure(figsize=(12, 8))
        
        # Pro grafy s více komponentami nebo izolovanými uzly použijeme seed
        try:
            pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
        except:
            # Fallback na jiný layout
            try:
                pos = nx.kamada_kawai_layout(G)
            except:
                pos = nx.circular_layout(G)
        
        # Uzly
        nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                               node_size=1500, alpha=0.9)
        
        # Hrany - šipky pouze pro orientované grafy
        is_directed = graph.is_directed()
        
        # Pro grafy s vícenásobnými hranami používáme connectionstyle
        if has_multiple:
            if is_directed:
                nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, 
                                       arrows=True, arrowsize=20,
                                       connectionstyle='arc3,rad=0.1')
            else:
                nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, 
                                       arrows=False,
                                       connectionstyle='arc3,rad=0.1')
        else:
            if is_directed:
                nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, 
                                       arrows=True, arrowsize=20)
            else:
                nx.draw_networkx_edges(G, pos, width=2, alpha=0.6, 
                                       arrows=False)
        
        # Popisky uzlů
        nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
        
        # Popisky hran (váhy)
        edge_labels = {}
        for edge in graph.edges_list:
            if edge.directed:
                key = (edge.source, edge.target)
            else:
                key = (edge.node1, edge.node2)
            
            label_parts = []
            if edge.weight is not None:
                label_parts.append(str(edge.weight))
            if edge.label:
                label_parts.append(edge.label)
            
            if label_parts:
                edge_labels[key] = ' '.join(label_parts)
        
        if edge_labels:
            nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=10)
        
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_file, dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"Graf vykreslen do souboru: {output_file}")
        return True
        
    except ImportError as e:
        print(f"Chybí požadované knihovny: {e}")
        print("Pro instalaci: pip install matplotlib networkx")
        return False
    except Exception as e:
        print(f"Chyba při vykreslování grafu: {e}")
        print("Zkouším alternativní metodu...")
        return False


def visualize_graph(graph, method='auto', output_file='graph_output'):
    """
    Univerzální funkce pro vizualizaci grafu.
    
    Args:
        graph (Graph): Instance grafu
        method (str): Metoda vizualizace ('auto', 'text', 'matplotlib', 'graphviz')
        output_file (str): Název výstupního souboru
        
    Returns:
        str: Cesta k výstupnímu souboru nebo textová reprezentace
    """
    if method == 'text':
        visualizer = TextVisualizer(graph)
        return visualizer.draw_text()
    
    elif method == 'matplotlib':
        success = try_matplotlib_visualization(graph, output_file + '.png')
        if success:
            return output_file + '.png'
        else:
            # Fallback na textovou vizualizaci
            print("Fallback na textovou vizualizaci...")
            visualizer = TextVisualizer(graph)
            return visualizer.draw_text()
    
    elif method == 'graphviz':
        success = try_graphviz_visualization(graph, output_file)
        if success:
            return output_file + '.png'
        else:
            # Fallback na textovou vizualizaci
            print("Fallback na textovou vizualizaci...")
            visualizer = TextVisualizer(graph)
            return visualizer.draw_text()
    
    else:  # method == 'auto'
        # Zkusíme matplotlib, pak graphviz, nakonec text
        if try_matplotlib_visualization(graph, output_file + '.png'):
            return output_file + '.png'
        elif try_graphviz_visualization(graph, output_file):
            return output_file + '.png'
        else:
            visualizer = TextVisualizer(graph)
            return visualizer.draw_text()

