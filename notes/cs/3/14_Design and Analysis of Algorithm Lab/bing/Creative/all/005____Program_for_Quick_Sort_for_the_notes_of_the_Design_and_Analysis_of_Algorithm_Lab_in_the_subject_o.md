## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a divide-and-conquer algorithm that sorts an array of elements by recursively partitioning it into smaller subarrays and sorting them independently.
- The algorithm works as follows:
  - Choose a pivot element from the array, typically the last element.
  - Partition the array into two subarrays: one with elements less than or equal to the pivot, and one with elements greater than the pivot.
  - Recursively sort the subarrays using the same algorithm.
  - Concatenate the sorted subarrays and the pivot to obtain the sorted array.
- The pseudocode for the quick sort algorithm is:

```
function quick_sort(array, low, high)
  if low < high then
    pivot_index = partition(array, low, high)
    quick_sort(array, low, pivot_index - 1)
    quick_sort(array, pivot_index + 1, high)
  end if
end function

function partition(array, low, high)
  pivot = array[high]
  i = low - 1
  for j = low to high - 1 do
    if array[j] <= pivot then
      i = i + 1
      swap array[i] and array[j]
    end if
  end for
  swap array[i + 1] and array[high]
  return i + 1
end function
```

- The time complexity of quick sort is O(n log n) on average, where n is the number of elements in the array. However, in the worst case, when the array is already sorted or nearly sorted, the time complexity is O(n^2), as the partitioning produces one subarray with n - 1 elements and one with 0 elements.
- The space complexity of quick sort is O(log n) on average, as the algorithm uses a stack to store the recursive calls. However, in the worst case, the space complexity is O(n), as the stack depth is equal to the number of elements in the array.
- Quick sort is an efficient and widely used sorting algorithm, but it has some drawbacks, such as:
  - It is not stable, meaning that it does not preserve the relative order of equal elements in the array.
  - It is sensitive to the choice of the pivot element, which can affect the performance and the balance of the subarrays.
  - It is not adaptive, meaning that it does not take advantage of the existing order in the array.