
## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm

Kruskal's algorithm is an algorithm used to find the Minimum Cost Spanning Tree (MCST) of a given connected undirected graph. The algorithm works by sorting the edges of the graph by weight and then adding them to the tree one by one, ensuring that the tree remains connected. The algorithm uses the Union-Find data structure to detect cycles in the graph and prevent them from forming.

The algorithm can be used to solve various problems related to graph theory, such as finding the shortest path between two nodes, or finding the minimum cost of a network. It is also useful in real-time systems, where it can be used to find the most efficient route from one point to another in a given time frame.

### Steps of the algorithm

1. Sort all the edges of the graph in non-decreasing order of their weights.
2. Pick the smallest edge and check if it forms a cycle with the spanning tree formed so far.
  - If the edge does not form a cycle, include it in the spanning tree.
  - If the edge forms a cycle, discard it.
3. Repeat steps 2 and 3 until there are (V-1) edges in the spanning tree.

### Union-Find Algorithms

Union-Find algorithms are used to detect cycles in a graph. The algorithms work by keeping track of the components of a graph, and if two components are connected, they are merged into a single component. This process is repeated until all the components are merged into one component.

If a cycle is detected, the algorithm will not add the edge to the spanning tree as it would create a cycle.

### Time Complexity

The time complexity of Kruskal's algorithm is O(ElogE), where E is the number of edges in the graph. This is because the algorithm sorts the edges of the graph in non-decreasing order of their weights, which takes O(ElogE) time. The rest of the algorithm takes linear time, making the overall time complexity O(ElogE).