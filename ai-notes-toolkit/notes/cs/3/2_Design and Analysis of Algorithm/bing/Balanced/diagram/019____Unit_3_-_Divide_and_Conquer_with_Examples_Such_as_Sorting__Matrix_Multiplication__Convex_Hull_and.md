## Unit 3 - Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching. Greedy Methods with Examples Such as Optimal Reliability Allocation, Knapsack, Minimum Spanning Trees – Prim’s and Kruskal’s Algorithms, Single Source Shortest Paths - Dijkstra’s and Bellman Ford Algorithms.

### Divide and Conquer

- Divide and conquer is a technique of solving a complex problem by breaking it into smaller and simpler subproblems that can be solved recursively  .
- The general idea of divide and conquer is to have three steps:
  - Divide the problem into a number of subproblems that are smaller instances of the same problem.
  - Conquer the subproblems by solving them recursively. If they are small enough, solve the subproblems as base cases.
  - Combine the solutions to the subproblems into the solution for the original problem.
- Some examples of divide and conquer algorithms are :
  - Binary search: Given a sorted array of elements, find a target element by repeatedly dividing the array into two halves and comparing the middle element with the target. The time complexity is O(log n).
  - Merge sort: Given an array of elements, sort them by dividing the array into two halves, sorting the two halves recursively, and then merging the sorted halves. The time complexity is O(n log n).
  - Quick sort: Given an array of elements, sort them by choosing a pivot element, partitioning the array into two subarrays such that all elements less than the pivot are in the left subarray and all elements greater than or equal to the pivot are in the right subarray, and then sorting the two subarrays recursively. The average time complexity is O(n log n).
  - Strassen's algorithm: Given two matrices, multiply them by dividing each matrix into four submatrices, computing seven products of submatrices recursively, and then combining the products into the final result. The time complexity is O(n^2.8074).
  - Fast Fourier transform: Given a sequence of complex numbers, compute its discrete Fourier transform by dividing the sequence into two subsequences of even and odd indices, computing the Fourier transforms of the subsequences recursively, and then combining them using the butterfly operation. The time complexity is O(n log n).
  - Convex hull: Given a set of points in the plane, find the smallest convex polygon that contains all the points by dividing the set into two subsets, finding the convex hulls of the subsets recursively, and then merging the hulls using the upper and lower tangent algorithm. The time complexity is O(n log n).

### Greedy Methods

- Greedy methods are a technique of solving an optimization problem by making a sequence of choices that are locally optimal, hoping that they will lead to a globally optimal solution.
- The general idea of greedy methods is to have two steps:
  - Make a greedy choice that is the best option at the moment, without considering the future consequences.
  - Reduce the problem to a smaller subproblem that satisfies the feasibility and optimality conditions, and apply the same method recursively.
- Some examples of greedy methods are:
  - Optimal reliability allocation: Given a system of n components, each with a reliability and a cost, and a budget B, find the optimal allocation of the budget to improve the reliability of the components such that the overall reliability of the system is maximized. The greedy method is to sort the components by the ratio of reliability improvement to cost, and then allocate the budget to the components in that order until the budget is exhausted or all components are improved. The time complexity is O(n log n).
  - Knapsack problem: Given a set of items, each with a weight and a value, and a capacity W, find the subset of items that maximizes the total value without exceeding the capacity. The greedy method is to sort the items by the ratio of value to weight, and then select the items in that order until the capacity is reached or all items are considered. The time complexity is O(n log n).
  - Minimum spanning tree: Given a connected, undirected, weighted graph, find a subset of edges that connects all the vertices with the minimum total weight. The greedy method is to start with an empty set of edges, and then repeatedly add the edge with the minimum weight that does not create a cycle, until all the vertices are connected. There are two variants of this method: Prim's algorithm and Kruskal's algorithm. The