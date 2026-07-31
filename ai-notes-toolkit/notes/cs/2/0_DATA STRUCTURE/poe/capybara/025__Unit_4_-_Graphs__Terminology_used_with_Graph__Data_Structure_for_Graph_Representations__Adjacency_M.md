## Unit 4 - Graphs: Terminology used with Graph, Data Structure for Graph Representations: Adjacency Matrices, Adjacency List, Adjacency. Graph Traversal: Depth First Search and Breadth First Search, Connected Component, Spanning Trees, Minimum Cost Spanning Trees: Prims and Kruskal algorithm. Transitive Closure and Shortest Path algorithm: Warshal Algorithm and Dijikstra Algorithm.

### Terminology used with Graph
- A **graph** is a non-linear data structure consisting of vertices and edges. 
- Vertices are the nodes or points in a graph, and edges are the lines connecting them. 
- A **directed graph** is a graph where the edges have a specific direction, while an **undirected graph** has edges without a specific direction.
- The **degree** of a vertex is the number of edges connecting it. 
- A **path** is a sequence of vertices connected by edges. 
- A **cycle** is a path where the first and last vertices are the same. 
- A **subgraph** is a graph that is a subset of another graph. 

### Data Structure for Graph Representations
- There are three common ways to represent a graph: **adjacency matrix**, **adjacency list**, and **adjacency set**. 
- An **adjacency matrix** is a 2D array where the rows and columns represent vertices, and each entry represents whether there is an edge between the corresponding vertices.
- An **adjacency list** is a collection of lists, where each list corresponds to a vertex and contains the vertices it is connected to.
- An **adjacency set** is a set of sets, where each set corresponds to a vertex and contains the vertices it is connected to.

### Graph Traversal
- Graph traversal is the process of visiting all the vertices and edges in a graph. 
- Two common methods of graph traversal are **depth first search (DFS)** and **breadth first search (BFS)**. 
- In DFS, we start at a vertex and explore as far as possible along each branch before backtracking. 
- In BFS, we start at a vertex and visit all the vertices that are one edge away before visiting vertices that are two edges away, and so on. 
- A **connected component** is a subgraph where all the vertices are connected to each other.

### Spanning Trees
- A **spanning tree** is a subgraph that contains all the vertices of a graph and is a tree (i.e., has no cycles).
- Two common algorithms to find minimum cost spanning trees are **Prim's algorithm** and **Kruskal's algorithm**. 
- Prim's algorithm starts with a single vertex and grows the tree by adding the edge with the smallest weight that connects it to the tree. 
- Kruskal's algorithm starts with all the vertices as separate trees and grows the forest by adding the edge with the smallest weight that connects two different trees.

### Transitive Closure
- The **transitive closure** of a graph is a new graph that shows all the paths between vertices in the original graph. 
- One common algorithm to find the transitive closure is the **Warshal algorithm**.

### Shortest Path Algorithm
- The **shortest path algorithm** is used to find the shortest path between two vertices in a graph. 
- Two common algorithms to find the shortest path are **Dijkstra's algorithm** and **Bellman-Ford algorithm**. 
- Dijkstra's algorithm starts at a vertex and grows the shortest path tree by adding the vertex with the smallest distance from the tree. 
- Bellman-Ford algorithm works by relaxing all the edges in the graph repeatedly until the shortest path is found.