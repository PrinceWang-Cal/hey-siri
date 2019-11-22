import networkx as nx
import matplotlib.pyplot as plt
import large_special1 as ls1


# return a list of special subgraphs and all homes in big graph
def subgraphs():
    i = 1
    homes = []
    subgraphs = []
    while i < 195:
        #print(ls1.special_g_map(i).number_of_nodes())
        #print(list(ls1.special_g_map(i).nodes()))
        small, small_homes = ls1.special_g_map(i)
        subgraphs.append(small)
        homes += small_homes
        i = i + 15
    return subgraphs, homes

#glue small graphs to get bigger one
def glue(small_graphs):
    large_graph = nx.Graph()
    large_graph.add_node(0)
    for i in range(len(small_graphs)):
        small = small_graphs[i]
        large_graph = nx.compose(small, large_graph)
        large_graph.add_edge(0, 1 + 15 * i)
    return large_graph


smalls, result_homes = subgraphs()
print(result_homes)
print(len(result_homes))
L_G = glue(smalls)
print(L_G.number_of_nodes())
#nx.draw_networkx(L_G)
#plt.show()
