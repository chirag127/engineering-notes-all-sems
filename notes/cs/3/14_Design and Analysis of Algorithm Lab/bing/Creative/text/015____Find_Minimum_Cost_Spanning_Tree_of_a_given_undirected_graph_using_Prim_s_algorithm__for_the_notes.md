## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., has no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:

  - Start with an arbitrary vertex as the root of the MCST.
  - Maintain a set of vertices that are already included in the MCST, and a set of edges that connect the included vertices to the rest of the graph.
  - Repeat until all the vertices are included in the MCST:
    - Find the edge with the minimum weight among the edges that connect the included vertices to the rest of the graph.
    - Add this edge and the corresponding vertex to the MCST, and update the set of edges accordingly.
  - Return the MCST.

- The algorithm can be implemented using a priority queue or a heap to store the edges and their weights, and to find the minimum weight edge in each iteration.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The space complexity of the algorithm is O(E + V), where E is the number of edges and V is the number of vertices in the graph.
- An example of applying Prim's algorithm to a given undirected graph is shown below:

![Prim's algorithm example](https://upload.wikimedia.org/wikipedia/commons/9/9b/PrimAlgDemo.gif)

- The MCST of the graph has a total weight of 16, and consists of the edges AB, BC, CD, DE, and EF.