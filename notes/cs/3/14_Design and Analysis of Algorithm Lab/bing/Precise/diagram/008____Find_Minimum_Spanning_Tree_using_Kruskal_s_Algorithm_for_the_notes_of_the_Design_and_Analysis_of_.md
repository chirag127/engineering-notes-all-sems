## Find Minimum Spanning Tree using Kruskal’s Algorithm

Kruskal's algorithm is a greedy algorithm in graph theory that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to find the minimum spanning tree using Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

This algorithm can be used in the Design and Analysis of Algorithm Lab in the subject of Real Time System to find the minimum spanning tree of a given graph. It is an efficient and widely used algorithm for this purpose.