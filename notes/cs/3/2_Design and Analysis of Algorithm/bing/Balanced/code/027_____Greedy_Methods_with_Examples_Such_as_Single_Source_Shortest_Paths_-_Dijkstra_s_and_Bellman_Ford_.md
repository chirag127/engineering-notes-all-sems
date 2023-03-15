# Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast, and easy to implement, but they may not always yield the best solution.
- Greedy methods can be applied to various problems, such as optimal reliability allocation, knapsack, minimum spanning trees, and single source shortest paths.

## Single Source Shortest Paths

- The single source shortest paths problem is to find the shortest paths from a given source vertex to all other vertices in a weighted graph.
- The graph may contain positive or negative edge weights, but no negative cycles (a cycle whose total weight is negative).
- There are two well-known greedy algorithms for this problem: Dijkstra's algorithm and Bellman-Ford algorithm.

### Dijkstra's Algorithm

- Dijkstra's algorithm is a greedy algorithm that works for graphs with non-negative edge weights.
- The algorithm maintains a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined.
- The algorithm repeatedly extracts the vertex with the minimum distance from the source from the priority queue, and updates the distances of its adjacent vertices.
- The algorithm terminates when the priority queue is empty or the destination vertex is extracted.
- The time complexity of Dijkstra's algorithm is O((V+E)logV), where V is the number of vertices and E is the number of edges in the graph.
- Dijkstra's algorithm can be implemented using a Fibonacci heap, a binary heap, or an array as the priority queue.

### Bellman-Ford Algorithm

- Bellman-Ford algorithm is a greedy algorithm that works for graphs with negative edge weights, but no negative cycles.
- The algorithm iterates over all the edges of the graph V-1 times, where V is the number of vertices in the graph.
- In each iteration, the algorithm relaxes each edge, that is, it updates the distance of the destination vertex if it can be reduced by using the edge.
- The algorithm detects a negative cycle if it can relax any edge in the V-th iteration.
- The time complexity of Bellman-Ford algorithm is O(VE), where V is the number of vertices and E is the number of edges in the graph.
- Bellman-Ford algorithm is simpler than Dijkstra's algorithm and suits well for distributed systems.