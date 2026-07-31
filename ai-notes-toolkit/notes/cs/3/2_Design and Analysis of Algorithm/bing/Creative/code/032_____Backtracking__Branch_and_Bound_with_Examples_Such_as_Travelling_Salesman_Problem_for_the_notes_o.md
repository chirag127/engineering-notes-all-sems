### Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem

Backtracking and branch and bound are two techniques for solving optimization problems, such as finding the shortest path, the minimum cost, the maximum profit, etc. They both use a tree-like structure to explore the possible solutions, but they differ in how they prune the branches that are not promising.

Backtracking is a technique that tries to find a feasible solution by recursively generating partial candidates and testing them against some constraints. If a partial candidate is found to be invalid, the algorithm backtracks to the previous level and tries another option. Backtracking can be used to solve problems that have a finite number of possible solutions, such as the n-queen problem, the graph coloring problem, the Hamiltonian cycle problem, etc.

Branch and bound is a technique that tries to find an optimal solution by maintaining a lower bound and an upper bound on the objective function. The algorithm starts with a root node that represents the entire problem, and then generates child nodes that represent subproblems. The algorithm evaluates each node by computing a lower bound and an upper bound on the objective function, and then discards the nodes that cannot lead to a better solution than the current best one. Branch and bound can be used to solve problems that have a continuous or discrete solution space, such as the travelling salesman problem, the knapsack problem, the sum of subsets problem, etc.

#### Travelling Salesman Problem

The travelling salesman problem (TSP) is a classic optimization problem that asks for the shortest possible route that visits each city exactly once and returns to the starting point. The problem can be modeled as a graph, where the cities are the vertices and the distances between them are the edges. The objective is to find a Hamiltonian cycle with the minimum total weight.

One way to solve the TSP using branch and bound is as follows:

- Start with a root node that represents the entire problem, and assign it a lower bound of zero and an upper bound of infinity.
- Generate child nodes by selecting a city and adding it to the current route. For each child node, compute a lower bound and an upper bound on the total distance, using some heuristic function, such as the minimum spanning tree, the reduced cost matrix, etc.
- Compare the lower bound and the upper bound of each node with the current best solution. If the lower bound is greater than or equal to the current best solution, discard the node. If the upper bound is less than the current best solution, update the current best solution and discard any node with a lower bound greater than or equal to the new best solution.
- Repeat the above steps until all nodes are either discarded or expanded. The current best solution is the optimal solution.

An example of solving the TSP using branch and bound is shown below:

![TSP example](https://i.imgur.com/0c7yY8H.png)

The numbers in the parentheses are the lower and upper bounds of each node. The dashed lines indicate the discarded nodes. The final solution is A-B-D-C-A with a total distance of 19.