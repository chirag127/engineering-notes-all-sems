 Here is the content in Markdown format without any emojis or external links and in a formal tone:

## Program for Heap Sort

- Heap sort is a comparison-based sorting algorithm.
- It follows the heap data structure to sort the elements.
- A heap is a complete binary tree with the property that the value of each node is greater than or equal to the value of its children.
- The steps involved in heap sort are:

1. Build a max heap - Rearrange the array elements so that the maximum element is at the root. This is done by swapping elements and recursively heapifying from the bottom up.
2. Swap the first element (maximum) with the last element - The maximum element is at the first index, swap it with the last element.
3. Sink down the new first element - The new first element is out of order. Sink it down to the correct position by comparing it with its children and swapping.
4. Repeat steps 2 and 3 - Keep extracting the maximum element and sinking down the new root until the heap size reduces to 1.

- The time complexity of heap sort is O(n log n) as we do O(log n) heapify operations for n elements.
- Heap sort is an in-place sorting algorithm with O(1) extra space.
- It is not a stable sort.

The above points cover the key aspects of heap sort with a formal tone and without any emojis or external links as requested. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.