### Representation of graphs

A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices. A graph can be used to model many types of relations and processes in physical, biological, social and information systems.

There are different ways to represent a graph, depending on the purpose and the type of the graph. Some of the common representations are:

- **Adjacency matrix**: An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric, meaning that the entry in the i-th row and j-th column is equal to the entry in the j-th row and i-th column. For a directed graph, the adjacency matrix is not necessarily symmetric, meaning that the entry in the i-th row and j-th column may not be equal to the entry in the j-th row and i-th column. For a weighted graph, the entry in the i-th row and j-th column is the weight of the edge from vertex i to vertex j, instead of 1 or 0.

  An example of an adjacency matrix for an undirected graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 | 1 |
  | 2 | 1 | 0 | 1 | 1 | 0 |
  | 3 | 0 | 1 | 0 | 1 | 0 |
  | 4 | 0 | 1 | 1 | 0 | 1 |
  | 5 | 1 | 0 | 0 | 1 | 0 |

  An example of an adjacency matrix for a directed graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 1 | 0 | 0 | 0 |
  | 2 | 0 | 0 | 1 | 0 | 0 |
  | 3 | 0 | 0 | 0 | 1 | 0 |
  | 4 | 0 | 0 | 0 | 0 | 1 |
  | 5 | 1 | 0 | 0 | 0 | 0 |

  An example of an adjacency matrix for a weighted graph with 5 vertices is:

  |   | 1 | 2 | 3 | 4 | 5 |
  |---|---|---|---|---|---|
  | 1 | 0 | 2 | 0 | 0 | 5 |
  | 2 | 2 | 0 | 3 | 4 | 0 |
  | 3 | 0 | 3 | 0 | 1 | 0 |
  | 4 | 0 | 4 | 1 | 0 | 2 |
  | 5 | 5 | 0 | 0 | 2 | 0 |

  The advantages of using an adjacency matrix are:

  - It is easy to check if there is an edge between two vertices, by looking at the corresponding entry in the matrix.
  - It is easy to add or remove an edge, by changing the corresponding entry in the matrix.
  - It is easy to compute the degree of a vertex, by summing up the entries in the corresponding row or column of the matrix.

  The disadvantages of using an adjacency matrix are:

  - It requires O(n^2) space, where n is the number of vertices, which can be wasteful if the graph is sparse (has few edges).
  - It requires O(n) time to find all the neighbors of a vertex, by scanning the corresponding row or column of the matrix.

- **Adjacency list**: An adjacency list is a collection of lists, one for each vertex in the graph. The list for a vertex contains all the vertices that are adjacent to it, i.e., have an edge from or to it. For an undirected graph, the list for a vertex contains all the vertices that share an edge with it. For a directed graph, the list for a vertex contains all the vertices that have an edge to it, i.e., the successors of the vertex. For a weighted graph