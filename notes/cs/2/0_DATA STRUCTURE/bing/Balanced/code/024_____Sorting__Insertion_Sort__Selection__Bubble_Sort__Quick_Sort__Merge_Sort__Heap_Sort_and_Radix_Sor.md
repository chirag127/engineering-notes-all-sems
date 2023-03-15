# Sorting Algorithms

Sorting algorithms are methods of reorganizing a large number of items into some specific order such as highest to lowest, or vice-versa, or even in some alphabetical order. These algorithms are important for optimizing the use of other algorithms (such as search and merge algorithms) that require sorted lists to work correctly and efficiently. Sorting algorithms are also often used for canonicalizing data and for producing human-readable output.

There are many types of sorting algorithms, each with different time and space complexities, stability, and adaptability. Some of the most common sorting algorithms are:

- **Insertion sort**: This algorithm works by inserting each element of the array into its correct position in a sorted subarray that grows from left to right. It is simple, stable, and adaptive, but has a worst-case time complexity of O(n^2^), where n is the number of elements in the array .
- **Selection sort**: This algorithm works by finding the smallest (or largest) element of the array and swapping it with the first (or last) element, then repeating the process for the remaining subarray. It is simple and in-place, but has a worst-case time complexity of O(n^2^), and is unstable and not adaptive .
- **Bubble sort**: This algorithm works by repeatedly swapping adjacent elements of the array that are out of order, until no more swaps are needed. It is simple, stable, and adaptive, but has a worst-case time complexity of O(n^2^), and is inefficient for large arrays .
- **Quick sort**: This algorithm works by choosing a pivot element from the array and partitioning the array into two subarrays, such that all elements less than the pivot are in the left subarray and all elements greater than or equal to the pivot are in the right subarray, then recursively sorting the subarrays. It is fast, in-place, and has an average time complexity of O(n log n), where n is the number of elements in the array, but has a worst-case time complexity of O(n^2^), and is unstable and not adaptive .
- **Merge sort**: This algorithm works by dividing the array into two equal halves, recursively sorting each half, and then merging the two sorted halves into one sorted array. It is stable, and has a worst-case time complexity of O(n log n), but requires extra space for merging and is not adaptive .
- **Heap sort**: This algorithm works by building a heap (a binary tree where each node is greater than or equal to its children) from the array, then repeatedly removing the root (the largest element) of the heap and placing it at the end of the array, and restoring the heap property. It is fast, in-place, and has a worst-case time complexity of O(n log n), but is unstable and not adaptive .
- **Radix sort**: This algorithm works by sorting the array based on the individual digits or characters of each element, starting from the least significant digit or character and moving to the most significant one. It is stable, and has a worst-case time complexity of O(d(n+k)), where d is the number of digits or characters, n is the number of elements in the array, and k is the range of values of each digit or character, but requires extra space and is not adaptive .

# References

: https://www.geeksforgeeks.org/sorting-algorithms/
: https://www.upgrad.com/blog/sorting-in-data-structure-with-examples/
: https://cselectricalandelectronics.com/sorting-in-data-structure-and-algorithms-code-working-types-of-sorting/
: https://www.programiz.com/dsa/sorting-algorithm