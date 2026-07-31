# Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization and decision problems that involve searching a large space of possible solutions. They both use a state-space tree to represent the partial and complete solutions, and they both use a bounding function to prune the tree and eliminate suboptimal or infeasible solutions. However, they differ in the way they explore the tree and the type of problems they can solve.

## Backtracking

Backtracking is an algorithm for finding all solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

Backtracking uses a depth-first search (DFS) method to traverse the state-space tree. When the algorithm begins to explore a solution, it applies a bounding function to check whether the current partial solution satisfies the constraints of the problem. If not, the algorithm backtracks to the previous level and tries another branch. If yes, the algorithm continues to extend the partial solution until it reaches a complete solution or a dead end.

Backtracking can be used to solve problems such as:

- Sudoku
- N-queens
- Hamiltonian cycle
- Graph coloring
- Subset sum
- Cryptarithmetic

## Branch and Bound

Branch and bound is an algorithm for discrete and combinatorial optimization problems and mathematical optimization. It can be used to find optimal solutions (such as minimum or maximum) or to find whether a feasible solution exists.

Branch and bound uses a best-first search (BFS) method to traverse the state-space tree. When the algorithm begins to explore a solution, it applies a bounding function to estimate the lower and upper bounds of the objective function for the current partial solution. If the lower bound is greater than the current best solution, the algorithm prunes the branch and does not explore it further. If the upper bound is less than the current best solution, the algorithm updates the best solution and continues to explore the branch. The algorithm terminates when all branches are pruned or explored.

Branch and bound can be used to solve problems such as:

- 0/1 knapsack
- Travelling salesman
- Job scheduling
- Facility location
- Linear programming

## Examples

### Travelling Salesman Problem

The travelling salesman problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the origin city. It is an NP-hard problem, meaning that there is no known polynomial-time algorithm to solve it exactly.

One way to solve the TSP using branch and bound is to use a minimum spanning tree (MST) as a bounding function. A MST is a subset of edges that connects all the vertices in a graph with the minimum possible total edge weight. A MST can be computed in polynomial time using algorithms such as Prim's or Kruskal's.

The idea is to construct a state-space tree where each node represents a partial tour, and each edge represents the inclusion or exclusion of a city in the tour. The root node represents an empty tour, and the leaf nodes represent complete tours. The algorithm starts from the root node and explores the tree using BFS. For each node, the algorithm computes the lower bound of the tour cost by adding the cost of the partial tour, the cost of the MST of the remaining cities, and the cost of the two edges that connect the partial tour to the MST. If the lower bound is greater than the current best tour cost, the node is pruned. Otherwise, the node is expanded by adding or excluding the next city in the tour. The algorithm updates the best tour cost whenever it finds a complete tour that is better than the current best tour. The algorithm terminates when all nodes are pruned or explored.

The following figure shows an example of the state-space tree for a TSP with four cities A, B, C, and D, and the corresponding MSTs and lower bounds for each node.

![TSP example](https://media.geeksforgeeks.org/wp-content/uploads/20190702124804/Untitled-Diagram-2019-07-02T124724.690.png)

The optimal tour is A-B-C-D-A with a cost of 10 + 25 + 30 + 15 = 80.