# Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator. Sorting algorithms are the methods of implementing sorting in data structures. Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, and recursion.

## Insertion Sort

Insertion sort is a simple and stable sorting algorithm that works by inserting each element of the array into its correct position in the sorted part of the array. The algorithm starts from the second element and compares it with the previous elements, shifting them to the right until it finds the correct position to insert the current element. The algorithm repeats this process for each element until the array is sorted. The time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity of insertion sort is O(1) as it only requires a constant amount of extra space.

## Selection Sort

Selection sort is a simple and unstable sorting algorithm that works by selecting the smallest or largest element of the array and swapping it with the first or last element of the unsorted part of the array. The algorithm repeats this process for each element until the array is sorted. The time complexity of selection sort is O(n^2) in all cases, as it always performs n-1 comparisons for each of the n elements. The space complexity of selection sort is O(1) as it only requires a constant amount of extra space.

## Bubble Sort

Bubble sort is a simple and stable sorting algorithm that works by repeatedly swapping the adjacent elements of the array if they are in the wrong order. The algorithm passes through the array n-1 times, where n is the number of elements, and each pass reduces the size of the unsorted part of the array by one. The algorithm stops when no swaps are performed in a pass, indicating that the array is sorted. The time complexity of bubble sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity of bubble sort is O(1) as it only requires a constant amount of extra space.

## Quick Sort

Quick sort is a fast and unstable sorting algorithm that works by using the divide and conquer technique. The algorithm chooses a pivot element from the array and partitions the array into two subarrays, such that all the elements less than the pivot are in the left subarray and all the elements greater than or equal to the pivot are in the right subarray. The algorithm then recursively sorts the left and right subarrays until the array is sorted. The time complexity of quick sort is O(n log n) in the best and average case, and O(n^2) in the worst case when the array is already sorted or contains many duplicate elements. The space complexity of quick sort is O(log n) in the best and average case, and O(n) in the worst case, as it requires extra space for the recursive calls.

## Merge Sort

Merge sort is a fast and stable sorting algorithm that works by using the divide and conquer technique. The algorithm splits the array into two equal halves and recursively sorts each half until the array is sorted. The algorithm then merges the two sorted halves into one sorted array by comparing the elements of each half and placing the smaller one into the final array. The time complexity of merge sort is O(n log n) in all cases, as it always performs log n splits and n comparisons for each split. The space complexity of merge sort is O(n) as it requires extra space for the temporary array used for merging.

## Heap Sort

Heap sort is a fast and unstable sorting algorithm that works by using a data structure called a heap. A heap is a binary tree that satisfies the heap property, which states that the value of each node is greater than or equal to the value of its children. The algorithm builds a max-heap from the array, which places the largest element at the root of the heap. The algorithm then swaps the root element with the last element of the heap and reduces the size of the heap by one. The algorithm then restores the heap property by sifting down the new root element until it reaches its correct position. The algorithm repeats this process until the heap is empty and the array is sorted. The time complexity of heap sort is O(n log n) in all cases, as it takes O(n) time to build the heap and O