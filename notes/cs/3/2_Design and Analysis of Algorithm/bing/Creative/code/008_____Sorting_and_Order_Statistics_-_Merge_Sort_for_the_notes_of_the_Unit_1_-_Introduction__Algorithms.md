### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays, sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  - **Base case**: If the array has zero or one element, it is already sorted and no further action is needed.
  - **Recursive case**: If the array has more than one element, divide it into two subarrays of roughly equal size, and sort each subarray recursively using merge sort.
  - **Merge step**: After sorting the subarrays, merge them into a single sorted array by repeatedly taking the smallest element from either subarray and appending it to the output array, until both subarrays are empty.

- The pseudocode for merge sort is given below:

  ```
  MERGE-SORT(A, p, r)
  // A is the array to be sorted
  // p and r are the indices of the first and last element of the subarray
  // initially p = 1 and r = n, where n is the length of A
  if p < r
    q = floor((p + r) / 2) // find the midpoint of the subarray
    MERGE-SORT(A, p, q) // sort the left subarray recursively
    MERGE-SORT(A, q + 1, r) // sort the right subarray recursively
    MERGE(A, p, q, r) // merge the two sorted subarrays
  ```

  ```
  MERGE(A, p, q, r)
  // A is the array to be merged
  // p, q, and r are the indices of the first, middle, and last element of the subarray
  // assume that A[p..q] and A[q+1..r] are sorted
  n1 = q - p + 1 // the length of the left subarray
  n2 = r - q // the length of the right subarray
  create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
  for i = 1 to n1
    L[i] = A[p + i - 1] // copy the left subarray to L
  for j = 1 to n2
    R[j] = A[q + j] // copy the right subarray to R
  L[n1 + 1] = infinity // a sentinel value to mark the end of L
  R[n2 + 1] = infinity // a sentinel value to mark the end of R
  i = 1 // the index of the current element in L
  j = 1 // the index of the current element in R
  for k = p to r // loop through the output array
    if L[i] <= R[j] // if the current element in L is smaller or equal to the current element in R
      A[k] = L[i] // copy it to the output array
      i = i + 1 // increment the index of L
    else // otherwise
      A[k] = R[j] // copy the current element in R to the output array
      j = j + 1 // increment the index of R
  ```

- The time complexity of merge sort is O(n log n) in the worst, average, and best case, where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge step takes O(n) time to combine the two sorted subarrays into one. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm uses two temporary arrays of size n/2 each to store the subarrays during the merge step, and the space used by the recursion stack is O(log n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of elements with equal keys. For example, if the input array is [a1, b1, a2, b2], where a1 and a2 have the same key, and b1 and b2 have the same key, then the output array will be [a1, a2, b1, b2], and not [a2, a1, b1, b2] or [a1, a2, b2, b1].
- Merge