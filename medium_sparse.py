import networkx as nx
import matplotlib.pyplot as plt
import medium_kite as mk
import random as random


# create a balanced tree with 31 vertices -> will pick home locations sparsely in the tree
# label 27 -> 57
def sparse_graph():
    G = nx.balanced_tree(2, 4)
    G = nx.relabel_nodes(G, lambda x: 27 + x)
    return G


# odd nodes are homes, will add more nodes to balance out
def sparse_home():
    sparse_h = []
    for node in range(27, 56):
        if node % 2 == 1:
            sparse_h.append(node)
    return sparse_h

# G = sparse_graph()
# print(G.nodes())
# homes = spare_home(G)
# print(homes)
# print(G.number_of_nodes())
# F = nx.compose(G, H)
# print(F.number_of_nodes())
# nx.draw_networkx(G)
# plt.show()
