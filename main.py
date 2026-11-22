import graph
import encoder
import solver

graphs = graph.read_graph("examples/test1.txt")

g = graphs[0]
h = graphs[1]
n = g.n
# print("vertices:", g.n)
# print("edges:", g.edges)

# print(encoder.variable(0, 0, 3))

# clauses = encoder.bijection(3)

# for clause in clauses:
#     print(clause)
# print(len(clauses))

clauses = encoder.encode(g, h)

# print(g.n * h.n)
# for clause in clauses:
#     print(clause)

# import solver

# clauses = [[1, 2], [-1, 2]]
output = solver.solve(clauses, g.n)
if "s SATISFIABLE" in output:
    print("Graphs are isomorphic")

    for line in output.splitlines():
        if line.startswith("v "):
            numbers = line.split()

            for number in numbers[1:]:
                x = int(number)

                if x > 0:
                    i = (x - 1) // n
                    j = (x - 1) % n
                    print(i, "->", j)
else:
    print("Graphs are not isomorphic")


