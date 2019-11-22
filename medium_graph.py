import medium_kite as mk
import medium_hamilton as mh
import medium_sparse as ms
import networkx as nx
import matplotlib.pyplot as plt

#return a graph with 86 nodes of 3 different types
def medium_graph():
    G1 = mk.combined_kites()
    G2 = mh.dense_graph()
    G3 = ms.sparse_graph()
    M_G = nx.compose(G1, G2)
    M_G = nx.compose(M_G, G3)
    return M_G

#return a list of 39 homes
def medium_homes():
    home_kite = mk.kite_home()
    home_dense = mh.dense_home()
    home_sparse = ms.sparse_home()
    home_medium = home_kite + home_dense + home_sparse
    return home_medium



#print(M_G.number_of_nodes())
#print(M_G.nodes())
#nx.draw_networkx(M_G)
#plt.show()
