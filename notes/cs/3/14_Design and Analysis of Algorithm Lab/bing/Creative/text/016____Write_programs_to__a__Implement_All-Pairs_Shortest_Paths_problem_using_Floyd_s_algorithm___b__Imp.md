## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm.

- The All-Pairs Shortest Paths problem is to find the shortest distance between every pair of vertices in a weighted graph.
- Floyd's algorithm is a dynamic programming approach that solves this problem in O(n^3) time, where n is the number of vertices in the graph.
- The algorithm works by iteratively updating a matrix D that stores the shortest distances between all pairs of vertices, using the following formula:

```
D[i][j][k] = min(D[i][j][k-1], D[i][k][k-1] + D[k][j][k-1])
```

- This means that the shortest distance between vertices i and j using only the first k vertices as intermediate nodes is either the same as the shortest distance using only the first k-1 vertices, or it is the sum of the shortest distances from i to k and from k to j using only the first k-1 vertices.
- The algorithm starts with D[i][j][0] = w(i,j), where w(i,j) is the weight of the edge from i to j, or infinity if there is no such edge.
- The algorithm ends with D[i][j][n] = d(i,j), where d(i,j) is the shortest distance from i to j in the graph.
- The pseudocode of the algorithm is as follows:

```
// Input: A weighted graph G with n vertices
// Output: A matrix D of shortest distances between all pairs of vertices
Floyd(G):
  // Initialize D with edge weights or infinity
  for i = 1 to n:
    for j = 1 to n:
      if i == j:
        D[i][j][0] = 0
      else if (i,j) is an edge in G:
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

### (b) Implement Travelling Sales Person problem using Dynamic programming.

- The Travelling Sales Person problem is to find the shortest tour that visits every vertex in a weighted graph exactly once and returns to the starting vertex.
- This problem is NP-hard, meaning that there is no known polynomial-time algorithm that can solve it optimally.
- However, using dynamic programming, we can find an optimal solution in O(n^2 * 2^n) time, where n is the number of vertices in the graph.
- The idea is to use a matrix C that stores the minimum cost of a tour that starts at vertex 1, visits a subset of vertices S, and ends at vertex i, for every i and S.
- The algorithm works by iteratively updating C using the following formula:

```
C[i][S] = min(C[j][S-{i}] + w(j,i)) for every j in S-{i}
```

- This means that the minimum cost of a tour that starts at 1, visits S, and ends at i is the minimum of the cost of a tour that starts at 1, visits S-{i}, and ends at j, plus the cost of the edge from j to i, for every j in S-{i}.
- The algorithm starts with C[1][{1}] = 0, and C[i][{1}] = infinity for every i > 1.
- The algorithm ends with C[1][{1,2,...,n}], which is the minimum cost of a tour that visits every vertex exactly once and returns to 1.
- The pseudocode of the algorithm is as follows:

```
// Input: A weighted graph G with n vertices
// Output: The minimum cost of a TSP tour
TSP(G):
  // Initialize C with 0 or infinity
  for i = 1 to n:
    for S = {1} to {1,2,...,n}:
      if i == 1 and S == {1}:
        C[i][S] = 0