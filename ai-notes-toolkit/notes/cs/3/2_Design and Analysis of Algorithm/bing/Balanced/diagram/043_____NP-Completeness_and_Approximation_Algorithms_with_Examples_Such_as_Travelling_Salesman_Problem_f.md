# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP problems, and P = NP.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To prove that a problem is NP-complete, we need to show two things: (1) the problem is in NP, and (2) there is a polynomial time reduction from a known NP-complete problem to the problem.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems. They do not guarantee the best solution, but they try to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution produced by the algorithm to the cost of the optimal solution. The smaller the ratio, the better the approximation.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, we need to find a way to relax the problem constraints, exploit some structure or property of the problem, or use some heuristic or greedy strategy.