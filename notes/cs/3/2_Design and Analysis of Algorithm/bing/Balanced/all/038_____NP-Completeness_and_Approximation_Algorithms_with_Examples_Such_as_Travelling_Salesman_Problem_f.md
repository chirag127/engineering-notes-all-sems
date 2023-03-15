# NP-Completeness and Approximation Algorithms with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## NP-Completeness

- NP-completeness is a concept that relates to the difficulty of solving certain problems in polynomial time.
- A problem is said to be in NP if it can be verified in polynomial time, given a possible solution.
- A problem is said to be NP-complete if it is in NP and every other problem in NP can be reduced to it in polynomial time.
- NP-complete problems are the hardest problems in NP, and it is widely believed that there is no polynomial time algorithm for them.
- Some examples of NP-complete problems are: satisfiability, vertex cover, clique, subset sum, traveling salesman problem, etc.

## Approximation Algorithms

- An approximation algorithm is a way of dealing with NP-completeness for an optimization problem.
- This technique does not guarantee the best solution, but rather a solution that is close to the optimal one, within some error bound.
- The goal of an approximation algorithm is to come as close as possible to the optimal solution in polynomial time.
- The quality of an approximation algorithm is measured by its approximation ratio, which is the ratio between the cost of the solution produced by the algorithm and the cost of the optimal solution.
- Some examples of approximation algorithms are: greedy algorithm, local search, randomized algorithm, etc.

## Examples of NP-Complete Problems and Approximation Algorithms

### Travelling Salesman Problem

- The travelling salesman problem (TSP) is to find the shortest tour that visits every city in a given set of cities and returns to the starting city.
- The TSP is NP-complete, and there is no polynomial time algorithm that can find the optimal tour.
- One approximation algorithm for the TSP is the nearest neighbor algorithm, which starts from a random city and repeatedly visits the nearest unvisited city until all cities are visited.
- The nearest neighbor algorithm has an approximation ratio of 2, which means that the cost of the tour produced by the algorithm is at most twice the cost of the optimal tour.

### Graph Coloring

- The graph coloring problem is to assign colors to the vertices of a graph such that no two adjacent vertices have the same color, using the minimum number of colors.
- The graph coloring problem is NP-complete, and there is no polynomial time algorithm that can find the optimal coloring.
- One approximation algorithm for the graph coloring problem is the greedy algorithm, which assigns colors to the vertices in some order, using the first available color that does not conflict with any previously colored neighbor.
- The greedy algorithm has an approximation ratio of ∆ + 1, where ∆ is the maximum degree of the graph, which means that the number of colors used by the algorithm is at most ∆ + 1 times the number of colors used by the optimal coloring.

### n-Queen Problem

- The n-queen problem is to place n queens on an n x n chessboard such that no two queens attack each other, i.e., no two queens share the same row, column, or diagonal.
- The n-queen problem is NP-complete, and there is no polynomial time algorithm that can find a valid placement of the queens.
- One approximation algorithm for the n-queen problem is the backtracking algorithm, which tries to place a queen in each row, starting from the first row, and recursively explores the possible positions for the remaining queens, backtracking if a conflict occurs.
- The backtracking algorithm has an approximation ratio of 1, which means that it always finds a valid placement of the queens, if one exists.

### Hamiltonian Cycles

- A Hamiltonian cycle is a cycle that visits every vertex of a graph exactly once and returns to the starting vertex.
- The Hamiltonian cycle problem is to determine whether a given graph has a Hamiltonian cycle or not.
- The Hamiltonian cycle problem is NP-complete, and there is no polynomial time algorithm that can solve it.
- One approximation algorithm for the Hamiltonian cycle problem is the Christofides algorithm, which works for graphs that are complete and have non-negative edge weights.
- The Christofides algorithm first finds a minimum spanning tree of the graph, then adds the minimum weight matching of the odd degree vertices of the tree, and finally shortcuts the resulting Eulerian cycle to obtain a Hamiltonian cycle.
- The Christofides algorithm has an approximation ratio of 3/2, which means that the cost of the cycle produced by the algorithm is at most 3/2 times the cost of the optimal cycle.

### Sum of Sub