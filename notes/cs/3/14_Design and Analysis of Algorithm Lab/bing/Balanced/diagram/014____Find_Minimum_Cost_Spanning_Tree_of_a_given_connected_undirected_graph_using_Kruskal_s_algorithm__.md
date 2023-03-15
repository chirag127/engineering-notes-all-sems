## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by sorting the edges in non-decreasing order of their weights and adding them one by one to the MST, as long as they do not create a cycle.
- **Union-Find** algorithms are data structures that support two operations: **find** and **union**. Find returns the representative element of a set that contains a given element, and union merges two sets into one by making one of their representatives point to the other.
- Union-Find algorithms can be used to implement a **disjoint-set** data structure, which maintains a collection of disjoint sets and allows efficient queries and updates. Disjoint sets are useful for keeping track of the connected components of a graph.
- To use Kruskal's algorithm with Union-Find algorithms, we need to do the following steps:
  - Create a disjoint set for each vertex of the graph.
  - Sort the edges of the graph in non-decreasing order of their weights.
  - For each edge in the sorted order, do the following:
    - Find the sets that contain the endpoints of the edge using the find operation.
    - If the sets are different, then the edge does not create a cycle and can be added to the MST. Use the union operation to merge the sets.
    - If the sets are the same, then the edge creates a cycle and cannot be added to the MST. Ignore the edge.
  - Repeat until the MST has (V-1) edges, where V is the number of vertices in the graph, or until all the edges are processed.
  - Return the MST.