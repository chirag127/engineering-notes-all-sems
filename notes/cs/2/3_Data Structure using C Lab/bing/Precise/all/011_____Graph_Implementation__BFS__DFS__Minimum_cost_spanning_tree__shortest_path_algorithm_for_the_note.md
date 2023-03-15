# Graph Implementation, BFS, DFS, Minimum cost spanning tree, shortest path algorithm

## Graph Implementation
A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. There are two common ways to implement a graph: using an adjacency matrix or using an adjacency list.

### Adjacency Matrix
An adjacency matrix is a two-dimensional array where the element at row i and column j represents the edge between vertex i and vertex j. If the graph is undirected, the adjacency matrix is symmetric. If the graph is directed, the adjacency matrix is not necessarily symmetric.

### Adjacency List
An adjacency list is an array of linked lists. The linked list at index i represents the edges connected to vertex i. Each element in the linked list contains the index of the vertex it is connected to and the weight of the edge (if the graph is weighted).

## Breadth-First Search (BFS)
Breadth-First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the tree root (or some arbitrary node of a graph) and explores the neighbor nodes first, before moving to the next level neighbors.

## Depth-First Search (DFS)
Depth-First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. The algorithm starts at the root node (or some arbitrary node of a graph) and explores as far as possible along each branch before backtracking.

## Minimum Cost Spanning Tree
A minimum cost spanning tree is a spanning tree of a connected, undirected graph that connects all the vertices together with the minimum possible total edge weight. There are several algorithms to find the minimum cost spanning tree, including Kruskal's algorithm and Prim's algorithm.

## Shortest Path Algorithm
The shortest path algorithm is used to find the shortest path between two vertices in a graph. There are several algorithms to find the shortest path, including Dijkstra's algorithm and the Bellman-Ford algorithm.