## Unit 4 - Dynamic Programming with Examples Such as Knapsack. All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms, Resource Allocation Problem. Backtracking, Branch and Bound with Examples Such as Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets.

### Dynamic Programming
- Dynamic programming is a technique for solving optimization problems that have overlapping subproblems and optimal substructure.
- Overlapping subproblems means that the same subproblem is solved repeatedly, and optimal substructure means that the optimal solution of a problem can be obtained from the optimal solutions of its subproblems.
- Dynamic programming reduces the time complexity of solving a problem by storing and reusing the solutions of subproblems, instead of recomputing them.
- Dynamic programming can be applied to problems that have the following characteristics:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems are independent of each other, i.e., solving one subproblem does not affect the solution of another subproblem.
  - There is an optimal solution for each subproblem, and the optimal solution of the original problem can be obtained by combining the optimal solutions of the subproblems.
  - There is a recursive relation that defines the optimal solution of a problem in terms of the optimal solutions of its subproblems.

### Knapsack Problem
- The knapsack problem is an example of a dynamic programming problem that involves choosing a subset of items with maximum total value, subject to a weight constraint.
- The problem can be stated as follows: Given a set of n items, each with a weight w_i and a value v_i, and a knapsack with a maximum capacity W, find a subset of items that maximizes the total value of the items in the knapsack, without exceeding the weight limit W.
- The knapsack problem can be solved by using a two-dimensional array K[n+1][W+1], where K[i][j] represents the maximum value that can be obtained by using the first i items and a knapsack with capacity j.
- The recursive relation for the knapsack problem is:

  - K[i][j] = 0, if i = 0 or j = 0
  - K[i][j] = K[i-1][j], if w_i > j
  - K[i][j] = max(K[i-1][j], K[i-1][j-w_i] + v_i), if w_i <= j

- The optimal solution can be obtained by tracing back the array K from the bottom-right corner to the top-left corner, and selecting the items that contribute to the maximum value.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms
- The all pair shortest paths problem is another example of a dynamic programming problem that involves finding the shortest distance between every pair of vertices in a weighted graph.
- The problem can be stated as follows: Given a graph G = (V, E), where V is the set of vertices, E is the set of edges, and each edge has a weight w(u, v) that represents the distance between vertices u and v, find the shortest distance d(u, v) between every pair of vertices u and v in G.
- Warshal's algorithm and Floyd's algorithm are two dynamic programming algorithms that can solve the all pair shortest paths problem.
- Warshal's algorithm is based on the idea of transitive closure, which means that if there is a path from u to v and a path from v to w, then there is a path from u to w. Warshal's algorithm uses a boolean matrix A[n][n], where A[i][j] is true if there is a path from vertex i to vertex j in G, and false otherwise. The algorithm iterates over all the vertices k, and updates the matrix A by setting A[i][j] to true if A[i][k] and A[k][j] are both true, for all i and j. The algorithm terminates when no more changes are made to the matrix A. The shortest distance d(u, v) between any pair of vertices u and v can be obtained by counting the number of edges in the shortest path from u to v, which is equal to the minimum number of true values in the row A[u] or the column A[v].
- Floyd's algorithm is based on the idea of intermediate vertices, which means that the shortest path from u to v may pass through some other vertices in G. Floyd's algorithm uses a numeric matrix D[n][n], where D[i][j] represents the shortest distance from vertex i to vertex j in G, initially equal to the weight of the edge (i,