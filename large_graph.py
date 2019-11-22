import networkx as nx
import matplotlib.pyplot as plt
import large_special1 as ls1


# return large graphs with 196 nodes and 91 home nodes
def large_graph():
    subs, L_homes = sub_graphs()
    L_G = glue(subs)
    return L_G, L_homes


# return a list of special small graphs and all homes in big graph
def sub_graphs():
    i = 1
    homes = []
    small_graphs = []
    while i < 195:
        small, small_homes = ls1.special_g_map(i)
        small_graphs.append(small)
        homes += small_homes
        i = i + 15
    return small_graphs, homes


# glue small graphs to get bigger one
def glue(small_graphs):
    l_graph = nx.Graph()
    l_graph.add_node(0)
    for i in range(len(small_graphs)):
        small = small_graphs[i]
        l_graph = nx.compose(small, l_graph)
        l_graph.add_edge(0, 1 + 15 * i)
    return l_graph


#smalls, result_homes = sub_graphs()
# print(result_homes)
#print(len(result_homes))
#L_G = glue(smalls)
#print(L_G.number_of_nodes())

# nx.draw_networkx(L_G)
# plt.show()
