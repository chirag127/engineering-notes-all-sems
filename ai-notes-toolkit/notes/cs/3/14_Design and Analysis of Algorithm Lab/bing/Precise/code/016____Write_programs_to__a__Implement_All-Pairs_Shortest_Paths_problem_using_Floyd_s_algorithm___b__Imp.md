## Design and Analysis of Algorithm Lab: Real Time System

### Floyd's Algorithm for All-Pairs Shortest Paths Problem

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path distances between all pairs of vertices until the estimate is accurate.

Here is the pseudocode for Floyd's algorithm:

```
let dist be a |V| × |V| array of minimum distances initialized to ∞ (infinity)
for each edge (u,v)
    dist[u][v] ← w(u,v)  // the weight of the edge (u,v)
for each vertex v
    dist[v][v] ← 0
for k from 1 to |V|
    for i from 1 to |V|
        for j from 1 to |V|
            if dist[i][j] > dist[i][k] + dist[k][j] 
                dist[i][j] ← dist[i][k] + dist[k][j]
            end if
```

### Dynamic Programming for Travelling Sales Person Problem

The Travelling Sales Person (TSP) problem is a well-known NP-hard problem in computer science. It involves finding the shortest possible route that visits a given set of cities and returns to the starting city. Dynamic programming can be used to solve the TSP problem by breaking it down into smaller subproblems and solving them recursively.

Here is the pseudocode for solving the TSP problem using dynamic programming:

```
function TSP(graph, start)
    let n = number of vertices in graph
    let C = array of size [1..n, 1..2^(n-1)] initialized to ∞
    C[start, {start}] = 0
    for s = 2 to n
        for all subsets S ⊆ {1,2,...,n} of size s and containing start
            for all j ∈ S, j ≠ start
                C[j,S] = min { C[i,S-{j}] + d(i,j) : i ∈ S, i ≠ j }
            end for
        end for
    end for
    return min { C[i,{1,2,...,n}] + d(i,start) : i ∈ {1,2,...,n}, i ≠ start }
```

In the above pseudocode, `C[j,S]` represents the minimum cost of visiting all vertices in the set `S` and ending at vertex `j`. The function `d(i,j)` represents the distance between vertices `i` and `j`. The final result is the minimum cost of visiting all vertices and returning to the starting vertex.