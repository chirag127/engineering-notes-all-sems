### Divide and Conquer with Examples Such as Searching

Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are typically solved using the same algorithm, and the solutions to the subproblems are combined to form the solution to the original problem.

Some examples of algorithms that use the Divide and Conquer paradigm include:

1. **Sorting**: QuickSort and MergeSort are two sorting algorithms that use the Divide and Conquer paradigm. QuickSort partitions the input array into two smaller sub-arrays and recursively sorts them. MergeSort divides the input array into two halves, recursively sorts them, and then merges the two sorted halves.
2. **Matrix Multiplication**: The Strassen's algorithm for matrix multiplication uses the Divide and Conquer paradigm to multiply two matrices. The algorithm divides the matrices into smaller submatrices and recursively multiplies them.
3. **Convex Hull**: The QuickHull algorithm for finding the convex hull of a set of points uses the Divide and Conquer paradigm. The algorithm recursively finds the convex hull of subsets of the input points and combines them to form the convex hull of the entire set.
4. **Searching**: Binary Search is an algorithm that uses the Divide and Conquer paradigm to search for a value in a sorted array. The algorithm divides the array into two halves and recursively searches the half that could contain the value.

### Greedy Methods with Examples

Greedy methods are a class of algorithms that make locally optimal choices at each step in the hope of finding a global optimum. These algorithms do not always guarantee an optimal solution, but they often provide good approximations to the optimal solution.

Some examples of algorithms that use greedy methods include:

1. **Optimal Reliability Allocation**: The greedy algorithm for optimal reliability allocation assigns the available resources to the components in decreasing order of their importance, until the resources are exhausted or the desired reliability is achieved.
2. **Knapsack**: The 0-1 Knapsack problem can be solved using a greedy algorithm that selects items in decreasing order of their value-to-weight ratio, until the knapsack is full or there are no more items to select.
3. **Minimum Spanning Trees**: Prim's and Kruskal's algorithms are two greedy algorithms for finding the minimum spanning tree of a graph. Prim's algorithm starts with an arbitrary vertex and adds edges to the tree in increasing order of their weight, while Kruskal's algorithm adds edges to the tree in increasing order of their weight, as long as they do not form a cycle.
4. **Single Source Shortest Paths**: Dijkstra's and Bellman-Ford algorithms are two greedy algorithms for finding the shortest paths from a single source to all other vertices in a graph. Dijkstra's algorithm selects the vertex with the minimum distance from the source and relaxes its outgoing edges, while Bellman-Ford algorithm relaxes all the edges in the graph in each iteration.
