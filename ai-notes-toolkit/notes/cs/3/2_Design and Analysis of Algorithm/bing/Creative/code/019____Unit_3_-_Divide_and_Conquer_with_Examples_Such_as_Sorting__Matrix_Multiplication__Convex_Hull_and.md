Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use as study material.

## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Divide and Conquer
- Divide and conquer is a technique of solving a complex problem by breaking it into smaller and simpler subproblems that can be solved recursively or iteratively.
- The general idea of divide and conquer is to divide the problem into a number of subproblems that are smaller instances of the same problem, conquer the subproblems by solving them recursively or directly, and combine the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms have three main steps:
  - **Divide**: Split the problem into smaller and simpler subproblems, usually of the same type as the original problem.
  - **Conquer**: Solve the subproblems recursively or directly. If the subproblems are small enough, they can be solved as base cases.
  - **Combine**: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the problem size exponentially and exploit the properties of the subproblems. However, they also have some drawbacks, such as the overhead of recursion, the complexity of combining the solutions, and the difficulty of finding the optimal way of dividing the problem.
- Some examples of divide and conquer algorithms are:
  - **Binary search**: A search algorithm that finds the position of a target value within a sorted array by repeatedly dividing the search interval in half and comparing the target value with the middle element. Binary search has a time complexity of O(log n), where n is the size of the array.
  - **Merge sort**: A sorting algorithm that sorts an array by recursively dividing it into two halves, sorting each half, and merging the sorted halves. Merge sort has a time complexity of O(n log n), where n is the size of the array.
  - **Quick sort**: A sorting algorithm that sorts an array by recursively choosing a pivot element, partitioning the array around the pivot, and sorting the subarrays on each side of the pivot. Quick sort has an average time complexity of O(n log n), where n is the size of the array, but a worst-case time complexity of O(n^2) if the pivot is chosen poorly.
  - **Strassen's algorithm**: A matrix multiplication algorithm that multiplies two n x n matrices by recursively dividing them into four n/2 x n/2 submatrices, computing seven products of the submatrices, and combining the products to obtain the final result. Strassen's algorithm has a time complexity of O(n^2.8074), where n is the size of the matrices, which is better than the naive algorithm that has a time complexity of O(n^3).
  - **Convex hull**: A geometric problem that finds the smallest convex polygon that contains a set of points in the plane. A convex polygon is a polygon that has no interior angles greater than 180 degrees. A convex hull can be computed by recursively dividing the set of points into two subsets, finding the convex hulls of each subset, and merging the convex hulls using a technique called Graham scan. The time complexity of this algorithm is O(n log n), where n is the number of points.

### Greedy Methods
- Greedy methods are a technique of solving a problem by making a sequence of choices that are locally optimal, hoping that they will lead to a globally optimal solution.
- The general idea of greedy methods is to start with an empty or partial solution, and iteratively add or remove elements that are the best choice at each step, until the solution is complete or optimal.
- Greedy methods are often simple and fast, as they make decisions based on the current state and do not look ahead or backtrack. However, they also have some drawbacks, such as the possibility of getting stuck in a local optimum and missing the global optimum, and the difficulty of proving the correctness and optimality of the solution.
- Some examples of greedy methods are:
  - **Optimal reliability allocation**: A problem that allocates a given budget to improve the reliability of a system composed of n components, such that the overall reliability of the system is maximized. A reliability of a component