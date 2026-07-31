## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- Heap sort works by first building a max-heap or a min-heap from the input array, then repeatedly extracting the root element (which is the maximum or minimum element) and placing it at the end of the sorted array, and then restoring the heap property by adjusting the remaining heap.
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. The space complexity of heap sort is O(1), as it only requires a constant amount of auxiliary space.
- The following is a pseudocode for heap sort using a max-heap:

```
heap_sort(array):
  n = length(array)
  # Build a max-heap from the array
  for i from n/2 down to 1:
    heapify(array, i, n)
  # Extract the root element and place it at the end of the sorted array
  for i from n down to 2:
    swap(array[1], array[i])
    n = n - 1
    # Restore the heap property by adjusting the remaining heap
    heapify(array, 1, n)
  return array

heapify(array, i, n):
  # Assume that the node at index i is the root of a subtree
  # and its left and right children are at index 2i and 2i+1
  largest = i
  left = 2i
  right = 2i + 1
  # Compare the root with its left and right children and find the largest element
  if left <= n and array[left] > array[largest]:
    largest = left
  if right <= n and array[right] > array[largest]:
    largest = right
  # If the root is not the largest element, swap it with the largest child and recursively heapify the affected subtree
  if largest != i:
    swap(array[i], array[largest])
    heapify(array, largest, n)
```