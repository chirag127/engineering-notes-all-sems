# Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

## (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a given graph, which may have positive or negative edge weights, but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The main idea of Floyd's algorithm is to iteratively improve an estimate of the shortest distance between any two vertices, by considering all possible intermediate vertices that may lie on a shorter path.
- The algorithm maintains a matrix D, where D[i][j] is the current estimate of the shortest distance from vertex i to vertex j. Initially, D[i][j] is set to the edge weight between i and j, or infinity if there is no edge.
- The algorithm then performs n iterations, where n is the number of vertices in the graph. In each iteration, it considers a new intermediate vertex k, and updates D[i][j] for all i and j by checking if going through k gives a shorter path: D[i][j] = min(D[i][j], D[i][k] + D[k][j]).
- After n iterations, D[i][j] will contain the shortest distance from i to j, or infinity if there is no path. The algorithm can also keep track of the predecessors of each vertex, to reconstruct the shortest paths.
- The algorithm runs in O(n^3) time and O(n^2) space, where n is the number of vertices in the graph.

- Pseudocode for Floyd's algorithm:

```
// Input: A graph G with n vertices and a matrix W of edge weights
// Output: A matrix D of shortest distances and a matrix P of predecessors
Floyd(G, W):
  // Initialize D and P
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0 // Distance from a vertex to itself is zero
        P[i][j] = null // No predecessor for a vertex to itself
      else if W[i][j] != infinity:
        D[i][j] = W[i][j] // Distance from i to j is the edge weight
        P[i][j] = i // Predecessor of j is i
      else:
        D[i][j] = infinity // No edge from i to j
        P[i][j] = null // No predecessor for j
  // Iterate over all intermediate vertices
  for k = 1 to n:
    // Update D and P for all pairs of vertices
    for i = 1 to n:
      for j = 1 to n:
        if D[i][k] + D[k][j] < D[i][j]: // Check if going through k is better
          D[i][j] = D[i][k] + D[k][j] // Update the distance
          P[i][j] = P[k][j] // Update the predecessor
  return D, P
```