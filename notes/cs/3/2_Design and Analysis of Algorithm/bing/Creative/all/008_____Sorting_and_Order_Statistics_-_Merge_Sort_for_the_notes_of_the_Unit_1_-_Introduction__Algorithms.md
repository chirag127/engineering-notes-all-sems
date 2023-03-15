# Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a sorted array.
- The algorithm can be described as follows:

  - If the array has zero or one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted subarrays into a single sorted array.

- The merge operation takes two sorted arrays and combines them into one sorted array. It can be implemented as follows:

  - Initialize two pointers, i and j, to point to the first elements of the left and right subarrays, respectively.
  - Initialize an empty array, result, to store the merged array.
  - While both i and j are within the bounds of their respective subarrays, compare the elements at A[i] and A[j].
  - If A[i] <= A[j], append A[i] to result and increment i. Otherwise, append A[j] to result and increment j.
  - If either i or j reaches the end of its subarray, append the remaining elements of the other subarray to result.
  - Return result as the merged array.

- The pseudocode for merge sort is as follows:

  ```
  MERGE-SORT(A, p, r)
    if p < r
      q = floor((p + r) / 2)
      MERGE-SORT(A, p, q)
      MERGE-SORT(A, q + 1, r)
      MERGE(A, p, q, r)

  MERGE(A, p, q, r)
    n1 = q - p + 1
    n2 = r - q
    create arrays L[1..n1 + 1] and R[1..n2 + 1]
    for i = 1 to n1
      L[i] = A[p + i - 1]
    for j = 1 to n2
      R[j] = A[q + j]
    L[n1 + 1] = infinity
    R[n2 + 1] = infinity
    i = 1
    j = 1
    for k = p to r
      if L[i] <= R[j]
        A[k] = L[i]
        i = i + 1
      else
        A[k] = R[j]
        j = j + 1
  ```

- The time complexity of merge sort is O(n log n), where n is the number of elements in the array. This is because the algorithm divides the array into two subarrays of size n/2 at each level of recursion, and there are log n levels of recursion. At each level, the merge operation takes O(n) time to combine the subarrays. Therefore, the total time is O(n log n).
- The space complexity of merge sort is O(n), where n is the number of elements in the array. This is because the algorithm creates auxiliary arrays of size n/2 at each level of recursion, and there are log n levels of recursion. Therefore, the total space is O(n).
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array. This is because the merge operation always chooses the element from the left subarray over the element from the right subarray when they are equal, thus maintaining their original order.
- Merge sort is not an in-place sorting algorithm, meaning that it requires extra space to store the auxiliary arrays. This can be a disadvantage when the array is large and memory is limited. However, there are variants of merge sort that can reduce the space complexity to O(1) by using clever techniques such as bitonic sorting or in-place merging.