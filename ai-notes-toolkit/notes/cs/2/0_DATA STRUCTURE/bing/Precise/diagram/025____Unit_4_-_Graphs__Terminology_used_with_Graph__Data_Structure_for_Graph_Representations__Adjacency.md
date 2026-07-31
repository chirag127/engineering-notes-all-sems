## Unit 4 - Graphs

### Terminology used with Graph
- **Graph**: A graph is a set of vertices (or nodes) connected by edges.
- **Vertex**: A vertex is a node in a graph.
- **Edge**: An edge is a connection between two vertices in a graph.
- **Directed Graph**: A directed graph is a graph in which the edges have a direction, from one vertex to another.
- **Undirected Graph**: An undirected graph is a graph in which the edges do not have a direction.
- **Weighted Graph**: A weighted graph is a graph in which the edges have a weight or cost associated with them.

### Data Structure for Graph Representations
- **Adjacency Matrices**: An adjacency matrix is a two-dimensional array in which the element at the ith row and jth column represents the presence or absence of an edge between the ith and jth vertices.
- **Adjacency List**: An adjacency list is an array of linked lists in which the ith element of the array is a linked list containing the neighbors of the ith vertex.
- **Adjacency**: Adjacency refers to the presence of an edge between two vertices in a graph.

### Graph Traversal
- **Depth First Search**: Depth First Search (DFS) is a graph traversal algorithm that starts at a given vertex and explores as far as possible along each branch before backtracking.
- **Breadth First Search**: Breadth First Search (BFS) is a graph traversal algorithm that starts at a given vertex and explores all the neighboring vertices at the present depth level before moving on to the vertices at the next depth level.
- **Connected Component**: A connected component is a subgraph in which any two vertices are connected to each other by a path, and which is connected to no other vertices outside the subgraph.
- **Spanning Trees**: A spanning tree is a subgraph that includes all the vertices of the original graph and is a tree.
- **Minimum Cost Spanning Trees**: A minimum cost spanning tree is a spanning tree with the minimum possible total edge weight.
    - **Prims algorithm**: Prims algorithm is a greedy algorithm that finds a minimum cost spanning tree for a weighted undirected graph.
    - **Kruskal algorithm**: Kruskal algorithm is a greedy algorithm that finds a minimum cost spanning tree for a weighted undirected graph by adding edges in increasing order of their weight, as long as they do not form a cycle.

### Transitive Closure and Shortest Path algorithm
- **Transitive Closure**: The transitive closure of a graph is a graph in which there is an edge between two vertices if and only if there is a path between them in the original graph.
- **Shortest Path algorithm**: A shortest path algorithm finds the shortest path between two vertices in a graph.
    - **Warshal Algorithm**: Warshal algorithm is an algorithm for finding the transitive closure of a graph.
    - **Dijikstra Algorithm**: Dijikstra algorithm is an algorithm for finding the shortest path between two vertices in a weighted graph.