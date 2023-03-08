 Here is the content in markdown format:

### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods make locally optimal choices at each stage with the hope of finding a global optimum.

Examples:

- Dijkstra's algorithm: Finds the shortest path from a source vertex to all other vertices in a weighted graph. It picks the unvisited vertex with the lowest distance and considers it as the next vertex in the shortest path.
- Prim's algorithm: Finds a minimum spanning tree for a weighted undirected graph. It repeatedly picks the edge with lowest weight connecting the tree to an unconnected vertex.

Advantages:

- Simple and efficient for small graphs.
- Guaranteed to find an optimal solution in some cases (e.g. Dijkstra's algorithm finding shortest paths with non-negative weights).

Disadvantages:

- Does not always lead to optimal solutions.
- May be inefficient for large problems.

Applications:

- Finding shortest paths in networks.
- Minimum spanning tree problem.
- Optimization problems where an optimal choice can be made at each step.

Single Source Shortest Paths - Dijkstra's and Bellman Ford Algorithms

Dijkstra's algorithm:

- Use a min priority queue to keep track of vertices ordered by shortest distance from source.
- Repeatedly remove vertex u with smallest dist[u] and relax all edges (u, v).
- Runs in O(E log V) time.

Bellman-Ford algorithm:

- Repeatedly relax all edges V-1 times.
- Detects negative weight cycles.
- Slower than Dijkstra's with runtime O(VE).

Advantages:

- Dijkstra's algorithm is efficient for sparse graphs.
- Bellman-Ford detects negative weight cycles.

Disadvantages:

- Dijkstra's algorithm is inefficient for dense graphs.
- Bellman-Ford is slower than Dijkstra's for graphs without negative weight cycles.

Applications:

- Finding shortest paths in networks with non-negative edge weights (Dijkstra's) or arbitrary weights (Bellman-Ford).
- Detecting negative weight cycles (Bellman-Ford).