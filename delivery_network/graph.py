from operator import itemgetter
from time import perf_counter

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
        result = self.min_power(src, dest)
        if result[1] <= power:
            return result[0]
        else :
            return None
        raise NotImplementedError
        #La complexité dans ce cas est de O(V^2), où V est le nombre de sommets, car dans le pire des cas, 
        #on boucle sur tous les sommets dans le while et dans le for qui suit.

    def connected_components(self):
        components = []
        visited = [0] * len(self.nodes)
        for n in self.nodes:
            if not visited[n-1]:
                components.append(self.explore(n))
                for v in components[-1]: 
                    visited[v-1] = 1     
        return components
        #la complexité de l'algorithme DFS est de O(V + E), avec V le nombre de points et E le nombre d'arêtes

    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        same_component = 0 # on vérifie que la source et la destination sont bien dans la même composante, on retourne None sinon
        for e in self.connected_components_set() :
            if (src in e) and (dest in e) : 
                same_component = 1
                nodes_in_component = [n for n in e]
        if same_component == 0 : return None

        # On initialise la puissance de tous les sommets à l'infini sauf la source
        power = {node: float('inf') for node in nodes_in_component}
        power[src] = 0

        # On initialise la liste des sommets visités
        visited = set()

        # On initialise la table des parents
        parents = {node: None for node in nodes_in_component}

        # Boucle principale de l'algorithme de Dijkstra modifié, tourne tant qu'il reste des sommets non visités
        while len(visited) < len(nodes_in_component):
        # Recherche du sommet non visité avec la plus petite puissance
            current_node = None
            min_power = float('inf')
            for node in nodes_in_component:
                if node not in visited and power[node] < min_power:
                    current_node = node
                    min_power = power[node]

            # Ajout du sommet courant à la liste des sommets visités
            visited.add(current_node)

            # Parcours des voisins du sommet courant
            for edge in self.graph[current_node]:
                neighbor = edge[0]
                edge_cost = edge[1]
                # Calcul du coût maximal entre la source et le voisin
                max_cost = max(power[current_node], edge_cost)
            
                # Si ce coût est inférieur à la distance actuellement connue,
                # on met à jour la distance et le parent du voisin
                if max_cost < power[neighbor]:
                    power[neighbor] = max_cost
                    parents[neighbor] = current_node

        # Retrace le chemin de la destination vers la source en remontant les parents successifs de la destination
        path = [dest]
        while path[-1] != src:
            path.append(parents[path[-1]])
        path.reverse()

        # Retourne à la fois la puissance minimale maximale et le chemin
        return path, power[dest]
        #La complexité dans ce cas est de O(V^2), où V est le nombre de sommets, car dans le pire des cas, 
        #on boucle sur tous les sommets dans le while et dans le for qui suit.


    def explore(self, v, visited = None):
        if visited == None:
            visited = [0] * len(self.nodes) # on créé une liste
        visited[v-1] = 1 # on indique que l'origine a été visitée

        for e in self.graph[v]: # pour toutes les arêtes partant de v
            if not visited[e[0]-1]: # si le deuxième node n'a pas été visité
                self.explore(e[0], visited) # on repart en exploration dans le node qu'on a pas exploré, en ne perdant pas la trace des noeud visité
        
        return [n for n in self.nodes if visited[n-1]]





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
        # La complexité pour donner le graphe de Kruskal (avec une méthode Union-Find de compression des chemins) est de O(E log(V))

    def dfs(self, src, dest, chemin = [], puissance_min=0):
        """
        DFS dans l'arbre obtenu par l'algo de Kruskal
        """
        chemin.append(src)
        if src == dest:
            return chemin, puissance_min #La destination est atteinte
        for enfant in self.graph[src]:
            enfant_noeud=enfant[0] #on prend la destination de l'arête
            enfant_puissance=enfant[1] #on prend la puissance de l'arête
            nouvelle_puissance_min = max(puissance_min, enfant_puissance) #la nouvelle puissance est le max entre l'ancienne et celle de l'arête considérée
            if enfant_noeud not in chemin: #si on est pas déjà passé par ce noeud, on lui applique l'algorithme DFS
                nouveau_chemin, puissance_min= self.dfs(enfant_noeud, dest, chemin, nouvelle_puissance_min)
                if nouveau_chemin is not None:
                    return nouveau_chemin, max(nouvelle_puissance_min, puissance_min)
        chemin.pop()
        return None,0
        # La complexité de l'algorithme de DFS est de O(S+A)
        # C'est cette fonction qui calcule le chemin de puissance minimale dans le MST


    def dfs2(self, src = None, parents = None, visited = None):
        if src == None :
            src = self.nodes[0]
        if visited == None :
            visited = set()
        visited.add(src)
        if parents is None:
            parents = {src : [None, 0, 0]} #on stocke le parent, la puissance min et la profondeur
        for enfant in self.graph[src]:
            if enfant[0] not in visited:
                parents[enfant[0]] = [src, enfant[1], parents[src][2] + 1]
                self.dfs2(enfant[0], parents, visited)
        return parents
            
    def saumon(self, parents, src, dest): #on va remonter le dictionnaire parent pour trouver le chemin entre src et dest
        if (src not in parents.keys()) or (dest not in parents.keys()): #on renvoie None si un des deux noeuds n'est pas dans le graphe
            return None, None

        profondeur_src = parents[src][2] #on récupère les profondeurs des trajets pour les égaliser
        profondeur_dest = parents[dest][2]
        node_src = src
        node_dest = dest
        puissance_min = 0
        chemin_src = [src]
        chemin_dest = [dest]
        
        while profondeur_src > profondeur_dest: #on égalise les profondeurs(1)
            puissance_min = max(puissance_min, parents[node_src][1])
            node_src = parents[node_src][0]
            chemin_src.append(node_src)
            profondeur_src -= 1

        while profondeur_dest > profondeur_src: #on égalise les profondeurs(2)
            puissance_min = max(puissance_min, parents[node_dest][1])           
            node_dest = parents[node_dest][0]
            chemin_dest.append(node_dest)
            profondeur_dest -= 1

        while node_dest != node_src: #une fois que les profondeurs sont égalisées, on remonte jusqu'à tomber sur un noeud commun
            puissance_min = max(puissance_min, parents[node_src][1])
            node_src = parents[node_src][0]
            chemin_src.append(node_src)
            puissance_min = max(puissance_min, parents[node_dest][1])
            node_dest = parents[node_dest][0]
            chemin_dest.append(node_dest)
        
        del chemin_dest[-1] #on supprime le dernier élément de chemin_dest, pour ne pas le répéter
        return chemin_src + chemin_dest[::-1], puissance_min   #on concatène les deux chemins afin de créer le trajet de src à dest
        

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
        line = f.readline() #on lit la ligne suivante
        chara = line.split() #on récupère ce qui est écrit
        if len(chara) == 4: #on vérifie si la distance est indiquée
            graph.add_edge(int(chara[0]), int(chara[1]), int(chara[2]), int(chara[3])) #on ajoute l'arête
        else:
            graph.add_edge(int(chara[0]), int(chara[1]), int(chara[2])) #on ajoute l'arête sans préciser la distance
    f.close()
    return graph
    raise NotImplementedError

