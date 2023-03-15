## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

### Terminology used with Graph

Some common terms used with graphs are:

- **Degree** of a vertex: The number of edges incident to the vertex.
- **Parallel edges**: Two or more edges that connect the same pair of vertices.
- **Self-loop**: An edge that connects a vertex to itself.
- **Simple graph**: A graph that has no parallel edges or self-loops.
- **Directed graph**: A graph in which each edge has a direction, from one vertex to another.
- **Undirected graph**: A graph in which each edge has no direction, and can be traversed in either way.
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that is not connected.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Subgraph**: A graph that is formed by a subset of vertices and edges of another graph.
- **Tree**: A connected, undirected graph that has no cycles.
- **Forest**: A collection of trees.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph.
- **Spanning forest**: A collection of spanning trees of a graph.

### Data Structure for Graph Representations

There are different ways to represent a graph in a computer. Some common data structures are:

- **Adjacency matrix**: A two-dimensional array of size n x n, where n is the number of vertices in the graph. The element at row i and column j indicates the presence or absence of an edge between vertex i and vertex j. For an undirected graph, the matrix is symmetric. For a weighted graph, the matrix stores the weights of the edges instead of 1 or 0.
- **Adjacency list**: An array of lists, where each list corresponds to a vertex in the graph. The list contains the adjacent vertices of that vertex. For a weighted graph, the list also stores the weights of the edges.
- **Adjacency map**: A variation of the adjacency list, where each list is replaced by a map (or a dictionary). The map stores the adjacent vertices as keys and the weights of the edges as values.

### Graph Traversal

Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way. There are two common methods of graph traversal:

- **Depth-first search (DFS)**: A recursive algorithm that starts from a given vertex and explores as far as possible along each branch before backtracking. DFS uses a stack to keep track of the vertices to visit next.
- **Breadth-first search (BFS)**: An iterative algorithm that starts from a given vertex and explores all the neighboring vertices at the same level before moving to the next level. BFS uses a queue to keep track of the vertices to visit next.

### Connected Component

A connected component of a graph is a subgraph in which any two vertices are connected by a path, and which is not connected to any other subgraph. A graph can have one or more connected components. The number of connected components of a graph can be found by applying DFS or BFS and counting the number of times the traversal starts from a new vertex.

### Spanning Trees

A spanning tree of a graph is a subgraph that is a tree and contains all the vertices of the graph. A graph can have one or more spanning trees. A spanning tree can be found by applying DFS or BFS and removing any edge that forms a cycle. A spanning tree has n-1 edges, where n is the number of vertices in the graph.

### Minimum Cost Spanning Trees

A minimum cost spanning tree (MCST) of a weighted graph is a spanning tree that has the minimum total weight of all the spanning trees of the graph. A graph can have one or more MCSTs. There are two common algorithms to find a MCST of a graph:

- **Prim's algorithm**: A greedy algorithm that starts from an arbitrary vertex and grows the tree by adding the edge with the minimum weight that connects a vertex in the tree to a vertex outside the tree, until all the vertices are included.
- **Krus