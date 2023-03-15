# Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## Dynamic Programming
- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have a recursive formulation, where the problem can be divided into smaller and simpler subproblems of the same type.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and recursively solves the subproblems until the base cases are reached. The results of subproblems are stored in a table and retrieved when needed.
- Bottom-up approach starts with the base cases and iteratively builds up the solution of larger subproblems using the results of smaller subproblems stored in a table.
- Dynamic programming can be used to solve various problems such as knapsack, all pair shortest paths, resource allocation, etc.

## Knapsack Problem
- Knapsack problem is a problem of packing a set of items with different weights and values into a knapsack with a limited capacity, such that the total value of the packed items is maximized.
- Knapsack problem can be formulated as follows:

  - Let n be the number of items, W be the capacity of the knapsack, w[i] be the weight of the i-th item, and v[i] be the value of the i-th item, for i = 1, 2, ..., n.
  - Let x[i] be a binary variable that indicates whether the i-th item is packed or not, for i = 1, 2, ..., n.
  - The objective is to maximize the total value of the packed items, which is given by:

    - `sum(v[i] * x[i]) for i = 1, 2, ..., n`

  - The constraint is that the total weight of the packed items does not exceed the capacity of the knapsack, which is given by:

    - `sum(w[i] * x[i]) for i = 1, 2, ..., n <= W`

- Knapsack problem can be solved using dynamic programming by defining a subproblem as follows:

  - Let K[i][j] be the maximum value that can be obtained by packing items from 1 to i into a knapsack with capacity j, for i = 0, 1, 2, ..., n and j = 0, 1, 2, ..., W.
  - The base cases are:

    - K[0][j] = 0 for j = 0, 1, 2, ..., W, since no item can be packed.
    - K[i][0] = 0 for i = 0, 1, 2, ..., n, since the knapsack has no capacity.

  - The recursive relation is:

    - K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]) for i = 1, 2, ..., n and j = 1, 2, ..., W, since the i-th item can be either packed or not packed.

  - The optimal solution is given by K[n][W], which is the maximum value that can be obtained by packing items from 1 to n into a knapsack with capacity W.
  - The optimal subset of items can be traced back by checking the table K and comparing the values of K[i][j] and K[i-1][j] for i = n, n-1, ..., 1 and j = W, W-w[i], ..., 0.

- Knapsack problem can be solved using a top-down or a bottom-up approach, depending on whether the table K is filled recursively or iteratively.

## All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- All pair shortest paths problem is a problem of finding the shortest paths between every pair of vertices in a weighted graph, where the weight of an edge represents the distance or cost between the two vertices.
- All pair shortest paths problem can be formulated as follows:

  - Let G