### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

- Greedy methods are a class of algorithms that make locally optimal choices at each step, hoping to find a global optimum.
- Greedy methods are often simple, fast and easy to implement, but they may not always guarantee the best solution.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: A globally optimal solution can be reached by making a locally optimal (greedy) choice at each step, without considering the future consequences.
- Some examples of greedy methods are:

#### Single Source Shortest Paths - Dijkstra’s Algorithm
- This algorithm finds the shortest path from a given source vertex to all other vertices in a weighted graph, where the weights are non-negative.
- The algorithm maintains a set of visited vertices, and a set of unvisited vertices with their tentative distances from the source.
- The algorithm repeatedly selects the unvisited vertex with the smallest tentative distance, marks it as visited, and updates the tentative distances of its adjacent vertices by adding the weight of the edge.
- The algorithm terminates when all vertices are visited or when the smallest tentative distance among the unvisited vertices is infinity, indicating that there is no path to the remaining vertices.
- The algorithm can be implemented using a priority queue to store the unvisited vertices and their tentative distances, which allows selecting the minimum in O(log n) time, where n is the number of vertices.
- The time complexity of the algorithm is O((n + m) log n), where m is the number of edges, assuming a binary heap is used as the priority queue.

#### Single Source Shortest Paths - Bellman Ford Algorithm
- This algorithm also finds the shortest path from a given source vertex to all other vertices in a weighted graph, but it can handle negative weights, as long as there are no negative cycles (a cycle whose total weight is negative).
- The algorithm relaxes all the edges of the graph n - 1 times, where n is the number of vertices, by updating the tentative distance of the destination vertex if it can be improved by going through the source vertex and the edge weight.
- The algorithm can also detect negative cycles by performing one more relaxation and checking if any distance can be improved further. If so, then there is a negative cycle and the shortest path is not well-defined.
- The time complexity of the algorithm is O(nm), where n is the number of vertices and m is the number of edges.