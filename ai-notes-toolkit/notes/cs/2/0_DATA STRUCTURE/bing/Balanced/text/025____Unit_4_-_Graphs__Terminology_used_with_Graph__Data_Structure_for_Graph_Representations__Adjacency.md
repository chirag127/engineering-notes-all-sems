## Unit 4 - Graphs

A graph is a data structure that consists of a set of vertices (or nodes) and a set of edges that connect pairs of vertices. A graph can be used to model many types of problems, such as networks, maps, games, social networks, etc.

Some of the terminology used with graphs are:

- **Degree of a vertex**: The number of edges incident to a vertex.
- **Parallel edges**: Two or more edges that connect the same pair of vertices.
- **Self-loop**: An edge that connects a vertex to itself.
- **Simple graph**: A graph that has no parallel edges or self-loops.
- **Multigraph**: A graph that may have parallel edges or self-loops.
- **Directed graph**: A graph in which each edge has a direction, from one vertex to another.
- **Undirected graph**: A graph in which each edge has no direction, and can be traversed in either way.
- **Weighted graph**: A graph in which each edge has a numerical value (or weight) associated with it.
- **Path**: A sequence of vertices and edges that connects two vertices in a graph.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected graph**: A graph in which there is a path between any two vertices.
- **Disconnected graph**: A graph that is not connected.
- **Subgraph**: A graph that is formed by a subset of vertices and edges of another graph.
- **Complete graph**: A graph in which there is an edge between every pair of vertices.
- **Bipartite graph**: A graph in which the vertices can be divided into two disjoint sets, such that there is no edge between vertices in the same set.
- **Tree**: A connected, undirected graph that has no cycles.
- **Forest**: A collection of trees.

There are different ways to represent a graph in a computer, such as:

- **Adjacency matrix**: A two-dimensional array of size n x n, where n is the number of vertices in the graph. The element at row i and column j is 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For an undirected graph, the adjacency matrix is symmetric. For a weighted graph, the element at row i and column j is the weight of the edge from vertex i to vertex j, and 0 if there is no edge. The space complexity of this representation is O(n^2), where n is the number of vertices in the graph.
- **Adjacency list**: An array of lists, where each list corresponds to a vertex in the graph. The list at index i contains the vertices that are adjacent to vertex i, along with their weights if the graph is weighted. The space complexity of this representation is O(n + m), where n is the number of vertices and m is the number of edges in the graph.
- **Adjacency map**: A variation of the adjacency list, where each list is replaced by a map (or a dictionary or a hash table) that maps the adjacent vertices to their weights. This allows for faster access and update of the weights, but may require more space than the adjacency list.

Graph traversal is the process of visiting all the vertices and edges of a graph in a systematic way. There are two common methods of graph traversal:

- **Depth-first search (DFS)**: A recursive algorithm that starts from a given vertex and explores as far as possible along each branch before backtracking. It uses a stack (or the call stack) to keep track of the vertices to visit. The time complexity of DFS is O(n + m), where n is the number of vertices and m is the number of edges in the graph.
- **Breadth-first search (BFS)**: An iterative algorithm that starts from a given vertex and explores all the vertices at the same distance from the source before moving to the next level. It uses a queue to keep track of the vertices to visit. The time complexity of BFS is O(n + m), where n is the number of vertices and m is the number of edges in the graph.

Some of the applications of graph traversal are:

- **Connected component**: A subgraph of a graph that is connected. To find the connected components of a graph, we can perform DFS or BFS from any vertex and mark all the vertices that are visited. Then, we can repeat the process for any unmarked vertex until all the vertices are marked. The number of times we perform DFS or BFS is the number of connected components in the graph.
- **Spanning tree**: A subgraph of a graph that is a tree and contains all the vertices of the graph. To find a spanning tree of a graph, we can perform DFS