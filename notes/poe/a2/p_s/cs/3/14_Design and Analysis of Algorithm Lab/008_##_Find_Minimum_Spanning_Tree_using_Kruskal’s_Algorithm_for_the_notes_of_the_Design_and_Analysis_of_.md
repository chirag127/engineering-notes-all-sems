 Here is the content in markdown format for the topic ## Find Minimum Spanning Tree using Kruskal’s Algorithm for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System:

# Find Minimum Spanning Tree using Kruskal’s Algorithm

## Algorithm
- Sort all edges in increasing order of their weight.
- Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
- Repeat step#2 until there are (V - 1) edges in the spanning tree.

## Example
Consider a graph with V = 5 and E = 8 with the following edges:
```
Edge: u v w
1:    1   2   6
2:    1   3   1
3:    2   4   5
4:    2   5   3
5:    3   4   4
6:    3   5   2
7:    4   5   8
8:    1   5   7
```

1. Sort all edges in increasing order of their weight. Edges will be:
```
Edge: u v w
2:    1   3   1
6:    3   5   2
5:    3   4   4
3:    2   5   3
4:    2   4   5
8:    1   5   7
1:    1   2   6
7:    4   5   8
```

2. Consider the smallest edge (1, 3, 1) and check if it forms a cycle. It doesn't form cycle. Include this edge in the spanning tree.
3. Next smallest edge (3, 5, 2) forms a cycle, so discard it.
4. Next smallest edge (3, 4, 4) doesn't form cycle, include it in the spanning tree.
5. Next smallest edge (2, 5, 3) forms a cycle, so discard it.
6. Next smallest edge (2, 4, 5) doesn't form cycle, include it in the spanning tree.
7. Next smallest edge (1, 5, 7) forms a cycle, so discard it.
8. Finally, consider (4, 5, 8) and include it.

Tree grows gradually:
```
Edge: u v
2:    1   3
4:    3   4
5:    2   4
```

## Advantages
- Simplicity: Easy to understand and implement.
- Efficient: Has a time complexity of O(E log E) or O(E log V).
- Optimal: Finds the minimum spanning tree.