# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure
A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate point C and the shortest path from C to B.

## Greedy Choice Property
A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

### Optimal Reliability Allocation
The optimal reliability allocation problem is to allocate a given budget to improve the reliability of a system consisting of n components. The objective is to maximize the overall system reliability, which is the probability that all components function properly. The reliability of each component can be improved by investing some amount of money, but the marginal benefit decreases as the reliability increases. The problem can be solved by a greedy method that allocates the budget to the component with the highest marginal benefit at each step.

### Knapsack Problem
The knapsack problem is to fill a knapsack with a given capacity with items that have different weights and values. The objective is to maximize the total value of the items in the knapsack. There are two variants of the problem: the 0-1 knapsack problem, where each item can be either taken or left, and the fractional knapsack problem, where each item can be taken partially. The 0-1 knapsack problem cannot be solved by a greedy method, but the fractional knapsack problem can be solved by choosing the item with the highest value per unit weight at each step.

### Minimum Spanning Tree
The minimum spanning tree problem is to find a subset of edges in a weighted undirected graph that connects all the vertices and has the minimum total weight. The problem can be solved by two greedy methods: Prim's algorithm and Kruskal's algorithm. Prim's algorithm starts with an arbitrary vertex and adds the edge with the minimum weight that connects a vertex in the tree to a vertex outside the tree at each step. Kruskal's algorithm sorts the edges by weight and adds the edge with the minimum weight that does not create a cycle at each step.

### Single Source Shortest Path
The single source shortest path problem is to find the shortest path from a given source vertex to every other vertex in a weighted directed graph. The problem can be solved by two greedy methods: Dijkstra's algorithm and Bellman-Ford algorithm. Dijkstra's algorithm maintains a set of vertices whose shortest distance from the source is known and adds the vertex with the minimum distance to the set at each step. Bellman-Ford algorithm relaxes the distance of each edge at each iteration and repeats the process n-1 times, where n is the number of vertices.