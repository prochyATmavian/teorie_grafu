"""
Modul pro práci s maticemi a seznamy grafů.

Implementuje:
a) matice sousednosti, b) znaménková matice, c) mocniny matice sousednosti,
d) matice incidence, e) matice délek, f) matice předchůdců,
g) tabulka incidentních hran, h) seznam sousedů, i) seznam uzlů a hran
"""


class MatrixBuilder:
    """Třída pro sestavování matic a seznamů grafů."""
    
    def __init__(self, graph):
        """
        Args:
            graph (Graph): Instance grafu
        """
        self.graph = graph
        # Vytvoříme uspořádaný seznam uzlů pro indexování
        self.node_list = sorted(self.graph.nodes.keys())
        self.node_index = {node: i for i, node in enumerate(self.node_list)}
    
    def adjacency_matrix(self):
        """
        a) Matice sousednosti - A[i][j] = počet hran z uzlu i do uzlu j.
        Pro ohodnocený graf můžeme použít váhy.
        
        Returns:
            tuple: (matice, seznam uzlů)
        """
        n = len(self.node_list)
        matrix = [[0] * n for _ in range(n)]
        
        for edge in self.graph.edges_list:
            i = self.node_index[edge.node1]
            j = self.node_index[edge.node2]
            
            if edge.directed:
                # Orientovaná hrana
                src_idx = self.node_index[edge.source]
                tgt_idx = self.node_index[edge.target]
                matrix[src_idx][tgt_idx] += 1
            else:
                # Neorientovaná hrana - symetrická
                matrix[i][j] += 1
                if i != j:  # Pokud není smyčka
                    matrix[j][i] += 1
        
        return matrix, self.node_list
    
    def weighted_adjacency_matrix(self):
        """
        Matice sousednosti s vahami - A[i][j] = váha hrany z uzlu i do uzlu j.
        Pro více hran mezi stejnými uzly používáme součet vah.
        
        Returns:
            tuple: (matice, seznam uzlů)
        """
        n = len(self.node_list)
        matrix = [[0] * n for _ in range(n)]
        
        for edge in self.graph.edges_list:
            weight = edge.weight if edge.weight is not None else 1
            
            if edge.directed:
                src_idx = self.node_index[edge.source]
                tgt_idx = self.node_index[edge.target]
                matrix[src_idx][tgt_idx] += weight
            else:
                i = self.node_index[edge.node1]
                j = self.node_index[edge.node2]
                matrix[i][j] += weight
                if i != j:
                    matrix[j][i] += weight
        
        return matrix, self.node_list
    
    def signed_matrix(self):
        """
        b) Znaménková matice podle matice sousednosti.
        A[i][j] = 1 pokud existuje hrana, 0 pokud neexistuje.
        
        Returns:
            tuple: (matice, seznam uzlů)
        """
        adj_matrix, nodes = self.adjacency_matrix()
        n = len(nodes)
        
        signed = [[1 if adj_matrix[i][j] > 0 else 0 for j in range(n)] for i in range(n)]
        
        return signed, nodes
    
    def matrix_power(self, matrix, power):
        """
        Násobení matic (pomocná funkce).
        
        Args:
            matrix (list): Čtvercová matice
            power (int): Mocnina
            
        Returns:
            list: Výsledná matice
        """
        n = len(matrix)
        
        if power == 0:
            # Jednotková matice
            return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        
        if power == 1:
            return [row[:] for row in matrix]  # Kopie
        
        # Iterativní násobení
        result = [row[:] for row in matrix]
        
        for _ in range(power - 1):
            result = self._multiply_matrices(result, matrix)
        
        return result
    
    def _multiply_matrices(self, a, b):
        """
        Násobení dvou matic.
        
        Args:
            a, b (list): Matice k vynásobení
            
        Returns:
            list: Výsledná matice
        """
        n = len(a)
        result = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    result[i][j] += a[i][k] * b[k][j]
        
        return result
    
    def adjacency_matrix_powers(self, max_power=3):
        """
        c) Druhá a třetí mocnina matice sousednosti.
        A^k[i][j] = počet cest délky k z uzlu i do uzlu j.
        
        Args:
            max_power (int): Maximální mocnina k výpočtu
            
        Returns:
            dict: {mocnina: (matice, seznam uzlů)}
        """
        adj_matrix, nodes = self.adjacency_matrix()
        
        powers = {}
        for p in range(2, max_power + 1):
            powers[p] = (self.matrix_power(adj_matrix, p), nodes)
        
        return powers
    
    def incidence_matrix(self):
        """
        d) Matice incidence - řádky = uzly, sloupce = hrany.
        
        Pro neorientovaný graf:
        - M[i][j] = 1 pokud uzel i je incidentní s hranou j
        
        Pro orientovaný graf:
        - M[i][j] = 1 pokud hrana j vychází z uzlu i
        - M[i][j] = -1 pokud hrana j vstupuje do uzlu i
        
        Returns:
            tuple: (matice, seznam uzlů, seznam hran)
        """
        n = len(self.node_list)
        m = len(self.graph.edges_list)
        
        matrix = [[0] * m for _ in range(n)]
        
        for j, edge in enumerate(self.graph.edges_list):
            if edge.directed:
                # Orientovaná hrana
                src_idx = self.node_index[edge.source]
                tgt_idx = self.node_index[edge.target]
                matrix[src_idx][j] = 1   # Výstupní
                matrix[tgt_idx][j] = -1  # Vstupní
            else:
                # Neorientovaná hrana
                i = self.node_index[edge.node1]
                j_idx = self.node_index[edge.node2]
                matrix[i][j] = 1
                if i != j_idx:  # Pokud není smyčka
                    matrix[j_idx][j] = 1
        
        return matrix, self.node_list, self.graph.edges_list
    
    def distance_matrix(self):
        """
        e) Matice délek - D[i][j] = nejkratší vzdálenost z uzlu i do uzlu j.
        Používáme Floyd-Warshallův algoritmus.
        
        Returns:
            tuple: (matice, seznam uzlů)
        """
        n = len(self.node_list)
        INF = float('inf')
        
        # Inicializace
        dist = [[INF] * n for _ in range(n)]
        
        # Diagonála = 0
        for i in range(n):
            dist[i][i] = 0
        
        # Přímé hrany
        for edge in self.graph.edges_list:
            weight = edge.weight if edge.weight is not None else 1
            
            if edge.directed:
                src_idx = self.node_index[edge.source]
                tgt_idx = self.node_index[edge.target]
                dist[src_idx][tgt_idx] = min(dist[src_idx][tgt_idx], weight)
            else:
                i = self.node_index[edge.node1]
                j = self.node_index[edge.node2]
                dist[i][j] = min(dist[i][j], weight)
                dist[j][i] = min(dist[j][i], weight)
        
        # Floyd-Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        return dist, self.node_list
    
    def predecessor_matrix(self):
        """
        f) Matice předchůdců - P[i][j] = předchůdce uzlu j na nejkratší cestě z i do j.
        
        Returns:
            tuple: (matice, seznam uzlů)
        """
        n = len(self.node_list)
        INF = float('inf')
        
        # Inicializace vzdáleností
        dist = [[INF] * n for _ in range(n)]
        pred = [[None] * n for _ in range(n)]
        
        for i in range(n):
            dist[i][i] = 0
        
        # Přímé hrany
        for edge in self.graph.edges_list:
            weight = edge.weight if edge.weight is not None else 1
            
            if edge.directed:
                src_idx = self.node_index[edge.source]
                tgt_idx = self.node_index[edge.target]
                if weight < dist[src_idx][tgt_idx]:
                    dist[src_idx][tgt_idx] = weight
                    pred[src_idx][tgt_idx] = self.node_list[src_idx]
            else:
                i = self.node_index[edge.node1]
                j = self.node_index[edge.node2]
                if weight < dist[i][j]:
                    dist[i][j] = weight
                    pred[i][j] = self.node_list[i]
                if weight < dist[j][i]:
                    dist[j][i] = weight
                    pred[j][i] = self.node_list[j]
        
        # Floyd-Warshall s předchůdci
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] != INF and dist[k][j] != INF:
                        new_dist = dist[i][k] + dist[k][j]
                        if new_dist < dist[i][j]:
                            dist[i][j] = new_dist
                            pred[i][j] = pred[k][j]
        
        return pred, self.node_list
    
    def incident_edges_table(self):
        """
        g) Tabulka incidentních hran - pro každý uzel seznam incidentních hran.
        
        Returns:
            dict: {uzel: [hrany]}
        """
        table = {node: [] for node in self.node_list}
        
        for edge in self.graph.edges_list:
            if edge.node1 in table:
                table[edge.node1].append(edge)
            if edge.node2 in table and edge.node1 != edge.node2:
                table[edge.node2].append(edge)
        
        return table
    
    def neighbor_list(self):
        """
        h) Seznam sousedů - pro každý uzel seznam sousedních uzlů.
        
        Returns:
            dict: {uzel: [sousedé]}
        """
        neighbors = {}
        
        for node in self.node_list:
            neighbors[node] = sorted(self.graph.get_all_neighbors(node))
        
        return neighbors
    
    def node_and_edge_list(self):
        """
        i) Seznam uzlů a hran.
        
        Returns:
            dict: {'nodes': list, 'edges': list}
        """
        return {
            'nodes': self.node_list,
            'edges': self.graph.edges_list
        }
    
    def build_all_matrices(self):
        """
        Sestaví všechny matice a seznamy.
        
        Returns:
            dict: Slovník se všemi maticemi a seznamy
        """
        results = {}
        
        results['a_adjacency_matrix'] = self.adjacency_matrix()
        results['a_weighted_adjacency_matrix'] = self.weighted_adjacency_matrix()
        results['b_signed_matrix'] = self.signed_matrix()
        results['c_matrix_powers'] = self.adjacency_matrix_powers()
        results['d_incidence_matrix'] = self.incidence_matrix()
        results['e_distance_matrix'] = self.distance_matrix()
        results['f_predecessor_matrix'] = self.predecessor_matrix()
        results['g_incident_edges_table'] = self.incident_edges_table()
        results['h_neighbor_list'] = self.neighbor_list()
        results['i_node_edge_list'] = self.node_and_edge_list()
        
        return results

