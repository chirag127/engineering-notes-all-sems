## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim's algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:
  - Start with an arbitrary vertex as the root of the tree.
  - Repeat until all the vertices are in the tree:
    - Find the minimum weight edge that connects a vertex in the tree to a vertex not in the tree.
    - Add that edge and the new vertex to the tree.
- The algorithm can be implemented using a priority queue to store the edges that connect the vertices in the tree to the vertices not in the tree, and extract the minimum weight edge at each step.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm can be illustrated by the following example:

![Example of Prim's algorithm](https://upload.wikimedia.org/wikipedia/commons/9/9b/PrimAlgDemo.gif)

- The graph has 9 vertices and 14 edges, and the algorithm starts with vertex A as the root of the tree.
- The algorithm adds the edges AB, BC, CD, DE, EF, FG, GH, and HI to the tree, in that order, and the final MCST has a total weight of 37.