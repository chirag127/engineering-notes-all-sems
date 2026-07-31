Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content for your notes:

## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph, possibly with negative edge weights but no negative cycles.
- Floyd's algorithm, also known as the Floyd-Warshall algorithm, is an algorithm that solves this problem by using dynamic programming.
- The main idea of Floyd's algorithm is to iteratively update a matrix D that stores the shortest distances between all pairs of vertices, using the following formula:

`D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1] + D[k][j][k-1])`

- This means that the shortest distance between vertices i and j using only the first k vertices as intermediate nodes is either the same as the previous iteration, or can be improved by going through vertex k.
- The algorithm starts with D[i][j][0] = w(i,j), where w(i,j) is the weight of the edge from i to j, or infinity if there is no such edge.
- The algorithm then repeats the above formula for k = 1, 2, ..., n, where n is the number of vertices in the graph.
- The final matrix D[i][j][n] contains the shortest distances between all pairs of vertices.
- The algorithm runs in O(n^3) time and O(n^2) space, where n is the number of vertices in the graph.
- Here is a pseudocode implementation of Floyd's algorithm:

```
// Input: A weighted graph G with n vertices and no negative cycles
// Output: A matrix D of shortest distances between all pairs of vertices
function Floyd(G):
  // Initialize D with edge weights or infinity
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j][0] = 0
      else if there is an edge from i to j in G:
        D[i][j][0] = w(i,j)
      else:
        D[i][j][0] = infinity
  // Update D using the formula
  for k = 1 to n:
    for i = 1 to n:
      for j = 1 to n:
        D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1] + D[k][j][k-1])
  // Return the final matrix
  return D
```