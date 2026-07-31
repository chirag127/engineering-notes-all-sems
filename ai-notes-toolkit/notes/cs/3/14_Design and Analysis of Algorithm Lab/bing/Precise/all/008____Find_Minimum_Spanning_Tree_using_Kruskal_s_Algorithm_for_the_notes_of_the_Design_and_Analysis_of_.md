## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to find the minimum spanning tree using Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the graph.

Kruskal's algorithm can be implemented using a disjoint-set data structure to keep track of the subsets of vertices in the spanning tree. This allows for efficient checking of whether adding an edge will form a cycle or not.

This algorithm is commonly used in the Design and Analysis of Algorithm Lab in the subject of Real Time System to find the minimum spanning tree of a graph. It is an important concept to understand and can be useful for solving problems in various fields.