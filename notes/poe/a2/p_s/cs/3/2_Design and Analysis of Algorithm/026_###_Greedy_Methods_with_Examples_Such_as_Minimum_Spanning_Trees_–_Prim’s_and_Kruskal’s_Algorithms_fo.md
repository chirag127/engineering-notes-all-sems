 Here are the notes for the topic ### Greedy Methods with Examples Such as Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms:

Greedy Algorithms:
Greedy algorithms make the locally optimum choice at each stage with the hope of finding a global optimum.
They can be efficient but are not guaranteed to always find the optimal solution.

Minimum Spanning Trees:
A minimum spanning tree (MST) of a weighted graph is a tree that connects all vertices together while minimizing the sum of weights of its edges.
They are useful for solving many problems such as finding efficient networks and connectivity.

Prim's Algorithm:
Prim's algorithm is a greedy approach to find the MST. It starts from an arbitrary root vertex and greedily adds the next lightest edge that doesn't create cycles.
1. Initialize a tree with just the root vertex
2. While there are vertices in the graph not in the tree:
3. Find the lightest edge connecting the tree to the remaining graph
4. Add the edge and its endpoint to the tree
Running time: O(E log V) where E is number of edges and V is number of vertices

Kruskal's Algorithm:
Kruskal's algorithm is another greedy approach to find the MST. It sorts all edges by weight and then adds them one by one as long as they do not create cycles.
1. Sort all edges by weight in increasing order
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V - 1) edges in the spanning tree.
Running time: O(E log E) or O(E + log E) where E is number of edges

Advantages and Disadvantages:
Prim's Algorithm
Advantages: Always finds an MST, can implement using heaps for efficient runtime
Disadvantages: May not be space efficient if using an adjacency list representation

Kruskal's Algorithm
Advantages: Always finds an MST, typically more space efficient
Disadvantages: May be slower than Prim's on dense graphs since it involves more sorting

Applications:
Minimum spanning trees have applications in:
- Efficient network creation
- Clustering data
- Image segmentation
- And more!