### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The main idea of merge sort is to divide the problem of sorting an array of n elements into two subproblems of sorting two subarrays of n/2 elements each, and then combine the solutions of the subproblems by merging the two sorted subarrays.
- The algorithm can be described as follows:

  - **Base case:** If the array has zero or one element, it is already sorted and no further action is needed.
  - **Divide:** If the array has more than one element, split it into two subarrays of equal or nearly equal size.
  - **Conquer:** Recursively sort the two subarrays using merge sort.
  - **Combine:** Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and merges them into a single sorted array. It uses an auxiliary array to store the merged elements, and two pointers to keep track of the current position in each subarray. It compares the elements at the current positions of the two subarrays, and copies the smaller one to the auxiliary array, advancing the corresponding pointer. It repeats this process until one of the subarrays is exhausted, and then copies the remaining elements of the other subarray to the auxiliary array. Finally, it copies the auxiliary array back to the original array.
- The pseudocode for the merge operation is as follows:

  ```
  MERGE(A, p, q, r)
  // A is an array, p, q, and r are indices such that p <= q < r
  // A[p..q] and A[q+1..r] are sorted subarrays
  // Merges the two subarrays into a single sorted subarray A[p..r]

  n1 = q - p + 1 // the length of the first subarray
  n2 = r - q // the length of the second subarray
  create arrays L[1..n1+1] and R[1..n2+1] // auxiliary arrays
  for i = 1 to n1
      L[i] = A[p + i - 1] // copy the first subarray to L
  for j = 1 to n2
      R[j] = A[q + j] // copy the second subarray to R
  L[n1 + 1] = infinity // a sentinel value to mark the end of L
  R[n2 + 1] = infinity // a sentinel value to mark the end of R
  i = 1 // the current position in L
  j = 1 // the current position in R
  for k = p to r
      if L[i] <= R[j]
          A[k] = L[i] // copy the smaller element to A
          i = i + 1 // advance the pointer in L
      else
          A[k] = R[j] // copy the smaller element to A
          j = j + 1 // advance the pointer in R
  ```

- The pseudocode for the merge sort algorithm is as follows:

  ```
  MERGE-SORT(A, p, r)
  // A is an array, p and r are indices such that p <= r
  // Sorts the subarray A[p..r] using merge sort

  if p < r // the base case is when p >= r, meaning the subarray has zero or one element
      q = floor((p + r) / 2) // find the middle point of the subarray
      MERGE-SORT(A, p, q) // recursively sort the left subarray
      MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
      MERGE(A, p, q, r) // merge the two sorted subarrays
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to merge the two subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm uses an auxiliary array of size n to store the merged elements at each level of recursion. Therefore, the total space is O(n).
-