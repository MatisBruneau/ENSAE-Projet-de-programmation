from graph import Graph, graph_from_file


data_path = "/home/onyxia/ENSAE-Projet-de-programmation/input/"
file_name = "network.01.in"

g = graph_from_file(data_path + file_name)
print(g)
component = g.connected_components_set()
print(component)
print(g.get_path_with_power(4, 6, 1))