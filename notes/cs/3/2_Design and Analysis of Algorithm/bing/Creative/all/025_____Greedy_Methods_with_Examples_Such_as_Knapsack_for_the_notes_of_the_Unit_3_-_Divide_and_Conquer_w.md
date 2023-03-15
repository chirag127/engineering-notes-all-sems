# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure
A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate point C and the shortest path from C to B.

## Greedy Choice Property
A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

### Fractional Knapsack Problem
Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, determine the maximum value that can be obtained by filling the knapsack with a fraction of each item. The fractional knapsack problem can be solved by a greedy method as follows:

- Sort the items in decreasing order of their value per unit weight.
- Initialize the total value to zero and the remaining capacity to the maximum capacity.
- For each item in the sorted order, do the following:
  - If the item's weight is less than or equal to the remaining capacity, then take the whole item and add its value to the total value. Subtract its weight from the remaining capacity.
  - If the item's weight is more than the remaining capacity, then take a fraction of the item that fills the remaining capacity. Add the fraction of the item's value to the total value. Set the remaining capacity to zero.
  - If the remaining capacity is zero, then stop.

### Minimum Spanning Tree
Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. A minimum spanning tree (MST) is such a subset of edges. The minimum spanning tree problem can be solved by two greedy methods: Prim's algorithm and Kruskal's algorithm.

#### Prim's Algorithm
Prim's algorithm starts with an arbitrary vertex and grows the MST one edge at a time. At each step, it adds the minimum weight edge that connects a vertex in the MST to a vertex not in the MST. Prim's algorithm can be implemented as follows:

- Initialize the MST to an empty set and the set of visited vertices to contain the arbitrary vertex.
- While there are still unvisited vertices, do the following:
  - Find the minimum weight edge that connects a visited vertex to an unvisited vertex. Add this edge to the MST and the unvisited vertex to the set of visited vertices.

#### Kruskal's Algorithm
Kruskal's algorithm starts with an empty MST and adds edges one by one in increasing order of weight. At each step, it adds the minimum weight edge that does not create a cycle in the MST. Kruskal's algorithm can be implemented as follows:

- Sort the edges in increasing order of weight.
- Initialize the MST to an empty set and a disjoint-set data structure to contain each vertex as a separate set.
- For each edge in the sorted order, do the following:
  - If the edge connects two vertices that belong to different sets, then add this edge to the MST and union the two sets.

### Single Source Shortest Path
Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex in the graph. The single source shortest path problem can be solved by two greedy methods: Dijkstra's algorithm and Bellman-Ford algorithm.

#### Dijkstra's Algorithm
Dijkstra's algorithm maintains a set of visited vertices and a priority queue of unvisited vertices with their distances from the source. At each step, it extracts the minimum distance vertex from the priority queue and adds it to the set of visited vertices. Then, it relaxes the edges outgoing from the extracted vertex, updating the distances and the priority queue. Dijkstra's algorithm can be implemented as follows:

- Initialize the distance of the source vertex to zero and the distance of every other vertex to infinity. Initialize the set of visited vertices to an empty set and the priority queue of unvisited vertices to contain all the vertices with their