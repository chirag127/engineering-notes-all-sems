### Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

- Optimal substructure means that an optimal solution to the problem can be constructed from optimal solutions to its subproblems.
- Greedy choice property means that a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step, without considering the future consequences.

Some examples of greedy methods are:

- Minimum spanning tree: A minimum spanning tree (MST) of a weighted undirected graph is a subset of edges that connects all the vertices with the minimum total weight. There are two well-known greedy algorithms to find the MST of a graph: Prim's algorithm and Kruskal's algorithm.

  - Prim's algorithm starts with an arbitrary vertex and grows the MST by adding the edge with the minimum weight that connects a vertex in the MST to a vertex outside the MST, until all the vertices are included.
  - Kruskal's algorithm starts with an empty set of edges and adds the edge with the minimum weight that does not create a cycle, until all the vertices are connected.

- Knapsack problem: The knapsack problem is to find the maximum value of items that can be packed into a knapsack with a given capacity. There are two variants of the knapsack problem: the 0-1 knapsack problem and the fractional knapsack problem.

  - The 0-1 knapsack problem assumes that each item can be either taken or left, and the goal is to maximize the total value of the taken items without exceeding the capacity of the knapsack. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio and take the items with the highest ratio until the knapsack is full or no more items can be taken. This algorithm does not always give the optimal solution, but it gives a good approximation.
  - The fractional knapsack problem assumes that each item can be divided into smaller parts, and the goal is to maximize the total value of the items in the knapsack without exceeding the capacity. A greedy algorithm for this problem is to sort the items by their value-to-weight ratio and take as much as possible of the item with the highest ratio, then move to the next item with the next highest ratio, and so on, until the knapsack is full or no more items are available. This algorithm always gives the optimal solution.

- Single source shortest path: The single source shortest path problem is to find the shortest path from a given source vertex to every other vertex in a weighted directed graph. There are two well-known greedy algorithms to solve this problem: Dijkstra's algorithm and Bellman-Ford algorithm.

  - Dijkstra's algorithm maintains a set of vertices whose shortest distance from the source is known, and a priority queue of vertices whose shortest distance is tentative. It repeatedly extracts the vertex with the minimum tentative distance from the queue, updates the tentative distance of its adjacent vertices, and adds them to the queue, until the queue is empty or the destination is reached. This algorithm works only for graphs with non-negative edge weights.
  - Bellman-Ford algorithm iterates over all the edges of the graph and relaxes them, that is, updates the tentative distance of the destination vertex if it can be improved by using the edge. It repeats this process for |V| - 1 times, where |V| is the number of vertices in the graph. This algorithm works for graphs with negative edge weights, but not for graphs with negative cycles.