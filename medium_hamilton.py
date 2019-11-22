import networkx as nx
import matplotlib.pyplot as plt
import random

#Dense group with many paths but only one is ideal(break dij/sp)
#pick path with both home and normal locations
# label 56 -> 85
def dense_graph():
    G = nx.gnp_random_graph(30, 0.4)
    G = nx.relabel_nodes(G, lambda x: 57 + x)
    return G
#pick ten locations as home, remember to disconnect home and add shortest paths
def dense_home():
    dense_home = []
    for i in range(10):
       dense_home.append(random.randint(56, 85))
    return dense_home

#G = dense_graph()
#print(G.nodes())
#nx.draw_networkx(G)
#plt.show()
