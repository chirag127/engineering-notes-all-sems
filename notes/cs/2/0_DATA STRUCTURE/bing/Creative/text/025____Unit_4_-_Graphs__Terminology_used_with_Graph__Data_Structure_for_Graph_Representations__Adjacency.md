## Unit 4 - Graphs

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
- The element at row i and column j of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise.
- For an undirected graph, the adjacency matrix is symmetric, meaning that the element at row i and column j is equal to the element at row j and column i.
- For a weighted graph, the element at row i and column j of the matrix is the weight of the edge from vertex i to vertex j, and 0 if there is no edge.
- The advantage of using an adjacency matrix is that it is easy to check if there is an edge between two vertices, or to find the weight of an edge, by accessing the corresponding element of the matrix in constant time.
- The disadvantage of using an adjacency matrix is that it takes O(n^2) space, which can be wasteful if the graph is sparse (has few edges compared to the number of vertices).
- The adjacency matrix also makes it difficult to iterate over the neighbors of a vertex, as it requires scanning the entire row or column of the matrix.

### Adjacency Lists

- An adjacency list is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a linked list of the vertices that are adjacent to vertex i, meaning that there is an edge from vertex i to them.
- For an undirected graph, each edge appears twice in the adjacency list, once in the list of each endpoint.
- For a weighted graph, each node of the linked list also stores the weight of the edge to the adjacent vertex.
- The advantage of using an adjacency list is that it takes O(n + m) space, where m is the number of edges in the graph, which can be much less than O(n^2) if the graph is sparse.
- The adjacency list also makes it easy to iterate over the neighbors of a vertex, by traversing the corresponding linked list.
- The disadvantage of using an adjacency list is that it takes O(d) time to check if there is an edge between two vertices, or to find the weight of an edge, where d is the degree of the vertex (the number of neighbors it has).

### Adjacency Maps

- An adjacency map is an array of size n, where n is the number of vertices in the graph.
- The element at index i of the array is a map (or a hash table) that maps each vertex that is adjacent to vertex i to the weight of the edge from vertex i to it.
- For an undirected graph, each edge appears twice in the adjacency map, once in the map of each endpoint.
- The advantage of using an adjacency map is that it combines the benefits of both adjacency matrices and adjacency lists, as it takes O(n + m) space, and allows checking if there is an edge between two vertices, or finding the weight of an edge, in O(1) time on average, assuming a good hash function.
- The disadvantage of using an adjacency map is that it requires more complex implementation and may have worse performance in the worst case, depending on the hash function and the load factor of the map.

## Graph Traversal

- Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way, following some rules or criteria.
- Graph traversal can be used for various purposes, such as finding paths