# Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

## Dynamic Programming
- Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, which leads to wasteful computation.
- Optimal substructure means that the optimal solution of a problem can be obtained by combining the optimal solutions of its subproblems.
- Dynamic programming avoids repeated computation by storing the results of subproblems in a table and reusing them when needed.
- Dynamic programming can be applied to problems that have a recursive formulation, where the problem can be divided into smaller and simpler subproblems of the same type.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up.
- Top-down approach starts with the original problem and recursively solves the subproblems until the base cases are reached. The results of subproblems are stored in a table and looked up when needed.
- Bottom-up approach starts with the base cases and iteratively builds up the solution of larger subproblems using the results of smaller subproblems stored in a table.
- Dynamic programming can be used to solve problems such as knapsack, all pair shortest paths, resource allocation, etc.

## Knapsack Problem
- Knapsack problem is a problem of finding the most valuable subset of items that can be packed into a knapsack with a limited capacity.
- Knapsack problem can be classified into two types: 0-1 knapsack and fractional knapsack.
- 0-1 knapsack problem means that each item can be either taken or left out, and the value and weight of each item are integers.
- Fractional knapsack problem means that each item can be taken partially, and the value and weight of each item are real numbers.
- 0-1 knapsack problem can be solved using dynamic programming, while fractional knapsack problem can be solved using a greedy approach.
- To solve 0-1 knapsack problem using dynamic programming, we define a table K[n+1][W+1], where n is the number of items and W is the capacity of the knapsack.
- K[i][j] represents the maximum value that can be obtained by using the first i items and a knapsack of capacity j.
- The base cases are K[0][j] = 0 for all j and K[i][0] = 0 for all i, meaning that no value can be obtained with no items or no capacity.
- The recursive formula is K[i][j] = max(K[i-1][j], K[i-1][j-w[i]] + v[i]), where w[i] and v[i] are the weight and value of the ith item, respectively.
- The first term K[i-1][j] means that the ith item is not taken, and the second term K[i-1][j-w[i]] + v[i] means that the ith item is taken and the remaining capacity is j-w[i].
- The maximum value is K[n][W], and the optimal subset can be traced back by checking which items are taken or not.
- The time complexity of this algorithm is O(nW), and the space complexity is O(nW).

## All Pair Shortest Paths
- All pair shortest paths problem is a problem of finding the shortest paths between every pair of vertices in a weighted graph.
- All pair shortest paths problem can be solved using dynamic programming, such as Warshal's and Floyd's algorithms.
- Warshal's algorithm is a special case of Floyd's algorithm for unweighted graphs, where the edge weights are either 0 or 1, representing the absence or presence of an edge.
- Warshal's algorithm uses a boolean matrix A[n][n], where n is the number of vertices in the graph.
- A[i][j] represents whether there is a path from vertex i to vertex j in the graph.
- The base case is A[i][j] = true if there is an edge from i to j, and A[i][j] = false otherwise.
- The recursive formula is A[i][j] = A[i][j] or (A[i][k] and A[k][j]), where k is an intermediate vertex.
- The first term A[i][j] means that there is a direct path from i to j, and the second term (A[i][k] and A[k][j]) means that there is a path