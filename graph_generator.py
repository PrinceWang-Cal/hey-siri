import large_graph as lg
import medium_graph as mg


# generate medium graph
def gen_medium_graph():
    medium_g = mg.medium_graph()[0]
    return medium_g


# generate medium homes
def gen_medium_homes():
    medium_h = mg.medium_graph()[1]
    return medium_h


# generate large graph
def gen_large_graph():
    large_g = lg.large_graph()[0]
    return large_g


# generate large homes
def gen_large_homes():
    large_h = lg.large_graph()[1]
    return large_h
