from graph import Graph, graph_from_file, routes, routes2, routes_test, routes_test2, glutonny
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/network.6.in"
route_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/routes.6.in"
routes = "/home/onyxia/ENSAE-Projet-de-programmation/output/route.2.out"
camions = "/home/onyxia/ENSAE-Projet-de-programmation/input/trucks.2.in"

#routes(graph_path, route_path)
#print("finish")
#g = graph_from_file(graph_path)
#k = g.kruskal()
#parents = k.dfs2()
#print(k.saumon(parents, 2, 103))
#print(g.min_power(2, 103))
#routes2(graph_path, route_path)
print(glutonny(routes, camions))



#k = g.kruskal()

#print(k)

#print(k.dfs(13,16, []))​
