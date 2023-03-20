 Here is the formal content in Markdown format without emojis or external links:

## Unit 7 - Graphs

1. A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges.

2. Vertices: These are the nodes of the graph. Vertices are the individual points forming the graph.

3. Edges: These are the connections between the vertices. Edges can be directed or undirected. Directed edges have a source and destination vertex while undirected edges simply connect two vertices.

4. Adjacency: Two vertices are said to be adjacent if there is an edge connecting them. The neighboring vertices of a vertex v are the vertices that are adjacent to v.

5. Degree: The degree of a vertex is the number of edges connected to that vertex. The indegree is the number of incoming edges and the outdegree is the number of outgoing edges for directed graphs. The degree for undirected graphs is simply the number of connected edges.

6. Graph Representations: There are two common ways to represent graphs:

- Adjacency List: An array of lists is used. The index of each list represents a vertex and each list contains the vertices that are adjacent to the vertex.
- Adjacency Matrix: A 2D matrix is used. The rows and columns represent vertices. A 1 at position [i][j] indicates an edge between vertices i and j. A 0 indicates no edge.

7. Weighted and Unweighted Graphs: Edges in graphs can optionally have weights. These weights can represent distances or costs. Graphs with weighted edges are called weighted graphs and those without are unweighted graphs. Shortest path algorithms can utilize the weights to find optimal paths.

8. Graph Traversals: Algorithms to systematically visit each vertex and edge in a graph. Common graph traversals are:

- Depth First Search: Explores as far as possible along each branch before backtracking.
- Breadth First Search: Explores the graph level by level, checking all vertices on a level before moving to the next.
- Dijkstra's Algorithm: Finds the shortest path between two vertices in a weighted graph.