# Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** is a subset of the edges of a connected, edge-weighted graph that connects all the vertices together, without any cycles and with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST for a weighted graph.
- The algorithm works as follows :
  - Sort all the edges in non-decreasing order of their weight.
  - Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
  - Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.
- The algorithm can be implemented using a **priority queue** to store the edges by weight, a **union-find** data structure to check for cycles, and a **queue** to collect the MST edges.
- The time complexity of the algorithm is O(E log E) or O(E log V), where E is the number of edges and V is the number of vertices, as the most expensive part is sorting the edges.
- The space complexity of the algorithm is O(E + V), as we need to store the edges, the union-find data structure, and the MST edges.
- An example of applying the algorithm to a graph is shown below:

![Kruskal's algorithm example](https://media.geeksforgeeks.org/wp-content/uploads/KruskalExample.png)

- The edges are sorted by weight as follows: (7, 6), (8, 2), (6, 5), (0, 1), (2, 5), (8, 6), (2, 3), (7, 8), (0, 7), (1, 2), (3, 4), (4, 5), (1, 7), (3, 5).
- The algorithm picks the smallest edge (7, 6) and adds it to the MST.
- The algorithm picks the next smallest edge (8, 2) and adds it to the MST.
- The algorithm picks the next smallest edge (6, 5) and adds it to the MST.
- The algorithm picks the next smallest edge (0, 1) and adds it to the MST.
- The algorithm picks the next smallest edge (2, 5) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (8, 6) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (2, 3) and adds it to the MST.
- The algorithm picks the next smallest edge (7, 8) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (0, 7) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (1, 2) and adds it to the MST.
- The algorithm picks the next smallest edge (3, 4) and adds it to the MST.
- The algorithm picks the next smallest edge (4, 5) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (1, 7) and discards it as it forms a cycle with the MST.
- The algorithm picks the next smallest edge (3, 5) and discards it as it forms a cycle with the MST.
- The algorithm stops as there are (9-1) = 8 edges in the MST.
- The MST is shown below with the total weight of 37:

![Kruskal's algorithm MST](https://media.geeksforgeeks.org/wp-content/uploads/KruskalOutput.png)