### Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods are a class of algorithms that make locally optimal choices at each step in the hope of finding a global optimum. These methods are often used to solve optimization problems, where the goal is to find the best solution among a set of possible solutions.

One example of a problem that can be solved using greedy methods is the single source shortest paths problem. This problem involves finding the shortest path from a given source vertex to all other vertices in a weighted graph. Two algorithms that can be used to solve this problem are Dijkstra’s algorithm and Bellman Ford algorithm.

Dijkstra’s algorithm works by maintaining a set of vertices for which the shortest path from the source has already been determined. At each step, the algorithm selects the vertex with the minimum distance from the source and adds it to the set. The distances of the neighboring vertices are then updated, and the process is repeated until all vertices have been added to the set.

Bellman Ford algorithm, on the other hand, works by iteratively relaxing the edges of the graph. At each iteration, the algorithm updates the distance of each vertex by considering the minimum distance that can be achieved by going through one of its neighbors. This process is repeated until no more updates can be made, or until a negative cycle is detected.

Both Dijkstra’s and Bellman Ford algorithms can be used to solve the single source shortest paths problem. However, Dijkstra’s algorithm is generally faster and more efficient, while Bellman Ford algorithm can handle graphs with negative edge weights.