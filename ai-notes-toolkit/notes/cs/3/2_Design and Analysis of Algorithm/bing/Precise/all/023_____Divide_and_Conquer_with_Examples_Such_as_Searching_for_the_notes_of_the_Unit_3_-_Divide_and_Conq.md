# Divide and Conquer with Examples Such as Searching

Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are typically solved using the same algorithm as the original problem. The solutions to the subproblems are then combined to form the solution to the original problem.

Some examples of algorithms that use the Divide and Conquer paradigm are:

1. **Sorting**: QuickSort and MergeSort are two sorting algorithms that use the Divide and Conquer paradigm. QuickSort works by partitioning the array into two smaller sub-arrays and then recursively sorting them. MergeSort works by dividing the array into two halves, recursively sorting them, and then merging the two sorted halves.

2. **Matrix Multiplication**: The Strassen's algorithm for matrix multiplication uses the Divide and Conquer paradigm. It works by dividing the matrices into smaller submatrices and recursively multiplying them.

3. **Convex Hull**: The QuickHull algorithm for finding the convex hull of a set of points uses the Divide and Conquer paradigm. It works by dividing the set of points into two subsets and recursively finding the convex hull of each subset.

4. **Searching**: Binary Search is a searching algorithm that uses the Divide and Conquer paradigm. It works by dividing the search space in half and recursively searching the half that contains the target value.

# Greedy Methods with Examples

Greedy Methods is an algorithmic paradigm that builds a solution to a problem by making a sequence of choices that are locally optimal. The hope is that the sequence of locally optimal choices will lead to a globally optimal solution.

Some examples of algorithms that use the Greedy Methods paradigm are:

1. **Optimal Reliability Allocation**: The greedy algorithm for optimal reliability allocation works by allocating the available resources to the component with the highest marginal increase in reliability.

2. **Knapsack**: The greedy algorithm for the Knapsack problem works by selecting the items with the highest value-to-weight ratio until the knapsack is full.

3. **Minimum Spanning Trees**: Prim's and Kruskal's algorithms are two algorithms for finding the minimum spanning tree of a graph that use the Greedy Methods paradigm. Prim's algorithm works by growing the minimum spanning tree one vertex at a time, always adding the edge with the smallest weight that connects a vertex in the tree to a vertex not in the tree. Kruskal's algorithm works by sorting the edges by weight and always adding the edge with the smallest weight that does not create a cycle.

4. **Single Source Shortest Paths**: Dijkstra's and Bellman Ford algorithms are two algorithms for finding the shortest paths from a single source to all other vertices in a graph that use the Greedy Methods paradigm. Dijkstra's algorithm works by maintaining a priority queue of vertices, always selecting the vertex with the smallest distance from the source, and relaxing its edges. Bellman Ford algorithm works by iteratively relaxing all the edges in the graph.
