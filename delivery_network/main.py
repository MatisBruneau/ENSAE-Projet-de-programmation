from graph import Graph, graph_from_file
from operator import itemgetter
from time import perf_counter

data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
file_name = "network.04.in"

g = graph_from_file(data_path + file_name)



"""
component = g.connected_components_set()
print(component)
print(g.get_path_with_power(1, 2, 10))
"""
print(g)
print(g.get_path_with_power(1, 4, 6))
