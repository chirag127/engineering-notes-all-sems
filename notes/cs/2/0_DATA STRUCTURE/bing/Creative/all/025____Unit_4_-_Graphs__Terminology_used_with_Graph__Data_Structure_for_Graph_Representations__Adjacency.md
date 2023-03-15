## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

### Terminology used with Graph

Some common terms used with graphs are:

- **Degree** of a vertex: The number of edges incident to the vertex.
- **Parallel edges**: Two or more edges that connect the same pair of vertices.
- **Self-loop**: An edge that connects a vertex to itself.
- **Simple graph**: A graph that has no parallel edges or self-loops.
- **Multigraph**: A graph that may have parallel edges or self-loops.
- **Directed graph** (or digraph): A graph in which each edge has a direction, from one vertex to another.
- **Undirected graph**: A graph in which each edge has no direction, and can be traversed in either direction.
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it, which can represent the cost, distance, time, etc. of traversing the edge.
- **Unweighted graph**: A graph in which each edge has no weight associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Acyclic graph**: A graph that has no cycles.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that has at least two vertices that are not connected by a path.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Subgraph**: A graph that is formed by a subset of the vertices and edges of another graph.
- **Tree**: A connected, acyclic, undirected graph.
- **Forest**: A collection of trees.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph.
- **Minimum spanning tree**: A spanning tree of a weighted graph that has the minimum total weight among all possible spanning trees.

### Data Structure for Graph Representations

There are different ways to represent a graph in a computer, depending on the type and size of the graph, and the operations that need to be performed on it. Some common data structures for graph representations are:

- **Adjacency matrix**: A two-dimensional array of size V x V, where V is the number of vertices in the graph, and each element A[i][j] indicates the presence or absence of an edge between vertex i and vertex j. If the graph is weighted, A[i][j] can also store the weight of the edge. The adjacency matrix is a simple and compact way to represent a graph, but it has some drawbacks, such as:
  - It requires O(V^2) space, which can be wasteful if the graph is sparse (has few edges).
  - It takes O(V) time to find the neighbors of a vertex, which can be slow if the graph is dense (has many edges).
  - It is not suitable for dynamic graphs (graphs that change over time), as adding or removing a vertex requires resizing the matrix.

- **Adjacency list**: A one-dimensional array of size V, where each element A[i] is a linked list of the vertices that are adjacent to vertex i. If the graph is weighted, each node in the linked list can also store the weight of the edge. The adjacency list is a flexible and efficient way to represent a graph, as it has some advantages, such as:
  - It requires O(V + E) space, where E is the number of edges in the graph, which can be optimal if the graph is sparse.
  - It takes O(degree) time to find the neighbors of a vertex, where degree is the number of edges incident to the vertex, which can be fast if the graph is sparse.
  - It is suitable for dynamic graphs, as adding or removing a vertex or an edge requires only updating the corresponding linked list.

- **Adjacency map**: A one-dimensional array of size V, where each element A[i] is a map (or a hash table) of the vertices that are adjacent to vertex i, and the values are the weights of the edges. The adjacency map is a variant of the adjacency list, that can be useful for weighted graphs, as it has some benefits, such as:
  - It requires O(V + E) space, which can be optimal if the graph is sparse.
  - It takes O(1) time