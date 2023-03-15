### Divide and Conquer

Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are typically solved using the same algorithm, and the solutions to the subproblems are combined to form the solution to the original problem.

Some examples of algorithms that use the Divide and Conquer paradigm are:

- **Sorting**: QuickSort and MergeSort are two sorting algorithms that use the Divide and Conquer approach. QuickSort works by partitioning the input array into two smaller sub-arrays and then recursively sorting the sub-arrays. MergeSort works by dividing the input array into two halves, recursively sorting the halves, and then merging the two sorted halves.

- **Matrix Multiplication**: The Strassen's algorithm for matrix multiplication uses the Divide and Conquer approach. It works by dividing the input matrices into smaller submatrices and recursively multiplying them.

- **Convex Hull**: The QuickHull algorithm for finding the convex hull of a set of points uses the Divide and Conquer approach. It works by dividing the set of points into two subsets and recursively finding the convex hull of each subset.

- **Searching**: Binary Search is a searching algorithm that uses the Divide and Conquer approach. It works by dividing the input array into two halves and recursively searching the half that may contain the target value.

### Greedy Methods

Greedy Methods are an algorithmic paradigm that builds a solution to a problem by making a sequence of choices that are locally optimal. The hope is that the sequence of locally optimal choices will lead to a globally optimal solution.

Some examples of algorithms that use the Greedy Methods paradigm are:

- **Optimal Reliability Allocation**: The greedy algorithm for optimal reliability allocation works by iteratively allocating the available resources to the component with the highest marginal increase in reliability.

- **Knapsack**: The greedy algorithm for the Knapsack problem works by iteratively selecting the item with the highest value-to-weight ratio that fits in the remaining capacity of the knapsack.

- **Minimum Spanning Trees**: Prim's and Kruskal's algorithms are two algorithms for finding the minimum spanning tree of a graph that use the Greedy Methods approach. Prim's algorithm works by iteratively adding the edge with the lowest weight that connects a vertex in the current tree to a vertex outside the tree. Kruskal's algorithm works by iteratively adding the edge with the lowest weight that does not create a cycle.

- **Single Source Shortest Paths**: Dijkstra's and Bellman Ford algorithms are two algorithms for finding the shortest paths from a single source to all other vertices in a graph that use the Greedy Methods approach. Dijkstra's algorithm works by iteratively selecting the vertex with the minimum distance from the source and relaxing its outgoing edges. Bellman Ford algorithm works by iteratively relaxing all the edges in the graph.
