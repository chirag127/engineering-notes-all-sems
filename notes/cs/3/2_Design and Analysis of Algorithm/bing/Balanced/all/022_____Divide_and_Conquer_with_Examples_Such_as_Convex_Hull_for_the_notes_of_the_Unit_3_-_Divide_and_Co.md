# Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps:
  - Divide: Split the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: Solve the subproblems recursively, either directly or by applying the divide and conquer approach again.
  - Combine: Merge the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient, as they reduce the problem size exponentially at each level of recursion, and they are suitable for parallel and distributed computing.
- Some examples of divide and conquer algorithms are:
  - Merge sort: A sorting algorithm that divides the array into two halves, sorts them recursively, and then merges the sorted halves.
  - Quick sort: A sorting algorithm that partitions the array around a pivot element, such that all elements smaller than the pivot are on its left and all elements larger than the pivot are on its right, and then sorts the two subarrays recursively.
  - Binary search: A search algorithm that finds the position of a target value in a sorted array by repeatedly comparing the target with the middle element and halving the search range accordingly.
  - Strassen's algorithm: A matrix multiplication algorithm that divides each matrix into four submatrices, computes seven products of submatrices recursively, and then combines them to get the final product.
  - Fast Fourier transform: A numerical algorithm that computes the discrete Fourier transform of a sequence of complex numbers by dividing the sequence into two subsequences of even and odd indices, computing their Fourier transforms recursively, and then combining them using complex roots of unity.
  - Convex hull: A geometric algorithm that finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two subsets, finding their convex hulls recursively, and then merging them using a linear-time algorithm.