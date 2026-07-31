# Unit 4 - Graphs

## Terminology used with Graph

- A graph is a collection of **vertices** (also called nodes or points) and **edges** (also called arcs or lines) that connect pairs of vertices.
- A graph can be **directed** or **undirected**. A directed graph has edges that are associated with a direction, indicating the source and destination vertices. An undirected graph has edges that are not associated with any direction, indicating a mutual relationship between the vertices.
- A graph can be **weighted** or **unweighted**. A weighted graph has edges that are assigned a numerical value, called the weight or cost, that represents some attribute of the edge, such as distance, time, or capacity. An unweighted graph has edges that are not assigned any weight or cost.
- A graph can be **simple** or **non-simple**. A simple graph has no **loops** (edges that connect a vertex to itself) and no **multiple edges** (more than one edge between the same pair of vertices). A non-simple graph may have loops and multiple edges.
- A graph can be **cyclic** or **acyclic**. A cyclic graph has a **cycle** (a path that starts and ends at the same vertex) and an acyclic graph has no cycles.
- A graph can be **connected** or **disconnected**. A connected graph has a **path** (a sequence of edges that connects two vertices) between any pair of vertices. A disconnected graph has at least one pair of vertices that are not connected by any path.
- A graph can be **complete** or **incomplete**. A complete graph has an edge between every pair of vertices. An incomplete graph has at least one pair of vertices that are not connected by any edge.
- A **subgraph** of a graph is a graph that consists of a subset of the vertices and edges of the original graph.
- A **spanning subgraph** of a graph is a subgraph that contains all the vertices of the original graph.
- A **spanning tree** of a graph is a spanning subgraph that is a tree (a connected acyclic graph).
- A **minimum spanning tree** of a weighted graph is a spanning tree that has the minimum possible sum of edge weights among all spanning trees of the graph.

## Data Structure for Graph Representations

- There are different ways to represent a graph in a computer, depending on the type and size of the graph, and the operations that need to be performed on the graph.
- The most common data structures for graph representations are **adjacency matrices**, **adjacency lists**, and **adjacency maps**.

### Adjacency Matrices

- An adjacency matrix is a two-dimensional array of size n x n, where n is the number of vertices in the graph.
- The element at row i and column j of the matrix, denoted by A[i][j], indicates the presence or absence of an edge between vertex i and vertex j in the graph.
- If the graph is unweighted, A[i][j] can be either 0 or 1, where 0 means no edge and 1 means an edge.
- If the graph is weighted, A[i][j] can be either 0 or the weight of the edge between vertex i and vertex j.
- If the graph is directed, A[i][j] represents the edge from vertex i to vertex j, and A[j][i] represents the edge from vertex j to vertex i. If the graph is undirected, A[i][j] and A[j][i] are the same.
- The main advantage of an adjacency matrix is that it allows constant-time access to check if there is an edge between any two vertices, or to get the weight of an edge if it exists.
- The main disadvantage of an adjacency matrix is that it requires O(n^2) space, which can be wasteful if the graph is sparse (has few edges compared to the number of vertices).

### Adjacency Lists

- An adjacency list is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array, denoted by L[i], is a linked list of the vertices that are adjacent to vertex i in the graph.
- If the graph is unweighted, each node of the linked list contains only the vertex number of the adjacent vertex.
- If the graph is weighted, each node of the linked list contains the vertex number and the weight of the edge to the adjacent vertex.
- If the graph is directed, L[i] represents the vertices that can be reached from vertex i by following an edge. If the graph is undirected, L[i] represents