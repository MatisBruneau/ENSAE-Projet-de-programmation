from graph import Graph, graph_from_file


data_path = "/home/onyxia/work/ENSAE-Projet-de-programmation/input/"
file_name = "network.04.in"

g = graph_from_file(data_path + file_name)
print(g)
component = g.connected_components_set()
print(component)
print(g.get_path_with_power1(1, 3, 0))
