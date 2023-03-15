```
# Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## Dynamic Programming
- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which can be avoided by storing the solutions in a table and reusing them.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming can be applied to problems that have a recursive formulation, where the problem is divided into smaller and simpler subproblems of the same type.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and recursively solves the subproblems until the base cases are reached. The solutions of the subproblems are stored in a table and retrieved when needed.
- Bottom-up approach starts with the base cases and iteratively builds up the solutions of larger subproblems using the solutions of smaller subproblems. The solutions are stored in a table and the final solution is obtained from the table.

## Examples of Dynamic Programming Problems

### Knapsack Problem
- The knapsack problem is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized.
- The knapsack problem can be formulated as follows:

  - Let n be the number of items, W be the capacity of the knapsack, w[i] be the weight of the i-th item, and v[i] be the value of the i-th item, for i = 1, 2, ..., n.
  - Let K[i][w] be the maximum value that can be obtained by packing items from 1 to i into a knapsack with capacity w, for i = 0, 1, ..., n and w = 0, 1, ..., W.
  - The base cases are K[0][w] = 0 for all w, and K[i][0] = 0 for all i.
  - The recursive formulation is K[i][w] = max(K[i-1][w], K[i-1][w-w[i]] + v[i]) for i = 1, 2, ..., n and w = 1, 2, ..., W, where the max function returns the larger of the two arguments.
  - The optimal solution is K[n][W].

- The knapsack problem can be solved using dynamic programming by filling the table K[i][w] in a bottom-up manner, starting from the base cases and moving towards the final solution.
- The time complexity of the dynamic programming solution is O(nW), where n is the number of items and W is the capacity of the knapsack.
- The space complexity of the dynamic programming solution is O(nW), where n is the number of items and W is the capacity of the knapsack.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- The all pair shortest paths problem is a problem of finding the shortest paths between every pair of vertices in a weighted graph, where the weights can be positive, negative, or zero.
- The all pair shortest paths problem can be formulated as follows:

  - Let G = (V, E) be a weighted graph, where V is the set of vertices, E is the set of edges, and w(u, v) is the weight of the edge (u, v) in E, or infinity if there is no such edge.
  - Let n be the number of vertices in V, and let d[i][j] be the length of the shortest path from vertex i to vertex j in G, for i, j = 1, 2, ..., n.
  - The base cases are d[i][i] = 0 for all i, and d[i][j] = w(i, j) for all (i, j) in E.
  - The recursive formulation is d[i][j] = min(d[i][j], d[i][k] + d[k][j]) for i, j, k = 1, 2, ..., n, where the min function returns the smaller of the two arguments.
  - The optimal solution is d[i][j] for all i, j.

- The all pair shortest paths problem can be solved using dynamic programming by filling the