import networkx as nx
import matplotlib.pyplot as plt

#Dense group with many paths but only one is ideal(break dij/sp)
#pick path with both home and normal locations
def dense_graph():
    G = nx.gnp_random_graph(30, 0.4)
    G = nx.relabel_nodes(G, lambda x: 58 + x);
    return G

#G = dense_graph()
#nx.draw_networkx(G)
#plt.show()
