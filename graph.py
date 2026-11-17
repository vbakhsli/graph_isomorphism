class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.edges = edges

    def has_edge(self, u, v):
        if (u, v) in self.edges:
            return True
        elif (v, u) in self.edges:
            return True
        return False

def read_graph(filename):
    file = open(filename, "r")

    lines = file.read().strip().split("\n\n")
    file.close()

    graphs = []

    for part in lines:
        rows = part.strip().split("\n")

        n = int(rows[0])

        edges = []

        for row in rows[1:]:
            numbers = row.split()
            u = int(numbers[0])
            v = int(numbers[1])

            edges.append((u,v))

        graph = Graph(n, edges)
        graphs.append(graph)

    return graphs
