Hello, I am Sydney, your AI assistant. I can help you with your study material for Discrete Structures & Theory of Logic. Here is the content for the topic of Representation of graphs:

### Representation of graphs

A graph is a mathematical structure that consists of a set of vertices and a set of edges that connect pairs of vertices. A graph can be used to model various phenomena, such as networks, relations, paths, circuits, etc.

There are different ways to represent a graph, depending on the purpose and the level of detail required. Some of the common methods are:

- **Adjacency matrix**: An adjacency matrix is a square matrix of size n x n, where n is the number of vertices in the graph. The entry in the i-th row and j-th column of the matrix is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric, meaning that the entry in the i-th row and j-th column is equal to the entry in the j-th row and i-th column. For a directed graph, the adjacency matrix is not necessarily symmetric, meaning that the entry in the i-th row and j-th column may not be equal to the entry in the j-th row and i-th column. For example, the following graph:

```
  1
 / \
2---3
 \ /
  4
```

can be represented by the following adjacency matrix:

```
  1 2 3 4
1 0 1 1 0
2 1 0 1 1
3 1 1 0 1
4 0 1 1 0
```

- **Adjacency list**: An adjacency list is a collection of lists, one for each vertex in the graph. Each list contains the vertices that are adjacent to the corresponding vertex, i.e., the vertices that are connected by an edge to the vertex. For an undirected graph, each edge appears twice in the adjacency list, once for each endpoint. For a directed graph, each edge appears once in the adjacency list, for the vertex that is the source of the edge. For example, the following graph:

```
  1
 / \
2-->3
 \ /
  4
```

can be represented by the following adjacency list:

```
1: 2, 3
2: 3, 4
3: 
4: 2, 3
```

- **Incidence matrix**: An incidence matrix is a rectangular matrix of size n x m, where n is the number of vertices and m is the number of edges in the graph. The entry in the i-th row and j-th column of the matrix is 1 if vertex i is incident to edge j, i.e., vertex i is one of the endpoints of edge j, and 0 otherwise. For an undirected graph, each column of the incidence matrix has exactly two 1s, corresponding to the two endpoints of the edge. For a directed graph, each column of the incidence matrix has exactly one 1 in the row of the source vertex, and one -1 in the row of the destination vertex, of the edge. For example, the following graph:

```
  1
 / \
2-->3
 \ /
  4
```

can be represented by the following incidence matrix, where the edges are labeled as e1, e2, e3, e4, and e5:

```
    e1 e2 e3 e4 e5
1    1  1  0  0  0
2   -1  0  1 -1  1
3    0 -1 -1  1  0
4    0  0  0  0 -1
```

- **Edge list**: An edge list is a collection of pairs, each pair representing an edge in the graph. Each pair consists of the two vertices that are the endpoints of the edge. For an undirected graph, the order of the vertices in the pair does not matter. For a directed graph, the order of the vertices in the pair matters, as it indicates the direction of the edge. For example, the following graph:

```
  1
 / \
2-->3
 \ /
  4
```

can be represented by the following edge list:

```
(1, 2), (1, 3), (2, 3), (2, 4), (4, 2)
```

- **Graph drawing**: A graph drawing is a visual representation of a graph, where the vertices are represented by