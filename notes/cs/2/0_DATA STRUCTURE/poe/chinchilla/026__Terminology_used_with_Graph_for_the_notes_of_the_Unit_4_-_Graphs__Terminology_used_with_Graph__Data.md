### Terminology used with Graph

- **Graph**: A non-linear data structure that consists of vertices or nodes connected by edges.
- **Vertex/Node**: A point or object in a graph that represents a unique entity.
- **Edge**: A line or connection between two vertices that represents a relationship or connection between them.
- **Weight**: A value assigned to an edge that represents the cost or distance between two vertices.
- **Directed Graph**: A graph where each edge has a direction, indicating the flow or relationship between vertices.
- **Undirected Graph**: A graph where each edge has no direction and represents a symmetric relationship between vertices.
- **Degree**: The number of edges connected to a vertex.
- **Path**: A sequence of vertices connected by edges.
- **Cycle**: A path that starts and ends at the same vertex.

### Data Structure for Graph Representations

- **Adjacency Matrix**: A 2D array that represents a graph where the rows and columns represent vertices and the cells represent the edges between them. The value in the cell indicates the weight of the edge or a boolean value indicating its existence.
- **Adjacency List**: A list that represents a graph where each vertex is represented by a list of its adjacent vertices.
- **Adjacency**: The relationship between two vertices that share an edge.

### Graph Traversal

- **Depth First Search (DFS)**: A traversal algorithm that starts at a vertex and explores as far as possible along each branch before backtracking. It uses a stack or recursion to keep track of visited vertices.
- **Breadth First Search (BFS)**: A traversal algorithm that starts at a vertex and explores all the neighboring vertices before moving on to the next level of vertices. It uses a queue to keep track of visited vertices.
- **Connected Component**: A subgraph of a graph where all vertices are connected to each other through edges.
- **Spanning Tree**: A subgraph of a graph that contains all vertices and is a tree, meaning it has no cycles.

### Minimum Cost Spanning Trees

- **Prim's Algorithm**: A greedy algorithm that starts at a vertex and adds the minimum weight edge to the tree until all vertices are included.
- **Kruskal's Algorithm**: A greedy algorithm that sorts all edges by weight and adds them to the tree as long as they don't create a cycle.

### Transitive Closure and Shortest Path Algorithm

- **Transitive Closure**: The process of finding all pairs of vertices that are reachable from each other in a directed graph.
- **Warshall Algorithm**: An algorithm that finds the transitive closure of a graph using dynamic programming.
- **Shortest Path**: The path with the minimum weight between two vertices in a graph.
- **Dijkstra Algorithm**: A greedy algorithm that finds the shortest path between two vertices by selecting the minimum weight path at each step.