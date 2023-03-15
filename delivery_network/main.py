from graph import Graph, graph_from_file, routes, routes_test
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/network.2.in"
route_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/routes.2.in"

#routes(graph_path, route_path)
#print("finish")

routes_test(graph_path, route_path)


#k = g.kruskal()
#print(k)
#print(k.dfs(13,16, []))


