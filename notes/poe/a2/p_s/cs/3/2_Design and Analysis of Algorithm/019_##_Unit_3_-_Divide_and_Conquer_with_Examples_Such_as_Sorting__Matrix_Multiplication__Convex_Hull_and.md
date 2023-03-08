 Here is the content in markdown format:

## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

Divide and Conquer is a algorithm design technique based on solving a problem by:

1. Breaking it down into smaller subproblems.
2. Solving these subproblems (conquer).
3. Combining their solutions to get the solution of the original problem (combine).

Some key examples of Divide and Conquer are:

- Sorting: Break the array into halves, sort each half recursively and then merge the sorted halves.
- Matrix Multiplication: Break the matrices into quadrants and solve for each quadrant recursively and then combine.
- Convex Hull: Find the leftmost and rightmost points to get the initial upper and lower hulls and then recursively filter out points between them.
- Searching: Break the array into halves and check if the key lies in the left or right half and search recursively.

Greedy methods make a choice at each step that looks the best at that moment.They do not guarantee to lead to optimal solutions always but terminates in a short time. Some examples are:

- Optimal Reliability Allocation: Allocate reliability to components one by one in the order of increasing reliability to component offering most reliability gain.
- Knapsack: Choose items one by one in decreasing order of profit to weight ratio and add to knapsack if capacity allows.
- Minimum Spanning Tree: Choose the edge with least weight at each step and add to spanning tree. Prim's uses nearest neighbor and Kruskal's uses disjoint sets.

Single Source Shortest Paths find shortest paths from a source vertex to all other vertices in a weighted graph. Examples are:

- Dijkstra's: Uses min-priority queue and relaxes adjacent vertices. Works for non-negative weights.
- Bellman-Ford: Relaxes all edges repeatedly. Can detect negative weight cycles.

[Include relevant diagrams, code and other details here if required]