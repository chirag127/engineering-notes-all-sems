## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal’s algorithm is a greedy algorithm used to find the minimum spanning tree (MST) of a given graph. The MST is a subgraph of the original graph that connects all the vertices with minimum total edge weight.

### Steps for finding MST using Kruskal’s Algorithm:

1. Sort all the edges of the graph in non-decreasing order of their weight.
2. Create an empty MST and initialize it with an empty set of edges.
3. Iterate over all the edges in the sorted order. For each edge, check if adding it to the MST forms a cycle. If not, add it to the MST.
4. Repeat step 3 until all the edges have been processed or the MST contains n-1 edges, where n is the number of vertices in the graph.

### Pseudo Code for Kruskal’s Algorithm:

```
KruskalMST(G):
  sort all the edges of G in non-decreasing order of their weight
  initialize an empty set of edges as MST
  for each vertex v in G:
    makeSet(v)
  for each edge (u, v) in G:
    if findSet(u) != findSet(v):
      add (u, v) to MST
      union(u, v)
  return MST
```

### Example:

Consider the following undirected graph with 6 vertices and 9 edges:

![graph](./graph.png)

The edges are sorted in non-decreasing order of their weight as follows:

```
(B, C) -> weight: 2
(E, F) -> weight: 2
(A, B) -> weight: 3
(C, D) -> weight: 4
(B, D) -> weight: 5
(D, F) -> weight: 5
(A, D) -> weight: 6
(C, E) -> weight: 6
(B, E) -> weight: 7
```

The MST of the graph can be found using Kruskal’s Algorithm as follows:

1. Create an empty MST: `MST = {}`
2. Initialize disjoint sets for each vertex: `{A}, {B}, {C}, {D}, {E}, {F}`
3. Process the edges in the sorted order:
   - Add edge (B, C) to the MST as it does not form a cycle: `MST = {(B, C)}`
   - Add edge (E, F) to the MST as it does not form a cycle: `MST = {(B, C), (E, F)}`
   - Add edge (A, B) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B)}`
   - Add edge (C, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D)}`
   - Add edge (B, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D)}`
   - Skip edge (D, F) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D)}`
   - Add edge (A, D) to the MST as it does not form a cycle: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
   - Skip edge (C, E) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
   - Skip edge (B, E) as it forms a cycle with the MST: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`
4. The MST of the graph is: `MST = {(B, C), (E, F), (A, B), (C, D), (B, D), (A, D)}`

### Time Complexity:

The time complexity of Kruskal’s Algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices in the graph. The sorting step takes O(E log E) time and the disjoint set operations take O(E log V) time. Since E is at most V^2, the time complexity is O(V^2 log V) in the worst case.