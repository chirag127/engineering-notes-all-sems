# Greedy Methods with Examples

Greedy methods are a class of algorithms that make local optimal choices at each step, hoping to find a global optimal solution. Greedy methods do not always guarantee the best solution, but they are often efficient and easy to implement. Greedy methods are suitable for problems where the optimal substructure and the greedy choice property hold.

## Optimal Substructure

A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. For example, the shortest path problem has optimal substructure, because the shortest path from A to B consists of the shortest path from A to some intermediate node C and the shortest path from C to B.

## Greedy Choice Property

A problem has the greedy choice property if a globally optimal solution can be obtained by making a locally optimal (greedy) choice at each step. For example, the fractional knapsack problem has the greedy choice property, because the optimal solution can be obtained by choosing the item with the highest value per unit weight at each step.

## Examples of Greedy Methods

Some examples of problems that can be solved by greedy methods are:

- Fractional Knapsack Problem: Given a set of items, each with a weight and a value, and a knapsack with a maximum capacity, find the maximum value of items that can be packed in the knapsack. The items can be split into fractions. The greedy choice is to pick the item with the highest value per unit weight at each step. 
- Minimum Spanning Tree: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy choice is to pick the edge with the minimum weight that does not form a cycle with the existing edges at each step. Two common algorithms for finding the minimum spanning tree are Prim's algorithm and Kruskal's algorithm.  
- Single Source Shortest Path: Given a weighted, directed graph and a source vertex, find the shortest path from the source to every other vertex. The greedy choice is to pick the vertex with the minimum distance from the source that has not been visited yet at each step. Two common algorithms for finding the single source shortest path are Dijkstra's algorithm and Bellman-Ford algorithm.  
- Activity Selection Problem: Given a set of activities, each with a start and finish time, find the maximum number of activities that can be performed by a single person or machine, assuming that only one activity can be performed at a time. The greedy choice is to pick the activity with the earliest finish time that does not overlap with the previous activity at each step. 
- Job Sequencing Problem: Given a set of jobs, each with a deadline and a profit, find the maximum profit that can be earned by scheduling the jobs on a single machine, assuming that only one job can be performed at a time and each job takes one unit of time. The greedy choice is to pick the job with the highest profit that can be completed before its deadline at each step. 
- Huffman Code Generation: Given a set of characters and their frequencies, find a variable-length prefix code that minimizes the total number of bits required to encode a given message. The greedy choice is to merge the two characters with the lowest frequencies into a new node with the sum of their frequencies at each step.