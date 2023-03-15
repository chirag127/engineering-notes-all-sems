# NP-Completeness and Approximation Algorithms

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for all NP problems, and P = NP.
- Some examples of NP-complete problems are: Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets, etc.
- To prove that a problem is NP-complete, one can use the following steps:
  - Show that the problem is in NP, i.e., given a solution, it can be verified in polynomial time.
  - Choose a known NP-complete problem and show that it can be reduced to the given problem in polynomial time, i.e., given an instance of the known NP-complete problem, it can be transformed into an instance of the given problem in polynomial time, such that the answer is preserved.
- To cope with NP-completeness, one can use the following strategies:
  - Restrict the problem to a special case that is solvable in polynomial time, e.g., bipartite graph coloring, 2-SAT, etc.
  - Use heuristics or approximation algorithms that can find good solutions in polynomial time, but not necessarily the optimal ones.
  - Use exponential time algorithms that can solve small instances of the problem, or use randomized algorithms that can find the optimal solution with high probability.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution found by the algorithm to the cost of the optimal solution. The performance ratio can be either a constant, a function of the input size, or a function of some parameter of the problem. The smaller the performance ratio, the better the approximation algorithm.
- Some examples of approximation algorithms are: 2-approximation algorithm for Vertex Cover, 7/8-approximation algorithm for Max 3-SAT, 2-approximation algorithm for Travelling Salesman Problem, etc.
- To design an approximation algorithm, one can use the following techniques:
  - Greedy method: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to a linear program and round the fractional solution to an integer solution.
  - Randomization: Use random choices to find a good solution with high probability.
  - Local search: Start with a feasible solution and improve it by making local changes.