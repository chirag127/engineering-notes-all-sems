## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Divide and Conquer
Divide and Conquer is an algorithmic paradigm that solves a problem by dividing it into smaller subproblems and solving them recursively. The subproblems are typically solved using the same algorithm as the original problem. The solutions to the subproblems are then combined to form the solution to the original problem.

#### Examples
1. **Sorting**: QuickSort and MergeSort are two popular sorting algorithms that use the divide and conquer approach. QuickSort works by partitioning the input array into two smaller sub-arrays and then recursively sorting the sub-arrays. MergeSort works by dividing the input array into two halves, recursively sorting the halves, and then merging the two sorted halves.
2. **Matrix Multiplication**: The Strassen's algorithm for matrix multiplication uses the divide and conquer approach to multiply two matrices. The algorithm works by dividing the input matrices into smaller submatrices and recursively multiplying the submatrices.
3. **Convex Hull**: The Graham's scan algorithm for finding the convex hull of a set of points uses the divide and conquer approach. The algorithm works by dividing the set of points into two halves, recursively finding the convex hull of each half, and then merging the two convex hulls.
4. **Searching**: Binary search is a popular searching algorithm that uses the divide and conquer approach. The algorithm works by dividing the input array into two halves and recursively searching the half that contains the target value.

### Greedy Methods
Greedy methods are a class of algorithms that make locally optimal choices at each step in the hope of finding a global optimum. Greedy algorithms do not always guarantee an optimal solution, but they are often efficient and easy to implement.

#### Examples
1. **Optimal Reliability Allocation**: The greedy algorithm for optimal reliability allocation works by allocating the available budget to the component with the highest reliability per unit cost at each step.
2. **Knapsack**: The greedy algorithm for the knapsack problem works by selecting the item with the highest value per unit weight at each step.
3. **Minimum Spanning Trees**: Prim's and Kruskal's algorithms are two popular greedy algorithms for finding the minimum spanning tree of a graph. Prim's algorithm works by growing the minimum spanning tree one vertex at a time, while Kruskal's algorithm works by adding the next lightest edge that does not form a cycle at each step.
4. **Single Source Shortest Paths**: Dijkstra's and Bellman Ford algorithms are two popular greedy algorithms for finding the shortest paths from a single source to all other vertices in a graph. Dijkstra's algorithm works by iteratively selecting the vertex with the minimum distance from the source and relaxing its outgoing edges, while Bellman Ford algorithm works by iteratively relaxing all the edges in the graph.