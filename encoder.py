def variable(i, j, n):
    return i * n + j + 1

def bijection(n):
    # all clauses so that each vertex of g maps to one vertex of h 
    clauses = []

    for i in range(n):
        clause = []

        for j in range(n):
            x = variable(i, j, n)
            clause.append(x)

        clauses.append(clause)
        
    # each vertex of h receives a mapping
    for j in range(n):
        clause = []

        for i in range(n):
            x = variable(i, j, n)
            clause.append(x)
        clauses.append(clause)

    return clauses

