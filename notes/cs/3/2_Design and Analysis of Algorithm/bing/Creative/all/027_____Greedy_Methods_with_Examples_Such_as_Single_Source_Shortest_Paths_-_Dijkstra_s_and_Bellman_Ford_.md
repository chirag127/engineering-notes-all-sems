# Greedy Methods with Examples Such as Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms

## Introduction

- Greedy methods are a class of algorithms that make a series of local, optimal choices to find a global, optimal solution.
- Greedy methods do not consider the future consequences of their choices, and may end up with a suboptimal solution in some cases.
- Greedy methods are usually easy to implement and have low time complexity, but they require a proof of correctness and optimality.
- Greedy methods are suitable for problems that have the following properties:
  - Optimal substructure: The optimal solution to the problem can be obtained by combining the optimal solutions to its subproblems.
  - Greedy choice property: There is a locally optimal choice that leads to the globally optimal solution, and this choice can be made without considering the subproblems.
  - Matroid: A mathematical structure that captures the notion of independence and exchangeability of subsets.

## Examples

### Single Source Shortest Paths - Dijkstra’s Algorithm

- The problem of finding the shortest paths from a single source vertex to all other vertices in a weighted, directed graph.
- Dijkstra’s algorithm is a greedy method that maintains a set of vertices whose shortest paths from the source are known, and a priority queue of vertices whose shortest paths are to be determined.
- The algorithm repeatedly extracts the vertex with the minimum distance from the source from the priority queue, and updates the distances of its adjacent vertices.
- The algorithm terminates when the priority queue is empty or the destination vertex is extracted.
- Dijkstra’s algorithm is correct and optimal because it always chooses the vertex with the minimum distance from the source, which is the greedy choice that leads to the shortest path.
- Dijkstra’s algorithm has a time complexity of O((V+E) log V), where V is the number of vertices and E is the number of edges in the graph, using a binary heap as the priority queue.

### Single Source Shortest Paths - Bellman Ford Algorithm

- The problem of finding the shortest paths from a single source vertex to all other vertices in a weighted, directed graph that may contain negative edge weights, but no negative cycles.
- Bellman Ford algorithm is a dynamic programming method that relaxes all the edges of the graph V-1 times, where V is the number of vertices in the graph.
- Relaxing an edge means updating the distance of the destination vertex if it can be reduced by going through the source vertex and the edge weight.
- Bellman Ford algorithm is correct and optimal because it guarantees that after V-1 iterations, the distance of any vertex is equal to the length of the shortest path from the source, or infinity if there is no such path.
- Bellman Ford algorithm has a time complexity of O(VE), where V is the number of vertices and E is the number of edges in the graph.