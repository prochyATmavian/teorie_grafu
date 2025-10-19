"""
Modul pro analýzu vlastností grafů.

Implementuje detekci různých vlastností grafu podle zadání:
a) ohodnocený, b) orientovaný, c) souvislý, d) prostý, e) jednoduchý,
f) rovinný, g) konečný, h) úplný, i) regulární, j) bipartitní
"""

from collections import deque


class GraphAnalyzer:
    """Třída pro analýzu vlastností grafů."""
    
    def __init__(self, graph):
        """
        Args:
            graph (Graph): Instance grafu k analýze
        """
        self.graph = graph
    
    def is_weighted(self):
        """
        a) Ohodnocený graf - pokud má hrany váhy.
        
        Returns:
            bool: True pokud je graf ohodnocený
        """
        return self.graph.is_weighted()
    
    def is_directed(self):
        """
        b) Orientovaný graf - pokud mají hrany směr.
        
        Returns:
            bool: True pokud je graf orientovaný
        """
        return self.graph.is_directed()
    
    def is_connected(self):
        """
        c) Souvislý graf.
        Pro neorientované grafy: z každého uzlu existuje cesta do každého ostatního.
        Pro orientované grafy: rozlišujeme silně a slabě souvislé.
        
        Returns:
            dict: {'connected': bool, 'type': 'strongly'/'weakly'/None}
        """
        if self.graph.get_node_count() == 0:
            return {'connected': True, 'type': None}
        
        if not self.is_directed():
            # Neorientovaný graf - stačí BFS z libovolného uzlu
            start = next(iter(self.graph.nodes))
            reachable = self.graph.bfs(start)
            connected = len(reachable) == self.graph.get_node_count()
            return {'connected': connected, 'type': None}
        else:
            # Orientovaný graf - kontrolujeme silnou souvislost
            strongly = self._is_strongly_connected()
            if strongly:
                return {'connected': True, 'type': 'strongly'}
            
            # Pokud není silně souvislý, kontrolujeme slabou souvislost
            weakly = self._is_weakly_connected()
            if weakly:
                return {'connected': True, 'type': 'weakly'}
            
            return {'connected': False, 'type': None}
    
    def _is_strongly_connected(self):
        """
        Kontroluje silnou souvislost orientovaného grafu.
        Ze všech uzlů lze dojít do všech ostatních uzlů.
        
        Returns:
            bool: True pokud je silně souvislý
        """
        if self.graph.get_node_count() == 0:
            return True
        
        # Z každého uzlu musíme dosáhnout všech ostatních
        for node in self.graph.nodes:
            reachable = self.graph.bfs(node)
            if len(reachable) != self.graph.get_node_count():
                return False
        return True
    
    def _is_weakly_connected(self):
        """
        Kontroluje slabou souvislost orientovaného grafu.
        Z nějakého uzlu lze dojít do všech uzlů (ignorujeme směry hran).
        
        Returns:
            bool: True pokud je slabě souvislý
        """
        if self.graph.get_node_count() == 0:
            return True
        
        start = next(iter(self.graph.nodes))
        reachable = self.graph.bfs_undirected(start)
        return len(reachable) == self.graph.get_node_count()
    
    def is_simple(self):
        """
        d) Prostý graf - neobsahuje vícenásobné hrany.
        
        Vícenásobné hrany = hrany orientované stejným směrem z A do B 
        (u orientovaných grafů) nebo hrany mezi A a B (u neorientovaných grafů).
        
        Returns:
            bool: True pokud je graf prostý (bez vícenásobných hran)
        """
        return not self.graph.has_multiple_edges()
    
    def is_loop_free(self):
        """
        e) Jednoduchý graf - neobsahuje smyčky a je prostý.
        
        Jednoduchý graf = prostý graf + bez smyček.
        Smyčka = hrana z uzlu do sebe sama.
        
        Returns:
            bool: True pokud graf neobsahuje smyčky a vícenásobné hrany
        """
        return not self.graph.has_self_loop() and not self.graph.has_multiple_edges()
    
    def is_planar(self):
        """
        f) Rovinný graf - lze nakreslit na rovinu bez křížení hran.
        
        Používáme Kuratowského větu:
        Graf je rovinný právě tehdy, když neobsahuje podgraf homeomorfní s K5 nebo K3,3.
        
        Pro malé grafy také platí: pokud |E| <= 3|V| - 6 (pro |V| >= 3)
        
        Returns:
            dict: {'planar': bool, 'method': str, 'note': str}
        """
        n = self.graph.get_node_count()
        m = self.graph.get_edge_count()
        
        # Grafy s méně než 5 uzly jsou vždy rovinné
        if n < 5:
            return {
                'planar': True,
                'method': 'vertex_count',
                'note': 'Grafy s méně než 5 uzly jsou vždy rovinné'
            }
        
        # Eulerova formule pro rovinné grafy: m <= 3n - 6
        if m > 3 * n - 6:
            return {
                'planar': False,
                'method': 'euler_formula',
                'note': f'Příliš mnoho hran: {m} > 3*{n}-6 = {3*n-6}'
            }
        
        # Pro bipartitní grafy: m <= 2n - 4
        if self.is_bipartite()['bipartite'] and m > 2 * n - 4:
            return {
                'planar': False,
                'method': 'bipartite_formula',
                'note': f'Příliš mnoho hran pro bipartitní graf: {m} > 2*{n}-4'
            }
        
        # Pokud prošel základními testy, je pravděpodobně rovinný
        # (úplná kontrola by vyžadovala složitější algoritmus)
        return {
            'planar': True,
            'method': 'basic_checks',
            'note': 'Prošel základními testy rovinnosti (nezaručuje 100% správnost)'
        }
    
    def is_finite(self):
        """
        g) Konečný graf - má konečný počet uzlů a hran.
        
        Returns:
            bool: True (vždy, protože pracujeme s konečnou reprezentací)
        """
        return True
    
    def is_complete(self):
        """
        h) Úplný graf - každý uzel je spojen s každým ostatním uzlem.
        
        Returns:
            bool: True pokud je graf úplný
        """
        n = self.graph.get_node_count()
        
        if n <= 1:
            return True
        
        # Pro neorientovaný graf: musí mít n*(n-1)/2 hran
        # Pro orientovaný graf: musí mít n*(n-1) hran
        if not self.is_directed():
            expected_edges = n * (n - 1) // 2
        else:
            expected_edges = n * (n - 1)
        
        # Kontrola počtu hran
        actual_edges = self.graph.get_edge_count()
        if actual_edges != expected_edges:
            return False
        
        # Kontrola, že každý uzel je spojen se všemi ostatními
        for node in self.graph.nodes:
            neighbors = self.graph.get_all_neighbors(node)
            if len(neighbors) != n - 1:
                return False
        
        return True
    
    def is_regular(self):
        """
        i) Regulární graf - všechny uzly mají stejný stupeň.
        
        Returns:
            dict: {'regular': bool, 'degree': int or None}
        """
        if self.graph.get_node_count() == 0:
            return {'regular': True, 'degree': None}
        
        degrees = [self.graph.get_degree(node) for node in self.graph.nodes]
        
        if len(set(degrees)) == 1:
            return {'regular': True, 'degree': degrees[0]}
        else:
            return {'regular': False, 'degree': None}
    
    def is_bipartite(self):
        """
        j) Bipartitní graf - lze rozdělit na dvě disjunktní podmnožiny uzlů,
        tak že žádné dva uzly z téže podmnožiny nemají společnou hranu.
        
        Hledání pomocí cyklů liché délky: graf je bipartitní právě tehdy,
        když neobsahuje cykly liché délky.
        
        Používáme obarvení grafů (2-coloring).
        
        Returns:
            dict: {'bipartite': bool, 'partition': tuple or None}
        """
        if self.graph.get_node_count() == 0:
            return {'bipartite': True, 'partition': (set(), set())}
        
        # Obarvení uzlů (0 nebo 1)
        color = {}
        
        # Pro každou komponentu souvislosti
        for start_node in self.graph.nodes:
            if start_node in color:
                continue
            
            # BFS s obarvováním
            queue = deque([start_node])
            color[start_node] = 0
            
            while queue:
                node = queue.popleft()
                current_color = color[node]
                next_color = 1 - current_color
                
                # Všichni sousedé musí mít opačnou barvu
                neighbors = self.graph.get_all_neighbors(node)
                for neighbor in neighbors:
                    if neighbor not in color:
                        color[neighbor] = next_color
                        queue.append(neighbor)
                    elif color[neighbor] != next_color:
                        # Konflikt - graf není bipartitní
                        return {'bipartite': False, 'partition': None}
        
        # Rozdělíme uzly podle barvy
        partition_0 = {node for node, c in color.items() if c == 0}
        partition_1 = {node for node, c in color.items() if c == 1}
        
        return {'bipartite': True, 'partition': (partition_0, partition_1)}
    
    def analyze_all(self):
        """
        Provede kompletní analýzu grafu a vrátí všechny vlastnosti.
        
        Returns:
            dict: Slovník se všemi vlastnostmi grafu
        """
        results = {}
        
        results['a_weighted'] = self.is_weighted()
        results['b_directed'] = self.is_directed()
        results['c_connected'] = self.is_connected()
        results['d_simple'] = self.is_simple()
        results['e_loop_free'] = self.is_loop_free()
        results['f_planar'] = self.is_planar()
        results['g_finite'] = self.is_finite()
        results['h_complete'] = self.is_complete()
        results['i_regular'] = self.is_regular()
        results['j_bipartite'] = self.is_bipartite()
        
        return results

