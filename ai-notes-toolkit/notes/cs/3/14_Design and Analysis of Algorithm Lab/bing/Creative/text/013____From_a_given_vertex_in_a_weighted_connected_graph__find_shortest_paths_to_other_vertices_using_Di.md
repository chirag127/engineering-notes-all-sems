## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

- Dijkstra's algorithm is a greedy algorithm that finds the shortest path from a given vertex to all other vertices in a weighted graph, where the weights represent the distances or costs of the edges.
- The algorithm maintains a set of visited vertices, initially empty, and a priority queue of unvisited vertices, initially containing all the vertices with their distances from the source vertex.
- The algorithm repeatedly extracts the vertex with the minimum distance from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices in the priority queue.
- The algorithm terminates when the priority queue is empty or when the destination vertex is extracted.
- The algorithm can be implemented using an array, a binary heap, or a Fibonacci heap as the data structure for the priority queue.
- The algorithm has a time complexity of O(V^2) using an array, O(E log V) using a binary heap, or O(E + V log V) using a Fibonacci heap, where V is the number of vertices and E is the number of edges in the graph.
- The algorithm can be used to solve various problems such as finding the shortest path between two cities, routing packets in a network, or finding the optimal sequence of tasks in a project.

Here is an example of how the algorithm works on a graph with six vertices and nine edges:

![Graph](https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif)

- The source vertex is A and the destination vertex is F.
- The algorithm starts with the priority queue containing all the vertices with their distances from A: {A:0, B:∞, C:∞, D:∞, E:∞, F:∞}.
- The algorithm extracts A from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices B and C: {B:7, C:9, D:∞, E:∞, F:∞}.
- The algorithm extracts B from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices D and E: {C:9, D:15, E:10, F:∞}.
- The algorithm extracts E from the priority queue, adds it to the visited set, and updates the distances of its adjacent vertices D and F: {C:9, D:11, F:13}.
- The algorithm extracts C from the priority queue, adds it to the visited set, and updates the distance of its adjacent vertex D: {D:11, F:13}.
- The algorithm extracts D from the priority queue, adds it to the visited set, and updates the distance of its adjacent vertex F: {F:13}.
- The algorithm extracts F from the priority queue, adds it to the visited set, and terminates.
- The shortest path from A to F is A-B-E-F with a distance of 13.