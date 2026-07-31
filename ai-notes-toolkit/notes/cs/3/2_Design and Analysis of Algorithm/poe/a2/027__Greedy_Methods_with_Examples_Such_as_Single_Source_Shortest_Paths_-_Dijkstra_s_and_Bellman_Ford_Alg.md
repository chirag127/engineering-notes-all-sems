 Here are the notes for the given topic in markdown format:

### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods make locally optimal choices at each stage with the hope of finding a global optimum.
- Examples of greedy methods:
    - Optimal reliability allocation
    - Knapsack problem
    - Minimum spanning trees (Prim's and Kruskal's algorithms)
    - Single-source shortest paths (Dijkstra's and Bellman-Ford algorithms)

#### Dijkstra's Algorithm

- Dijkstra's algorithm solves the single-source shortest path problem for a graph with non-negative edge weights.
- It maintains a set S of vertices whose final shortest-path weights from the source vertex s have already been determined.
- The algorithm repeatedly selects the vertex u outside of S with the minimum shortest-path estimate, adds u to S, and relaxes all edges leaving u.
- The running time of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph.

[Additional details and examples of Dijkstra's algorithm...]

#### Bellman-Ford Algorithm

- Bellman-Ford algorithm solves the single-source shortest path problem for a graph with arbitrary edge weights (not necessarily non-negative).
- It performs a sequence of relaxations of all edges, each iteration potentially increasing the distance estimates of some vertices.
- If there are no negative cycles in the graph, the algorithm eventually converges to correct shortest path distances from the source.
- The running time of Bellman-Ford algorithm is O(VE), where V is the number of vertices and E is the number of edges in the graph.

[Additional details and examples of Bellman-Ford algorithm...]