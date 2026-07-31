 Here are the notes in markdown format without any emojis or external links:

### Graph Implementation

- Graph is a non-linear data structure consisting of nodes and edges.
- Edges connect the nodes.
- Edges can be directed or undirected.
- Vertices/Nodes can be weighted or unweighted.
- Represented using:
	- Adjacency Matrix: 2D array of size V x V where V is number of vertices.
	- Adjacency List: Array of lists where each list represents adjacent vertices of a vertex.

### BFS (Breadth First Search)

- Traverses the graph layer by layer.
- Uses a queue to store the nodes to be traversed.
- Time complexity: O(V+E) where V is number of vertices and E is number of edges.
- Applications: Shortest path, connected components.

### DFS (Depth First Search)

- Traverses the graph recursively.
- Uses a stack to store the nodes to be traversed.
- Time complexity: O(V+E)
- Applications: Topological sorting, cycle detection.

### Minimum Cost Spanning Tree

- A spanning tree of a weighted graph with minimum total edge weight.
- Algorithms:
	- Prim's: Starts from an arbitrary root node and greedily adds lowest weight edge that doesn't cause cycles.
	- Kruskal's: Sorts all edges in ascending order of their weight and picks the smallest edge.

### Shortest Path Algorithm

- Dijkstra's: Greedy approach, works on non-negative weighted graphs. Time complexity: O((V+E)logV).
- Bellman-Ford: Relaxation based, works on graphs with negative weights but no negative cycles. Time complexity: O(VE).
- Floyd-Warshall: Calculates shortest distances between all pairs of vertices. Time complexity: O(V^3).