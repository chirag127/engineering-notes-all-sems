# Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum spanning tree (MST)** of a weighted graph is a spanning tree whose sum of edge weights is minimum among all possible spanning trees.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected, weighted, undirected graph by selecting the edges with the smallest weights that do not form a cycle with the edges already in the MST.
- **Union-Find** algorithms are data structures and methods that support two operations: **union** (merging two disjoint sets into one) and **find** (determining which set an element belongs to).
- Union-Find algorithms can be used to implement **disjoint-set** data structures, which can efficiently track the connected components of a graph and check whether adding an edge creates a cycle or not.
- The steps of Kruskal's algorithm using Union-Find are as follows:
  - Sort all the edges in non-decreasing order of their weights.
  - Initialize a MST as an empty set and a disjoint-set data structure with each vertex as a separate set.
  - Repeat until the MST has (V-1) edges or the edge list is empty:
    - Pick the edge with the smallest weight from the edge list and remove it.
    - If the edge connects two vertices that belong to different sets in the disjoint-set data structure, then add the edge to the MST and perform a union operation on the two sets.
    - Otherwise, discard the edge as it creates a cycle in the MST.
  - Return the MST or report that the graph is not connected.