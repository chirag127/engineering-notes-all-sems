## Write programs to (a) Implement All-Pairs Shortest Paths problem using Floyd's algorithm. (b) Implement Travelling Sales Person problem using Dynamic programming.

### All-Pairs Shortest Paths problem using Floyd's algorithm
- The All-Pairs Shortest Paths problem is to find the shortest path between all pairs of vertices in a given weighted graph.
- The Floyd's algorithm is an efficient algorithm to solve this problem.
- The algorithm uses a dynamic programming approach to compute the shortest path between any two vertices in the graph.
- The algorithm maintains a matrix of distances between all pairs of vertices.
- Initially, the matrix is initialized with the edge weights of the graph.
- Then, the algorithm iteratively updates the matrix by considering all possible intermediate vertices.
- The time complexity of the algorithm is O(n^3), where n is the number of vertices in the graph.

**Pseudocode:**

```
function FloydWarshall (graph[][], n)
    for k from 1 to n
        for i from 1 to n
            for j from 1 to n
                if graph[i][j] > graph[i][k] + graph[k][j]
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph
```

### Travelling Sales Person problem using Dynamic programming
- The Travelling Sales Person problem is to find the shortest possible route that visits each city exactly once and returns to the starting city.
- The dynamic programming approach can be used to solve this problem efficiently.
- The algorithm maintains a matrix of subproblems, where each subproblem represents the shortest path from the starting city to a specific city, visiting a subset of cities along the way.
- Initially, the matrix is initialized with the distances from the starting city to each of the other cities.
- Then, the algorithm iteratively updates the matrix by considering all possible intermediate cities.
- The time complexity of the algorithm is O(n^2 * 2^n), where n is the number of cities in the problem.

**Pseudocode:**

```
function TSP (dist[][], n)
    let C[2^n][n] be a new array
    for k from 0 to n-1
        C[{k},k] = dist[0][k]
    for s from 2 to n
        for subset in all subsets of {1, 2, ..., n-1} of size s
            for k in subset
                C[subset,k] = min over all m in subset,m!=k {C[subset-{k},m] + dist[m][k]}
    tour = min over all k in {1, 2, ..., n-1} {C[{1, 2, ..., n-1},k] + dist[k][0]}
    return tour
```