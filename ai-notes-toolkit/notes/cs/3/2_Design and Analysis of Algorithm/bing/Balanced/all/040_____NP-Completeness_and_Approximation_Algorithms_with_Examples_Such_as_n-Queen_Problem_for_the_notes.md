# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-Completeness is a class of problems that are hard to solve in polynomial time, but easy to verify the correctness of a given solution in polynomial time.
- A problem is NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time. This means that if there is a polynomial time algorithm for any NP-complete problem, then there is a polynomial time algorithm for every problem in NP.
- Some examples of NP-complete problems are: 3-SAT, Clique, Vertex Cover, Subset Sum, Hamiltonian Cycle, Travelling Salesman Problem, etc.
- To prove that a problem is NP-complete, we need to show two things:
  - The problem is in NP, i.e., there is a polynomial time algorithm to verify a given solution.
  - The problem is NP-hard, i.e., there is a polynomial time reduction from any other problem in NP to this problem.
- To show that a problem is NP-hard, we can use the technique of reduction. This means that we can transform an instance of a known NP-hard problem into an instance of the problem we want to prove NP-hard, such that the answer is preserved. For example, we can reduce 3-SAT to Clique by constructing a graph where each vertex represents a literal and each edge represents a clause, and finding a k-clique in this graph is equivalent to finding a satisfying assignment for the 3-SAT formula.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem. This technique does not guarantee the best solution. The goal of the approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- An approximation algorithm has a performance ratio, which is the ratio of the cost of the solution produced by the algorithm to the cost of the optimal solution. For example, if the optimal solution has a cost of 100 and the algorithm produces a solution with a cost of 120, then the performance ratio is 120/100 = 1.2. The smaller the performance ratio, the better the approximation.
- Some examples of approximation algorithms are: 2-approximation for Vertex Cover, 7/8-approximation for Max 3-SAT, 2-approximation for Travelling Salesman Problem with triangle inequality, etc.
- To design an approximation algorithm, we can use different techniques, such as:
  - Greedy: Choose the best option at each step, without looking ahead.
  - Rounding: Relax the problem to make it easier to solve, and then round the solution to make it feasible.
  - Randomization: Use random choices to explore different possibilities and avoid getting stuck in local optima.
  - Linear Programming: Formulate the problem as a linear program, and then use the optimal solution of the linear program as a guide to construct a feasible solution for the original problem.

## Examples of NP-Complete Problems and Approximation Algorithms

### Travelling Salesman Problem (TSP)

- The Travelling Salesman Problem is to find the shortest tour that visits every city in a given set of cities and returns to the starting city.
- The TSP is NP-complete, as we can reduce Hamiltonian Cycle to it by assigning a unit distance to every edge in the graph and finding the shortest tour in the resulting metric space.
- A 2-approximation algorithm for TSP with triangle inequality is to find a minimum spanning tree of the cities, and then traverse the tree in a preorder fashion, skipping any repeated cities. The cost of this tour is at most twice the cost of the optimal tour, as the cost of the tree is a lower bound on the optimal tour, and the cost of the preorder traversal is at most twice the cost of the tree.

### Graph Coloring

- The Graph Coloring problem is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color, and the number of colors used is minimized.
- The Graph Coloring problem is NP-complete, as we can reduce 3-SAT to it by constructing a graph where each vertex represents a literal and each edge represents a clause, and finding a 3-coloring of this graph is equivalent to finding a satisfying assignment for the 3-SAT formula.
- A simple approximation algorithm for Graph Coloring is to order the vertices in some arbitrary way, and then assign the smallest available color to each vertex