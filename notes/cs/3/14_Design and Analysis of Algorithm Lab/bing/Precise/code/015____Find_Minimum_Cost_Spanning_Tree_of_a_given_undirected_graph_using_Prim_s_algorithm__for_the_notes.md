## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to implement Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

The time complexity of Prim's algorithm depends on the data structures used for the graph and for ordering the edges by weight, which can be done using a priority queue. Using an adjacency matrix representation and a binary heap-based priority queue, Prim's algorithm can be shown to run in O(V^2) time, where V is the number of vertices in the graph.

This algorithm can be useful for solving problems in the Design and Analysis of Algorithm Lab in the subject of Real Time Systems. It is important to understand the steps and the time complexity of the algorithm in order to apply it effectively.