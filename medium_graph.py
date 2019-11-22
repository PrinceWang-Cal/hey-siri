import medium_kite as mk
import medium_hamilton as mh
import medium_sparse as ms
import networkx as nx
import medium_known_optimal as mo
import matplotlib.pyplot as plt
import random


# return a graph with 100 nodes of 4 different types with sharing node *57* -> soda, and its homes
def medium_graph():
    G1 = mk.combined_kites()
    G2 = mh.dense_graph()
    G3 = ms.sparse_graph()
    G4 = mo.tree_path_graph()
    M_G = nx.compose(G1, G2)
    M_G = nx.compose(M_G, G3)
    M_G = nx.compose(M_G, G4)
    M_homes = medium_homes()

    return M_G, M_homes


# return a list of 49 homes
def medium_homes():
    home_kite = mk.kite_home()
    home_dense = mh.dense_home()
    home_sparse = ms.sparse_home()
    home_special = mo.speical_home()
    home_medium = home_kite + home_dense + home_sparse + home_special
    return home_medium


"""def add_distraction(G, list_of_homes):
    # connect 87 with some non-home locations in 3 graphs
    all_nodes = list(G.nodes())
    non_home_locs = [loc for loc in all_nodes if loc not in list_of_homes]
    add_edge_to_nodes = []
    for i in range(6):
        index = random.randint(0, len(non_home_locs) -1)
        picked_loc = non_home_locs[index]
        G.add_edge(87, picked_loc)
        add_edge_to_nodes.append(picked_loc)
    return add_edge_to_nodes """

M_G = medium_graph()
homes = medium_homes()
# print(M_G.nodes())
print(M_G.number_of_nodes())
print(len(homes))
# nx.draw_networkx(M_G)
# plt.show()
