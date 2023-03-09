from graph import Graph, graph_from_file
from operator import itemgetter

data_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/"
file_name = "network.4.in"

g = graph_from_file(data_path + file_name)
"""
print(g)
component = g.connected_components_set()
print(component)
print(g.get_path_with_power(1, 2, 10))
"""
KR=g.kruskal()
print(KR)