def routes(graphe_path, route_path):
    g = graph_from_file(graphe_path) #on génère le graph du fichier
    kruskal = g.kruskal() #on récupère le minimal spanning tree en appliquant la méthode kruskal
    f = open(route_path, "r") #on récupère les routes
    h = open("/home/onyxia/work/ENSAE-Projet-de-programmation/output/route.x.out", "w") #on génère un fichier qui contiendra les résultats
    nb_route = f.readline() #on récupère le nombre de routes qui se trouve sur la première ligne du fichier
    for i in range(int(nb_route) - 1): #on boucle sur les lignes du fichier qui représentent des routes à tester
        print(i)
        line = f.readline().split() #on split les lignes pour avoir une liste contenant la source la destination et l'utilité
        src = int(line[0])
        dest = int(line[1])
        h.write(line[0] + " " + line[1] + " " + str(kruskal.dfs(src, dest, [])[1]) + " " + line[2] + "\n") #on note dans le fichier de sorti l'utilité minimale qui est calculé en appliquant la méthode dfs à l'arbre
    f.close()
    h.close()

def routes2(graphe_path, route_path):
    g = graph_from_file(graphe_path) #on génère le graph du fichier
    kruskal = g.kruskal() #on récupère le minimal spanning tree en appliquant la méthode kruskal
    parents = kruskal.dfs2() #on récupère le dictionnaire des parents
    f = open(route_path, "r") #on récupère les routes
    h = open("/home/onyxia/ENSAE-Projet-de-programmation/output/route.x.out", "w") #on génère un fichier qui contiendra les résultats
    nb_route = f.readline() #on récupère le nombre de routes qui se trouve sur la première ligne du fichier
    for i in range(int(nb_route) - 1): #on boucle sur les lignes du fichier qui représentent des routes à tester
        print(i)
        line = f.readline().split() #on split les lignes pour avoir une liste contenant la source la destination et l'utilité
        src = int(line[0])
        dest = int(line[1])
        h.write(line[0] + " " + line[1] + " " + str(kruskal.saumon(parents, src, dest)[1]) + " " + line[2] + "\n") #on note dans le fichier de sorti la puissance minimale qui est calculé en appliquant la méthode dfs à l'arbre
    f.close()
    h.close()



