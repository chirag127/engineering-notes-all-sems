# Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

## Divide and Conquer
- Divide and conquer is a technique of solving complex problems by breaking them into smaller and simpler subproblems that can be solved independently and then combining the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer has three steps:
  - Divide: Split the problem into smaller subproblems of the same type.
  - Conquer: Solve each subproblem recursively or directly if they are simple enough.
  - Combine: Merge the solutions of the subproblems to get the solution of the original problem.
- Divide and conquer is useful for problems that have the following properties:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and their solutions can be combined efficiently.
  - The subproblems are not too many or too small, otherwise the overhead of dividing and combining may outweigh the benefits of solving them separately.

### Examples of Divide and Conquer
- Sorting: Sorting is the problem of arranging a list of elements in a certain order, such as ascending or descending. Sorting can be done using divide and conquer by splitting the list into two halves, sorting each half recursively, and then merging the two sorted halves into one sorted list. This is the idea behind merge sort and quick sort algorithms, which have a time complexity of O(n log n) in the average case, where n is the number of elements in the list.
- Matrix Multiplication: Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining a new matrix as the result. Matrix multiplication can be done using divide and conquer by splitting each matrix into four submatrices of equal size, multiplying each pair of submatrices recursively, and then adding the results to get the final matrix. This is the idea behind Strassen's algorithm, which has a time complexity of O(n^2.81), where n is the dimension of the matrices.
- Convex Hull: Convex hull is the problem of finding the smallest convex polygon that contains a given set of points in the plane. Convex hull can be done using divide and conquer by splitting the set of points into two halves, finding the convex hull of each half recursively, and then merging the two convex hulls into one convex hull. This is the idea behind Graham scan and Chan's algorithm, which have a time complexity of O(n log n) and O(n log h), where n is the number of points and h is the number of vertices in the convex hull.
- Searching: Searching is the problem of finding a target element in a list of elements or a key in a dictionary of key-value pairs. Searching can be done using divide and conquer by splitting the list or the dictionary into two halves, checking which half contains the target element or the key, and then searching that half recursively. This is the idea behind binary search and interpolation search algorithms, which have a time complexity of O(log n) and O(log log n) in the average case, where n is the number of elements or the size of the dictionary.

## Greedy Methods
- Greedy methods are a technique of solving optimization problems by making a sequence of choices that look best at the moment, without considering the future consequences of those choices. Greedy methods are based on the assumption that a locally optimal choice will lead to a globally optimal solution.
- Greedy methods have two steps:
  - Selection: Choose the next element that offers the most benefit or the least cost according to some criterion.
  - Feasibility: Check if the chosen element is compatible with the current solution and the problem constraints.
- Greedy methods are useful for problems that have the following properties:
  - The problem can be decomposed into a sequence of choices or steps.
  - There is a clear criterion to compare and rank the choices or steps.
  - There is an optimal substructure, meaning that an optimal solution to the problem contains optimal solutions to the subproblems.
  - There is a greedy choice property, meaning that a locally optimal choice is always part of an optimal solution.

### Examples of Greedy Methods
- Optimal Reliability Allocation: Optimal reliability allocation is the problem of allocating a given budget to improve the reliability of a system composed of n components, such that the overall reliability of the system is maximized. Optimal reliability allocation can be done using greedy methods by choosing the component that has the highest marginal increase in reliability per unit cost at each step, until