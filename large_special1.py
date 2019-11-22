import networkx as nx
import matplotlib.pyplot as plt


# return a small graph with start_node and the homes on this graph
def special_g_map(start_node):
    special = nx.Graph()
    special.add_edge(1, 2)
    special.add_edge(1, 7)
    special.add_edge(2, 3)
    special.add_edge(3, 4)
    special.add_edge(4, 5)
    special.add_edge(5, 6)
    special.add_edge(6, 7)

    special.add_edge(1, 8)
    special.add_edge(1, 9)
    special.add_edge(1, 12)
    special.add_edge(1, 10)
    special.add_edge(9, 11)
    special.add_edge(12, 14)
    special.add_edge(1, 10)
    special.add_edge(10, 13)
    special.add_edge(13, 15)

    homes = [3, 4, 5, 6, 11, 14, 15]
    homes = list(map(lambda x: x + start_node - 1, homes))
    special = nx.relabel_nodes(special, lambda x: x + start_node - 1)
    return special, homes


#nx.draw_networkx(special_g_map(16)[0])
#plt.show()

#result = special_g_map(16)[1]
#print(result)
