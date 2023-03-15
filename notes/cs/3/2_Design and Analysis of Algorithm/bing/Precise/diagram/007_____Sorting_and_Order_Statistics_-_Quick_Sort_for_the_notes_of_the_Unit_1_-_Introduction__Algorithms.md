### Sorting and Order Statistics - Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The steps involved in Quick Sort are:
1. Choose a pivot element from the array.
2. Partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot.
3. Recursively apply the above steps to the sub-arrays until the base case is reached (sub-array is empty or contains only one element).

The performance of Quick Sort depends on the choice of the pivot element. In the worst case, if the pivot is chosen as the smallest or largest element, the time complexity is O(n^2). However, if the pivot is chosen randomly or as the median, the expected time complexity is O(n log n).

Quick Sort is an in-place sorting algorithm, meaning it does not require additional storage space. It is also a comparison-based sorting algorithm, meaning it can sort items of any type for which a "less-than" relation is defined.

In summary, Quick Sort is a fast, in-place, comparison-based sorting algorithm that uses the divide-and-conquer approach. Its performance depends on the choice of the pivot element, with an expected time complexity of O(n log n) if the pivot is chosen randomly or as the median. It is commonly used in practice due to its efficiency and simplicity.