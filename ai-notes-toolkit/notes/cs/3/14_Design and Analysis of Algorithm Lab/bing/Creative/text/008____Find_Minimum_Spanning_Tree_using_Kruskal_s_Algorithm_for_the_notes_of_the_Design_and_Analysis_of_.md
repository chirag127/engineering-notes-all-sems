## Find Minimum Spanning Tree using Kruskal’s Algorithm

- A **minimum spanning tree (MST)** of a weighted, undirected graph is a subgraph that connects all the vertices with the minimum possible total edge weight.
- **Kruskal's algorithm** is a greedy algorithm that finds a MST by selecting the edges with the lowest weight that do not form a cycle  .
- The algorithm works as follows  :
  - Sort all the edges in non-decreasing order of their weight.
  - Initialize a forest of disjoint sets, where each set contains one vertex of the graph.
  - Initialize an empty queue to store the MST edges.
  - Repeat until the queue has V-1 edges, where V is the number of vertices in the graph:
    - Pick the smallest edge from the sorted edge list and remove it.
    - If the edge connects two different sets in the forest, then add it to the queue and union the two sets.
    - Otherwise, discard the edge.
  - Return the queue as the MST.
- The algorithm can be implemented using a priority queue to store the sorted edges, a union-find data structure to maintain the forest of disjoint sets, and a queue to collect the MST edges.
- The time complexity of the algorithm is O(E log E), where E is the number of edges in the graph, since the sorting step dominates the other operations.
- The algorithm can handle graphs that are not connected, in which case it will find a **minimum spanning forest**, which is a collection of MSTs for each connected component.
- The algorithm is optimal, meaning that it always finds a MST with the minimum possible weight.