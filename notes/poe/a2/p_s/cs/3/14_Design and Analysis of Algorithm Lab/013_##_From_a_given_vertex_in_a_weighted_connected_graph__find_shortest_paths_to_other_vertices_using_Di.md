 Here are the notes for the topic **_From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm_**:

**Dijkstra's algorithm**: Dijkstra's algorithm is used to find the shortest path from a single source vertex to all other vertices in a weighted graph. It is a greedy algorithm and works on the principle of relaxation.

**Steps:**
1. Take the source vertex and assign a distance value of 0 to it and infinity to all other vertices.
2. Pick the vertex with the minimum distance and mark it as visited.
3. Relax all its adjacent vertices. This means, if there is an adjacent vertex which is not visited, check if the distance value of the picked vertex plus the weight of the edge connecting the two vertices is less than the distance value of the adjacent vertex. If yes, update the distance value of the adjacent vertex.
4. Repeat steps#2 and #3 until all vertices are visited.
5. The distance values of all vertices now have the shortest path distances from the source vertex.

**Example:**

![](https://www.geeksforgeeks.org/wp-content/uploads/dijkstra.png)

**Advantages:**
- Guarantees to find the shortest path.
- Works for both directed and undirected graphs.

**Disadvantages:**
- Time complexity is O((V + E)logV) which makes it inefficient for dense graphs.
- Does not work for graphs with negative weight cycles.

**Applications:** Dijkstra's algorithm is used in many applications such as:
- Routing algorithms to find shortest path in networks.
- Navigation systems to find the shortest route between two locations.
- Finding critical paths in project management.