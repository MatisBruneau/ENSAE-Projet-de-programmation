from operator import itemgetter

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
            if (src in e) and (dest in e) : 
                same_component = 1
                nodes_in_components = [n for n in e]
        if same_component == 0 : return None
        
        inf = 150000 #on utilise un majorant de la somme des puissances comme inf
        s_a_explorer = {n : [inf, ""] for n in nodes_in_components if n != src} #On associe au sommet d'origine src la liste [puissance, plus court chemin]
        s_explore = {src : [0, [src]]} #on créée un dictionnaire avec les sommets déjà explorer

        for e in self.graph[src]:
            s_a_explorer[e[0]] = [e[1], src] #on ajoute dans les sommets en clé le sommet et en valeur la puissance et la source

        while s_a_explorer and any(s_a_explorer[i][0] < inf for i in s_a_explorer): #tant qu'il reste des sommets à explorer
            s_min = min(s_a_explorer, key = s_a_explorer.get) #on sélectionne le sommet connecté à la source avec la puissance minimale
            puissance_s_min, precedent_s_min = s_a_explorer[s_min] #on retient la puissance min et le parent
            for successeur in [e[0] for e in self.graph[s_min]]:
                if successeur in s_a_explorer:
                    puissance = max(puissance_s_min, e[1])
                    if puissance < s_a_explorer[successeur][0]:
                        s_a_explorer[successeur] = [puissance, s_min]
            s_explore[s_min] = [puissance_s_min, s_explore[precedent_s_min][1] + [s_min]]
            del s_a_explorer[s_min]          

        if s_explore[dest][0] <= power:
            return s_explore[dest]
        else :
            return None 
        raise NotImplementedError

