from graph import Graph, graph_from_file, routes, routes_test, routes_test2, glutonny
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/network.1.in"
route_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/routes.1.in"
route_1 = "/home/onyxia/ENSAE-Projet-de-programmation/output/route.1.out"
camion_1 = "/home/onyxia/ENSAE-Projet-de-programmation/input/trucks.1.in"

#routes(graph_path, route_path)
#print("finish")
#g = graph_from_file(graph_path)
#print(g.min_power(6, 11))
routes_test2(graph_path, route_path)





#k = g.kruskal()

#print(k)

#print(k.dfs(13,16, []))​
