## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The algorithm works by iteratively improving an estimate of the shortest distance between any two vertices, based on the previous estimate and the distance of a possible intermediate vertex.
- The algorithm maintains a matrix D of size n x n, where n is the number of vertices in the graph, and D[i][j] is the current estimate of the shortest distance from vertex i to vertex j.
- Initially, D[i][j] is set to the weight of the edge (i, j) if it exists, or infinity otherwise. D[i][i] is set to zero for all i.
- The algorithm then performs n iterations, where in each iteration k, it updates D[i][j] for all i and j by checking if going through vertex k can improve the current estimate. That is, D[i][j] is set to the minimum of D[i][j] and D[i][k] + D[k][j].
- After n iterations, D[i][j] will contain the shortest distance from i to j, or infinity if there is no path from i to j.
- The algorithm can also be used to find the transitive closure of a graph, by replacing the minimum operation with a logical OR, and the addition operation with a logical AND.
- The algorithm has a time complexity of O(n^3), where n is the number of vertices in the graph, and a space complexity of O(n^2), where n is the number of vertices in the graph.

- A possible pseudocode for the algorithm is:

```
// Input: A weighted graph G with n vertices
// Output: A matrix D of size n x n, where D[i][j] is the shortest distance from i to j in G
Floyd(G):
  // Initialize D with the edge weights or infinity
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0
      else if (i, j) is an edge in G:
        D[i][j] = weight of (i, j)
      else:
        D[i][j] = infinity
  // Perform n iterations of updating D
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        // Check if going through k can improve the current estimate
        D[i][j] = min(D[i][j], D[i][k] + D[k][j])
  // Return D
  return D
```