# Voir algo BFS

    def get_path_with_power2(self, src, dest, power):
        same_component = 0
        for e in self.connected_components_set() :
            if (src in e) and (dest in e) : 
                same_component = 1
                nodes_in_components = [n for n in e]
        if same_component == 0 : return None
        
        inf = 150000 #on utilise un majorant de la somme des puissances comme inf
        s_a_explorer = {n : [inf, ""] for n in nodes_in_components if n != src} #On associe au sommet d'origine src la liste [puissance, plus court chemin]
        s_explore = {src : [0, [src]]} #on créée un dictionnaire avec les sommets déjà explorer

        for e in self.graph[src]:
            s_a_explorer[e[0]] = [e[1], src] #on ajoute dans les sommets en clé le sommet et en valeur la puissance et la source

        while s_a_explorer and any(s_a_explorer[i][0] < inf for i in s_a_explorer):
            s_min = min(s_a_explorer, key = s_a_explorer.get)
            longueur_s_min, precedent_s_min = s_a_explorer[s_min]
            for successeur in [e[0] for e in self.graph[s_min]]:
                if successeur in s_a_explorer:
                    dist = longueur_s_min + e[1]
                    if dist < s_a_explorer[successeur][0]:
                        s_a_explorer[successeur] = [dist, s_min]
            s_explore[s_min] = [longueur_s_min, s_explore[precedent_s_min][1] + [s_min]]
            del s_a_explorer[s_min]          

        return s_explore[dest][1] 
        raise NotImplementedError
    

    def connected_components(self) :
        nodes_component = [n for n in self.nodes] #initialisation d'une liste contenant les components de chaque node (la position i contient la composante du noeud i)
        for n in range(self.nb_nodes) : #on parcourt les nodes
            for e in self.graph[n+1] : #pour chaque node on regarde ses arêtes
                nodes_component[e[0]-1] = min(nodes_component[n], nodes_component[e[0]-1]) #on place les deux nodes dans la même composante (en choisissant le minimum)
                nodes_component[n] = min(nodes_component[n], nodes_component[e[0]-1])
        unique_values = set(nodes_component) #on regarde les composantes qui restent après avoir parcourut tout les noeuds
        components = {} #on va stocker les composantes dans un dictionnaire
        for u in unique_values : #on parcourt les composantes
            components[u] = [n+1 for (n, component) in enumerate(nodes_component) if component == u] #on retrouve les noeuds dans la composante u
        return components.values() #on revoit les listes contenant les noeuds des composantes
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






        #TP2
    def transfor(self): #on a besoin de représenter le graphe par des listes pour pouvoir le trier
        G=[]
        for node in self.graph:
            liste_clé = self.graph[node]
            for arrete in liste_clé:
                G.append((node,arrete[0],arrete[1],arrete[2])) #on implémente le noeud de départ, d'arrivée, la puissance min
        return G


    def tri(self,liste): #On a besoin de trier les arrêtes pour l'algo de Kruskal
        liste = sorted(liste, key=itemgetter(2)) #on trie liste en fonction du deuxième élément des ses tuples
        return liste

    def union(self,parent, taille, x, y):
        """
        Fusionne les ensembles contenant les sommets x et y.
        """
        origine_x = self.find(parent, x)
        origine_y = self.find(parent, y)

        # Sinon, on fusionne les ensembles en mettant l'origine de l'arbre le plus petit comme enfant de l'origine de l'arbre le plus grand.
        if taille[origine_x-1] < taille[origine_y-1]:
            parent[origine_x-1] = origine_y
            taille[origine_y-1] += taille[origine_x-1]
        else:
            parent[origine_y-1] = origine_x
            taille[origine_x-1] += taille[origine_y-1]

    def find(self,parent, x):
        """
        Trouve le représentant de l'ensemble auquel appartient le sommet donné.
        """
        # Si le parent du sommet est lui-même, cela signifie que c'est la racine de l'arbre, donc on le renvoie.
        if parent[x-1] == x:
            return x
        # Sinon, on continue de remonter l'arbre jusqu'à atteindre la racine.
        else:
            return self.find(parent, parent[x-1])

    def kruskal(self):
        #On a besoin de Union-find pour vérifier lorsque l'on ajoute une arrête que l'on préserve le caractère acyclique 
        #Initialisation  
        KR=[]
        Liste_arrete=self.tri(self.transfor())
        parent=[0]*len(self.graph) #indique pour chaque noeud quel est le "noeud-père" 
        taille=[1]*len(self.graph) #taille de chaque set, afin d'optimiser les calculs
        for node in self.graph: #on construit les cycles nécessaires à l'union-find
            parent[node-1]=node
        
        #Principal
        for arrete in Liste_arrete:
            x=arrete[0] #on simplifie l'écriture (x,y) point de départ et d'arrivée de l'arrête examinée
            y=arrete[1]
            if self.find(parent, x) != self.find(parent, y): #on veut que x et y ne soient pas dans le même set
                self.union(parent, taille, x, y)
                KR.append(arrete)


        #Transformation de la liste obtenue en graphe
        KR_nodes=set()
        for arrete in KR: #on a besoin d'une liste de noeuds pour créer un graphe
            KR_nodes.add(arrete[0])
            KR_nodes.add(arrete[1])
        KR_nodes=list(KR_nodes)
        KRUSKAL = Graph(KR_nodes)
        for arrete in KR : #on boucle sur les arêtes pour les ajouter
            KRUSKAL.add_edge(arrete[0], arrete[1], arrete[2], arrete[3])

        return KRUSKAL

    def dfs(self, src, dest, chemin=[]):
        """
        DFS dans l'arbre obtenu par l'algo de Kruskal
        """
        chemin.append(src)
        if src == dest:
            return chemin #La destination est atteinte
        for enfant in self.graph[src]:
            enfant=enfant[0] #on ne prend que la destination de l'arrête
            if enfant not in chemin:
                nouveau_chemin= self.dfs(enfant, dest, chemin)
                if nouveau_chemin is not None:
                    return nouveau_chemin
        
        return None

#calculer la puissance nécessaire





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
        graph.add_edge(int(chara[0]), int(chara[1]), int(chara[2]), int(chara[3]))
    f.close()
    return graph
    raise NotImplementedError
