## Unit 4 - Graphs: Terminology used with Graph, Data Structure for Graph Representations: Adjacency Matrices, Adjacency List, Adjacency. Graph Traversal: Depth First Search and Breadth First Search, Connected Component, Spanning Trees, Minimum Cost Spanning Trees: Prims and Kruskal algorithm. Transitive Closure and Shortest Path algorithm: Warshal Algorithm and Dijikstra Algorithm.

### Graph Terminology
- **Graph**: A non-linear data structure consisting of nodes(vertices) and edges that connect them.
- **Vertex**: A node in a graph.
- **Edge**: A connection between two vertices in a graph.
- **Weight**: A numerical value assigned to an edge representing its cost or distance.
- **Degree**: The number of edges connected to a vertex.
- **Path**: A sequence of vertices connected by edges.
- **Cycle**: A path that starts and ends at the same vertex.
- **Connected Graph**: A graph in which there exists a path between every pair of vertices.
- **Disconnected Graph**: A graph in which there exists at least one pair of vertices with no path between them.
- **Directed Graph**: A graph in which the edges have a direction or one-way flow.
- **Undirected Graph**: A graph in which the edges have no direction or two-way flow.

### Data Structures for Graph Representations
- **Adjacency Matrix**: A 2D array where the values represent the weight of the edge between two vertices. If there is no edge between two vertices, the value is usually set to `0`.
- **Adjacency List**: A list of vertices where each vertex has a list of its adjacent vertices. The weight of the edges can also be stored in the list.
- **Adjacency**: A set of vertices where each vertex has a set of its adjacent vertices. The weight of the edges can also be stored in the set.

### Graph Traversal
- **Depth First Search (DFS)**: A graph traversal algorithm that explores as far as possible along each branch before backtracking. It uses a stack data structure to keep track of visited vertices and to determine the next vertex to visit.
- **Breadth First Search (BFS)**: A graph traversal algorithm that explores all the vertices at the current depth before moving on to the next depth. It uses a queue data structure to keep track of visited vertices and to determine the next vertex to visit.

### Connected Component
- **Connected Component**: A subgraph in which every pair of vertices is connected by a path. In a connected graph, there is only one connected component.

### Spanning Trees
- **Spanning Tree**: A subgraph that is a tree and includes all the vertices in the original graph.
- **Minimum Spanning Tree (MST)**: A spanning tree with the minimum total weight of its edges.

### Minimum Cost Spanning Trees
- **Prim's Algorithm**: A greedy algorithm that starts with a single vertex and grows the MST one edge at a time by selecting the edge with the smallest weight that connects a vertex in the MST to a vertex not yet in the MST.
- **Kruskal's Algorithm**: A greedy algorithm that starts with the edges with the smallest weights and adds them to the MST as long as they do not create a cycle.

### Transitive Closure
- **Transitive Closure**: The transitive closure of a graph is a new graph that includes all possible edges between vertices based on the existing edges. If there is a path from vertex A to vertex B, there will be an edge between them in the transitive closure.

### Shortest Path Algorithms
- **Dijkstra's Algorithm**: A greedy algorithm that finds the shortest path from a single source vertex to all other vertices in a weighted graph.
- **Warshall's Algorithm**: An algorithm that finds the shortest path between all pairs of vertices in a weighted graph.