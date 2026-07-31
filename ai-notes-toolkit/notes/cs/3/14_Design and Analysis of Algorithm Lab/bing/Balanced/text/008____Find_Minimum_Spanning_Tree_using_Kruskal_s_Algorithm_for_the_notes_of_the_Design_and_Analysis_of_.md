## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, connected and undirected graph is a subset of the edges that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a graph.
- The algorithm works as follows     :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- To detect if an edge forms a cycle with the spanning tree, we can use a **union-find** data structure that keeps track of the connected components of the graph.
- The time complexity of Kruskal's algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, since the most time consuming operation is sorting the edges .
- The space complexity of Kruskal's algorithm is O(E + V), since we need to store the edges, the spanning tree and the union-find data structure .
- An example of applying Kruskal's algorithm to a graph is shown below:

![Kruskal's algorithm example](https://media.geeksforgeeks.org/wp-content/uploads/KruskalExample.png)

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The MST is initially empty. We pick the smallest edge (7, 6) and add it to the MST.
- We pick the next smallest edge (8, 2) and check if it forms a cycle with the MST. Since it does not, we add it to the MST.
- We repeat this process for the remaining edges, skipping those that form cycles, until we have 8 edges in the MST (the graph has 9 vertices).
- The final MST is shown below, with a total weight of 37:

![Kruskal's algorithm MST](https://media.geeksforgeeks.org/wp-content/uploads/KruskalOutput.png)