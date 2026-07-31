## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MST)** of a graph is a spanning tree that has the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected undirected graph by sorting the edges in non-decreasing order of their weight and adding them one by one to the spanning tree, as long as they do not create a cycle.
- **Union-Find algorithms** are data structures and algorithms that support two operations: **union** and **find**. Union merges two disjoint sets into one, and find returns the representative element of the set that contains a given element.
- The pseudocode of Kruskal's algorithm using Union-Find algorithms is as follows:

```
Kruskal(G):
  Input: A connected undirected graph G = (V, E) with edge weights
  Output: A MST of G

  Initialize an empty set T to store the MST edges
  Initialize a Union-Find data structure U with each vertex in V as a singleton set
  Sort the edges in E in non-decreasing order of their weight
  For each edge (u, v) in E, in sorted order:
    If find(u) != find(v): # u and v belong to different sets, so adding (u, v) will not create a cycle
      Add (u, v) to T
      Union(u, v) # merge the sets containing u and v
  Return T
```

- The time complexity of Kruskal's algorithm using Union-Find algorithms is O(E log E + E log V), where E is the number of edges and V is the number of vertices in the graph. The first term is for sorting the edges, and the second term is for performing the union and find operations.