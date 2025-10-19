"""
Parser pro zpracování textového formátu grafů.

Podporované formáty:
- u identifikator [ohodnoceni];  - definice uzlu
- h uzel1 (< | - | >) uzel2 [ohodnoceni] [:oznaceni];  - definice hrany
- u *;  - vynechaný uzel (pro binární stromy)
"""

import re


class Node:
    """Reprezentace uzlu v grafu."""
    
    def __init__(self, identifier, weight=None):
        """
        Args:
            identifier (str): Identifikátor uzlu
            weight (float, optional): Ohodnocení uzlu
        """
        self.identifier = identifier
        self.weight = weight
    
    def __repr__(self):
        if self.weight is not None:
            return f"Node({self.identifier}, weight={self.weight})"
        return f"Node({self.identifier})"
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.identifier == other.identifier
        return False
    
    def __hash__(self):
        return hash(self.identifier)


class Edge:
    """Reprezentace hrany v grafu."""
    
    def __init__(self, node1, node2, directed=False, reverse=False, weight=None, label=None):
        """
        Args:
            node1 (str): Identifikátor prvního uzlu
            node2 (str): Identifikátor druhého uzlu
            directed (bool): True pokud je hrana orientovaná
            reverse (bool): True pokud směr hrany je node2 -> node1 (při < operátoru)
            weight (float, optional): Ohodnocení hrany
            label (str, optional): Označení hrany
        """
        self.node1 = node1
        self.node2 = node2
        self.directed = directed
        self.reverse = reverse
        self.weight = weight
        self.label = label
    
    @property
    def source(self):
        """Vrací zdrojový uzel orientované hrany."""
        if not self.directed:
            return self.node1
        return self.node2 if self.reverse else self.node1
    
    @property
    def target(self):
        """Vrací cílový uzel orientované hrany."""
        if not self.directed:
            return self.node2
        return self.node1 if self.reverse else self.node2
    
    def __repr__(self):
        direction = "<-" if self.reverse else "->" if self.directed else "-"
        parts = [f"{self.node1} {direction} {self.node2}"]
        if self.weight is not None:
            parts.append(f"weight={self.weight}")
        if self.label:
            parts.append(f"label={self.label}")
        return f"Edge({', '.join(parts)})"


class GraphParser:
    """Parser pro zpracování textového formátu grafů."""
    
    # Regex pro parsování příkazů
    NODE_PATTERN = re.compile(r'^\s*u\s+(.+?)\s*;\s*$')
    EDGE_PATTERN = re.compile(r'^\s*h\s+(.+?)\s+([<\->]+)\s+(.+?)\s*;\s*$')
    
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.is_binary_tree = None
    
    def parse_file(self, filepath):
        """
        Načte a parsuje soubor s grafem.
        
        Args:
            filepath (str): Cesta k souboru
            
        Returns:
            tuple: (nodes, edges, is_binary_tree)
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        return self.parse_content(content)
    
    def parse_content(self, content):
        """
        Parsuje textový obsah s grafem.
        
        Args:
            content (str): Textový obsah
            
        Returns:
            tuple: (nodes, edges, is_binary_tree)
        """
        self.nodes = []
        self.edges = []
        
        lines = content.strip().split('\n')
        
        # Nejprve detekujeme typ grafu
        self.is_binary_tree = self._detect_binary_tree(lines)
        
        # Parsujeme řádky
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            
            # Ignorujeme prázdné řádky a komentáře
            if not line or line.startswith('#'):
                continue
            
            try:
                if line.startswith('u '):
                    self._parse_node(line)
                elif line.startswith('h '):
                    self._parse_edge(line)
                else:
                    print(f"Varování: Neznámý příkaz na řádku {line_num}: {line}")
            except Exception as e:
                print(f"Chyba při parsování řádku {line_num}: {line}")
                print(f"  {e}")
        
        return self.nodes, self.edges, self.is_binary_tree
    
    def _detect_binary_tree(self, lines):
        """
        Detekuje, zda se jedná o binární strom.
        Binární strom = pouze příkazy 'u', žádné příkazy 'h'.
        
        Args:
            lines (list): Řádky souboru
            
        Returns:
            bool: True pokud je to binární strom
        """
        for line in lines:
            line = line.strip()
            if line.startswith('h '):
                return False
        return True
    
    def _parse_node(self, line):
        """
        Parsuje definici uzlu.
        Formát: u identifikator [ohodnoceni];
        
        Args:
            line (str): Řádek s definicí uzlu
        """
        # Odstraníme 'u ' a ';'
        content = line[2:].strip()
        if content.endswith(';'):
            content = content[:-1].strip()
        
        # Rozdělíme na identifikátor a případné ohodnocení
        parts = content.split(None, 1)
        
        identifier = parts[0]
        weight = None
        
        if len(parts) > 1:
            try:
                weight = float(parts[1])
            except ValueError:
                print(f"Varování: Nelze převést ohodnocení na číslo: {parts[1]}")
        
        # Speciální případ: hvězdička (vynechaný uzel v binárním stromu)
        if identifier == '*':
            node = Node('*', weight)
        else:
            node = Node(identifier, weight)
        
        self.nodes.append(node)
    
    def _parse_edge(self, line):
        """
        Parsuje definici hrany.
        Formát: h uzel1 (< | - | >) uzel2 [ohodnoceni] [:oznaceni];
        
        Args:
            line (str): Řádek s definicí hrany
        """
        # Odstraníme 'h ' a ';'
        content = line[2:].strip()
        if content.endswith(';'):
            content = content[:-1].strip()
        
        # Rozdělit na části podle operátoru
        # Podporujeme: <, -, >, ->, <-
        operator = None
        node1 = None
        node2 = None
        
        # Hledáme operátor
        for op in ['<-', '->', '<', '>', '-']:
            if op in content:
                parts = content.split(op, 1)
                if len(parts) == 2:
                    node1 = parts[0].strip()
                    rest = parts[1].strip()
                    operator = op
                    break
        
        if not operator:
            raise ValueError(f"Nenalezen operátor hrany v: {line}")
        
        # Zpracujeme zbytek (node2, ohodnocení, označení)
        # Formát: node2 [weight] [:label]
        parts = rest.split()
        node2 = parts[0]
        
        weight = None
        label = None
        
        # Procházíme zbylé části
        for part in parts[1:]:
            if part.startswith(':'):
                label = part[1:]
            else:
                try:
                    weight = float(part)
                except ValueError:
                    print(f"Varování: Nelze převést '{part}' na číslo")
        
        # Určíme směr hrany
        directed = operator in ['<', '>', '<-', '->']
        reverse = operator in ['<', '<-']
        
        edge = Edge(node1, node2, directed, reverse, weight, label)
        self.edges.append(edge)
    
    def get_node_identifiers(self):
        """
        Vrací seznam identifikátorů všech uzlů (bez hvězdiček).
        
        Returns:
            list: Seznam identifikátorů
        """
        return [node.identifier for node in self.nodes if node.identifier != '*']

