### Sorting and Order Statistics - Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The steps involved in Quick Sort are:
1. Choose a pivot element from the array.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Recursively apply the above steps to the sub-arrays until the base case is reached (sub-array is empty or contains only one element).

The worst-case time complexity of Quick Sort is O(n^2), where n is the number of elements in the array. However, the average-case time complexity is O(n log n). The space complexity of Quick Sort is O(log n).

Quick Sort is an in-place sorting algorithm, meaning it does not require additional storage space to sort the array. It is also an unstable sorting algorithm, meaning the relative order of equal elements may not be preserved.

Quick Sort is widely used due to its efficiency and ease of implementation. It is commonly used in computer science, data processing, and numerical analysis. However, it may not be the best choice for small data sets or data sets that are already partially sorted. In these cases, other sorting algorithms such as Insertion Sort or Shell Sort may be more efficient.