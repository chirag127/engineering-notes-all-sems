Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use as study material.

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
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that is not connected.
- **Subgraph**: A graph that is formed by a subset of vertices and edges of another graph.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Bipartite graph**: A graph in which the vertices can be divided into two disjoint sets, such that there is no edge between vertices in the same set.
- **Tree**: A connected, undirected graph that has no cycles.
- **Forest**: A disjoint set of trees.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph.
- **Minimum spanning tree**: A spanning tree of a weighted graph that has the minimum total weight among all possible spanning trees.

### Data Structure for Graph Representations

There are different ways to represent a graph in a computer. Some common data structures are:

- **Adjacency matrix**: A two-dimensional array of size V x V, where V is the number of vertices in the graph. The element at row i and column j indicates the presence or absence of an edge between vertex i and vertex j. If the graph is weighted, the element can also store the weight of the edge. The adjacency matrix is a simple and compact way to represent a graph, but it requires O(V^2) space and O(V) time to check if there is an edge between two vertices or to find the neighbors of a vertex.
- **Adjacency list**: An array of lists, where each list corresponds to a vertex in the graph. The list at index i contains the vertices that are adjacent to vertex i. If the graph is weighted, the list can also store the weights of the edges. The adjacency list is a more space-efficient way to represent a graph, as it requires O(V + E) space, where E is the number of edges in the graph. It also allows faster access to the neighbors of a vertex, as it requires O(degree) time. However, it requires more time to check if there is an edge between two vertices, as it requires O(min(degree)) time.
- **Adjacency map**: A variation of the adjacency list, where each list is replaced by a map (or a hash table). The map at index i stores the vertices that are adjacent to vertex i as keys, and the weights of the edges as values. The adjacency map is similar to the adjacency list in terms of space and time complexity, but it allows faster access to the weights of the edges, as it requires O(1) time to look up a key-value pair.

### Graph Traversal

Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way. There are two common methods of graph traversal: depth-first search (DFS) and breadth-first search (BFS).

- **Depth-first search (DFS)**: A recursive algorithm that starts from a given vertex and explores as far as possible along each branch before backtracking. DFS can be implemented using a stack (or the call stack) to keep track of the vertices to visit. DFS can be used to find cycles, connected components, topological order, etc. in a graph. The