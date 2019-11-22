import networkx as nx
import matplotlib.pyplot as plt
import random

def tree_path_graph():
    special = nx.Graph()
    special.add_edge(87, 88)
    special.add_edge(87, 100)
    special.add_edge(87, 91)
    special.add_edge(87, 89)
    special.add_edge(87, 93)

    special.add_edge(89, 90)
    special.add_edge(89, 98)

    special.add_edge(90, 99)
    special.add_edge(91, 97)
    special.add_edge(91, 92)

    special.add_edge(93, 94)
    special.add_edge(94, 95)
    special.add_edge(95, 96)

    special.add_edge(87, 57)
    special.add_edge(96, 57)

    return special

def speical_home():
    special_home = [88, 90, 92, 97, 98, 99, 93, 94, 95, 96, 100]
    return special_home

#G = tree_path_graph()
#nx.draw_networkx(G, with_labels=True)
#plt.show()