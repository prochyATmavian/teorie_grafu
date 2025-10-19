"""
Třída Graph pro reprezentaci grafu a základní operace.
"""

from collections import defaultdict, deque


class Graph:
    """Reprezentace grafu s uzly a hranami."""
    
    def __init__(self, nodes, edges, is_binary_tree=False):
        """
        Args:
            nodes (list): Seznam Node objektů
            edges (list): Seznam Edge objektů
            is_binary_tree (bool): True pokud je to binární strom
        """
        self.raw_nodes = nodes
        self.raw_edges = edges
        self.is_binary_tree = is_binary_tree
        
        # Filtrujeme hvězdičky (vynechané uzly)
        self.nodes = {node.identifier: node for node in nodes if node.identifier != '*'}
        
        # Seznamy sousedů pro rychlejší přístup
        self.adjacency_list = defaultdict(list)  # {node: [(neighbor, edge), ...]}
        self.in_neighbors = defaultdict(list)    # Pro orientované grafy
        self.out_neighbors = defaultdict(list)   # Pro orientované grafy
        
        # Procházíme hrany a budujeme seznamy
        self.edges_list = []
        for edge in edges:
            # Kontrola, že uzly existují
            if edge.node1 not in self.nodes or edge.node2 not in self.nodes:
                print(f"Varování: Hrana odkazuje na neexistující uzel: {edge}")
                continue
            
            self.edges_list.append(edge)
            
            if edge.directed:
                # Orientovaná hrana
                source = edge.source
                target = edge.target
                self.out_neighbors[source].append((target, edge))
                self.in_neighbors[target].append((source, edge))
                self.adjacency_list[source].append((target, edge))
            else:
                # Neorientovaná hrana
                self.adjacency_list[edge.node1].append((edge.node2, edge))
                self.adjacency_list[edge.node2].append((edge.node1, edge))
    
    def get_node_count(self):
        """Vrací počet uzlů v grafu."""
        return len(self.nodes)
    
    def get_edge_count(self):
        """Vrací počet hran v grafu."""
        return len(self.edges_list)
    
    def has_node(self, node_id):
        """Kontroluje, zda uzel existuje."""
        return node_id in self.nodes
    
    def get_neighbors(self, node_id):
        """
        Vrací seznam sousedů uzlu (pro neorientovaný nebo všechny sousedy).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam identifikátorů sousedních uzlů
        """
        if node_id not in self.nodes:
            return []
        return [neighbor for neighbor, _ in self.adjacency_list[node_id]]
    
    def get_successors(self, node_id):
        """
        Vrací následníky uzlu (U+).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam identifikátorů následníků
        """
        if node_id not in self.nodes:
            return []
        return [neighbor for neighbor, _ in self.out_neighbors[node_id]]
    
    def get_predecessors(self, node_id):
        """
        Vrací předchůdce uzlu (U-).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam identifikátorů předchůdců
        """
        if node_id not in self.nodes:
            return []
        return [neighbor for neighbor, _ in self.in_neighbors[node_id]]
    
    def get_all_neighbors(self, node_id):
        """
        Vrací všechny sousedy uzlu - předchůdce i následníky (U).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            set: Množina identifikátorů všech sousedů
        """
        if node_id not in self.nodes:
            return set()
        
        neighbors = set()
        neighbors.update(self.get_successors(node_id))
        neighbors.update(self.get_predecessors(node_id))
        neighbors.update(self.get_neighbors(node_id))
        return neighbors
    
    def get_outgoing_edges(self, node_id):
        """
        Vrací výstupní hrany uzlu (H+).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam Edge objektů
        """
        if node_id not in self.nodes:
            return []
        return [edge for _, edge in self.out_neighbors[node_id]]
    
    def get_incoming_edges(self, node_id):
        """
        Vrací vstupní hrany uzlu (H-).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam Edge objektů
        """
        if node_id not in self.nodes:
            return []
        return [edge for _, edge in self.in_neighbors[node_id]]
    
    def get_incident_edges(self, node_id):
        """
        Vrací všechny incidentní hrany uzlu (H).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            list: Seznam Edge objektů
        """
        if node_id not in self.nodes:
            return []
        
        edges = []
        # Výstupní hrany
        edges.extend(self.get_outgoing_edges(node_id))
        # Vstupní hrany
        edges.extend(self.get_incoming_edges(node_id))
        # Neorientované hrany
        for neighbor, edge in self.adjacency_list[node_id]:
            if not edge.directed and edge not in edges:
                edges.append(edge)
        
        return edges
    
    def get_out_degree(self, node_id):
        """
        Vrací výstupní stupeň uzlu (d+).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            int: Výstupní stupeň
        """
        return len(self.get_outgoing_edges(node_id))
    
    def get_in_degree(self, node_id):
        """
        Vrací vstupní stupeň uzlu (d-).
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            int: Vstupní stupeň
        """
        return len(self.get_incoming_edges(node_id))
    
    def get_degree(self, node_id):
        """
        Vrací stupeň uzlu (d).
        Pro orientované grafy: d+ + d-
        Pro neorientované grafy: počet incidentních hran
        
        Args:
            node_id (str): Identifikátor uzlu
            
        Returns:
            int: Stupeň uzlu
        """
        if node_id not in self.nodes:
            return 0
        
        # Kontrola smyček (smyčka se počítá 2×)
        degree = 0
        for edge in self.get_incident_edges(node_id):
            if edge.node1 == edge.node2:  # Smyčka
                degree += 2
            else:
                degree += 1
        
        return degree
    
    def is_directed(self):
        """Kontroluje, zda je graf orientovaný."""
        return any(edge.directed for edge in self.edges_list)
    
    def is_weighted(self):
        """Kontroluje, zda je graf ohodnocený."""
        # Graf je ohodnocený, pokud má alespoň jedna hrana nebo uzel váhu
        for edge in self.edges_list:
            if edge.weight is not None:
                return True
        for node in self.nodes.values():
            if node.weight is not None:
                return True
        return False
    
    def has_self_loop(self):
        """Kontroluje, zda graf obsahuje smyčku."""
        for edge in self.edges_list:
            if edge.node1 == edge.node2:
                return True
        return False
    
    def has_multiple_edges(self):
        """Kontroluje, zda graf obsahuje vícenásobné hrany."""
        edge_set = set()
        for edge in self.edges_list:
            if edge.directed:
                key = (edge.source, edge.target)
            else:
                # Pro neorientované hrany normalizujeme pořadí
                key = tuple(sorted([edge.node1, edge.node2]))
            
            if key in edge_set:
                return True
            edge_set.add(key)
        return False
    
    def bfs(self, start_node):
        """
        Prohledávání do šířky (BFS) z daného uzlu.
        
        Args:
            start_node (str): Počáteční uzel
            
        Returns:
            set: Množina dosažitelných uzlů
        """
        if start_node not in self.nodes:
            return set()
        
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            node = queue.popleft()
            for neighbor in self.get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
            # Pro orientované grafy také následníky
            for successor in self.get_successors(node):
                if successor not in visited:
                    visited.add(successor)
                    queue.append(successor)
        
        return visited
    
    def bfs_undirected(self, start_node):
        """
        BFS ignorující směry hran (pro slabou souvislost).
        
        Args:
            start_node (str): Počáteční uzel
            
        Returns:
            set: Množina dosažitelných uzlů
        """
        if start_node not in self.nodes:
            return set()
        
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        while queue:
            node = queue.popleft()
            # Všichni sousedé bez ohledu na směr
            neighbors = self.get_all_neighbors(node)
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return visited

