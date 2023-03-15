# Divide and Conquer with Examples Such as Sorting, Matrix Multiplication, Convex Hull and Searching

- Divide and conquer is a technique for solving problems by breaking them into smaller and simpler subproblems, solving them recursively, and combining their solutions to obtain the solution for the original problem.
- Divide and conquer has three main steps:
  - Divide: Split the problem into smaller subproblems of the same type.
  - Conquer: Solve the subproblems recursively. If the subproblems are small enough, solve them directly.
  - Combine: Merge the solutions of the subproblems to obtain the solution for the original problem.
- Divide and conquer is useful for solving problems that have the following characteristics:
  - The problem can be divided into smaller subproblems of the same type.
  - The subproblems can be solved independently and in parallel.
  - The subproblems are not too many and not too small.
  - The solution for the original problem can be obtained by combining the solutions of the subproblems in a simple and efficient way.
- Some examples of problems that can be solved by divide and conquer are:

## Sorting
- Sorting is the problem of arranging a sequence of elements in a specific order, such as ascending or descending.
- Sorting can be done by divide and conquer by splitting the sequence into two halves, sorting them recursively, and merging them in a sorted order.
- Some sorting algorithms that use divide and conquer are:
  - Merge sort: Divide the sequence into two halves, sort them recursively, and merge them in a sorted order. The time complexity is O(n log n), where n is the number of elements.
  - Quick sort: Choose a pivot element, partition the sequence into two subarrays such that the elements in the left subarray are smaller than or equal to the pivot and the elements in the right subarray are larger than the pivot, sort the subarrays recursively, and concatenate them. The time complexity is O(n log n) on average, but O(n^2) in the worst case, where n is the number of elements.
  - Heap sort: Build a max-heap or a min-heap from the sequence, repeatedly extract the root element and place it at the end of the sequence, and reduce the heap size by one. The time complexity is O(n log n), where n is the number of elements.

## Matrix Multiplication
- Matrix multiplication is the problem of multiplying two matrices of compatible dimensions and obtaining a product matrix.
- Matrix multiplication can be done by divide and conquer by splitting the matrices into four submatrices of equal size, multiplying them recursively, and adding or subtracting the results to obtain the product matrix.
- Some matrix multiplication algorithms that use divide and conquer are:
  - Strassen's algorithm: Divide the matrices into four submatrices of size n/2 x n/2, compute seven products of submatrices using recursive calls, and combine them using addition and subtraction to obtain the product matrix. The time complexity is O(n^2.81), where n is the dimension of the matrices.
  - Coppersmith-Winograd algorithm: Divide the matrices into submatrices of size n^(1/3) x n^(1/3), compute 23 products of submatrices using recursive calls, and combine them using addition and subtraction to obtain the product matrix. The time complexity is O(n^2.375), where n is the dimension of the matrices.

## Convex Hull
- Convex hull is the problem of finding the smallest convex polygon that contains a set of points in the plane.
- Convex hull can be done by divide and conquer by splitting the points into two subsets by a vertical line, finding the convex hulls of the subsets recursively, and merging them by finding the upper and lower tangents. The time complexity is O(n log n), where n is the number of points.

## Searching
- Searching is the problem of finding an element in a sequence or a data structure that satisfies a given condition or matches a given value.
- Searching can be done by divide and conquer by splitting the sequence or the data structure into two parts, checking the condition or the value in one part, and searching recursively in the other part if needed.
- Some searching algorithms that use divide and conquer are:
  - Binary search: Given a sorted sequence and a value, find the index of the value in the sequence or return -1 if not found. Compare the value with the middle element of the sequence, and search recursively in the left or right half depending on the comparison result. The time complexity is O(log n), where n is the number of elements.
  - Interpolation search: Given a sorted sequence and a value, find the index of the value in the sequence or return -1 if not found. Estimate