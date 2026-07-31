### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods are algorithms that make the locally optimal choice at each step to find a global optimum. These methods are often used to solve optimization problems.

#### Dijkstra’s Algorithm

Dijkstra’s algorithm is a greedy algorithm used to find the shortest path between a single source vertex and all other vertices in a graph. The time complexity of this algorithm is O((V+E)LogV) with the use of the Fibonacci heap . However, Dijkstra’s algorithm does not work for graphs with negative weights.

#### Bellman-Ford Algorithm

The Bellman-Ford algorithm is another algorithm used to find the shortest paths from a single source vertex to all other vertices in a weighted digraph. It is slower than Dijkstra's algorithm, but more versatile, as it is capable of handling graphs in which some of the edge weights are negative numbers . Bellman-Ford is also simpler than Dijkstra and suites well for distributed systems .