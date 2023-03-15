# Unit 5 - NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets

## NP-Completeness

- NP-Completeness is a class of problems in computational complexity theory.
- A problem is NP-Complete if it is both in NP (Nondeterministic Polynomial time) and NP-Hard.
- NP problems are problems for which a proposed solution can be verified in polynomial time.
- NP-Hard problems are problems that are at least as hard as the hardest problems in NP.
- The most famous NP-Complete problem is the Boolean Satisfiability Problem (SAT).

## Approximation Algorithms

- Approximation algorithms are algorithms used to find approximate solutions to optimization problems.
- These algorithms are used when finding an exact solution is computationally infeasible.
- Approximation algorithms have a guaranteed performance ratio, which is the ratio of the cost of the solution produced by the algorithm to the cost of the optimal solution.
- Common techniques for designing approximation algorithms include greedy algorithms, linear programming, and dynamic programming.

## n-Queen Problem

- The n-Queen problem is the problem of placing n queens on an n×n chessboard such that no two queens threaten each other.
- This problem can be solved using backtracking, which is a form of depth-first search.
- The time complexity of this algorithm is O(n!) as there are n! permutations of the queens.
- There are also other algorithms that can solve the n-Queen problem, such as genetic algorithms and simulated annealing.

## Travelling Salesman Problem

- The Travelling Salesman Problem (TSP) is the problem of finding the shortest possible route that visits a given set of cities and returns to the starting city.
- TSP is an NP-Hard problem.
- There are several approximation algorithms for TSP, such as the nearest neighbor algorithm and the Christofides algorithm.
- The nearest neighbor algorithm has a performance ratio of 2, while the Christofides algorithm has a performance ratio of 3/2.

## Graph Coloring

- Graph coloring is the problem of assigning colors to the vertices of a graph such that no two adjacent vertices share the same color.
- This problem can be solved using backtracking, which is a form of depth-first search.
- The time complexity of this algorithm is O(n^m) where n is the number of vertices and m is the number of colors.
- There are also other algorithms that can solve the graph coloring problem, such as greedy algorithms and genetic algorithms.

## Hamiltonian Cycles

- A Hamiltonian cycle is a cycle in a graph that visits each vertex exactly once.
- The problem of finding a Hamiltonian cycle in a graph is NP-Complete.
- There are several algorithms that can find Hamiltonian cycles in special classes of graphs, such as bipartite graphs and chordal graphs.
- There are also approximation algorithms for finding Hamiltonian cycles in general graphs, such as the greedy algorithm and the Christofides algorithm.

## Sum of Subsets

- The Sum of Subsets problem is the problem of finding a subset of a given set of integers that adds up to a given target sum.
- This problem can be solved using dynamic programming, which has a time complexity of O(nW) where n is the number of integers and W is the target sum.
- There are also other algorithms that can solve the Sum of Subsets problem, such as backtracking and branch and bound.
