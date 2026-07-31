## From a given vertex in a weighted connected graph, find shortest paths to other vertices using Dijkstra's algorithm.

In the Design and Analysis of Algorithm Lab for the subject of Real Time System, we will be covering the topic of finding shortest paths to other vertices using Dijkstra's algorithm in a weighted connected graph. Here are the key points to keep in mind:

- Dijkstra's algorithm is a popular algorithm used to find the shortest path from a source vertex to all other vertices in a weighted graph.
- This algorithm works only for non-negative weighted graphs.
- The basic idea of Dijkstra's algorithm is to start at the source vertex and then consider all the adjacent vertices. For each adjacent vertex, we calculate the distance from the source vertex and update the distance if it is smaller than the current distance.
- We also keep track of the visited vertices to avoid revisiting them.
- After visiting all the adjacent vertices, we select the vertex with the smallest distance and mark it as visited.
- We repeat this process until all vertices have been visited.
- At the end of the algorithm, we will have the shortest distance from the source vertex to all other vertices in the graph.
- The time complexity of Dijkstra's algorithm is O(V^2) if we use an adjacency matrix to represent the graph. However, with the help of a priority queue, we can achieve a time complexity of O(E log V).

In conclusion, Dijkstra's algorithm is a fundamental algorithm in graph theory that is used to find the shortest path from a source vertex to all other vertices in a weighted connected graph. It is essential to understand the basics of this algorithm to solve real-world problems efficiently.