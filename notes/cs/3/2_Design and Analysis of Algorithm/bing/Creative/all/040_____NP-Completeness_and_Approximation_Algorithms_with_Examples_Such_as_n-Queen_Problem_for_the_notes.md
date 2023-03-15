# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a concept that deals with the complexity of decision problems, which are problems that have a yes or no answer.
- A decision problem is said to be in NP if it can be verified in polynomial time, given a certificate or a witness for the yes instances. For example, the problem of checking whether a graph has a Hamiltonian cycle is in NP, because given a cycle, we can verify in polynomial time that it visits every vertex exactly once and returns to the starting point.
- A decision problem is said to be NP-hard if every problem in NP can be reduced to it in polynomial time. This means that an NP-hard problem is at least as hard as any problem in NP, and finding a polynomial time algorithm for it would imply finding a polynomial time algorithm for all problems in NP. For example, the problem of finding the maximum independent set in a graph is NP-hard, because we can reduce the problem of finding the maximum clique in a graph to it in polynomial time, by taking the complement of the graph.
- A decision problem is said to be NP-complete if it is both in NP and NP-hard. This means that an NP-complete problem is the hardest problem in NP, and finding a polynomial time algorithm for it would solve the famous P vs NP problem, which asks whether every problem in NP can be solved in polynomial time. For example, the problem of determining whether a Boolean formula in conjunctive normal form is satisfiable is NP-complete, because it is in NP (given a satisfying assignment, we can verify it in polynomial time) and NP-hard (we can reduce any problem in NP to it in polynomial time, using a technique called Cook's theorem).
- Some examples of NP-complete problems are:

  - Travelling Salesman Problem: Given a set of cities and distances between them, find the shortest tour that visits every city exactly once and returns to the starting point.
  - Graph Coloring: Given a graph and a number k, determine whether the vertices of the graph can be colored with k colors such that no two adjacent vertices have the same color.
  - n-Queen Problem: Given a number n, determine whether n queens can be placed on an n x n chessboard such that no two queens attack each other.
  - Hamiltonian Cycle: Given a graph, determine whether it has a cycle that visits every vertex exactly once and returns to the starting point.
  - Sum of Subsets: Given a set of positive integers and a target sum, determine whether there is a subset of the set that adds up to the target sum.

## Approximation Algorithms

- Approximation Algorithms are a way of dealing with NP-completeness for optimization problems, which are problems that seek to find the best solution among a set of feasible solutions. For example, the problem of finding the minimum number of colors needed to color a graph is an optimization problem, because we want to find the best coloring among all possible colorings.
- Approximation Algorithms do not guarantee the best solution, but they aim to find a solution that is close to the optimal solution in polynomial time. For example, an approximation algorithm for the graph coloring problem may find a coloring that uses more colors than the minimum, but not too many more.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the cost of the solution found by the algorithm and the cost of the optimal solution. For example, if an approximation algorithm for the graph coloring problem finds a coloring that uses k colors, and the optimal coloring uses k* colors, then the approximation ratio is k/k*. The smaller the approximation ratio, the better the approximation algorithm.
- Some examples of approximation algorithms are:

  - Travelling Salesman Problem: There is a 2-approximation algorithm for the metric version of the problem, where the distances between the cities satisfy the triangle inequality. The algorithm is based on finding a minimum spanning tree of the cities, and then taking a shortcut tour that visits every city in the order they appear in a preorder traversal of the tree. The cost of the tour is at most twice the cost of the optimal tour, because the cost of the tree is a lower bound on the cost of the optimal tour, and the cost of the shortcut tour is at most twice the cost of the tree.
  - Graph Coloring: There is a simple greedy algorithm that colors the vertices of the graph in any order, assigning each vertex the smallest available color