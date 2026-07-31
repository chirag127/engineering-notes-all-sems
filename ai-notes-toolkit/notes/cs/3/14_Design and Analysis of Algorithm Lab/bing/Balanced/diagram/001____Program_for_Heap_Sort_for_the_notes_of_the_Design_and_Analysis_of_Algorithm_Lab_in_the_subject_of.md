## Program for Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a list of elements. It works by dividing the list into two regions: a sorted region and an unsorted region. It iteratively extracts the largest element from the unsorted region and inserts it into the sorted region, until the list is fully sorted. Heap sort is an in-place algorithm, meaning it does not require extra space to store the sorted elements. However, it is not a stable algorithm, meaning it does not preserve the relative order of equal elements.

The heap sort algorithm can be divided into two steps:

1. Build a max heap from the input list. A max heap is a complete binary tree where each node is greater than or equal to its children. The root node is the largest element in the heap. The max heap can be built using a bottom-up approach, starting from the last non-leaf node and sifting it down until it satisfies the heap property. This can be done in O(n) time, where n is the number of elements in the list.
2. Repeatedly swap the root node with the last node in the heap, and reduce the heap size by one. This moves the largest element to the end of the list, and creates a new root node that may violate the heap property. To restore the heap property, sift down the new root node until it is in the correct position. This can be done in O(log n) time, where n is the current heap size. Repeat this step until the heap size is one, which means the list is fully sorted. This can be done in O(n log n) time, where n is the number of elements in the list.

The total time complexity of heap sort is O(n log n), where n is the number of elements in the list. The space complexity is O(1), as no extra space is required.

Here is a pseudocode for heap sort:

```
heap_sort(list):
  n = length(list)
  build_max_heap(list, n) // build a max heap from the list
  for i from n-1 to 1: // iterate from the last node to the second node
    swap(list[0], list[i]) // swap the root node with the last node
    n = n - 1 // reduce the heap size by one
    max_heapify(list, 0, n) // restore the heap property of the new root node

build_max_heap(list, n):
  for i from floor(n/2) - 1 to 0: // iterate from the last non-leaf node to the root node
    max_heapify(list, i, n) // sift down the node until it satisfies the heap property

max_heapify(list, i, n):
  largest = i // assume the current node is the largest
  left = 2*i + 1 // get the index of the left child
  right = 2*i + 2 // get the index of the right child
  if left < n and list[left] > list[largest]: // if the left child is larger than the current node
    largest = left // update the largest index
  if right < n and list[right] > list[largest]: // if the right child is larger than the current node
    largest = right // update the largest index
  if largest != i: // if the current node is not the largest
    swap(list[i], list[largest]) // swap the current node with the largest child
    max_heapify(list, largest, n) // recursively sift down the swapped child node
```

Here is an example of heap sort on the list [4, 10, 3, 5, 1]:

![Heap sort example](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

Source: [Heapsort - Wikipedia](https://en.wikipedia.org/wiki/Heapsort)