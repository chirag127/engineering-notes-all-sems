## Find Minimum Cost Spanning Tree of a given connected undirected graph using Kruskal's algorithm. Use Union-Find algorithms in your program.

Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected weighted graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized.

Here are the steps to implement Kruskal's algorithm:

1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step 2 until there are (V-1) edges in the spanning tree, where V is the number of vertices in the given graph.

To detect if an edge forms a cycle with the current spanning tree, we can use the Union-Find algorithm. This algorithm keeps track of the connected components in the graph and allows us to efficiently check if two vertices are in the same connected component.

Here is an example of how to implement the Union-Find algorithm:

1. Create a parent array to keep track of the parent of each vertex in the connected components.
2. Initialize all the vertices as individual sets with only one element.
3. To find the parent of a vertex, follow the parent pointers until you reach the root of the set.
4. To merge two sets, make the root of one set the parent of the root of the other set.

With the help of the Union-Find algorithm, we can efficiently implement Kruskal's algorithm to find the minimum cost spanning tree of a given connected undirected graph.