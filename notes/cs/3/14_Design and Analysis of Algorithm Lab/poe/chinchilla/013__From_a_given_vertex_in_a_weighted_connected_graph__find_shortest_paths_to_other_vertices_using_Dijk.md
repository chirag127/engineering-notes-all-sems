## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

Dijkstra's algorithm is a popular algorithm for finding the shortest path between a source vertex and all other vertices in a weighted graph. This algorithm is widely used in real-world applications such as GPS navigation and network routing.

### Algorithm Steps:

1. Initialize the distance of all vertices to infinity and the distance of the source vertex to 0.
2. Create a priority queue and insert the source vertex with distance 0.
3. While the priority queue is not empty, do the following:
   1. Extract the vertex with the minimum distance from the priority queue.
   2. For each adjacent vertex v, calculate the distance from the source vertex to v through the extracted vertex u. If this distance is less than the current distance of v, update the distance of v to this new distance and add v to the priority queue.
4. The final distances of all vertices from the source vertex will be the shortest paths.

### Example:

Consider the following weighted graph:

![Graph Example](https://i.imgur.com/wz5Z5J5.png)

Let the source vertex be vertex A. We can use Dijkstra's algorithm to find the shortest paths to all other vertices.

1. Initialize the distance of all vertices to infinity and the distance of vertex A to 0.
   - Distance[A] = 0
   - Distance[B] = Distance[C] = Distance[D] = Distance[E] = Infinity
2. Insert vertex A with distance 0 into the priority queue.
3. While the priority queue is not empty, do the following:
   - Extract vertex A from the priority queue.
   - For each adjacent vertex v, calculate the distance from vertex A to v through vertex u. If this distance is less than the current distance of v, update the distance of v to this new distance and add v to the priority queue.
     - Distance[B] = min(Distance[B], Distance[A] + Weight[A,B]) = min(Infinity, 2) = 2
     - Distance[C] = min(Distance[C], Distance[A] + Weight[A,C]) = min(Infinity, 4) = 4
   - Vertex B is now the vertex with the minimum distance, so extract it from the priority queue.
     - Distance[D] = min(Distance[D], Distance[B] + Weight[B,D]) = min(Infinity, 1) = 1
     - Distance[E] = min(Distance[E], Distance[B] + Weight[B,E]) = min(Infinity, 3) = 3
   - Vertex D is now the vertex with the minimum distance, so extract it from the priority queue.
     - Vertex C is already visited, so no update is necessary.
     - Vertex E is already visited, so no update is necessary.
4. The final distances from vertex A to all other vertices are:
   - Distance[A] = 0
   - Distance[B] = 2
   - Distance[C] = 4
   - Distance[D] = 3
   - Distance[E] = 5

### Time Complexity:

The time complexity of Dijkstra's algorithm depends on the data structure used for the priority queue. Using a binary heap, the time complexity is O(VlogV + E), where V is the number of vertices and E is the number of edges in the graph. However, using a Fibonacci heap can reduce the time complexity to O(VlogV + E).