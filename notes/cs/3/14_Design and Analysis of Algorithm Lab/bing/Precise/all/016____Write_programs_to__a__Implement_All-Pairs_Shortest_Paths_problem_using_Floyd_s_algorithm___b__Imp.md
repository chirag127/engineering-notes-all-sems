## Design and Analysis of Algorithm Lab in the subject of Real Time System

### All-Pairs Shortest Paths problem using Floyd's algorithm

Floyd's algorithm is an efficient algorithm for finding the shortest paths between all pairs of vertices in a weighted graph. The algorithm works by iteratively improving an estimate of the shortest path between all pairs of vertices until the estimate is optimal.

Here is an example of how to implement Floyd's algorithm in Python:

```python
def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph
```

### Travelling Sales Person problem using Dynamic programming

The Travelling Sales Person (TSP) problem is a well-known problem in computer science. Given a set of cities and the distances between them, the goal is to find the shortest possible route that visits each city exactly once and returns to the starting city.

Dynamic programming is a powerful technique that can be used to solve the TSP problem. The idea is to break the problem down into smaller subproblems and solve them recursively.

Here is an example of how to implement the TSP problem using dynamic programming in Python:

```python
from math import inf

def tsp(graph):
    n = len(graph)
    C = [[inf] * (1 << n) for _ in range(n)]
    C[0][1] = 0
    for size in range(1, n):
        for S in range(1, 1 << n):
            if bin(S).count('1') == size:
                for i in range(n):
                    if (S >> i) & 1:
                        for j in range(n):
                            if (S >> j) & 1 and i != j:
                                C[i][S] = min(C[i][S], C[j][S ^ (1 << i)] + graph[j][i])
    return min(C[i][(1 << n) - 1] + graph[i][0] for i in range(n))
```

These are the implementations of the All-Pairs Shortest Paths problem using Floyd's algorithm and the Travelling Sales Person problem using Dynamic programming. These algorithms can be used to solve problems in the Design and Analysis of Algorithm Lab in the subject of Real Time System.