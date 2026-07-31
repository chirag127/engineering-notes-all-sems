# Merge Sort

## Introduction

- Merge sort is a sorting algorithm that uses the divide and conquer technique to sort a given set of n integer elements.
- The algorithm divides the input array into two subarrays of roughly equal size, recursively sorts each subarray, and then merges the two sorted subarrays into one final sorted array.
- The algorithm can be implemented using recursion or iteration, and can be adapted to sort arrays in ascending or descending order, as well as other data structures such as linked lists.

## Algorithm

- The algorithm can be described as follows:

```
merge_sort(A, p, r):
  // A is the input array, p is the starting index, r is the ending index
  if p < r: // base case: array has at least two elements
    q = floor((p + r) / 2) // find the middle point of the array
    merge_sort(A, p, q) // recursively sort the left subarray
    merge_sort(A, q + 1, r) // recursively sort the right subarray
    merge(A, p, q, r) // merge the two sorted subarrays

merge(A, p, q, r):
  // A is the input array, p is the starting index of the left subarray, 
  // q is the ending index of the left subarray, r is the ending index of the right subarray
  n1 = q - p + 1 // compute the length of the left subarray
  n2 = r - q // compute the length of the right subarray
  create arrays L[1..n1 + 1] and R[1..n2 + 1] // create temporary arrays to store the subarrays
  for i = 1 to n1: // copy the left subarray to L
    L[i] = A[p + i - 1]
  for j = 1 to n2: // copy the right subarray to R
    R[j] = A[q + j]
  L[n1 + 1] = infinity // set a sentinel value at the end of L
  R[n2 + 1] = infinity // set a sentinel value at the end of R
  i = 1 // initialize the index for L
  j = 1 // initialize the index for R
  for k = p to r: // loop through the elements of A
    if L[i] <= R[j]: // if the current element of L is smaller or equal to the current element of R
      A[k] = L[i] // copy the element of L to A
      i = i + 1 // increment the index for L
    else: // otherwise, the current element of R is smaller than the current element of L
      A[k] = R[j] // copy the element of R to A
      j = j + 1 // increment the index for R
```

## Time Complexity Analysis

- The time complexity of merge sort depends on the number of comparisons and data movements performed by the algorithm.
- The merge function takes O(n) time to merge two subarrays of size n, where n = r - p + 1.
- The merge sort function divides the array into two subarrays of size n/2, and recursively sorts each subarray in O(n log n) time, where n = r - p + 1.
- Therefore, the overall time complexity of merge sort is O(n log n) for the worst case, average case and best case scenarios, where n is the number of elements in the input array.

## Experiment

- To demonstrate the performance of merge sort, we can run the program for varied values of n > 5000, and record the time taken to sort.
- The elements can be read from a file or can be generated using the random number generator.
- We can plot a graph of the time taken versus n on a graph sheet, and observe the shape of the curve.
- We can also compare the results with other sorting algorithms, such as insertion sort, selection sort, bubble sort, quick sort, heap sort, etc., and analyze their time complexities and advantages and disadvantages.

## Divide and Conquer Method

- Merge sort is an example of the divide and conquer method, which is a general technique for solving problems by breaking them into smaller and simpler subproblems, solving each subproblem recursively or iteratively, and combining the solutions to obtain the final solution.
- The divide and conquer method works by following three steps:

  - Divide: Divide the problem into smaller and simpler subproblems of the same type.
  - Conquer: Solve each subproblem recursively or iteratively, until they are simple