## Unit 4 - Graphs

### Terminology used with Graph
- **Vertex**: A vertex, also called a node, is a fundamental unit of which graphs are formed.
- **Edge**: An edge is a connection between two vertices.
- **Degree**: The degree of a vertex is the number of edges connected to it.
- **Path**: A path is a sequence of edges that connect two vertices.
- **Cycle**: A cycle is a path that starts and ends at the same vertex.

### Data Structure for Graph Representations
- **Adjacency Matrices**: An adjacency matrix is a square matrix used to represent a graph. The elements of the matrix indicate whether pairs of vertices are adjacent or not in the graph.
- **Adjacency List**: An adjacency list is a collection of unordered lists used to represent a graph. Each list describes the set of neighbors of a vertex in the graph.
- **Adjacency**: Adjacency is a term used to describe the relationship between two vertices that are connected by an edge.

### Graph Traversal
- **Depth First Search**: Depth First Search (DFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores as far as possible along each branch before backtracking.
- **Breadth First Search**: Breadth First Search (BFS) is an algorithm for traversing or searching tree or graph data structures. It starts at the root node and explores all the neighboring nodes at the present depth level before moving on to the nodes at the next depth level.
- **Connected Component**: A connected component is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.
- **Spanning Trees**: A spanning tree is a subgraph that is a tree and connects all the vertices together.
- **Minimum Cost Spanning Trees**: A minimum cost spanning tree is a spanning tree with weight less than or equal to the weight of every other spanning tree.
    - **Prims algorithm**: Prim's algorithm is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph.
    - **Kruskal algorithm**: Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest.

### Transitive Closure and Shortest Path algorithm
- **Warshal Algorithm**: Warshall's algorithm is an algorithm for finding the transitive closure of a binary relation.
- **Dijikstra Algorithm**: Dijkstra's algorithm is an algorithm for finding the shortest paths between nodes in a graph.