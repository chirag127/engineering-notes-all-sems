 Here is the content in markdown format without any emojis or external links, being formal and written in points:

## Find Minimum Spanning Tree using Kruskal’s Algorithm

1. Take all edges of the graph and store them in a min-heap based on their weights. This step takes O(E log E) time where E is the number of edges.
2. Repeat the following steps until there are (V - 1) edges in the spanning tree:

- Extract the minimum weight edge from the min-heap.
- Check if the extracted edge is creating a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.

3. The resultant spanning tree will be the minimum spanning tree (MST) of the given graph.

This algorithm runs in O(E log E) time if implemented using min-heap. The space complexity is O(E) as we need to store all edges.

Kruskal's algorithm follows greedy approach as in every step it picks the smallest weight edge that doesn't cause a cycle and it leads to minimum spanning tree.

**Uses:**

- To find the minimum cost to connect all vertices of a graph.
- Widely used in network applications to find least cost paths.

**Advantages:**

- Simple and easy to implement.
- Runs in O(E log E) time which is faster than Prim's algorithm for sparse graphs.

**Disadvantages:**

- Does not work for disconnected graphs.