class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
        return 
        raise NotImplementedError
    

    def get_path_with_power(self, src, dest, power):
        same_component = 0
        for e in self.connected_components_set() :
            if (src in e) and (dest in e) : same_component = 1
        if same_component == 0 : return None
        
        raise NotImplementedError
    

    def connected_components(self) :
        nodes_component = [n for n in self.nodes] #initialisation d'une liste contenant les components de chaque node
        for n in range(self.nb_nodes) : #on parcourt les nodes
            for e in self.graph[n+1] : #pour chaque node on regarde ses arêtes
                nodes_component[e[0]-1] = min(nodes_component[n], nodes_component[e[0]-1]) #on place les deux nodes dans la même composante (en choisissant la minimum)
                nodes_component[n] = min(nodes_component[n], nodes_component[e[0]-1])
        unique_values = set(nodes_component) #on regarde les composantes qui restent à la fin
        components = {}
        for u in unique_values :
            components[u] = [n+1 for (n, component) in enumerate(nodes_component) if component == u ]
        return components.values()
        raise NotImplementedError


    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    f = open(filename, "r") #ouvre le fichier
    line = f.readline() #lit la première ligne
    chara = line.split() #on récupère les nombres écrit sur la ligne
    nb_nodes = int(chara[0])
    nb_edges = int(chara[1])
    nodes = [n+1 for n in range(nb_nodes)]
    graph = Graph(nodes)
    for i in range(nb_edges) : #on boucle sur les arêtes pour les ajouter
        line = f.readline()
        chara = line.split()
        graph.add_edge(int(chara[0]), int(chara[1]), int(chara[2]))
    f.close()
    return graph
    raise NotImplementedError