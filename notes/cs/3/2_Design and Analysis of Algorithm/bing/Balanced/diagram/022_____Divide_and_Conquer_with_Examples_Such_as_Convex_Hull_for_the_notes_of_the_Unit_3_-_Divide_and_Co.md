### Divide and Conquer with Examples Such as Convex Hull

- Divide and conquer is a paradigm for designing algorithms that solve a problem by breaking it into smaller subproblems, solving them recursively, and combining their solutions to get the final answer.
- Divide and conquer algorithms have three main steps: divide, conquer, and combine.
  - Divide: This step involves splitting the problem into smaller and simpler subproblems, typically of the same type as the original problem.
  - Conquer: This step involves solving each subproblem recursively, either directly or by applying the divide and conquer approach again.
  - Combine: This step involves merging the solutions of the subproblems to obtain the solution of the original problem.
- Divide and conquer algorithms are often efficient and elegant, as they reduce the complexity of the problem by exploiting its structure or properties.
- Some examples of divide and conquer algorithms are:
  - Merge sort: This algorithm sorts an array by dividing it into two halves, sorting each half recursively, and then merging the two sorted halves.
  - Quick sort: This algorithm sorts an array by choosing a pivot element, partitioning the array around the pivot, and then sorting the two subarrays recursively.
  - Binary search: This algorithm searches for a target element in a sorted array by comparing it with the middle element, and then recursively searching in the left or right subarray depending on the comparison result.
  - Strassen's algorithm: This algorithm multiplies two matrices by dividing them into four submatrices each, computing seven products of submatrices recursively, and then combining them to get the final product.
  - Fast Fourier transform: This algorithm computes the discrete Fourier transform of a sequence of complex numbers by dividing it into two sequences of even and odd indices, computing their transforms recursively, and then combining them using complex roots of unity.
  - Convex hull: This algorithm finds the smallest convex polygon that contains a set of points in the plane by dividing the set into two halves, finding the hulls of each half recursively, and then merging the two hulls using a linear scan.