### Sorting and Order Statistics - Merge Sort

- Merge sort is a divide-and-conquer algorithm that splits an array into two subarrays, recursively sorts them, and then merges them into a single sorted array.
- The algorithm can be described as follows:

  - If the array has zero or one element, it is already sorted and no further action is needed.
  - Otherwise, divide the array into two subarrays of equal or nearly equal size.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted subarrays into a single sorted array by repeatedly taking the smallest element from either subarray and appending it to the output array.

- The merge operation can be implemented using a temporary array and two pointers, one for each subarray, that keep track of the current element to be compared.
- The merge operation takes linear time, O(n), where n is the total number of elements in the two subarrays.
- The merge sort algorithm has a recurrence relation for its running time, T(n), given by:

  - T(n) = O(1) if n <= 1
  - T(n) = 2T(n/2) + O(n) if n > 1

- Using the master theorem, we can solve this recurrence and obtain that T(n) = O(n log n) for all n.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is also a comparison-based sorting algorithm, meaning that it only uses comparisons between elements to determine their order.
- Merge sort has a space complexity of O(n), since it requires a temporary array of the same size as the input array to perform the merge operation.