# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that a problem is in NP if there is a polynomial time algorithm that can verify a solution given a certificate (or a hint).
- NP-hard means that a problem is at least as hard as any problem in NP, which means that there is a polynomial time reduction from any NP problem to the NP-hard problem.
- A reduction is a way of transforming one problem into another problem, such that solving the second problem also solves the first problem.
- NP-Completeness is important because it shows the limits of efficient computation. If P ≠ NP, then there is no polynomial time algorithm for any NP-complete problem, unless there is a polynomial time algorithm for all NP problems.
- Some examples of NP-complete problems are:

  - SAT: Given a boolean formula in conjunctive normal form, is there an assignment of truth values to the variables that satisfies the formula?
  - 3-SAT: Same as SAT, but the formula is restricted to have clauses of exactly three literals.
  - Clique: Given a graph and a positive integer k, is there a subset of k vertices that are all adjacent to each other?
  - Vertex Cover: Given a graph and a positive integer k, is there a subset of k vertices that covers all the edges, i.e., every edge has at least one endpoint in the subset?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits every vertex exactly once?
  - Travelling Salesman Problem: Given a set of cities and distances between them, is there a tour that visits every city exactly once and has total length at most k?
  - Graph Coloring: Given a graph and a positive integer k, is there a way to assign k colors to the vertices such that no two adjacent vertices have the same color?
  - n-Queen Problem: Given a positive integer n, is there a way to place n queens on an n x n chessboard such that no two queens attack each other?
  - Sum of Subsets: Given a set of positive integers and a target sum, is there a subset of the set that adds up to the target sum?

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution.
- The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For a minimization problem, the approximation ratio is the maximum over all instances of the problem of the ratio between the algorithm's solution and the optimal solution. For a maximization problem, the approximation ratio is the minimum over all instances of the problem of the ratio between the algorithm's solution and the optimal solution.
- An approximation algorithm is called an α-approximation algorithm if its approximation ratio is at most α for a minimization problem, or at least α for a maximization problem.
- Some examples of approximation algorithms are:

  - 2-Approximation Algorithm for Vertex Cover: Given a graph G, find a maximal matching M, i.e., a set of disjoint edges. Then, output the set of vertices that are endpoints of the edges in M. This set is a vertex cover of size at most 2 times the optimal size, because every edge in the graph is covered by at most two vertices in the set, and every edge in the optimal vertex cover is also in the matching.
  - 7/8-Approximation Algorithm for 3-SAT: Given a 3-SAT formula F, randomly assign truth values to the variables with equal probability. Then, output the assignment. This assignment satisfies at least 7/8 of the clauses in expectation, because for each clause, the probability that it is satisfied is 7/8, and the expected number of satisfied clauses is the sum of the probabilities over all clauses.
  - 2-Approximation Algorithm for Travelling Salesman Problem: Given a set of cities and distances between them, find a minimum spanning tree T of the complete graph on the cities. Then, output a tour that follows the preorder traversal of T, i.e., visit