## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm

Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to follow to apply Prim's algorithm:

1. Initialize the minimum spanning tree with a vertex chosen at random.
2. Find all the edges that connect the tree to new vertices, find the minimum and add it to the tree.
3. Keep repeating step 2 until all the vertices are in the tree.

This algorithm can be implemented using a priority queue to select the next edge with the minimum weight. The time complexity of this algorithm is O(E log V), where E is the number of edges and V is the number of vertices in the graph.

This algorithm is useful in the Design and Analysis of Algorithm Lab in the subject of Real Time System as it provides an efficient way to find the minimum cost spanning tree of a given undirected graph. It is an important concept to understand and can be applied in various real-world scenarios.