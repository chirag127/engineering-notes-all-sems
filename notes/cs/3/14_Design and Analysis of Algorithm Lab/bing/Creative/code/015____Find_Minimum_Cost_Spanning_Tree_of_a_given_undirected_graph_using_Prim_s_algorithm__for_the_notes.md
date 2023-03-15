## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim’s algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:

  - Start with an arbitrary vertex as the root of the MCST.
  - Maintain a set of vertices that are already included in the MCST, and a set of edges that connect the included vertices to the rest of the graph.
  - Repeat until all the vertices are included in the MCST:
    - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph.
    - Add this edge and the corresponding vertex to the MCST, and update the set of edges accordingly.

- The algorithm can be implemented using a priority queue or a heap data structure to store the edges and find the minimum weight edge efficiently.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm is correct because at each step, it adds the edge that minimizes the cost of the MCST so far, and does not create any cycles. Therefore, the final MCST is optimal. This can be proved using a cut-and-paste argument or by contradiction.
- An example of applying Prim’s algorithm to a given undirected graph is shown below:

![Prim's algorithm example](https://i.imgur.com/4wZq3aS.png)

- The steps of the algorithm are:

  - Start with vertex A as the root of the MCST. The set of included vertices is {A}, and the set of edges is {(A, B), (A, C), (A, D)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (A, B) with weight 2. Add this edge and vertex B to the MCST. The set of included vertices is {A, B}, and the set of edges is {(A, C), (A, D), (B, C), (B, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (B, C) with weight 3. Add this edge and vertex C to the MCST. The set of included vertices is {A, B, C}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (C, F)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (C, F) with weight 4. Add this edge and vertex F to the MCST. The set of included vertices is {A, B, C, F}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (F, E), (F, G)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (F, G) with weight 5. Add this edge and vertex G to the MCST. The set of included vertices is {A, B, C, F, G}, and the set of edges is {(A, D), (B, E), (C, D), (C, E), (F, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (C, E) with weight 6. Add this edge and vertex E to the MCST. The set of included vertices is {A, B, C, F, G, E}, and the set of edges is {(A, D), (B, E), (C, D), (F, E)}.
  - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph. This is (A, D) with weight 7. Add this edge and vertex D to the MCST. The set of included vertices is {A, B, C, F, G, E, D}, and the set of edges is empty.
  - All the vertices are included in