# Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and some (or possibly all) of the edges of the graph.
- A **minimum cost spanning tree** (MCST) of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph by starting from an arbitrary vertex and adding the cheapest edge that connects a vertex in the tree to a vertex not in the tree, until all the vertices are in the tree.
- The steps of Prim's algorithm are as follows:

  1. Initialize a set S to contain the starting vertex and an empty set T to store the edges of the MCST.
  2. Repeat until S contains all the vertices of the graph:
     - Find the edge with the minimum weight that connects a vertex in S to a vertex not in S. If there are multiple such edges, choose any one of them arbitrarily.
     - Add the edge to T and the vertex not in S to S.
  3. Return T as the MCST of the graph.

- The following is an example of applying Prim's algorithm to a given undirected graph:

![graph](https://i.imgur.com/1RyY6Za.png)

  - Start from vertex A and add it to S. The cheapest edge from S to V-S is (A, B) with weight 2, so add it to T and B to S.
  - The cheapest edge from S to V-S is now (B, C) with weight 3, so add it to T and C to S.
  - The cheapest edge from S to V-S is now (A, D) with weight 5, so add it to T and D to S.
  - The cheapest edge from S to V-S is now (C, E) with weight 4, so add it to T and E to S.
  - The cheapest edge from S to V-S is now (D, F) with weight 6, so add it to T and F to S.
  - The cheapest edge from S to V-S is now (E, G) with weight 5, so add it to T and G to S.
  - Now S contains all the vertices of the graph, so the algorithm terminates and returns T as the MCST of the graph.

![mcst](https://i.imgur.com/9lXy0fS.png)

- The total weight of the MCST is 2 + 3 + 5 + 4 + 6 + 5 = 25.