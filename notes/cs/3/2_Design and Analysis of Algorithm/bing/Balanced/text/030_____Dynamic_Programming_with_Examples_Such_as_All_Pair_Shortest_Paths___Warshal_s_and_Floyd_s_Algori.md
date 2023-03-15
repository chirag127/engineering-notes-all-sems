### Dynamic Programming with Examples

Dynamic programming is a technique for solving problems that have overlapping subproblems and optimal substructure. It involves breaking down a complex problem into smaller and simpler subproblems, solving them once and storing their solutions in a table or an array, and then using these solutions to construct the solution for the original problem. Dynamic programming can reduce the time and space complexity of recursive algorithms by avoiding repeated computations.

Some examples of problems that can be solved using dynamic programming are:

- **Knapsack problem**: Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.
- **Coin change problem**: Given a set of coin denominations and a target amount, find the minimum number of coins needed to make the change or determine if it is impossible.
- **Longest common subsequence problem**: Given two sequences, find the length of the longest subsequence that is common to both of them.
- **Matrix chain multiplication problem**: Given a sequence of matrices, find the most efficient way to multiply them together. The cost of multiplying two matrices is equal to the number of scalar multiplications required.
- **All pair shortest paths problem**: Given a weighted graph, find the shortest distance between every pair of vertices in the graph. There are two algorithms for solving this problem using dynamic programming: Warshall's algorithm and Floyd's algorithm.

#### Warshall's Algorithm

Warshall's algorithm is a dynamic programming algorithm that computes the transitive closure of a directed graph. The transitive closure of a graph is a new graph that contains an edge from u to v if there is a path from u to v in the original graph. The algorithm works as follows:

- Initialize a matrix W of size n x n, where n is the number of vertices in the graph, such that W[i][j] = 1 if there is an edge from i to j, and W[i][j] = 0 otherwise.
- For k = 1 to n, do the following:
  - For i = 1 to n, do the following:
    - For j = 1 to n, do the following:
      - W[i][j] = W[i][j] or (W[i][k] and W[k][j])
- Return W as the transitive closure of the graph.

The time complexity of Warshall's algorithm is O(n^3), where n is the number of vertices in the graph. The space complexity is O(n^2), since we need to store the matrix W.

#### Floyd's Algorithm

Floyd's algorithm is a dynamic programming algorithm that computes the shortest distances between every pair of vertices in a weighted graph. The algorithm works as follows:

- Initialize a matrix D of size n x n, where n is the number of vertices in the graph, such that D[i][j] = w(i, j) if there is an edge from i to j with weight w(i, j), and D[i][j] = infinity otherwise. Also, set D[i][i] = 0 for all i.
- For k = 1 to n, do the following:
  - For i = 1 to n, do the following:
    - For j = 1 to n, do the following:
      - D[i][j] = min(D[i][j], D[i][k] + D[k][j])
- Return D as the matrix of shortest distances between every pair of vertices.

The time complexity of Floyd's algorithm is O(n^3), where n is the number of vertices in the graph. The space complexity is O(n^2), since we need to store the matrix D.