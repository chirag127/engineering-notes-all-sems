### Sorting and Order Statistics - Quick Sort

- Quick sort is a **divide-and-conquer** algorithm that sorts an array of elements by recursively partitioning it into two subarrays around a **pivot** element.
- The pivot element is chosen randomly or by some heuristic, such as the median of the first, middle, and last elements of the array.
- The partitioning step rearranges the array such that all elements less than or equal to the pivot are in the left subarray, and all elements greater than the pivot are in the right subarray.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted by the same procedure.
- The base case of the recursion is when the subarray has one or zero elements, in which case it is already sorted.
- The average-case time complexity of quick sort is **O(n log n)**, where n is the number of elements in the array.
- The worst-case time complexity of quick sort is **O(n^2)**, which occurs when the pivot element is always the smallest or the largest element in the subarray, resulting in unbalanced partitions.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion tree.
- Quick sort is an **in-place** sorting algorithm, meaning it does not use any extra space to store the sorted elements, but modifies the original array.
- Quick sort is not a **stable** sorting algorithm, meaning it does not preserve the relative order of equal elements in the array.