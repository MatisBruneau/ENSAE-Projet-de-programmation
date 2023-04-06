from graph import Graph, graph_from_file, routes, routes2, routes_test, routes_test2, glutonny, glutotest
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/network.4.in"
route_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/routes.4.in"
route_1 = "/home/onyxia/ENSAE-Projet-de-programmation/output/route.4.out"
camion_1 = "/home/onyxia/ENSAE-Projet-de-programmation/input/trucks.2.in"

#routes(graph_path, route_path)
#print("finish")
#g = graph_from_file(graph_path)
#k = g.kruskal()
#parents = k.dfs2()
#print(k.saumon(parents, 2, 103))
#print(g.min_power(2, 103))
#print(glutonny(route_1, camion_1))
print(glutotest(route_1, camion_1))





#k = g.kruskal()

#print(k)

#print(k.dfs(13,16, []))​
