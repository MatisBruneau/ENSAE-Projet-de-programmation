from graph import Graph, graph_from_file, routes
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/network.1.in"
route_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/routes.1.in"

#routes(graph_path, route_path)
#print("finish")
g = graph_from_file(graph_path)
k = g.kruskal()
print(g.min_power2(6, 11))
print(k.dfs(6, 11))


#k = g.kruskal()
#print(k)
#print(k.dfs(13,16, []))


