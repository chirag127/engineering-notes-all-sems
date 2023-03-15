## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph.
- The algorithm maintains a set of visited vertices and a priority queue of unvisited vertices, where the priority is the current distance from the source vertex.
- The algorithm works as follows:

  - Initialize the distance of the source vertex to zero and the distance of all other vertices to infinity.
  - Mark the source vertex as visited and add it to the priority queue with its distance as the priority.
  - While the priority queue is not empty, do the following:
    - Extract the vertex with the minimum priority from the queue. This is the current vertex.
    - For each neighbor of the current vertex that is not visited, do the following:
      - Calculate the distance to the neighbor by adding the edge weight to the current distance.
      - If the distance to the neighbor is smaller than the previous distance, update the distance and the predecessor of the neighbor.
      - Add the neighbor to the priority queue with its distance as the priority.
    - Mark the current vertex as visited.
  - The algorithm terminates when the priority queue is empty or when the destination vertex is visited.
- The algorithm returns the distance and the predecessor of each vertex, which can be used to reconstruct the shortest path from the source to any other vertex.
- The time complexity of the algorithm is O(E log V), where E is the number of edges and V is the number of vertices, assuming a binary heap is used as the priority queue.
- The space complexity of the algorithm is O(V), where V is the number of vertices, as it requires an array of distances and an array of predecessors for each vertex.