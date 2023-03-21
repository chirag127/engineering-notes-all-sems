### Sorting Algorithms-Recursive

Sorting is one of the most fundamental operations in computer science. It is the process of arranging elements in a particular order, usually in ascending or descending order. Recursive sorting algorithms are algorithms that use a recursive approach to sort elements. In this lab, we will discuss some of the popular recursive sorting algorithms.

#### Merge Sort

Merge sort is a divide-and-conquer algorithm that recursively divides the input array into halves, sorts the two halves, and then merges the two sorted halves. The algorithm works as follows:

1. Divide the input array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves.

The time complexity of merge sort is O(nlogn) in the worst case.

#### Quick Sort

Quick sort is another divide-and-conquer algorithm that recursively partitions the input array into sub-arrays based on a pivot element, and then recursively sorts the sub-arrays. The algorithm works as follows:

1. Choose a pivot element from the input array.
2. Partition the input array into two sub-arrays, one with elements smaller than the pivot and one with elements larger than the pivot.
3. Recursively sort the sub-array with elements smaller than the pivot.
4. Recursively sort the sub-array with elements larger than the pivot.

The time complexity of quick sort is O(nlogn) in the average case and O(n^2) in the worst case.

#### Heap Sort

Heap sort is an in-place sorting algorithm that uses a binary heap data structure to sort elements. The algorithm works as follows:

1. Build a binary heap from the input array.
2. Extract the maximum element from the binary heap and move it to the end of the array.
3. Repeat step 2 for the remaining elements in the binary heap.

The time complexity of heap sort is O(nlogn) in the worst case.

#### Conclusion

Recursive sorting algorithms are efficient algorithms that can sort large datasets in a relatively short amount of time. Merge sort, quick sort, and heap sort are some of the popular recursive sorting algorithms that are widely used in computer science. It is important to choose the right sorting algorithm based on the input data and the desired time complexity.