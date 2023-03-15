### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm converts the input array into a max-heap or a min-heap by repeatedly applying a procedure called heapify, which maintains the heap property from the bottom up. This phase takes O(n) time, where n is the number of elements in the array.
- Extracting the elements from the heap: the algorithm repeatedly swaps the root element of the heap with the last element of the heap, reduces the size of the heap by one, and restores the heap property by applying heapify from the top down. This phase takes O(n log n) time, where n is the number of elements in the heap.
- The overall time complexity of heap sort is O(n log n), where n is the number of elements in the input array. The space complexity is O(1), as the algorithm only requires constant extra space to perform the swaps.
- Heap sort is an in-place, unstable, and adaptive sorting algorithm. It is in-place because it does not require extra space to sort the array. It is unstable because it does not preserve the relative order of equal elements. It is adaptive because it performs better on partially sorted arrays than on random arrays.
- Heap sort has several advantages and disadvantages compared to other sorting algorithms. Some of the advantages are:
  - It has a guaranteed worst-case time complexity of O(n log n), which is better than some other comparison-based algorithms such as bubble sort, insertion sort, or selection sort.
  - It does not require extra space to sort the array, which is better than some other algorithms such as merge sort or quick sort with large stack space.
  - It can be easily implemented using an array as the underlying data structure, without requiring pointers or linked lists.
- Some of the disadvantages are:
  - It is not a stable sorting algorithm, which means it may change the relative order of equal elements, which may be undesirable in some applications.
  - It is not a cache-friendly algorithm, which means it may cause many cache misses and reduce the performance on modern hardware.
  - It is not a very efficient algorithm in practice, as it has a large hidden constant factor in the time complexity, and it performs poorly on partially sorted arrays.