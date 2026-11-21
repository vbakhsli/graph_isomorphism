# import graph
# import encoder

# graphs = graph.read_graph("examples/test1.txt")

# g = graphs[0]
# h = graphs[1]

# print("vertices:", g.n)
# print("edges:", g.edges)

# print(encoder.variable(0, 0, 3))

# clauses = encoder.bijection(3)

# for clause in clauses:
#     print(clause)
# print(len(clauses))

# clauses = encoder.encode(g, h)

# print(g.n * h.n)
# for clause in clauses:
#     print(clause)

import solver

clauses = [[1, 2], [-1, 2]]
print(solver.solve(clauses, 2))
