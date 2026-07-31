# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that there is a nondeterministic algorithm that can solve the problem in polynomial time.
- NP-hard means that any problem in NP can be reduced to the problem in polynomial time, which means that the problem is at least as hard as any problem in NP.
- NP-complete problems are the hardest problems in NP, and there is no known polynomial time algorithm for them, unless P = NP, which is a major open question in computer science.
- Some examples of NP-complete problems are:
  - Satisfiability problem (SAT): Given a Boolean formula, is there an assignment of truth values to the variables that makes the formula true?
  - Hamiltonian cycle problem: Given a graph, is there a cycle that visits every vertex exactly once?
  - Travelling salesman problem (TSP): Given a set of cities and distances between them, is there a tour that visits every city exactly once and has a total length less than a given value?
  - Graph coloring problem: Given a graph and a number of colors, is there a way to assign a color to each vertex such that no two adjacent vertices have the same color?
  - n-Queen problem: Given a chessboard of size n x n, is there a way to place n queens on the board such that no two queens attack each other?
  - Sum of subsets problem: Given a set of positive integers and a target value, is there a subset of the set that sums up to the target value?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, such as minimizing or maximizing some objective function.
- Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. For minimization problems, the approximation ratio is always greater than or equal to one, and for maximization problems, it is always less than or equal to one.
- The goal of an approximation algorithm is to achieve the best possible approximation ratio in polynomial time, or to prove that no such algorithm exists for a given problem.
- Some examples of approximation algorithms are:
  - 2-approximation algorithm for vertex cover: A vertex cover of a graph is a subset of vertices that covers all the edges, meaning that every edge has at least one endpoint in the subset. The vertex cover problem is to find the minimum size vertex cover of a graph. A 2-approximation algorithm for this problem is to repeatedly pick an arbitrary edge and add both of its endpoints to the vertex cover, until no edges are left. This algorithm runs in linear time and produces a vertex cover that is at most twice as large as the optimal vertex cover.
  - 7/8-approximation algorithm for max 3-SAT: A 3-SAT formula is a Boolean formula that is a conjunction of clauses, where each clause is a disjunction of exactly three literals, which are variables or their negations. The max 3-SAT problem is to find the maximum number of clauses that can be satisfied by an assignment of truth values to the variables. A 7/8-approximation algorithm for this problem is to randomly assign truth values to the variables with equal probability, and then count the number of satisfied clauses. This algorithm runs in linear time and produces an expected number of satisfied clauses that is at least 7/8 of the optimal number.
  - 2-approximation algorithm for TSP: The TSP problem is to find the minimum length tour that visits every city exactly once and returns to the starting city. A 2-approximation algorithm for this problem is to find a minimum spanning tree of the graph, and then traverse the tree in a preorder fashion, skipping any repeated vertices. This algorithm runs in polynomial time and produces a tour that is at most twice as long as the optimal tour.
  - Polynomial-time approximation scheme (PTAS) for knapsack: The knapsack problem is to find the maximum value