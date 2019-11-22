import medium_kite as mk
import medium_hamilton as mh
import medium_sparse as ms
import networkx as nx
import matplotlib.pyplot as plt

G1 = mk.combined_kites()
G2 = mh.dense_graph()
G3 = ms.sparse_graph()
M_G = nx.compose(G1, G2)
M_G = nx.compose(M_G, G3)

print(M_G.number_of_nodes())
print(M_G.nodes())
nx.draw_networkx(M_G)
plt.show()
