# Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

## (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The algorithm works by iteratively improving an estimate of the shortest distance between any two vertices, based on the previous estimate and the edge weights.
- The algorithm maintains a matrix D of size n x n, where n is the number of vertices in the graph, and D[i][j] is the current estimate of the shortest distance from vertex i to vertex j.
- Initially, D[i][j] is set to the edge weight w(i, j) if there is an edge from i to j, or infinity otherwise.
- Then, for each intermediate vertex k from 1 to n, the algorithm updates D[i][j] by checking if going through vertex k can improve the current estimate, i.e., if D[i][k] + D[k][j] < D[i][j].
- If so, the algorithm sets D[i][j] to D[i][k] + D[k][j], and records k as the predecessor of j on the shortest path from i to j.
- After n iterations, the matrix D contains the final shortest distances between all pairs of vertices, and the predecessor matrix can be used to reconstruct the shortest paths.
- The algorithm runs in O(n^3) time and O(n^2) space, where n is the number of vertices in the graph.

- Here is a pseudocode implementation of Floyd's algorithm:

```
// Input: A weighted graph G with n vertices and no negative cycles
// Output: A matrix D of shortest distances and a matrix P of predecessors
function Floyd(G):
  // Initialize D and P
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j] = 0 // The distance from a vertex to itself is zero
        P[i][j] = null // There is no predecessor for a vertex to itself
      else if there is an edge from i to j with weight w(i, j):
        D[i][j] = w(i, j) // The distance is the edge weight
        P[i][j] = i // The predecessor is the source vertex
      else:
        D[i][j] = infinity // There is no edge from i to j
        P[i][j] = null // There is no predecessor
  
  // Update D and P using intermediate vertices
  for k = 1 to n: // For each intermediate vertex k
    for i = 1 to n: // For each source vertex i
      for j = 1 to n: // For each destination vertex j
        if D[i][k] + D[k][j] < D[i][j]: // If going through k is better
          D[i][j] = D[i][k] + D[k][j] // Update the distance
          P[i][j] = P[k][j] // Update the predecessor
  
  // Return the final matrices
  return D, P
```