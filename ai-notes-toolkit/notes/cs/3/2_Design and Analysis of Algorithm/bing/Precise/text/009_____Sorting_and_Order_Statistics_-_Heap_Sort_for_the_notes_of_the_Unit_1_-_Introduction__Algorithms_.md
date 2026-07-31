### Sorting and Order Statistics - Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a data structure called a binary heap. It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region.

The steps for performing heap sort are as follows:

1. Build a max heap from the input data.
2. The largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of the heap by 1. Heapify the root of the tree.
3. Repeat step 2 while the size of the heap is greater than 1.

The time complexity of heap sort is O(n log n) for the best, average, and worst-case scenarios. This makes it an efficient sorting algorithm for large data sets.

Heap sort has several advantages over other sorting algorithms. It has a good time complexity and is an in-place sorting algorithm, meaning it does not require additional memory to perform the sorting. However, it is not a stable sorting algorithm, meaning that the relative order of equal elements may not be preserved.

In summary, heap sort is an efficient comparison-based sorting algorithm that uses a binary heap data structure. It has a good time complexity of O(n log n) and is an in-place sorting algorithm, but it is not a stable sorting algorithm. It is a good choice for sorting large data sets.