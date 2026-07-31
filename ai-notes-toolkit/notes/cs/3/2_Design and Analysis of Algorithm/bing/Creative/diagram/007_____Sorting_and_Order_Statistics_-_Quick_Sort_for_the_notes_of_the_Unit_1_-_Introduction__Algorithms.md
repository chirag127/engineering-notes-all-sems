### Sorting and Order Statistics - Quick Sort

- Quick sort is a divide-and-conquer sorting algorithm that works by selecting a pivot element from the array and partitioning the other elements into two subarrays, according to whether they are less than or greater than the pivot  .
- The subarrays are then sorted recursively using the same procedure until the array is sorted.
- Quick sort is an in-place algorithm, meaning it does not require additional memory to sort the array  .
- The average time complexity of quick sort is O(n log n), where n is the number of elements in the array  .
- The worst-case time complexity of quick sort is O(n^2), which occurs when the pivot element is the smallest or the largest element in the array, or when the array is already sorted  .
- The best-case time complexity of quick sort is O(n log n), which occurs when the pivot element is the median of the array, or when the array is randomly shuffled  .
- Quick sort can be easily implemented in both iterative and recursive forms.
- Quick sort is not a stable sorting algorithm, meaning it does not preserve the relative order of equal elements in the array .
- Quick sort can be improved by using different strategies to choose the pivot element, such as the median-of-three method, the random method, or the hybrid method  .
- Quick sort can also be improved by using different partitioning schemes, such as the Hoare partition scheme, the Lomuto partition scheme, or the three-way partition scheme  .
- Quick sort is one of the most widely used sorting algorithms in practice, due to its simplicity, efficiency, and adaptability  .