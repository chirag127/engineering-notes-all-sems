## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted array, until the heap is empty.
- The algorithm can be divided into two phases: heapify and extract.
- Heapify is the process of converting an array into a heap by adjusting the positions of the elements such that the heap property is maintained.
- Extract is the process of removing the root element from the heap and placing it at the end of the sorted array, and then restoring the heap property by swapping the last element of the heap with the new root and sifting it down the heap.
- The time complexity of heap sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array.
- The space complexity of heap sort is O(1) in the worst, average, and best cases, as it only requires a constant amount of auxiliary space to perform the swaps.
- Heap sort is an in-place and unstable sorting algorithm, which means that it does not require extra space to store the sorted array, and it does not preserve the relative order of equal elements.
- Heap sort is suitable for sorting large data sets, as it can handle them efficiently and does not depend on the initial order of the elements.
- Heap sort is not suitable for sorting small data sets, as it has a high overhead of building and maintaining the heap structure, and it does not take advantage of the existing order of the elements.

Here is a pseudocode for heap sort:

```
procedure heap_sort(array A)
  n = length(A)
  // build a max-heap from the array
  for i = n/2 downto 1
    heapify(A, i, n)
  end for
  // extract the root element and place it at the end of the sorted array
  for i = n downto 2
    swap(A[1], A[i]) // move the maximum element to the end
    n = n - 1 // reduce the size of the heap by one
    heapify(A, 1, n) // restore the heap property
  end for
end procedure

procedure heapify(array A, index i, size n)
  // assume that the subtrees rooted at i's left and right children are heaps
  // adjust the position of A[i] such that the subtree rooted at i is a heap
  largest = i // initialize the largest element as the root
  left = 2 * i // get the index of the left child
  right = 2 * i + 1 // get the index of the right child
  // compare the root with its left child
  if left <= n and A[left] > A[largest]
    largest = left
  end if
  // compare the root with its right child
  if right <= n and A[right] > A[largest]
    largest = right
  end if
  // if the root is not the largest element, swap it with the largest child and recurse
  if largest != i
    swap(A[i], A[largest])
    heapify(A, largest, n)
  end if
end procedure
```