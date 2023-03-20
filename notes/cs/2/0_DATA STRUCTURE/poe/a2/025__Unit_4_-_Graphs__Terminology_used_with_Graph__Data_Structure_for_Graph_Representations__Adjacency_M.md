 Here is the content in markdown format:

## Unit 4 - Graphs:

- Terminology used with Graph: Vertex, Edge, Degree of Vertex, Indegree, Outdegree, Directed/Undirected Graph.

- Data Structure for Graph Representations:

-- Adjacency Matrices: Square matrix of size V x V where V is number of vertices. If there is an edge from vertex i to j then mat[i][j] = 1 else 0.

-- Adjacency List: An array of lists is used. For each vertex, a list containing its adjacent vertices is maintained.

-- Adjacency Set: A collection of vertices that are adjacent to a given vertex.

- Graph Traversal:

-- Depth First Search: Start from a vertex, go to adjacent vertices, recurse on adjacent vertices. Mark visited vertices.

-- Breadth First Search: Start from a vertex, explore all adjacent vertices first before going to the adjacent vertices of the adjacent vertices. Use queue. Mark visited vertices.

- Connected Component: Groups of vertices in a graph which are connected in some way. Can be found using BFS/DFS.

- Spanning Trees: A subset of edges in a connected graph that connect all vertices together without any cycles and with minimum possible number of edges (n-1 edges for a graph with n vertices).

- Minimum Cost Spanning Trees: Choosing spanning trees with minimum cost(weights) of edges. Algorithms:

-- Prim's: Grow the spanning tree from a starting position by always choosing the lowest weight edge that connects the tree to an unconnected vertex.

-- Kruskal's: Sort all edges by weight and add the smallest edge that doesn't cause a cycle.

- Transitive Closure: Reachability matrix. mat[i][j] = 1 if there is a path from vertex i to j, else 0. Can be found using Warshall's algorithm.

- Shortest Path algorithm:

-- Warshall's Algorithm: Finds transitive closure. Can be used to find shortest paths.

-- Dijkstra's Algorithm: Find shortest path from a single source vertex to all other vertices. Uses priority queue (min-heap).