# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of decision problems that are both in NP and NP-hard.
- NP stands for nondeterministic polynomial time, which means that there is a nondeterministic algorithm that can solve the problem in polynomial time.
- NP-hard means that any problem in NP can be reduced to the problem in polynomial time, which means that the problem is at least as hard as any problem in NP.
- NP-complete problems are the hardest problems in NP, and there is no known polynomial time algorithm to solve them, unless P = NP, which is a major open question in computer science.
- Some examples of NP-complete problems are:

  - Satisfiability problem (SAT): Given a Boolean formula, is there an assignment of truth values to the variables that makes the formula true?
  - Clique problem: Given a graph and a number k, is there a subset of k vertices that are all adjacent to each other?
  - Subset sum problem: Given a set of integers and a target sum, is there a subset of the integers that adds up to the target sum?
  - Travelling salesman problem (TSP): Given a set of cities and the distances between them, is there a tour that visits each city exactly once and has a total length less than a given limit?
  - Hamiltonian cycle problem: Given a graph, is there a cycle that visits each vertex exactly once?
  - Graph coloring problem: Given a graph and a number k, is there a way to assign k colors to the vertices such that no two adjacent vertices have the same color?
  - n-Queen problem: Given a number n, is there a way to place n queens on an n x n chessboard such that no two queens attack each other?

## Approximation Algorithms

- Approximation algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among many possible solutions, such as finding the minimum or maximum of some objective function.
- Approximation algorithms do not guarantee the optimal solution, but they aim to find a solution that is close to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the value of the solution found by the algorithm and the value of the optimal solution. For minimization problems, the approximation ratio is always greater than or equal to one, and for maximization problems, it is always less than or equal to one.
- The goal of an approximation algorithm is to achieve the best possible approximation ratio, or to prove that no polynomial time algorithm can achieve a better approximation ratio, unless P = NP.
- Some examples of approximation algorithms are:

  - 2-approximation algorithm for vertex cover: A vertex cover of a graph is a subset of vertices that covers all the edges, meaning that every edge has at least one endpoint in the subset. The vertex cover problem is to find the minimum size vertex cover of a graph. A 2-approximation algorithm for this problem is to find a maximal matching of the graph, which is a subset of edges that do not share any endpoints, and then take the endpoints of the matching as the vertex cover. This algorithm runs in polynomial time and guarantees that the size of the vertex cover is at most twice the size of the optimal vertex cover.
  - 7/8-approximation algorithm for max 3-SAT: A 3-SAT formula is a Boolean formula that is a conjunction of clauses, where each clause is a disjunction of exactly three literals, which are variables or their negations. The max 3-SAT problem is to find the maximum number of clauses that can be satisfied by an assignment of truth values to the variables. A 7/8-approximation algorithm for this problem is to assign each variable randomly with probability 1/2, and then count the number of satisfied clauses. This algorithm runs in polynomial time and guarantees that the expected number of satisfied clauses is at least 7/8 of the optimal number of satisfied clauses.
  - 2-approximation algorithm for travelling salesman problem: The travelling salesman problem is to find the minimum length tour that visits each city exactly once and returns to the starting city. A 2-approximation algorithm for this problem is to find a minimum spanning tree of the graph, which is a subset of edges that connects all the vertices with the