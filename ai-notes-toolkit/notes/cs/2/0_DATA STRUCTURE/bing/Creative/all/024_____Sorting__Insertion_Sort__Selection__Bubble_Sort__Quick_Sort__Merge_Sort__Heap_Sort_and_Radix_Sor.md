# Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort

Sorting is the process of arranging the elements of an array or list in a specific order, such as ascending or descending, based on a comparison operator. Sorting algorithms are the methods of implementing sorting in data structures. Sorting algorithms can be classified into different categories based on their time complexity, space complexity, stability, adaptability, and recursion.

## Insertion Sort

Insertion sort is a simple and stable sorting algorithm that works by inserting each element of the array into its correct position in the sorted part of the array. The algorithm starts from the second element and compares it with the previous elements, shifting them to the right until it finds the correct position to insert the element. The algorithm repeats this process for each element until the array is sorted.

The time complexity of insertion sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Insertion sort is adaptive, meaning it performs better for partially sorted arrays. Insertion sort is not suitable for large arrays as it involves many comparisons and shifts.

## Selection Sort

Selection sort is a simple and unstable sorting algorithm that works by selecting the smallest or largest element of the array and placing it at the beginning or end of the sorted part of the array. The algorithm repeats this process for each element until the array is sorted.

The time complexity of selection sort is O(n^2) in all cases, as it involves n-1 comparisons for each of the n elements. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Selection sort is not adaptive, meaning it performs the same for any order of the array. Selection sort is not suitable for large arrays as it involves many comparisons.

## Bubble Sort

Bubble sort is a simple and stable sorting algorithm that works by swapping the adjacent elements of the array if they are in the wrong order. The algorithm repeats this process for each element until no swaps are required, indicating that the array is sorted.

The time complexity of bubble sort is O(n^2) in the worst and average case, and O(n) in the best case when the array is already sorted. The space complexity is O(1) as it only requires a constant amount of auxiliary space. Bubble sort is adaptive, meaning it performs better for partially sorted arrays. Bubble sort is not suitable for large arrays as it involves many comparisons and swaps.

## Quick Sort

Quick sort is a fast and unstable sorting algorithm that works by dividing the array into two subarrays based on a pivot element, such that all the elements in the left subarray are smaller than the pivot and all the elements in the right subarray are larger than the pivot. The algorithm then recursively sorts the subarrays until the array is sorted.

The time complexity of quick sort is O(n log n) in the average and best case, and O(n^2) in the worst case when the array is already sorted or contains many duplicate elements. The space complexity is O(log n) in the average and best case, and O(n) in the worst case due to the recursive calls. Quick sort is not adaptive, meaning it performs the same for any order of the array. Quick sort is suitable for large arrays as it involves fewer comparisons and swaps than other algorithms.

## Merge Sort

Merge sort is a fast and stable sorting algorithm that works by dividing the array into two equal or nearly equal subarrays, sorting them recursively, and then merging them back into a single sorted array. The algorithm uses a merge function that takes two sorted subarrays and merges them into one sorted array.

The time complexity of merge sort is O(n log n) in all cases, as it involves log n divisions and n comparisons for each division. The space complexity is O(n) as it requires an auxiliary array of the same size as the original array. Merge sort is not adaptive, meaning it performs the same for any order of the array. Merge sort is suitable for large arrays as it involves fewer comparisons than other algorithms.

## Heap Sort

Heap sort is a fast and unstable sorting algorithm that works by building a binary heap from the array, and then repeatedly extracting the maximum or minimum element from the heap and placing it at the end or beginning of the sorted part of the array. The algorithm maintains the heap property after each extraction by adjusting the heap.

The time complexity of heap sort is O(n log n) in all cases, as it involves n extractions and log n