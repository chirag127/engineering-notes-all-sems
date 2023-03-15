# Representation of graphs

- A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices.
- A graph can be represented in different ways, such as using an adjacency matrix, an adjacency list, or an incidence matrix.
- An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge between vertex i and vertex j, and 0 otherwise.
- An adjacency list is a collection of lists, one for each vertex in the graph. The list for vertex i contains the names or indices of the vertices that are adjacent to i, i.e., that share an edge with i.
- An incidence matrix is a rectangular matrix of size n x m, where n is the number of vertices and m is the number of edges in the graph. The entry in the i-th row and j-th column of the matrix is 1 if vertex i is incident to edge j, and 0 otherwise.
- An example of a graph and its different representations is shown below:

![graph](https://i.imgur.com/9w0y0wO.png)

- The adjacency matrix of the graph is:

|   | A | B | C | D | E |
|---|---|---|---|---|---|
| A | 0 | 1 | 0 | 1 | 0 |
| B | 1 | 0 | 1 | 0 | 1 |
| C | 0 | 1 | 0 | 1 | 0 |
| D | 1 | 0 | 1 | 0 | 1 |
| E | 0 | 1 | 0 | 1 | 0 |

- The adjacency list of the graph is:

| Vertex | Adjacent vertices |
|--------|-------------------|
| A      | B, D              |
| B      | A, C, E           |
| C      | B, D              |
| D      | A, C, E           |
| E      | B, D              |

- The incidence matrix of the graph is:

|   | e1 | e2 | e3 | e4 | e5 | e6 |
|---|----|----|----|----|----|----|
| A | 1  | 0  | 0  | 1  | 0  | 0  |
| B | 1  | 1  | 0  | 0  | 1  | 0  |
| C | 0  | 1  | 1  | 0  | 0  | 0  |
| D | 0  | 0  | 1  | 1  | 0  | 1  |
| E | 0  | 0  | 0  | 0  | 1  | 1  |

- The choice of representation depends on the type and size of the graph, and the operations that need to be performed on it. For example, adjacency matrices are easy to use for checking the existence of an edge, but they require more space and time for adding or deleting vertices or edges. Adjacency lists are more efficient for sparse graphs, where the number of edges is much less than the number of possible edges, but they require more time for searching for an edge. Incidence matrices are useful for representing bipartite graphs, where the vertices can be divided into two disjoint sets, but they require more space than adjacency matrices or lists.