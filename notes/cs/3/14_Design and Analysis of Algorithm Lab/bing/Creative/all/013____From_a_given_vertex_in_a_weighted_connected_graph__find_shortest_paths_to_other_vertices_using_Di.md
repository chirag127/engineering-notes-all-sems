## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- A weighted connected graph is a graph where each edge has a positive or negative weight associated with it, and there is a path between any two vertices.
- A shortest path from a vertex u to a vertex v is a path that has the minimum sum of edge weights among all possible paths from u to v.
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths from a given source vertex to all other vertices in a weighted connected graph with non-negative edge weights.
- The algorithm works as follows:

  - Initialize a distance array d, where d[u] stores the current shortest distance from the source vertex to u, and a predecessor array p, where p[u] stores the last vertex on the shortest path from the source to u.
  - Set d[source] = 0 and d[u] = infinity for all other vertices u.
  - Set p[source] = source and p[u] = null for all other vertices u.
  - Create a min-priority queue Q, where each vertex is ordered by its distance value, and insert all vertices into Q.
  - While Q is not empty, do the following:
    - Extract the vertex u with the minimum distance value from Q.
    - For each neighbor v of u, do the following:
      - If d[u] + w(u, v) < d[v], where w(u, v) is the weight of the edge (u, v), then update d[v] = d[u] + w(u, v) and p[v] = u, and decrease the priority of v in Q accordingly.
  - Return the distance array d and the predecessor array p.

- The distance array d contains the shortest distances from the source to all other vertices, and the predecessor array p can be used to reconstruct the shortest paths by following the pointers backwards from the destination to the source.
- The time complexity of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph, assuming that a binary heap is used to implement the priority queue Q. The space complexity is O(V), where V is the number of vertices in the graph.