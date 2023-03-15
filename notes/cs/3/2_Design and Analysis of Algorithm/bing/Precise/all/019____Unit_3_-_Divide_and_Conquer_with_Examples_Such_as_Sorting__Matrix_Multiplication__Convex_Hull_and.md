## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

Divide and Conquer is an algorithmic paradigm that solves a problem by breaking it down into smaller subproblems and solving them recursively. Some examples of algorithms that use this approach are:

1. Sorting: QuickSort and MergeSort are two popular sorting algorithms that use the divide and conquer approach. QuickSort works by partitioning the input array into two smaller sub-arrays and then recursively sorting them. MergeSort works by dividing the input array into two halves, recursively sorting them, and then merging the two sorted halves.

2. Matrix Multiplication: The Strassen's algorithm for matrix multiplication uses the divide and conquer approach to multiply two matrices. It works by dividing the matrices into smaller submatrices and recursively multiplying them.

3. Convex Hull: The Graham's scan algorithm for finding the convex hull of a set of points uses the divide and conquer approach. It works by sorting the points by their polar angle and then recursively finding the upper and lower hulls.

4. Searching: Binary search is a popular searching algorithm that uses the divide and conquer approach. It works by repeatedly dividing the search interval in half and checking if the middle element is the target value.

Greedy methods are another algorithmic paradigm that solves problems by making the locally optimal choice at each stage. Some examples of algorithms that use this approach are:

1. Optimal Reliability Allocation: The greedy algorithm for optimal reliability allocation works by allocating the available resources to the components with the highest failure rate.

2. Knapsack: The greedy algorithm for the knapsack problem works by selecting the items with the highest value-to-weight ratio and adding them to the knapsack until it is full.

3. Minimum Spanning Trees: Prim's and Kruskal's algorithms are two popular greedy algorithms for finding the minimum spanning tree of a graph. Prim's algorithm works by starting with an arbitrary vertex and repeatedly adding the edge with the smallest weight that connects a vertex in the tree to a vertex outside the tree. Kruskal's algorithm works by sorting the edges by their weight and repeatedly adding the edge with the smallest weight that does not create a cycle.

4. Single Source Shortest Paths: Dijkstra's and Bellman Ford algorithms are two popular greedy algorithms for finding the shortest paths from a single source to all other vertices in a graph. Dijkstra's algorithm works by maintaining a priority queue of vertices and repeatedly extracting the vertex with the smallest distance and relaxing its outgoing edges. Bellman Ford algorithm works by repeatedly relaxing all the edges in the graph and checking for negative cycles.