## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph.
- The algorithm maintains a set of visited vertices and a priority queue of unvisited vertices with their distances from the source vertex.
- The algorithm works as follows:

  - Initialize the distance of the source vertex to zero and the distance of all other vertices to infinity.
  - Mark the source vertex as visited and add it to the priority queue with its distance as the priority.
  - While the priority queue is not empty, do the following:
    - Extract the vertex with the minimum distance from the priority queue. This is the current vertex.
    - For each neighbor of the current vertex that is not visited, do the following:
      - Calculate the distance to the neighbor through the current vertex. This is the new distance.
      - If the new distance is smaller than the old distance, update the distance of the neighbor and add it to the priority queue with the new distance as the priority.
    - Mark the current vertex as visited.
  - The algorithm terminates when the priority queue is empty or when the destination vertex is visited.
- The algorithm returns the distance of each vertex from the source vertex and the previous vertex in the shortest path.
- The algorithm can be implemented using an array, a binary heap, or a Fibonacci heap as the priority queue data structure.
- The time complexity of the algorithm depends on the number of vertices (n), the number of edges (m), and the implementation of the priority queue. The worst-case time complexity is O(n^2) using an array, O((n+m)log n) using a binary heap, and O(n log n + m) using a Fibonacci heap.
- The space complexity of the algorithm is O(n) for storing the distances, the visited status, and the previous vertices of each vertex.