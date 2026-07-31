 Here are the notes in Markdown format:

## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

* Kruskal's algorithm:

1. Sort all the edges in increasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V - 1) edges in the spanning tree.

* Steps:

1. Sort all edges in increasing order of cost.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V - 1) edges in the spanning tree.

* Union-Find algorithm:

1. Initially, all vertices are in disjoint sets.
2. When an edge (u, v) is considered, check if u and v belong to same set. If they belong to same set, discard the edge, else include it in MST and merge the sets containing u and v.
3. This is implemented using a disjoint-set data structure that supports two operations:

* Find(x) - Returns the set that x belongs to.
* Union(x, y) - Merges the sets containing x and y.

* The time complexity of Kruskal's algorithm using Union-Find is O((E log V) + VE), where E is number of edges and V is number of vertices in the graph.

The content is written in points and formal tone without any emojis or external links as specified. Please let me know if you would like me to modify or add anything.