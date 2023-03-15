Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of sorting and order statistics - merge sort.

### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that recursively divides an array into two subarrays, sorts them, and then merges them into a single sorted array.
- The algorithm works as follows:

  1. If the array has only one element, it is already sorted and the algorithm returns it.
  2. Otherwise, the array is divided into two subarrays of equal or nearly equal size.
  3. The algorithm recursively sorts the two subarrays using merge sort.
  4. The algorithm merges the two sorted subarrays into a single sorted array by repeatedly comparing the smallest elements of each subarray and moving the smaller one to the output array.
  5. The algorithm returns the sorted array.

- The pseudocode for merge sort is:

  ```
  MERGE-SORT(A, p, r)
    if p < r
      q = floor((p + r) / 2)
      MERGE-SORT(A, p, q)
      MERGE-SORT(A, q + 1, r)
      MERGE(A, p, q, r)
  ```

  ```
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

- The time complexity of merge sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array.
- The space complexity of merge sort is O(n), as it requires an auxiliary array of the same size as the input array.
- Merge sort is stable, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is not adaptive, meaning that it does not take advantage of any existing order in the input array.