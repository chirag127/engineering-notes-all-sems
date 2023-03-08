### Sorting and Order Statistics - Heap Sort

Heap Sort is a comparison-based sorting algorithm that falls under the category of sorting algorithms that works on the principle of Binary Heap. It is an in-place algorithm that has a time complexity of O(n log n) and a space complexity of O(1).

**Working of Heap Sort:**

- Build a max heap from the input data.
- The maximum element of the heap is stored at the root.
- Replace the root with the last element of the heap.
- Heapify the remaining heap of size n-1.
- Repeat steps 2-4 until the heap is of size 1.

**Advantages of Heap Sort:**

- Heap Sort is an efficient sorting algorithm that has a time complexity of O(n log n).
- It is an in-place sorting algorithm, i.e., it does not require any extra space for sorting.
- Heap Sort is a stable sorting algorithm, i.e., it does not change the relative order of equal elements in the input array.

**Disadvantages of Heap Sort:**

- Heap Sort has a large constant factor in its time complexity, which makes it slower than other sorting algorithms for small input sizes.
- Heap Sort is not adaptive, i.e., it does not take into account the sortedness of the input array and always performs n log n comparisons.

**Example:**

Consider the following input array: [12, 11, 13, 5, 6, 7]

- Build a max heap from the input data: [13, 11, 12, 5, 6, 7]
- The maximum element of the heap is stored at the root (13).
- Replace the root with the last element of the heap (7).
- Heapify the remaining heap of size n-1: [12, 11, 7, 5, 6]
- Repeat steps 2-4 until the heap is of size 1: [11, 6, 7, 5, 12, 13]

The sorted array is [5, 6, 7, 11, 12, 13].

**Applications of Heap Sort:**

- Heap Sort is widely used in operating systems for memory management.
- It is used in priority queues for sorting elements based on their priority.
- Heap Sort is used in network routing algorithms for finding the shortest path between two nodes.