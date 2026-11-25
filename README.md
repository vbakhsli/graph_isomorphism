Graph Isomorphism using SAT

This project solves Graph Isomorphism problem using Glucose SAT solver.

Program takes two undirected graphs, then converts the problem into boolean formula
in DIMACS CNF format. 
Then uses Glucose solver to decide whether the grapsh are isomorphic or not.

If they are isomorphic, proram prints mappings between their vertices.


1. Problem Description

Two graphs are isomorphic if there exists a bijection:
f:V_G => V_H such that for every pair of vertices u, v:
{u, v} in G iff {f(u), f(v)} is in H

Given two graphs G and H, we want to find a one-to-one mapping between their vertices that preserves all edges.

The answer is either YES (isomorphic) or NO (not isomorphic).

2. SAT Encoding

We use Boolean variables x_i,j where:
x_i,j = 1 means vertex i of G maps to vertex j of H.
x_i,j = 0 means it does not.
The encoding has five main rules:
Every vertex of G must map to a vertex of H.
Every vertex of H must receive a vertex of G.
A vertex cannot map to two different vertices.
Two vertices cannot map to the same vertex.
Edges and non-edges must be preserved.

These rules make sure the mapping is a bijection.

If the graphs have different numbers of vertices or edges, they cannot be isomorphic.

The clauses are written manually in DIMACS CNF format.

3. Project Structure

graph_isomorphism/
--- main.py
--- graph.py
--- encoder.py
--- solver.py
--- examples/
--- glucose/
--- README.md
--- .gitignore


main.py – runs the program.
graph.py – reads and stores graphs.
encoder.py – creates SAT clauses.
solver.py – runs Glucose and gets the result.
examples/ – contains test graphs.

4. Input and Use

Each input file contains two graphs separated by an empty line.

The first line is the number of vertices, then the edges.

Example:
3
0 1
1 2

3
0 2
1 2


To run the program:
python3 main.py examples/test*.txt


If the graphs are isomorphic, the program prints, for example:
Graphs are isomorphic
0 -> 0
1 -> 2
2 -> 1


If not:
Graphs are not isomorphic

5. Experiments

I tested the program on small examples, and all got correct results.

I also created a bigger example with 12 vertices and 16 edges.

To check the running time, I used:
time python3 main.py examples/large_test.txt


The program took only 0.029 seconds.