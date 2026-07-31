### Sorting and Order Statistics - Heap Sort

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property: the value of each node is greater than or equal to the values of its children (max-heap) or less than or equal to the values of its children (min-heap).
- Heap sort consists of two phases: building the heap and extracting the elements from the heap.
- Building the heap: the algorithm rearranges the elements of the array into a max-heap or a min-heap, depending on the desired sorting order. This can be done in linear time using a bottom-up approach that starts from the last non-leaf node and moves up to the root, applying a procedure called heapify to each node. Heapify ensures that the subtree rooted at a given node satisfies the heap property by swapping the node with its largest or smallest child, if necessary, and recursing on the affected subtree.
- Extracting the elements from the heap: the algorithm repeatedly removes the root element of the heap, which is the largest or smallest element in the array, and places it at the end of the sorted output. Then, it restores the heap property by applying heapify to the new root node. This process is repeated until the heap is empty, resulting in a sorted array. This phase takes O(n log n) time, where n is the number of elements in the array, since each extraction and heapify operation takes O(log n) time and there are n such operations.
- Heap sort has the following advantages and disadvantages:
  - Advantages:
    - It is an in-place sorting algorithm, meaning it does not require extra space to store the sorted output.
    - It has a guaranteed worst-case running time of O(n log n), which is better than some other comparison-based sorting algorithms, such as bubble sort or insertion sort, that have quadratic worst-case running times.
    - It can be easily parallelized or adapted to handle external sorting, where the data does not fit in the main memory and has to be stored on disks or tapes.
  - Disadvantages:
    - It is not a stable sorting algorithm, meaning it does not preserve the relative order of equal elements in the input array.
    - It is not adaptive, meaning it does not take advantage of the existing order or partial order in the input array, and performs the same number of comparisons regardless of the input distribution.
    - It has a relatively large hidden constant factor in its running time, meaning it is often slower than some other comparison-based sorting algorithms, such as quick sort or merge sort, on average or in practice.