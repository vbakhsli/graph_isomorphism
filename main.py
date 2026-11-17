import graph

graphs = graph.read_graph("examples/triangle.txt")

g = graphs[0]
h = graphs[1]

print("vertices:", g.n)
print("edges:", g.edges)