### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy algorithms are algorithms that make the locally optimal choice at each step to find a global optimum. In the context of single source shortest paths, two well-known greedy algorithms are Dijkstra’s and Bellman Ford algorithms.

Dijkstra’s algorithm is used to find the shortest paths from a source vertex to all other vertices in a weighted digraph where all its edge weights are non-negative. The time complexity of Dijkstra’s algorithm is O((V+E)LogV) with the use of the Fibonacci heap .

However, Dijkstra’s algorithm doesn’t work for graphs with negative weights. In such cases, the Bellman-Ford algorithm can be used. Bellman-Ford algorithm is also simpler than Dijkstra’s algorithm and suits well for distributed systems .