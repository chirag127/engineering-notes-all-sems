### Sorting Algorithms-Non-Recursive

Sorting algorithms are methods of arranging a set of data elements in a specific order, such as ascending or descending. Non-recursive sorting algorithms are those that do not use recursion, which is a technique of calling a function within itself to solve smaller subproblems. Non-recursive sorting algorithms typically use loops, such as for or while, to iterate over the data elements and compare and swap them as needed.

Some examples of non-recursive sorting algorithms are:

- **Selection sort**: This algorithm finds the smallest (or largest) element in the unsorted part of the array and swaps it with the first (or last) element of the unsorted part, then repeats the process until the whole array is sorted. The time complexity of this algorithm is O(n^2), where n is the number of elements in the array.

- **Bubble sort**: This algorithm compares adjacent elements in the array and swaps them if they are in the wrong order, then repeats the process until no more swaps are needed. The time complexity of this algorithm is O(n^2) in the worst case, but can be improved to O(n) in the best case if the array is already sorted.

- **Insertion sort**: This algorithm iterates over the array and inserts each element into its correct position in the sorted part of the array, shifting the larger elements to the right as needed. The time complexity of this algorithm is O(n^2) in the worst case, but can be improved to O(n) in the best case if the array is already sorted or nearly sorted.

- **Merge sort**: This algorithm divides the array into two halves, sorts each half recursively, and then merges the two sorted halves into one sorted array. The time complexity of this algorithm is O(n log n), where n is the number of elements in the array. This algorithm can be implemented non-recursively by using a stack or a queue to store the subarrays that need to be merged.

- **Quick sort**: This algorithm chooses a pivot element in the array, partitions the array into two subarrays such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray, and then sorts each subarray recursively. The time complexity of this algorithm is O(n log n) on average, but can be O(n^2) in the worst case if the pivot is chosen poorly. This algorithm can be implemented non-recursively by using a stack to store the subarrays that need to be sorted.