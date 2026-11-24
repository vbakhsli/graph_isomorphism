import sys
import graph
import encoder
import solver

input = sys.argv[1]
graphs = graph.read_graph(input)

g = graphs[0]
h = graphs[1]
n = g.n

clauses = encoder.encode(g, h)

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


