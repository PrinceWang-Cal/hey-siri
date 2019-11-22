import networkx as nx
import matplotlib.pyplot as plt

#Dense group with many paths but only one is ideal(break dij/sp)
#pick path with both home and normal locations
# label 56 -> 86
def dense_graph():
    G = nx.gnp_random_graph(30, 0.4)
    G = nx.relabel_nodes(G, lambda x: 56 + x);
    return G

G = dense_graph()
print(G.number_of_nodes())
#nx.draw_networkx(G)
#plt.show()
