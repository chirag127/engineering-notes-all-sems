### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays, sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  - If the array has only one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the two sorted subarrays into a single sorted array.

- The merge operation takes two sorted subarrays and combines them into one sorted array. It can be implemented as follows:

  - Initialize two pointers, i and j, to point to the first elements of the left and right subarrays, respectively.
  - Initialize an empty array, C, to store the merged result.
  - While both i and j are within the bounds of their subarrays, compare the elements at A[i] and B[j], and append the smaller one to C. Increment the pointer of the subarray that provided the smaller element.
  - If one of the subarrays is exhausted, append the remaining elements of the other subarray to C.
  - Return C as the merged array.

- The pseudocode for merge sort is given below:

  ```
  MERGE-SORT(A, p, r)
  // A is the array to be sorted
  // p and r are the indices of the first and last elements of the subarray
  // Precondition: 0 <= p <= r < A.length
  // Postcondition: A[p..r] is sorted in ascending order
  1. if p < r
  2.     q = floor((p + r) / 2) // find the middle point of the subarray
  3.     MERGE-SORT(A, p, q) // recursively sort the left subarray
  4.     MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
  5.     MERGE(A, p, q, r) // merge the two sorted subarrays

  MERGE(A, p, q, r)
  // A is the array containing the two sorted subarrays
  // p, q, and r are the indices of the first, middle, and last elements of the subarray
  // Precondition: A[p..q] and A[q + 1..r] are sorted in ascending order
  // Postcondition: A[p..r] is sorted in ascending order
  1. n1 = q - p + 1 // the length of the left subarray
  2. n2 = r - q // the length of the right subarray
  3. create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
  4. for i = 1 to n1
  5.     L[i] = A[p + i - 1] // copy the left subarray to L
  6. for j = 1 to n2
  7.     R[j] = A[q + j] // copy the right subarray to R
  8. L[n1 + 1] = infinity // a sentinel value to mark the end of the left subarray
  9. R[n2 + 1] = infinity // a sentinel value to mark the end of the right subarray
  10. i = 1 // the pointer for the left subarray
  11. j = 1 // the pointer for the right subarray
  12. for k = p to r
  13.     if L[i] <= R[j] // compare the elements at the pointers
  14.         A[k] = L[i] // copy the smaller element to the merged array
  15.         i = i + 1 // increment the pointer of the left subarray
  16.     else
  17.         A[k] = R[j] // copy the smaller element to the merged array
  18.         j = j + 1 // increment the pointer of the right subarray
  ```

- The time complexity of merge sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and performs a linear merge operation