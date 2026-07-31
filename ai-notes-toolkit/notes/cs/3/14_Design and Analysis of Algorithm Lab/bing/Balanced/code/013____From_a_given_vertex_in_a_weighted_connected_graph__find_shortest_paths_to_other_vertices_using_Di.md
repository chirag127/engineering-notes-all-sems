## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph.
- The algorithm maintains a set of visited vertices and a priority queue of unvisited vertices with their distances from the source vertex.
- The algorithm works as follows:
  - Initialize the distance of the source vertex to zero and the distance of all other vertices to infinity.
  - Add the source vertex to the priority queue with its distance as the priority.
  - While the priority queue is not empty, do the following:
    - Extract the vertex with the minimum distance from the priority queue and mark it as visited.
    - For each neighbor of the extracted vertex that is not visited, do the following:
      - Calculate the distance to the neighbor through the extracted vertex.
      - If the distance to the neighbor is smaller than its current distance, update its distance and add it to the priority queue with its distance as the priority.
  - Return the distance array that contains the shortest distances from the source vertex to all other vertices.
- The time complexity of Dijkstra's algorithm is O((V+E) log V), where V is the number of vertices and E is the number of edges in the graph.
- The space complexity of Dijkstra's algorithm is O(V), where V is the number of vertices in the graph.