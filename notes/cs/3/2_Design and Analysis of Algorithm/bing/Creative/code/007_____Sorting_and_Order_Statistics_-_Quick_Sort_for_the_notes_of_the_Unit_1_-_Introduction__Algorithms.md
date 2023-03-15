### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The algorithm has an average-case time complexity of **O(n log n)**, where n is the number of elements in the array, and a worst-case time complexity of **O(n^2)**, which occurs when the pivot is always the smallest or the largest element in the array.
- The algorithm has a space complexity of **O(log n)**, which is the depth of the recursion tree.
- The algorithm is **in-place**, meaning it does not require additional memory to sort the array, and **unstable**, meaning it does not preserve the relative order of equal elements.
- The algorithm can be implemented using the following pseudocode:

```
QUICK-SORT(A, p, r)
  // A is the array to be sorted
  // p and r are the indices of the first and last elements of the subarray
  if p < r
    q = PARTITION(A, p, r) // q is the index of the pivot element
    QUICK-SORT(A, p, q - 1) // sort the left subarray
    QUICK-SORT(A, q + 1, r) // sort the right subarray

PARTITION(A, p, r)
  x = A[r] // choose the last element as the pivot
  i = p - 1 // i is the index of the last element in the left subarray
  for j = p to r - 1 // loop through the subarray
    if A[j] <= x // if the current element is less than or equal to the pivot
      i = i + 1 // increment i
      exchange A[i] with A[j] // swap the current element with the element at i
  exchange A[i + 1] with A[r] // place the pivot in its correct position
  return i + 1 // return the index of the pivot
```