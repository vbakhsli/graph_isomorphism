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

