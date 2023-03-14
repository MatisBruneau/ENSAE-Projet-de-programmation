from graph import Graph, graph_from_file, routes
from operator import itemgetter
from time import perf_counter

#data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
graph_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/network.1.in"
route_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/routes.1.in"

#routes(graph_path, route_path)
#print("finish")
g = graph_from_file(graph_path)
#k = g.kruskal()
#print(k)
#print(k.dfs(13,16, []))




t1_start = perf_counter()

print(g.min_power(6, 11))
print(g.kruskal().dfs(6, 11))

# Stop the stopwatch / counter
t1_stop = perf_counter()
print("Elapsed time:", t1_stop, t1_start) 
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)