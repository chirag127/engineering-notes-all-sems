### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The base case of the recursion is when the subarray has one or zero elements, which are trivially sorted.
- The average-case time complexity of quick sort is **O(n log n)**, where n is the number of elements in the array.
- The worst-case time complexity of quick sort is **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the subarray, resulting in unbalanced partitions.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion tree.
- Quick sort is an **in-place** sorting algorithm, meaning it does not require additional memory to store the sorted array.
- Quick sort is also an **unstable** sorting algorithm, meaning it does not preserve the relative order of equal elements in the array.

#### Pseudocode of quick sort

```
QUICK-SORT(A, p, r)
// A is the array to be sorted
// p and r are the indices of the first and last elements of the subarray
// initially, p = 0 and r = n - 1, where n is the size of the array
if p < r
    q = PARTITION(A, p, r) // q is the index of the pivot element after partitioning
    QUICK-SORT(A, p, q - 1) // recursively sort the left subarray
    QUICK-SORT(A, q + 1, r) // recursively sort the right subarray

PARTITION(A, p, r)
x = A[r] // choose the last element as the pivot
i = p - 1 // i is the index of the last element in the left subarray
for j = p to r - 1 // loop through the subarray, excluding the pivot
    if A[j] <= x // if the current element is less than or equal to the pivot
        i = i + 1 // increment i
        exchange A[i] with A[j] // swap the current element with the element at i
exchange A[i + 1] with A[r] // place the pivot element in its correct position
return i + 1 // return the index of the pivot element
```