# Unit 4 - Graphs

- A graph is a collection of vertices (or nodes) and edges (or arcs) that connect them.
- A graph can be directed or undirected, depending on whether the edges have a direction or not.
- A graph can be weighted or unweighted, depending on whether the edges have a numerical value or not.
- A graph can be simple or complex, depending on whether it has loops (edges that connect a vertex to itself) or multiple edges (more than one edge between two vertices) or not.
- A graph can be cyclic or acyclic, depending on whether it has a path that starts and ends at the same vertex or not.
- A graph can be connected or disconnected, depending on whether there is a path between any two vertices or not.
- A graph can be complete or incomplete, depending on whether there is an edge between every pair of vertices or not.

## Data Structure for Graph Representations

- There are different ways to represent a graph in a computer, depending on the type and size of the graph and the operations that need to be performed on it.
- The most common data structures for graph representations are adjacency matrices, adjacency lists, and adjacency maps.

### Adjacency Matrices

- An adjacency matrix is a two-dimensional array of size n x n, where n is the number of vertices in the graph.
- The element at row i and column j of the matrix indicates the presence or absence of an edge between vertex i and vertex j.
- If the graph is unweighted, the element can be either 0 or 1, where 0 means no edge and 1 means an edge.
- If the graph is weighted, the element can be either 0 or the weight of the edge, where 0 means no edge and a positive number means an edge with that weight.
- If the graph is directed, the element at row i and column j indicates the edge from vertex i to vertex j, and the element at row j and column i indicates the edge from vertex j to vertex i.
- If the graph is undirected, the matrix is symmetric, meaning that the element at row i and column j is equal to the element at row j and column i.
- The advantage of using an adjacency matrix is that it is easy to check if there is an edge between two vertices, or to find the weight of an edge, by accessing the corresponding element in the matrix.
- The disadvantage of using an adjacency matrix is that it takes O(n^2) space, which can be wasteful if the graph is sparse (has few edges compared to the number of vertices).
- Another disadvantage is that it takes O(n) time to find the neighbors of a vertex, or to add or remove an edge, by scanning the entire row or column of the matrix.

### Adjacency Lists

- An adjacency list is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a linked list of the vertices that are adjacent to vertex i, meaning that there is an edge between them.
- If the graph is unweighted, the linked list contains only the vertex numbers of the adjacent vertices.
- If the graph is weighted, the linked list contains pairs of vertex numbers and edge weights of the adjacent vertices.
- If the graph is directed, the linked list contains only the vertices that are reachable from vertex i, meaning that there is an edge from vertex i to them.
- If the graph is undirected, the linked list contains all the vertices that are connected to vertex i by an edge, regardless of the direction.
- The advantage of using an adjacency list is that it takes O(m + n) space, where m is the number of edges in the graph, which can be efficient if the graph is sparse.
- Another advantage is that it takes O(1) time to find the neighbors of a vertex, or to add or remove an edge, by accessing the corresponding linked list in the array.
- The disadvantage of using an adjacency list is that it takes O(n) time to check if there is an edge between two vertices, or to find the weight of an edge, by traversing the linked list of one of the vertices.

### Adjacency Maps

- An adjacency map is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a map (or a hash table) of the vertices that are adjacent to vertex i, meaning that there is an edge between them.
- The key of the map is the vertex number of the adjacent vertex, and the value of the map is the weight of the edge between them.
- If the graph is unweighted, the value of the map can be