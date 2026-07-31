### Representation of graphs

A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices. A graph can be used to model many types of relations and processes in physical, biological, social and information systems.

There are different ways to represent a graph, depending on the purpose and the type of the graph. Some of the common representations are:

- **Adjacency matrix**: An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric, meaning that the entry in the i-th row and j-th column is equal to the entry in the j-th row and i-th column. For a directed graph, the adjacency matrix is not necessarily symmetric, meaning that the entry in the i-th row and j-th column may not be equal to the entry in the j-th row and i-th column. For a weighted graph, the entry in the i-th row and j-th column is the weight of the edge from vertex i to vertex j, instead of 1 or 0.

  An example of an adjacency matrix for an undirected graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 1 |
  | 2 | 1 | 0 | 1 | 0 |
  | 3 | 0 | 1 | 0 | 1 |
  | 4 | 1 | 0 | 1 | 0 |

  An example of an adjacency matrix for a directed graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 |
  | 2 | 0 | 0 | 1 | 0 |
  | 3 | 0 | 0 | 0 | 1 |
  | 4 | 1 | 0 | 0 | 0 |

  An example of an adjacency matrix for a weighted graph with 4 vertices is:

  |   | 1 | 2 | 3 | 4 |
  |---|---|---|---|---|
  | 1 | 0 | 2 | 0 | 4 |
  | 2 | 2 | 0 | 3 | 0 |
  | 3 | 0 | 3 | 0 | 5 |
  | 4 | 4 | 0 | 5 | 0 |

  The advantages of using an adjacency matrix are:

  - It is easy to check if there is an edge between two vertices, by looking at the corresponding entry in the matrix.
  - It is easy to find the degree of a vertex, by summing up the entries in the corresponding row or column of the matrix.
  - It is easy to perform operations on graphs, such as adding or deleting edges, by changing the entries in the matrix.

  The disadvantages of using an adjacency matrix are:

  - It requires a lot of space, especially for sparse graphs, where most of the entries are 0.
  - It is not easy to visualize the structure of the graph, by looking at the matrix.

- **Adjacency list**: An adjacency list is a collection of lists, one for each vertex in the graph. Each list contains the vertices that are adjacent to the vertex, meaning that there is an edge from the vertex to the adjacent vertex. For an undirected graph, each edge appears twice in the adjacency list, once for each endpoint. For a directed graph, each edge appears once in the adjacency list, for the source vertex. For a weighted graph, each adjacent vertex is accompanied by the weight of the edge.

  An example of an adjacency list for an undirected graph with 4 vertices is:

  | Vertex | Adjacent vertices |
  |--------|-------------------|
  | 1      | 2, 4              |
  | 2      | 1, 3              |
  | 3      | 2, 4              |
  | 4      | 1, 3              |

  An example of an adjacency list for a directed graph with 4 vertices is:

  | Vertex | Adjacent vertices |
  |--------|-------------------|
  | 1      | 2