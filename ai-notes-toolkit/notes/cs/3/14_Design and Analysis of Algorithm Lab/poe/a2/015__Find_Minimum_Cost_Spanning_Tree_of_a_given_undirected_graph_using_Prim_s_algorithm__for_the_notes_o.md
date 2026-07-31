 Here are the notes in Markdown format without any emojis or external links:

## Find Minimum Cost Spanning Tree of a given undirected graph using Prim’s algorithm.

* Prim’s algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
* It starts from an arbitrary root vertex and greedily includes the lowest weight edge that doesn't create cycles.
* The time complexity of Prim's algorithm is O(E log V) where E is the number of edges and V is the number of vertices in the graph.
* The steps for Prim's algorithm are:

1. Select a root vertex arbitrarily. Mark it as visited.
2. Find the adjacent unvisited vertex u that has the least weight w. Include w into MST. Mark u as visited.
3. Find an adjacent unvisited vertex v of already included vertex u that has the least weight w. Include w into MST. Mark v as visited.
4. Repeat step#3 until all vertices are included in MST.

* The algorithm stops when all vertices are included in MST. The edges included form the minimum spanning tree with minimum total weight.
* An example graph and running Prim's algorithm on it is shown below:

[A graph is shown with example weights on edges and the MST formed from Prim's algorithm highlighted]

* The time complexity can be reduced to O(E log V) using efficient data structures like Fibonacci heaps or binary heaps. This improves the efficiency for sparse graphs.
* Prim's algorithm has a lot of applications in computer networks, circuit designing, etc. where minimum cost connections are necessary.