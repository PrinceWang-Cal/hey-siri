import networkx as nx
import matplotlib.pyplot as plt


# label 0 -> 25
# kite prevent path finding method

# construct a standard kite shape by hand (12 - 22)
def det_kite():
    G_kite1 = nx.Graph()
    G_kite1.add_edge(12, 13)
    G_kite1.add_edge(13, 14)
    G_kite1.add_edge(13, 15)
    G_kite1.add_edge(14, 17)
    G_kite1.add_edge(14, 16)
    G_kite1.add_edge(16, 18)
    G_kite1.add_edge(15, 17)
    G_kite1.add_edge(14, 19)
    G_kite1.add_edge(19, 20)
    G_kite1.add_edge(19, 21)
    G_kite1.add_edge(19, 22)
    return G_kite1


# modify krackhardt to reduce cycle
def modified_kite():
    G1 = nx.krackhardt_kite_graph()
    G1.remove_edge(1, 4)
    G1.remove_edge(0, 2)
    G1.remove_edge(1, 6)
    G1.remove_edge(4, 6)
    G1.remove_edge(1, 0)
    G1.remove_edge(2, 5)
    return G1


def combined_kites():
    G_kite1 = det_kite()
    G_kite2 = modified_kite()
    F = nx.compose(G_kite1, G_kite2)

    # add edges to connect two kites
    F.add_edge(11, 16)
    F.add_edge(10, 7)
    F.add_edge(14, 6)

    # add up to 25
    F.add_edge(23, 14)
    F.add_edge(23, 6)
    F.add_edge(24, 18)
    F.add_edge(25, 15)

    # connect 23 to 57
    F.add_edge(23, 57)

    return F


# the nodes in kite that are homes
def kite_home():
    kite_h = [1, 2, 4, 9, 10, 11, 12, 15, 20, 21, 22, 24, 15]
    return kite_h

# nx.draw_networkx(combined_kites(), with_labels=True)
# plt.show()
