### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  1. If the array has only one element, return it as the sorted array.
  2. Otherwise, divide the array into two subarrays of equal or nearly equal size.
  3. Recursively sort the left and right subarrays using merge sort.
  4. Merge the sorted left and right subarrays into a single sorted array.

- The merge operation takes two sorted arrays and combines them into one sorted array. It can be implemented as follows:

  1. Initialize an empty array to store the merged result.
  2. Initialize two pointers, one for each input array, to track the current element to be compared.
  3. While both input arrays have elements remaining, compare the elements pointed by the pointers and append the smaller one to the result array. Increment the pointer of the array that provided the smaller element.
  4. If one input array is exhausted, append the remaining elements of the other input array to the result array.
  5. Return the result array as the merged array.

- The pseudocode for merge sort is:

  ```
  MERGE-SORT(A, p, r)
    // A is the input array, p and r are the indices of the first and last elements
    if p < r
      q = floor((p + r) / 2) // find the middle point
      MERGE-SORT(A, p, q) // recursively sort the left subarray
      MERGE-SORT(A, q + 1, r) // recursively sort the right subarray
      MERGE(A, p, q, r) // merge the sorted subarrays
  ```

  ```
  MERGE(A, p, q, r)
    // A is the input array, p, q, and r are the indices of the first, middle, and last elements of the subarray to be merged
    n1 = q - p + 1 // the length of the left subarray
    n2 = r - q // the length of the right subarray
    create arrays L[1..n1 + 1] and R[1..n2 + 1] // temporary arrays to store the subarrays
    for i = 1 to n1
      L[i] = A[p + i - 1] // copy the left subarray to L
    for j = 1 to n2
      R[j] = A[q + j] // copy the right subarray to R
    L[n1 + 1] = infinity // sentinel value to mark the end of L
    R[n2 + 1] = infinity // sentinel value to mark the end of R
    i = 1 // pointer for L
    j = 1 // pointer for R
    for k = p to r
      if L[i] <= R[j]
        A[k] = L[i] // copy the smaller element from L to A
        i = i + 1 // increment the pointer for L
      else
        A[k] = R[j] // copy the smaller element from R to A
        j = j + 1 // increment the pointer for R
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to combine the subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm creates temporary arrays of size n/2 at each level of recursion, and there are log n levels of recursion. Therefore, the total space is O(n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array. This is because the merge operation always chooses the element from the left subarray when there is a tie, and the left subarray contains the elements that appeared earlier in the input array.
- Merge sort is not an in-place sorting algorithm, meaning that it uses extra space to store the temporary arrays. This can be a disadvantage when the input array is large and the available memory is limited.