def routes_test(graphe_path, route_path):
    g = graph_from_file(graphe_path) #on génère le graph du fichier
    t1_start = perf_counter() # on lance le chrono
    kruskal = g.kruskal() #on récupère le minimal spanning tree en appliquant la méthode kruskal
    f = open(route_path, "r") #on récupère les routes
    h = open("/home/onyxia/ENSAE-Projet-de-programmation/output/route.test.out", "w") #on génère un fichier qui contiendra les résultats
    nb_route = int(f.readline()) #on récupère le nombre de routes qui se trouve sur la première ligne du fichier
    for i in range(100): #on boucle sur les lignes du fichier qui représentent des routes à tester
        line = f.readline().split() #on split les lignes pour avoir une liste contenant la source la destination et l'utilité
        src = int(line[0])
        dest = int(line[1])
        h.write(str(kruskal.dfs(src, dest, [])[1]) + "\n")
    t1_stop = perf_counter() #on arrête le chrono
    duration = t1_stop-t1_start
    f.close()
    h.write(str((nb_route * duration) / 60000))
    h.close
    print((nb_route * duration) / 60000) #on retourne le temps estimé en minutes du traitement total du fichier


def routes_test2(graphe_path, route_path):

    g = graph_from_file(graphe_path) #on génère le graph du fichier
    t1_start = perf_counter() # on lance le chrono
    kruskal = g.kruskal() #on récupère le minimal spanning tree en appliquant la méthode 
    t1_stop = perf_counter()
    parents = kruskal.dfs2()
    f = open(route_path, "r") #on récupère les routes
    h = open("/home/onyxia/ENSAE-Projet-de-programmation/output/route.test.out", "w") #on génère un fichier qui contiendra les résultats
    t2_start = perf_counter()
    nb_route = int(f.readline()) #on récupère le nombre de routes qui se trouve sur la première ligne du fichier
    for i in range(1000): #on boucle sur les lignes du fichier qui représentent des routes à tester
        line = f.readline().split() #on split les lignes pour avoir une liste contenant la source la destination et l'utilité
        src = int(line[0])
        dest = int(line[1])
        h.write(str(kruskal.saumon(parents, src, dest)) + "\n")
    
    t2_stop = perf_counter() #on arrête le chrono
    duration_dfs = t1_stop-t1_start
    duration_routes = t2_stop-t2_start
    f.close()
    h.write(str(duration_dfs + (nb_route * duration_routes) / 1000))
    h.close()

"""
Q10 : notre algorithme ne fonctionne pas sur les graphes au-delà du graphe 1, car python s'arrête à cause d'une boucle trop longue
Q15 : en utilisant la fonction routes_test, notre programme estime mettre 110 minutes pour calculer les routes du fichier routes.2.in
"""
def glutonny(path_routes_x, path_trucks_x, budget = 25e9):
    
#on fait utilité/cout [trajet, optimal, coût] et on trie la liste selon 3
#on achète les camions de la liste jusqu'à atteindre le budget
    routes = open(path_routes_x, "r") #on récupère les routes
    camions = open(path_trucks_x, "r") #on récupère les camions
    nb_routes=routes.readline() #on retire la première ligne inutile
    nb_camions=camions.readline() #on retire la première ligne inutile
    lignes_routes = routes.readlines()
    lignes_camions = camions.readlines()
    liste_routes = []
    liste_camions = []

#extraction de données
    for ligne in lignes_routes: #liste contenant des listes représentant les routes [(src,dest),puissance_min,utilité]
        var=ligne.split(' ')
        var[3]=var[3].strip('\n')
        liste_routes.append([(int(var[0]),int(var[1])),int(var[2]),int(var[3])])
    for ligne in lignes_camions: #liste contenant les modèles de camions [puissance_min,coût]
        var=ligne.split(' ')
        var[1]=var[1].strip('\n')
        liste_camions.append([int(var[0]), int(var[1])])
    routes.close()
    camions.close()

