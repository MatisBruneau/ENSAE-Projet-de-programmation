from graph import Graph, graph_from_file


data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
file_name = "network.02.in"

g = graph_from_file(data_path + file_name)
print(g)
component = g.connected_components_set()
print(component)