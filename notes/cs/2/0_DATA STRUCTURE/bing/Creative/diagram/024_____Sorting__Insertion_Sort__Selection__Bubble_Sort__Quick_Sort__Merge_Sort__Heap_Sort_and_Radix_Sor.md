# Sorting Algorithms

Sorting algorithms are methods of reorganizing a large number of items into some specific order such as highest to lowest, or vice-versa, or even in some alphabetical order. These algorithms are important for optimizing the use of other algorithms (such as search and merge algorithms) that require sorted lists to work correctly and efficiently. Sorting algorithms also have applications in cryptography, data compression, and computer graphics.

There are many types of sorting algorithms, each with different time and space complexities, stability, and adaptability. Some of the most common types are:

## Insertion Sort

Insertion sort is a simple and stable sorting algorithm that works by inserting each element of the array into its correct position in a sorted subarray that grows from left to right. The algorithm iterates over the array from the second element to the last element, and compares each element with the elements in the sorted subarray to find its correct position. The algorithm then shifts the elements in the sorted subarray to the right to make space for the new element and inserts it. The algorithm repeats this process until the entire array is sorted.

The time complexity of insertion sort is O(n^2) in the worst and average cases, and O(n) in the best case (when the array is already sorted). The space complexity is O(1) as it only requires a constant amount of extra memory. Insertion sort is stable, meaning that it preserves the relative order of equal elements. It is also adaptive, meaning that it performs better on partially sorted arrays.

## Selection Sort

Selection sort is a simple and unstable sorting algorithm that works by selecting the smallest (or largest) element of the array and swapping it with the first (or last) element of the array. The algorithm then repeats this process on the remaining subarray, excluding the sorted element, until the entire array is sorted. The algorithm iterates over the array from the first element to the second last element, and finds the minimum (or maximum) element in the unsorted subarray. The algorithm then swaps the minimum (or maximum) element with the first (or last) element of the unsorted subarray. The algorithm repeats this process until the entire array is sorted.

The time complexity of selection sort is O(n^2) in all cases, as it always makes n(n-1)/2 comparisons. The space complexity is O(1) as it only requires a constant amount of extra memory. Selection sort is unstable, meaning that it may change the relative order of equal elements. It is also not adaptive, meaning that it performs the same on sorted and unsorted arrays.

## Bubble Sort

Bubble sort is a simple and stable sorting algorithm that works by repeatedly swapping adjacent elements of the array that are out of order. The algorithm iterates over the array from the first element to the last element, and compares each pair of adjacent elements. If the elements are in the wrong order, the algorithm swaps them. The algorithm repeats this process until no swaps are made in an iteration, which means that the array is sorted. The algorithm can be optimized by keeping track of the last swapped position, and only iterating up to that position in the next iteration, as the elements after that position are already sorted.

The time complexity of bubble sort is O(n^2) in the worst and average cases, and O(n) in the best case (when the array is already sorted). The space complexity is O(1) as it only requires a constant amount of extra memory. Bubble sort is stable, meaning that it preserves the relative order of equal elements. It is also adaptive, meaning that it performs better on partially sorted arrays.

## Quick Sort

Quick sort is a fast and unstable sorting algorithm that works by dividing the array into two subarrays based on a pivot element, and recursively sorting the subarrays. The algorithm chooses a pivot element from the array, and partitions the array into two subarrays: one with elements smaller than or equal to the pivot, and one with elements larger than the pivot. The algorithm then recursively sorts the subarrays until the base case of one or zero elements is reached. The algorithm can use different strategies to choose the pivot element, such as the first element, the last element, the median element, or a random element. The choice of the pivot element affects the performance of the algorithm.

The time complexity of quick sort is O(n^2) in the worst case, O(n log n) in the average and