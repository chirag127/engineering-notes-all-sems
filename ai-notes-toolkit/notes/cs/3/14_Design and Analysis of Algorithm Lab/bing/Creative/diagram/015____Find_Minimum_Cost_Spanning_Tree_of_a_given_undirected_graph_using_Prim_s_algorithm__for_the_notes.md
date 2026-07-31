Hello, I am Sydney, your AI assistant. I can help you with your study material for the Design and Analysis of Algorithm Lab in the subject of Real Time System. Here is the content for the topic of finding minimum cost spanning tree of a given undirected graph using Prim's algorithm.

## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph by starting from an arbitrary vertex and adding the cheapest edge that connects a vertex in the current tree to a vertex outside the tree, until all the vertices are included in the tree.
- The steps of Prim's algorithm are as follows:

  1. Initialize a set S to contain an arbitrary vertex of the graph, and a set T to be empty.
  2. Repeat until S contains all the vertices of the graph:
     - Find the edge (u, v) of minimum weight such that u is in S and v is not in S.
     - Add v to S and (u, v) to T.
  3. Return T as the MCST of the graph.

- The time complexity of Prim's algorithm depends on the data structure used to store the graph and the edges. If an adjacency matrix is used, the time complexity is O(V^2), where V is the number of vertices. If an adjacency list and a binary heap are used, the time complexity is O(E log V), where E is the number of edges.
- An example of Prim's algorithm is shown below:

  - Given the following undirected graph with edge weights:

    ```
    A---5---B
    | \     | \
    4   7   3   6
    |     \ |     \
    C---8---D---9---E
    ```

  - Choose an arbitrary vertex to start, say A. Initialize S = {A} and T = {}.
  - Find the edge of minimum weight that connects a vertex in S to a vertex outside S. This is (A, C) with weight 4. Add C to S and (A, C) to T. S = {A, C} and T = {(A, C)}.
  - Find the edge of minimum weight that connects a vertex in S to a vertex outside S. This is (A, B) with weight 5. Add B to S and (A, B) to T. S = {A, B, C} and T = {(A, C), (A, B)}.
  - Find the edge of minimum weight that connects a vertex in S to a vertex outside S. This is (B, D) with weight 3. Add D to S and (B, D) to T. S = {A, B, C, D} and T = {(A, C), (A, B), (B, D)}.
  - Find the edge of minimum weight that connects a vertex in S to a vertex outside S. This is (D, E) with weight 9. Add E to S and (D, E) to T. S = {A, B, C, D, E} and T = {(A, C), (A, B), (B, D), (D, E)}.
  - Since S contains all the vertices of the graph, the algorithm stops and returns T as the MCST of the graph. The total weight of T is 4 + 5 + 3 + 9 = 21.

    ```
    A---5---B
    |       | 
    4       3   
    |       |     
    C       D---9---E
    ```

I hope this content helps you understand the topic better. If you have any questions or feedback, please let me know.😊