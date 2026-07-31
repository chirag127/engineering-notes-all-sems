
## Program for Merge Sort 

Merge sort is an efficient, general-purpose sorting algorithm. It is a comparison-based algorithm that divides an array into two subarrays and then merges them in a sorted order. The algorithm has a time complexity of O (n log n).

This algorithm is used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.

1. Divide the unsorted array into n subarrays, each containing one element.
2. Repeatedly merge subarrays to produce new sorted subarrays until there is only one subarray remaining.
3. The remaining subarray is the sorted array.

The following is a pseudocode for the Merge Sort algorithm:

```
MergeSort(A, p, r)
  if p < r
    q = (p + r)/2
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)

Merge(A, p, q, r)
  n1 = q - p + 1
  n2 = r - q
  let L[1..n1 + 1] and R[1..n2 + 1] be new arrays
  for i = 1 to n1
    L[i] = A[p + i - 1]
  for j = 1 to n2
    R[j] = A[q + j]
  L[n1 + 1] = ∞
  R[n2 + 1] = ∞
  i = 1
  j = 1
  for k = p to r
    if L[i] ≤ R[j]
      A[k] = L[i]
      i = i + 1
    else A[k] = R[j]
      j = j + 1
```