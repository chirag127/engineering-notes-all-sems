 Here are the notes for the topic -

## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

**Kruskal's algorithm** -

- Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted undirected graph.
- It finds the minimum cost spanning tree by picking the lowest cost edge that doesn't cause cycles.
- The steps are -

1. Sort all edges in increasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V - 1) edges in the spanning tree.

**Union-Find algorithm** -

- The Union-Find algorithm is used to check if the picked edge forms a cycle with the spanning tree formed so far or not.
- It uses the disjoint-set data structure. Each vertex is initially in its own set. When two vertices are connected, their sets are merged.
- If the two vertices are already in the same set, then a cycle is formed. Else, the sets containing these vertices are merged.
- This is done in O(LogV) time using path compression and ranking techniques.

**Advantages** -

- The time complexity is O(ELogV) where E is the number of edges and V is the number of vertices.
- It is easier to implement than Prim's algorithm.
- It can handle graphs with weights that are not necessarily positive.

**Disadvantages** -

- It may not be efficient for dense graphs as the run time depends on E, the number of edges.
- The actual minimum spanning tree it finds depends on the order in which the edges are taken.

**Examples and applications** -

- Examples could include finding the minimum cost network to connect a set of cities, servers, etc.
- It has applications in minimizing the cost of a network, finding optimal routes, etc.

[Include diagrams and images if required]
[Include sample codes if required]