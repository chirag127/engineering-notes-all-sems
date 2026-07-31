## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps for implementing Kruskal's algorithm:
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

To detect if an edge forms a cycle with the current spanning tree, we can use the Union-Find algorithm. The Union-Find algorithm is used to keep track of a partition of a set into disjoint subsets. It has two primary operations: Find and Union.

- **Find**: Determine which subset a particular element is in. This can be used to determine if two elements are in the same subset.
- **Union**: Join two subsets into a single subset.

In the context of Kruskal's algorithm, we can use the Union-Find algorithm to keep track of the connected components in the current spanning tree. When we consider adding an edge to the tree, we can use the Find operation to determine if the two vertices connected by the edge are already in the same connected component. If they are, then adding the edge would create a cycle, so we discard it. If they are not, then we can use the Union operation to merge the two connected components into one.

Here is an example of how the algorithm might work on a given connected undirected graph:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree.
