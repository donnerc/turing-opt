import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

vertices = [
(50, 4), (26, 4), (37, 4), (13, 4), (24, 4), (11, 4), (0, 4), (37, 1), (50, 1), (50, 0), (50, 3), (50, 2), (37, 2), (37, 3), (24, 3), (24, 2), (11, 3)
]
vertices = [f"S{t}" for t in vertices]

vert_lists = [
    ["S(50, 4)", "S(50, 3)", "S(50, 2)", "S(50, 1)", "S(50, 0)"], 
    ["S(26, 4)", "S(50, 3)"], 
    ["S(37, 4)", "S(37, 3)", "S(37, 2)", "S(37, 1)", "S(50, 0)"], 
    ["S(13, 4)", "S(37, 3)"], 
    ["S(24, 4)", "S(24, 3)", "S(37, 2)", "S(50, 1)"], 
    ["S(0, 4)", "S(24, 3)"], 
    ["S(24, 3)", "S(24, 2)", "S(37, 1)"], 
    ["S(11, 4)", "S(11, 3)", "S(24, 2)"], 
]

all_edges = set()
for vert_list in vert_lists:
    edge_list = list(zip(vert_list, vert_list[1:] + vert_list[0:1]))
    for edge in edge_list:
        all_edges |= {edge}
    
print(all_edges)
    

G = nx.DiGraph(all_edges)
PG = nx.nx_pydot.to_pydot(G)
print(PG)
