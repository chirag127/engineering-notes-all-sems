## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree** (MST) of a graph is a spanning tree that has the minimum possible sum of edge weights among all the spanning trees of the graph.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a given connected undirected graph using the following steps:
  - Sort all the edges in non-decreasing order of their weights.
  - Initialize a forest of disjoint sets, where each set contains one vertex of the graph.
  - Repeat until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph:
    - Pick the smallest edge from the sorted list that does not create a cycle in the current spanning tree.
    - Add this edge to the spanning tree and merge the two sets that contain the end vertices of this edge.
- **Union-Find** algorithms are data structures that support two operations on disjoint sets:
  - **Find**: Given an element, find the set that contains it.
  - **Union**: Given two sets, merge them into one set.
- Union-Find algorithms can be implemented using arrays, linked lists, or trees. A common and efficient implementation is using **union by rank** and **path compression**:
  - **Union by rank**: When merging two sets, attach the smaller set (by number of elements or by height of the tree) to the root of the larger set. This keeps the height of the tree balanced and reduces the time complexity of the find operation.
  - **Path compression**: When finding the set that contains an element, make every node on the path from the element to the root point directly to the root. This flattens the tree and reduces the time complexity of the find operation.