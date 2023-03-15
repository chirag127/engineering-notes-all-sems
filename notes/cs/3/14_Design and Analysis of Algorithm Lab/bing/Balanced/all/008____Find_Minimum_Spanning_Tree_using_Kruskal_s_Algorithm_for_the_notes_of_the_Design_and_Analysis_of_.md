## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, undirected graph is a subgraph that connects all the vertices with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST by selecting the edges with the smallest weights in ascending order, as long as they do not create a cycle in the MST .
- The algorithm can be described as follows  :

  1. Sort all the edges in non-decreasing order of their weight.
  2. Pick the smallest edge and check if it forms a cycle with the MST constructed so far. If not, include it in the MST. If yes, discard it.
  3. Repeat step 2 until there are (V-1) edges in the MST, where V is the number of vertices in the graph.
  4. Return the MST.

- The algorithm can be implemented using a **priority queue** to store the edges in sorted order, a **union-find** data structure to check for cycles, and a **queue** to store the MST edges.
- The algorithm can be illustrated with an example:

  - Input graph:

    ![input graph](https://media.geeksforgeeks.org/wp-content/uploads/MST1.jpg)

  - Sorted edges:

    | Edge | Weight |
    |------|--------|
    | (7,6) | 1 |
    | (8,2) | 2 |
    | (6,5) | 2 |
    | (0,1) | 4 |
    | (2,5) | 4 |
    | (8,6) | 6 |
    | (2,3) | 7 |
    | (7,8) | 7 |
    | (0,7) | 8 |
    | (1,2) | 8 |
    | (3,4) | 9 |
    | (5,4) | 10 |
    | (1,7) | 11 |
    | (3,5) | 14 |

  - MST construction:

    - Pick edge (7,6) with weight 1. It does not form a cycle, so include it in the MST.

      ![step 1](https://media.geeksforgeeks.org/wp-content/uploads/MST2.jpg)

    - Pick edge (8,2) with weight 2. It does not form a cycle, so include it in the MST.

      ![step 2](https://media.geeksforgeeks.org/wp-content/uploads/MST3.jpg)

    - Pick edge (6,5) with weight 2. It does not form a cycle, so include it in the MST.

      ![step 3](https://media.geeksforgeeks.org/wp-content/uploads/MST4.jpg)

    - Pick edge (0,1) with weight 4. It does not form a cycle, so include it in the MST.

      ![step 4](https://media.geeksforgeeks.org/wp-content/uploads/MST5.jpg)

    - Pick edge (2,5) with weight 4. It forms a cycle with the MST, so discard it.

      ![step 5](https://media.geeksforgeeks.org/wp-content/uploads/MST6.jpg)

    - Pick edge (8,6) with weight 6. It forms a cycle with the MST, so discard it.

      ![step 6](https://media.geeksforgeeks.org/wp-content/uploads/MST7.jpg)

    - Pick edge (2,3) with weight 7. It does not form a cycle, so include it in the MST.

      ![step 7](https://media.geeksforgeeks.org/wp-content/uploads/MST8.jpg)

    - Pick edge (7,8) with weight 7. It forms a cycle with the MST, so discard it.

      ![step 8](https://media.geeksforgeeks.org/wp-content/uploads/MST9.jpg)

    - Pick edge (0,7) with weight 8. It forms a cycle with the MST, so discard it.

      ![step 9](https://media.geeksforgeeks.org/wp-content/uploads/MST10.jpg)

    - Pick edge (1,2) with weight 8. It does not form a cycle, so include it in the MST.