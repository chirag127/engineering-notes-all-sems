## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: heap construction and heap extraction.
- Heap construction: the given array is transformed into a binary heap by repeatedly applying a bottom-up procedure called heapify. Heapify ensures that the subtree rooted at a given index satisfies the heap property by swapping the node with its largest (or smallest) child if necessary and recursing on the affected subtree.
- Heap extraction: the root of the heap, which contains the maximum (or minimum) element of the array, is removed and replaced by the last element of the heap. The heap size is reduced by one and heapify is applied to the new root. This process is repeated until the heap is empty and the array is sorted in ascending (or descending) order.
- The pseudocode for heap sort is as follows:

```
heap_sort(array):
  n = length(array)
  # build a max-heap from the array
  for i from n/2 down to 1:
    heapify(array, i, n)
  # extract the elements from the heap one by one
  for i from n down to 2:
    # swap the root with the last element
    swap(array[1], array[i])
    # reduce the heap size by one
    n = n - 1
    # restore the heap property at the root
    heapify(array, 1, n)

heapify(array, i, n):
  # assume that the subtrees rooted at the left and right children of i are heaps
  left = 2 * i
  right = 2 * i + 1
  # find the largest element among the node i and its children
  largest = i
  if left <= n and array[left] > array[largest]:
    largest = left
  if right <= n and array[right] > array[largest]:
    largest = right
  # if the node i is not the largest, swap it with the largest child and recurse on the affected subtree
  if largest != i:
    swap(array[i], array[largest])
    heapify(array, largest, n)
```
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. This is because heap construction takes O(n) time and heap extraction takes O(log n) time for each element.
- The space complexity of heap sort is O(1) in the worst, average, and best cases, as it only requires a constant amount of auxiliary space to perform the swaps.
- Heap sort is an in-place, unstable, and non-recursive sorting algorithm. It is suitable for sorting large data sets that can fit in memory, but it is not very efficient for sorting small or nearly sorted data sets. It also does not preserve the relative order of equal elements, which may be important for some applications.