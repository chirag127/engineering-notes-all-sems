### Sorting and Order Statistics - Heap Sort

Heap sort is a comparison-based sorting algorithm that uses a data structure called a binary heap. It works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving it to the sorted region. The improvement consists of the use of a heap data structure rather than a linear-time search to find the maximum.

Here are the steps for performing a heap sort:

1. Build a max heap from the input data.
2. The largest item is stored at the root of the heap. Replace it with the last item of the heap followed by reducing the size of the heap by 1. Heapify the root of the tree.
3. Repeat step 2 while the size of the heap is greater than 1.

The time complexity of heap sort is O(n log n) for the best, average, and worst-case scenarios. This makes it an efficient sorting algorithm for large data sets. However, it is not a stable sort, meaning that the relative order of equal elements is not preserved.

Heap sort is part of the Unit 1 - Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time, in the subject of Design and Analysis of Algorithm. It is an important topic to understand for exams.