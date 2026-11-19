def variable(i, j, n):
    return i * n + j + 1

def bijection(n):
    # all clauses so that each vertex of g maps to at least one vertex of h 
    clauses = []

    for i in range(n):
        clause = []

        for j in range(n):
            x = variable(i, j, n)
            clause.append(x)

        clauses.append(clause)

    # each vertex of h receives at least a mapping
    for j in range(n):
        clause = []

        for i in range(n):
            x = variable(i, j, n)
            clause.append(x)
        clauses.append(clause)

    # each vertex of g maps to at most one vertex of h
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j < k: # prevent same vertex and duplicates
                    x = variable(i, j, n)
                    y = variable(i, k, n)
                    clauses.append([-x, -y])

    # each vertex of h receives at most one vertex of g
    for j in range(n):
        for i in range(n):
            for k in range(n):
                if i < k:
                    x = variable(i, j, n)
                    y = variable(k, j, n)
                    clauses.append([-x, -y])
    
    return clauses

def encode(graph1, graph2):
    n = graph1.n
    clauses = bijection(n)
    # if graphs have different # of edges, not isomorphic
    if len(graph1.edges) != len(graph2.edges):
        clauses.append([])
        return clauses
    # if graphs have different # of vertices, not isomorphic
    if graph1.n != graph2.n:
        clauses.append([])
        return clauses
    
    # preserving edges
    for edge in graph1.edges:
        i = edge[0]
        j = edge[1]

        for k in range(n):
            for l in range(k + 1, n):
                if not graph2.has_edge(k, l):
                    x = variable(i, k, n)
                    y = variable(j, l, n)

                    clauses.append([-x, -y])

                    x = variable(i, l, n)
                    y = variable(j, k, n)
                    clauses.append([-x, -y])
    return clauses