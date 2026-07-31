Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your notes.

## Find Minimum Spanning Tree using Kruskal’s Algorithm for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum spanning tree (MST)** of a graph is a spanning tree that has the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST of a graph in O(E log V) time, where E is the number of edges and V is the number of vertices.
- The algorithm works as follows:
  - Sort all the edges in non-decreasing order of their weight.
  - Initialize a set S to contain all the vertices of the graph, each as a separate component (i.e., a singleton set).
  - Initialize an empty set T to store the edges of the MST.
  - Repeat until T has V-1 edges or all the edges are processed:
    - Pick the smallest edge (u, v) that does not form a cycle with T.
    - Add (u, v) to T.
    - Union the components containing u and v in S.
  - Return T as the MST of the graph.
- To check if an edge forms a cycle with T, we can use a **disjoint-set data structure** that supports two operations: find and union.
  - **find(x)** returns the representative element of the set that contains x.
  - **union(x, y)** merges the sets that contain x and y into one set.
  - An edge (u, v) forms a cycle with T if and only if find(u) == find(v).
- Here is an example of applying Kruskal's algorithm to a graph:

![graph](https://i.imgur.com/9XZ6v9f.png)

- The edges are sorted as follows: (D, E) with weight 1, (C, E) with weight 2, (B, C) with weight 3, (A, B) with weight 4, (A, D) with weight 5, (B, E) with weight 6, (C, D) with weight 7.
- Initially, S = {{A}, {B}, {C}, {D}, {E}} and T = {}.
- The first edge (D, E) is added to T and the sets {D} and {E} are merged in S. S = {{A}, {B}, {C}, {D, E}} and T = {(D, E)}.
- The second edge (C, E) is added to T and the sets {C} and {D, E} are merged in S. S = {{A}, {B}, {C, D, E}} and T = {(D, E), (C, E)}.
- The third edge (B, C) is added to T and the sets {B} and {C, D, E} are merged in S. S = {{A}, {B, C, D, E}} and T = {(D, E), (C, E), (B, C)}.
- The fourth edge (A, B) is added to T and the sets {A} and {B, C, D, E} are merged in S. S = {{A, B, C, D, E}} and T = {(D, E), (C, E), (B, C), (A, B)}.
- The algorithm stops as T has V-1 edges. The MST is T with total weight 10.

![mst](https://i.imgur.com/8yfFvQs.png)