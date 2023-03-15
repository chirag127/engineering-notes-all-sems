Hello, I am Sydney, your AI assistant. I can help you with your topic of dynamic programming with examples such as all pair shortest paths, Warshal's and Floyd's algorithms, resource allocation problem, etc. Here are some notes that I have prepared for you based on the web search results:

### Dynamic Programming

- Dynamic programming is a technique of solving complex problems by breaking them down into smaller subproblems, and reusing the solutions of the subproblems to avoid repeated computations  .
- Dynamic programming can be applied to problems that have two main characteristics: optimal substructure and overlapping subproblems.
  - Optimal substructure means that the optimal solution of the original problem can be obtained by combining the optimal solutions of the subproblems.
  - Overlapping subproblems means that the same subproblems are encountered multiple times during the problem-solving process, and their solutions can be stored and reused to save time and space.
- Dynamic programming can be implemented using two approaches: top-down and bottom-up .
  - Top-down approach starts with the original problem and recursively divides it into smaller subproblems until the base cases are reached. Then, the solutions of the subproblems are combined to obtain the solution of the original problem .
  - Bottom-up approach starts with the base cases and iteratively builds up the solutions of larger subproblems until the solution of the original problem is obtained. This approach usually uses a table or an array to store the solutions of the subproblems .
- Dynamic programming can be used to solve various types of problems, such as optimization, counting, decision making, etc. Some common examples of dynamic programming problems are:
  - Knapsack problem: Given a set of items, each with a weight and a value, determine the number of each item to include in a knapsack so that the total weight is less than or equal to a given limit and the total value is as large as possible.
  - Coin change problem: Given an array of coin values and a target amount, find the minimum number of coins needed to make the change, or return -1 if it is not possible.
  - Longest common subsequence problem: Given two sequences, find the length of the longest subsequence that is common to both of them.
  - Matrix chain multiplication problem: Given a sequence of matrices, find the most efficient way to multiply them together. The cost of multiplying two matrices is equal to the number of scalar multiplications required.

### All Pair Shortest Paths – Warshal’s and Floyd’s Algorithms

- All pair shortest paths problem is to find the shortest distance between every pair of vertices in a weighted graph.
- Warshal's algorithm is a dynamic programming algorithm that can be used to find the transitive closure of a directed graph. The transitive closure of a graph is a graph that contains an edge from u to v if there is a path from u to v in the original graph.
- Warshal's algorithm works by iteratively adding intermediate vertices to the path between any two vertices, and updating the distance matrix accordingly. The algorithm runs in O(n^3) time, where n is the number of vertices in the graph.
- Floyd's algorithm is a dynamic programming algorithm that can be used to find the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively considering each vertex as an intermediate vertex, and updating the distance matrix accordingly. The algorithm runs in O(n^3) time, where n is the number of vertices in the graph.
- The pseudocode of Warshal's algorithm is:

```
function Warshal(G):
  // G is an n x n adjacency matrix of a directed graph
  // D is an n x n distance matrix, initialized to G
  D = G
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        // if there is a path from i to j through k, update D[i][j] to 1
        D[i][j] = D[i][j] or (D[i][k] and D[k][j])
  return D
```

- The pseudocode of Floyd's algorithm is:

```
function Floyd(G):
  // G is an n x n adjacency matrix of a weighted graph
  // D