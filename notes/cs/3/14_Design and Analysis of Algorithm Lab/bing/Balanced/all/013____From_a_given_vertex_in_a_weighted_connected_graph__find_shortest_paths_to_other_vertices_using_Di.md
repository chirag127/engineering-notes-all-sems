## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- A weighted connected graph is a graph where each edge has a positive or negative weight associated with it, and there is a path between any two vertices.
- A shortest path from a vertex u to a vertex v is a path that has the minimum total weight among all possible paths from u to v.
- Dijkstra's algorithm is a greedy algorithm that finds the shortest paths from a given source vertex to all other vertices in a weighted connected graph with non-negative edge weights.
- The algorithm works as follows:

  - Initialize a distance array dist, where dist[v] is the distance from the source to v, and a predecessor array pred, where pred[v] is the previous vertex on the shortest path from the source to v.
  - Set dist[source] to 0 and dist[v] to infinity for all other vertices v.
  - Set pred[source] to null and pred[v] to undefined for all vertices v.
  - Create a priority queue Q of vertices, where the priority of a vertex is its distance from the source, and insert the source into Q.
  - While Q is not empty, do the following:
    - Dequeue the vertex u with the minimum priority from Q.
    - For each neighbor v of u, do the following:
      - If dist[v] > dist[u] + weight(u, v), then
        - Update dist[v] to dist[u] + weight(u, v).
        - Update pred[v] to u.
        - If v is not in Q, then insert v into Q with priority dist[v].
        - Else, update the priority of v in Q to dist[v].
  - Return the distance array dist and the predecessor array pred.

- The time complexity of Dijkstra's algorithm is O((V + E) log V), where V is the number of vertices and E is the number of edges in the graph, assuming that the priority queue is implemented using a binary heap.
- The space complexity of Dijkstra's algorithm is O(V), where V is the number of vertices in the graph.
- An example of Dijkstra's algorithm is shown below:

![Dijkstra's algorithm example](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

- In this example, the source vertex is A, and the graph has 6 vertices and 9 edges. The algorithm finds the shortest paths from A to all other vertices, as shown by the colors and the numbers on the edges. The final distance and predecessor arrays are:

| Vertex | Distance | Predecessor |
|--------|----------|-------------|
| A      | 0        | null        |
| B      | 7        | A           |
| C      | 9        | A           |
| D      | 20       | B           |
| E      | 20       | C           |
| F      | 11       | C           |