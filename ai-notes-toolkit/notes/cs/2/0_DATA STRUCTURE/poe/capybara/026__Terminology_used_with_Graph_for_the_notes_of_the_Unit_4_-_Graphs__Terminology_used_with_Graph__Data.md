### Terminology used with Graph

Graphs are a fundamental data structure used in computer science to represent a set of objects and the relationships between them. Here are some important terms to understand when working with graphs:

- **Vertex/Node:** A vertex, also known as a node, is a point in a graph that represents an object or entity. Vertices are often labeled with unique identifiers.
- **Edge:** An edge is a line that connects two vertices in a graph, representing a relationship between the objects they represent.
- **Weight:** A weight is a numerical value assigned to an edge, representing the cost or distance between the two vertices it connects.
- **Degree:** The degree of a vertex is the number of edges that are connected to it.
- **Path:** A path is a sequence of vertices connected by edges. It represents a route from one vertex to another.
- **Cycle:** A cycle is a path that starts and ends at the same vertex, forming a closed loop.
- **Connected Graph:** A connected graph is a graph where there is a path between every pair of vertices.
- **Disconnected Graph:** A disconnected graph is a graph where there are one or more pairs of vertices that are not connected by a path.

### Data Structure for Graph Representations

There are different ways to represent a graph in computer memory. Here are some common data structures for graph representations:

- **Adjacency Matrix:** An adjacency matrix is a two-dimensional array where the rows and columns represent vertices, and the entries represent the weights of the edges between them. If there is no edge between two vertices, the corresponding entry is usually set to infinity or a very large number.
- **Adjacency List:** An adjacency list is a list of lists where each vertex has a list of its adjacent vertices. Each entry in the list contains the adjacent vertex and the weight of the edge connecting them.
- **Adjacency Set:** An adjacency set is a set of sets where each vertex has a set of its adjacent vertices. This data structure is similar to the adjacency list, but it is more space-efficient when the graph is sparse.

### Graph Traversal

Graph traversal is the process of visiting all the vertices and edges in a graph. There are two common techniques for graph traversal:

- **Depth First Search (DFS):** DFS starts at a vertex and explores as far as possible along each branch before backtracking. It uses a stack to keep track of the vertices to visit next.
- **Breadth First Search (BFS):** BFS starts at a vertex and explores all the vertices at a given distance from it before moving on to the vertices at the next distance. It uses a queue to keep track of the vertices to visit next.

### Connected Component

A connected component is a subgraph where there is a path between every pair of vertices. In other words, it is a maximal connected subgraph of the original graph.

### Spanning Trees

A spanning tree is a subgraph that contains all the vertices of the original graph and is also a tree (i.e., it is connected and acyclic). There can be multiple spanning trees for a given graph.

### Minimum Cost Spanning Trees

A minimum cost spanning tree is a spanning tree with the minimum possible sum of edge weights. There are two commonly used algorithms to find the minimum cost spanning tree:

- **Prim's Algorithm:** Prim's algorithm starts with a single vertex and grows the tree by adding the minimum weight edge that connects a tree vertex to a non-tree vertex.
- **Kruskal's Algorithm:** Kruskal's algorithm starts with a forest of single vertex trees and grows the forest by adding the minimum weight edge that connects two trees.

### Transitive Closure and Shortest Path algorithm

Transitive closure and shortest path algorithms are used to find the relationships between vertices in a graph:

- **Warshal Algorithm:** Warshal algorithm calculates the transitive closure of a graph, which is a matrix that represents the reachability between all pairs of vertices.
- **Dijkstra Algorithm:** Dijkstra algorithm finds the shortest path between two vertices in a graph. It uses a priority queue to keep track of the vertices to visit next, and it updates the shortest path to each vertex as it explores the graph.