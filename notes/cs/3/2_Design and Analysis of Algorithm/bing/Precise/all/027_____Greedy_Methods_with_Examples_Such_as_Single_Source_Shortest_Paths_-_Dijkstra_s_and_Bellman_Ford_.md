# Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

Greedy methods are a class of algorithms that make locally optimal choices at each step in the hope of finding a global optimum. These methods are often used to solve optimization problems, where the goal is to find the best solution from a set of possible solutions.

## Dijkstra’s Algorithm

Dijkstra’s algorithm is a greedy algorithm that solves the single-source shortest path problem for a graph with non-negative edge weights. The algorithm works by maintaining a set of nodes for which the shortest path from the source has already been determined, and iteratively selecting the node with the minimum distance from the source and updating the distances of its neighbors.

The algorithm can be implemented using a priority queue to efficiently select the node with the minimum distance from the source. The time complexity of the algorithm is O((V+E) log V), where V is the number of nodes and E is the number of edges in the graph.

## Bellman Ford Algorithm

The Bellman Ford algorithm is another algorithm that solves the single-source shortest path problem, but unlike Dijkstra’s algorithm, it can handle graphs with negative edge weights. The algorithm works by iteratively updating the distances of all nodes in the graph, and checking for negative cycles.

The time complexity of the Bellman Ford algorithm is O(VE), where V is the number of nodes and E is the number of edges in the graph. While the algorithm is slower than Dijkstra’s algorithm, it is more versatile as it can handle graphs with negative edge weights.

In summary, greedy methods are a powerful tool for solving optimization problems, and the Dijkstra’s and Bellman Ford algorithms are two examples of greedy algorithms that can be used to solve the single-source shortest path problem. These algorithms have different strengths and weaknesses, and the choice of algorithm depends on the specific problem at hand.