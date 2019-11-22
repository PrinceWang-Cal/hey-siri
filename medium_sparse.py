import networkx as nx
import matplotlib.pyplot as plt
import medium_kite as mk

# create a balanced tree with 31 vertices -> will pick home locations sparsely in the tree
# label 26 -> 56
def sparse_graph():
    G = nx.balanced_tree(2, 5)
    G = nx.relabel_nodes(G, lambda x: 26 + x);
    return G


#print(G.number_of_nodes())
#F = nx.compose(G, H)
#print(F.number_of_nodes())
#nx.draw_networkx(F)
#plt.show()