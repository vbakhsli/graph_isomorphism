import subprocess


def solve(clauses, n):
    with open("formula.cnf", "w") as file:
        header = "p cnf" + str(n * n) + " " + str(len(clauses))
        file.write(header)

        for clause in clauses:
            for literal in clause:
                file.write(str(literal) + " ")

            file.write("0\n")


    result = subprocess.run(["./glucose/simp/glucose", "-model", "formula.cnf"],
                            capture_output=True,
                            text=True)
    
    return result.stdout


