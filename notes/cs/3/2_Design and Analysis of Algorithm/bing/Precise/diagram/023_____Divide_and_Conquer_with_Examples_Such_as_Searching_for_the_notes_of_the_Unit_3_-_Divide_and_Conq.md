### Divide and Conquer with Examples Such as Searching

Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are typically solved using the same algorithm, and the solutions to the subproblems are combined to form the solution to the original problem.

Some common examples of problems that can be solved using the Divide and Conquer approach include:

1. **Sorting**: QuickSort and MergeSort are two popular sorting algorithms that use the Divide and Conquer approach. In QuickSort, the array is partitioned into two smaller sub-arrays, and the partitioning is done in such a way that elements smaller than the pivot element go to the left sub-array and elements greater than the pivot element go to the right sub-array. The same process is then applied recursively to the two sub-arrays. In MergeSort, the array is divided into two halves, and the two halves are sorted recursively. The two sorted halves are then merged to form the final sorted array.

2. **Matrix Multiplication**: The Strassen's algorithm for matrix multiplication uses the Divide and Conquer approach. The matrices are divided into smaller submatrices, and the multiplication is performed recursively on these smaller submatrices.

3. **Convex Hull**: The problem of finding the convex hull of a set of points can be solved using the Divide and Conquer approach. The set of points is divided into two halves, and the convex hulls of the two halves are computed recursively. The two convex hulls are then merged to form the final convex hull.

4. **Searching**: Binary Search is a popular searching algorithm that uses the Divide and Conquer approach. In Binary Search, the array is divided into two halves, and the element is searched in one of the two halves depending on the value of the middle element. The same process is then applied recursively to the half in which the element is present.

### Greedy Methods with Examples

Greedy Method is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most obvious and immediate benefit. Greedy algorithms are used for optimization problems, where the goal is to find the best solution among a set of feasible solutions.

Some common examples of problems that can be solved using the Greedy approach include:

1. **Optimal Reliability Allocation**: In this problem, the goal is to allocate the available resources in such a way that the system reliability is maximized. A greedy approach can be used to solve this problem by always allocating the resources to the component that provides the maximum increase in reliability.

2. **Knapsack**: The Knapsack problem is a combinatorial optimization problem where the goal is to select a subset of items with maximum total value, subject to a constraint on the total weight of the selected items. A greedy approach can be used to solve this problem by always selecting the item with the highest value-to-weight ratio.

3. **Minimum Spanning Trees**: Prim's and Kruskal's algorithms are two popular algorithms for finding the minimum spanning tree of a graph. Both these algorithms use the Greedy approach. In Prim's algorithm, the tree is grown one edge at a time by always adding the edge that connects the tree to a new vertex and has the minimum weight. In Kruskal's algorithm, the edges are sorted in non-decreasing order of their weights, and the edges are added to the tree in this order, as long as they do not form a cycle.

4. **Single Source Shortest Paths**: Dijkstra's and Bellman Ford algorithms are two popular algorithms for finding the shortest paths from a single source to all other vertices in a graph. Both these algorithms use the Greedy approach. In Dijkstra's algorithm, the distances to the vertices are updated iteratively, and in each iteration, the vertex with the minimum distance is selected and its distance is finalized. In Bellman Ford algorithm, the distances are updated iteratively, and in each iteration, the distances are updated by relaxing the edges.
