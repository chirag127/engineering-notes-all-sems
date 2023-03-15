# Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The main idea of merge sort is to divide the problem of sorting an array of n elements into two subproblems of sorting two subarrays of n/2 elements each, and then combine the solutions of the subproblems by merging the two sorted subarrays.
- The algorithm can be described as follows:

  - **Base case:** If the array has zero or one element, it is already sorted and no further action is needed.
  - **Recursive case:** If the array has more than one element, do the following steps:
    - Divide the array into two subarrays of equal or nearly equal size.
    - Recursively sort the left subarray using merge sort.
    - Recursively sort the right subarray using merge sort.
    - Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and combines them into a single sorted array. It can be implemented as follows:

  - Initialize three pointers: i to point to the first element of the left subarray, j to point to the first element of the right subarray, and k to point to the first element of the output array.
  - While i and j are both less than the size of their respective subarrays, do the following steps:
    - Compare the elements at A[i] and A[j], where A is the input array.
    - If A[i] <= A[j], copy A[i] to the output array at index k, and increment i and k by one.
    - If A[i] > A[j], copy A[j] to the output array at index k, and increment j and k by one.
  - If i reaches the end of the left subarray, copy the remaining elements of the right subarray to the output array.
  - If j reaches the end of the right subarray, copy the remaining elements of the left subarray to the output array.

- The pseudocode for merge sort is as follows:

  ```
  MERGE-SORT(A, p, r)
  // A is the input array, p is the starting index, r is the ending index
  // The subarray A[p..r] is sorted in place
  if p < r
    q = floor((p + r) / 2) // find the middle point
    MERGE-SORT(A, p, q) // sort the left subarray
    MERGE-SORT(A, q + 1, r) // sort the right subarray
    MERGE(A, p, q, r) // merge the two sorted subarrays

  MERGE(A, p, q, r)
  // A is the input array, p is the starting index of the left subarray, q is the ending index of the left subarray, r is the ending index of the right subarray
  // The subarrays A[p..q] and A[q + 1..r] are merged into a single sorted array A[p..r]
  n1 = q - p + 1 // the size of the left subarray
  n2 = r - q // the size of the right subarray
  create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
  for i = 1 to n1
    L[i] = A[p + i - 1] // copy the left subarray to L
  for j = 1 to n2
    R[j] = A[q + j] // copy the right subarray to R
  L[n1 + 1] = infinity // a sentinel value to mark the end of the left subarray
  R[n2 + 1] = infinity // a sentinel value to mark the end of the right subarray
  i = 1 // the pointer for the left subarray
  j = 1 // the pointer for the right subarray
  for k = p to r
    if L[i] <= R[j]
      A[k] = L[i] // copy the smaller element to the output array
      i = i + 1 // increment the pointer for the left subarray
    else
      A[k] = R[j] // copy the smaller element to the output array
      j = j + 1 // increment the pointer for the right subarray
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the