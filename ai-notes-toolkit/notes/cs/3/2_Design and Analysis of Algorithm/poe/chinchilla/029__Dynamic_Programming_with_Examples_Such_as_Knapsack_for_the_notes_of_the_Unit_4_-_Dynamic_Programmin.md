### Dynamic Programming with Examples Such as Knapsack

Dynamic programming is a powerful algorithmic technique that is used to solve optimization problems by breaking them down into smaller subproblems and solving them sequentially. This approach is particularly useful when the same subproblems are encountered repeatedly, as it allows for efficient solutions to be computed and stored for future use.

Here are some key concepts and examples of dynamic programming that you should know:

#### Knapsack Problem

- The knapsack problem is a classic optimization problem that involves selecting a subset of items to include in a knapsack, subject to a weight constraint, in order to maximize the total value of the items.
- The dynamic programming approach to solving the knapsack problem involves breaking it down into smaller subproblems, where we consider the optimal solution for each item and the remaining capacity of the knapsack.
- We can then use the solutions to the subproblems to compute the optimal solution for the entire problem.

#### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- The all-pairs shortest path problem involves finding the shortest path between all pairs of vertices in a graph.
- Two popular algorithms for solving this problem using dynamic programming are Warshall's algorithm and Floyd's algorithm.
- Warshall's algorithm computes the shortest path between all pairs of vertices by iteratively computing the shortest path between each pair of vertices using a boolean matrix to keep track of which vertices have been visited.
- Floyd's algorithm computes the shortest path between all pairs of vertices by iteratively updating a distance matrix until the shortest path is found.

#### Resource Allocation Problem

- The resource allocation problem involves allocating limited resources to a set of activities in order to maximize the overall value of the activities completed.
- This problem can be solved using dynamic programming by breaking it down into subproblems based on the amount of resources allocated to each activity and computing the optimal solution for each subproblem.

#### Backtracking, Branch and Bound

- Backtracking and branch and bound are two related techniques that can be used to solve optimization problems.
- Backtracking involves exploring all possible solutions to a problem by recursively building and exploring a tree of possible solutions.
- Branch and bound is a more efficient variant of backtracking that involves pruning parts of the search space that are guaranteed not to contain the optimal solution.

#### Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles, Sum of Subsets

- These are all classic optimization problems that can be solved using dynamic programming, backtracking, or branch and bound.
- The travelling salesman problem involves finding the shortest possible route that visits all cities in a given set exactly once.
- The graph coloring problem involves assigning colors to the vertices of a graph such that no adjacent vertices have the same color.
- The n-queen problem involves placing n queens on an n x n chessboard such that no two queens are attacking each other.
- The Hamiltonian cycle problem involves finding a cycle in a graph that visits every vertex exactly once.
- The sum of subsets problem involves finding a subset of a set of integers that adds up to a given target sum.

By understanding and applying dynamic programming techniques to these and other optimization problems, you can develop efficient algorithms for solving complex problems in a wide range of fields.