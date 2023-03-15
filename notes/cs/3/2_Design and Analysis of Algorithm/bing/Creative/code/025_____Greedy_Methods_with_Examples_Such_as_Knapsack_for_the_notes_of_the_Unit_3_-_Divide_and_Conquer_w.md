# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure
A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate point C and the shortest path from C to B.

## Greedy Choice Property
A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

### Fractional Knapsack Problem
Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, determine the maximum value that can be obtained by filling the knapsack with a fraction of each item. The greedy method for this problem is to sort the items by their value per unit weight in decreasing order, and then pick the items in that order until the knapsack is full or no more items are left. If the knapsack is not full and there is still some item left, take a fraction of that item to fill the knapsack completely. This method always gives the optimal solution, because at each step, it chooses the item that gives the most value per unit weight.

### Minimum Spanning Tree
Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy method for this problem is to start with an empty set of edges, and then repeatedly add the edge with the minimum weight that does not form a cycle with the existing edges, until all the vertices are connected. This method always gives the optimal solution, because at each step, it chooses the edge that minimizes the total weight of the spanning tree.

There are two well-known algorithms that implement this greedy method: Prim's algorithm and Kruskal's algorithm. Prim's algorithm starts with an arbitrary vertex and grows the spanning tree by adding the minimum weight edge that connects a vertex in the tree to a vertex outside the tree. Kruskal's algorithm starts with an empty set of edges and grows the spanning tree by adding the minimum weight edge that connects two disjoint components of the graph.

### Single Source Shortest Path
Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex in the graph. The greedy method for this problem is to maintain a set of vertices whose shortest distance from the source is known, and a priority queue of vertices whose shortest distance from the source is estimated. Initially, the set contains only the source vertex, and the priority queue contains all the other vertices with their distances set to infinity. Then, the algorithm repeatedly extracts the vertex with the minimum distance from the priority queue, adds it to the set, and updates the distances of its adjacent vertices in the priority queue. This method always gives the optimal solution, if the graph does not contain negative weight cycles.

There are two well-known algorithms that implement this greedy method: Dijkstra's algorithm and Bellman-Ford algorithm. Dijkstra's algorithm assumes that the graph does not have negative weight edges, and uses a binary heap as the priority queue. Bellman-Ford algorithm can handle negative weight edges, but not negative weight cycles, and uses a simple queue as the priority queue.