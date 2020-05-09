from igraph import Graph, plot
from grammar import grammar

g = Graph(directed=True)

g.add_vertices(len(grammar))
for index, (key, value) in enumerate(grammar.items()):
    g.vs[index]["name"] = key

for index, (key, value) in enumerate(grammar.items()):
    edges = []
    for rule in value[1]:
        for node in rule:
            if node[:2] != 'tk' and node[:2] != 'e':
                edges.append((index, g.vs.find(name=node).index))
    g.add_edges(edges)
n_vertices = len(grammar)
ts = g.topological_sorting()
print(ts)
visual_style = {}
visual_style["vertex_size"] = 100
visual_style["vertex_label"] = g.vs["name"]
visual_style["layout"] = g.layout("rt")
visual_style["bbox"] = (2000, 2000)
visual_style["margin"] = 200
visual_style["edge_curved"] = 0.2
visual_style["edge_width"] = 2
visual_style["edge_width"] = 2
plot(g, "grammar_tree.svg", **visual_style)

# g.add_edges([()])

# g = Graph([(0,1), (0,2), (2,3), (3,4), (4,2), (2,5), (5,0), (6,3), (5,6)])
# g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
# g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
# g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
# g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