#liste_camions = sorted(liste_camions, key=itemgetter(1)) cela ne fait rien car on suppose que les camions sont classé par leur puissance
#on associe à la route son camion optimal (boucle for et while) [(src,dest),puissance_min,utilité,index_camion]
    for route in liste_routes :
        puissance_min_nécessaire=route[1]
        i=0
        if liste_camions[-1][0] < puissance_min_nécessaire: #on vérifie si au moins un camion correspond
            route.append(None)
        else:
            while liste_camions[i][0]<puissance_min_nécessaire : #on retire les camions n'ayant pas la puissance _min_nécessaire
                i += 1
            camions_candidat=liste_camions[i:]
            valeur_min = min(camions_candidat, key = lambda x: x[1]) #on prend le camion ayant le coût minimal
            camion_optimal=liste_camions.index(valeur_min) #on ajoute l'index du camion en sachant que c'est -2 par rapport au document out
            route.append(camion_optimal) #on a maintenant [(src,dest),puissance, utilité,camion optimal    


    for trajet in liste_routes : # on ajoute le rapport utilité/cout à la liste des routes
        if trajet[2] != None and trajet[3] !=None:
            trajet.append(trajet[2] / liste_camions[trajet[3]][1])
        else :
            trajet.append(0)
    
    liste_routes.sort(key = itemgetter(4), reverse=True) # on trie la liste en fonction du rapport précédent

    nb_routes = len(liste_routes)
    budget = 25e9
    achat_camion = []
    utilité=0
    for route in liste_routes:
        if budget >0 and route[4]>0:
            achat_camion.append([route[3], route[0]]) # on ajoute à la liste des achats de camion un camion et son trajet
            budget = budget - liste_camions[route[3]][1] # on l'enlève du budget
            utilité += route[2]

    return achat_camion, utilité

    

# Méthodes non-utilisées dans le programme:

def get_path_with_power1(self, src, dest, power):
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


def get_path_with_power2(self, src, dest, power):
        same_component = 0
        for e in self.connected_components_set() :
            if (src in e) and (dest in e) : 
                same_component = 1
                nodes_in_components = [n for n in e]
        if same_component == 0 : return None
        
        inf = float("inf") #on utilise un majorant de la somme des puissances comme inf
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

def min_power2(self, src, dest):
        """
        Should return path, min_power. 
        """
        same_component = 0 # on vérifie que la source et la destination sont bien dans la même composante, on retourne None sinon
        for e in self.connected_components_set() :
            if (src in e) and (dest in e) : 
                same_component = 1
                nodes_in_components = [n for n in e]
        if same_component == 0 : return None
        
        inf = float("inf") #on utilise l'infini de la puissances comme inf
        s_a_explorer = {n : [inf, ""] for n in nodes_in_components if n != src} #On associe au sommet d'origine src la liste [puissance, plus court chemin]
        s_explore = {src : [0, [src]]} #on créée un dictionnaire avec les sommets déjà explorés

        for e in self.graph[src]:
            s_a_explorer[e[0]] = [e[1], src] #on ajoute dans les sommets en clé le sommet et en valeur la puissance et la source

        while s_a_explorer and any(s_a_explorer[i][0] < inf for i in s_a_explorer): #tant qu'il reste des sommets à explorer
            s_min = min(s_a_explorer, key = s_a_explorer.get) #on sélectionne le sommet connecté à la source avec la puissance minimale
            puissance_s_min, precedent_s_min = s_a_explorer[s_min] #on retient la puissance min et le parent
            for successeur in [e[0] for e in self.graph[s_min]]: #on boucle sur les nodes reliés à l'actuel
                if successeur in s_a_explorer:
                    puissance = max(puissance_s_min, e[1])
                    if puissance < s_a_explorer[successeur][0]:
                        s_a_explorer[successeur] = [puissance, s_min]
            s_explore[s_min] = [puissance_s_min, s_explore[precedent_s_min][1] + [s_min]]
            del s_a_explorer[s_min]

        return s_explore[dest][::-1] # on renvoie la liste en l'inversant parce qu'elle n'est pas dans le bon sens
        raise NotImplementedError
        # Pour faire cela nous avons utilisé un algorithme de Djikstra modifié (car les puissances ne se somment pas). Cela fait que la complexité est de
        # O((E + V) * log(V))

def connected_components2(self) :
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