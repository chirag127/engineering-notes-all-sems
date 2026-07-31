# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that a problem is in NP if there is a polynomial time algorithm that can verify a solution given a certificate (or a hint).
- NP-hard means that a problem is at least as hard as any problem in NP, which means that there is no polynomial time algorithm that can solve it unless P = NP.
- P is the class of decision problems that can be solved in polynomial time by a deterministic algorithm.
- The question of whether P = NP is one of the most important open problems in computer science and mathematics.
- If P = NP, then every problem in NP can be solved in polynomial time by a deterministic algorithm, and NP-Completeness becomes irrelevant.
- If P ≠ NP, then there are problems in NP that cannot be solved in polynomial time by any algorithm, and NP-Completeness is a way of identifying such problems.
- A problem is NP-complete if it is both in NP and NP-hard, which means that it is as hard as any problem in NP, and that any problem in NP can be reduced to it in polynomial time.
- A reduction is a way of transforming one problem into another problem, such that solving the second problem also solves the first problem.
- A polynomial time reduction is a reduction that can be done by a polynomial time algorithm.
- If a problem A can be reduced to a problem B in polynomial time, then A is no harder than B, and B is at least as hard as A.
- If a problem B is NP-complete, then any problem A that can be reduced to B in polynomial time is also NP-complete, because A is both in NP and NP-hard.
- To prove that a problem is NP-complete, it is sufficient to show that it is in NP and that it can be reduced from a known NP-complete problem in polynomial time.
- Some examples of NP-complete problems are:

  - SAT: Given a Boolean formula in conjunctive normal form (CNF), is there an assignment of truth values to the variables that satisfies the formula?
  - 3-SAT: Given a Boolean formula in CNF where each clause has exactly three literals, is there an assignment of truth values to the variables that satisfies the formula?
  - Clique: Given a graph and a positive integer k, is there a subset of k vertices that are all adjacent to each other (a clique)?
  - Vertex Cover: Given a graph and a positive integer k, is there a subset of k vertices that covers all the edges (a vertex cover)?
  - Hamiltonian Cycle: Given a graph, is there a cycle that visits every vertex exactly once (a Hamiltonian cycle)?
  - Travelling Salesman Problem (TSP): Given a set of n cities and a distance matrix, is there a tour that visits every city exactly once and has a total length at most k?
  - Subset Sum: Given a set of n positive integers and a target sum t, is there a subset of the integers that adds up to t?
  - Graph Coloring: Given a graph and a positive integer k, is there a way of assigning k colors to the vertices such that no two adjacent vertices have the same color (a k-coloring)?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, where the goal is to find the best solution among a set of feasible solutions.
- Optimization problems can be either minimization problems, where the goal is to minimize an objective function, or maximization problems, where the goal is to maximize an objective function.
- An approximation algorithm is a polynomial time algorithm that produces a feasible solution that is close to the optimal solution in some measure.
- The measure of closeness is usually the approximation ratio, which is the ratio between the value of the solution produced by the algorithm and the value of the optimal solution.
- For minimization problems, the approximation ratio is the value of the algorithm solution divided by the value of the optimal solution, and for maximization problems, it is the value of the optimal solution divided by the value of the algorithm solution.
- The approximation ratio is always at least 1, and the closer it is to 1, the better the approximation is.
- An approximation algorithm is called an α-approximation algorithm if it guarantees an approximation ratio of