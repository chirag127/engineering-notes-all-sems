## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

- A **spanning tree** of a graph is a subgraph that contains all the vertices and is a tree (i.e., no cycles).
- A **minimum cost spanning tree (MCST)** of a graph is a spanning tree that has the minimum possible total edge weight among all the spanning trees of the graph.
- **Prim’s algorithm** is a greedy algorithm that finds a MCST of a given undirected graph.
- The algorithm works as follows:

  - Start with an arbitrary vertex as the root of the tree.
  - Repeat until all the vertices are in the tree:
    - Find the minimum weight edge that connects a vertex in the tree to a vertex not in the tree.
    - Add that edge and the new vertex to the tree.
  - Return the tree as the MCST.

- The algorithm can be implemented using a priority queue to store the edges that connect the tree to the rest of the graph, and extract the minimum weight edge at each step.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.
- The algorithm is correct because at each step, it adds the edge that minimizes the cost of the tree, and does not create any cycles. Therefore, the final tree is a spanning tree with the minimum cost.

- An example of applying Prim’s algorithm to a graph is shown below:

```
    2
A-------B
| \     | \
|  \    |  \
|   \   |   \
|    \  |    \
|     \ |     \
|      \|      \
|       C-------D
|      / \     / \
|     /   \   /   \
|    /     \ /     \
|   /       E       \
|  /       / \       \
| /       /   \       \
|/       /     \       \
F-------G-------H-------I
    4       2       3
```

- The MCST of the graph using Prim’s algorithm is shown below (in bold):

```
    2
A-------B
|       | \
|       |  \
|       |   \
|       |    \
|       |     \
|       |      \
|       C-------D
|      /       / \
|     /       /   \
|    /       /     \
|   /       E       \
|  /       /         \
| /       /           \
|/       /             \
F-------G-------H-------I
    4       2       3
```

- The total cost of the MCST is 2 + 2 + 2 + 3 + 4 + 4 + 4 = 21.