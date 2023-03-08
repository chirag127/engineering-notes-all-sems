 Here is the content in markdown format for the given topic:

## Unit 4 - Dynamic Programming with Examples Such as Knapsack

Dynamic Programming is a technique to solve complex problems by breaking them down into smaller subproblems. It solves each subproblem only once, and then saves its answer in a table. Each answer that is saved can be used to solve larger subproblems.

**Knapsack Problem:** Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.

- Represented using a 2D array/table `dp[n+1][w+1]` where `dp[i][j]` represents the maximum value we can obtain using the first `i` items and a knapsack of capacity `j`.
- The recursive formula is: `dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i-1]] + value[i-1])`
- The optimal solution is tracked using a path array to store the result.
- Time complexity: `O(nw)` where `n` is the number of items and `w` is the knapsack capacity.

**All Pairs Shortest Paths - Warshall's and Floyd's Algorithms:** Warshall's algorithm is used to find shortest distances between all pairs of vertices in a given graph. It uses the idea of transitivity to compute the shortest distances. Floyd's algorithm is a simple recursive method to solve the same problem. It considers all possible intermediate vertices to find the shortest path between two vertices.

- Warshall's algorithm: Uses a `distance[V][V]` array to store the shortest distances. The recurrence is: `distance[i][j] = distance[i][j] if (i, j) is an edge else distance[i][j] = distance[i][k] + distance[k][j]`.
- Floyd's algorithm: Also uses a `distance[V][V]` array with a similar recurrence. The optimal substructure is that the shortest path between `i` and `j` contains an intermediate vertex `k` if `distance[i][j] > distance[i][k] + distance[k][j]`.
- Time complexity: `O(V3)` where `V` is the number of vertices.

[Detailed explanations and examples can be included here]

[Similar content can be written for Resource Allocation Problem, Backtracking, Branch and Bound, Travelling Salesman Problem, Graph Coloring, n-Queen Problem, Hamiltonian Cycles and Sum of Subsets with examples and applications.]