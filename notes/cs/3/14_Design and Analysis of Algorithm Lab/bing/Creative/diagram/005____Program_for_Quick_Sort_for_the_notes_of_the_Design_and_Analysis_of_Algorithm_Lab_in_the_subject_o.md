## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a divide-and-conquer algorithm that sorts an array of elements by recursively partitioning it into smaller subarrays and sorting them independently.
- The basic steps of quick sort are:
  - Choose a pivot element from the array, usually the first or the last element.
  - Partition the array into two subarrays, such that all the elements less than or equal to the pivot are in the left subarray, and all the elements greater than the pivot are in the right subarray.
  - Recursively sort the left and right subarrays using the same algorithm.
  - Concatenate the sorted left subarray, the pivot, and the sorted right subarray to obtain the final sorted array.
- The worst-case time complexity of quick sort is O(n^2), where n is the number of elements in the array. This happens when the pivot is always the smallest or the largest element, resulting in unbalanced partitions.
- The best-case time complexity of quick sort is O(n log n), where n is the number of elements in the array. This happens when the pivot is always the median of the array, resulting in balanced partitions.
- The average-case time complexity of quick sort is also O(n log n), where n is the number of elements in the array. This is because the probability of choosing a good pivot is high, and the partitions are usually balanced.
- The space complexity of quick sort is O(log n), where n is the number of elements in the array. This is because the algorithm uses a stack to store the recursive calls, and the depth of the recursion is O(log n) in the average case.
- Quick sort is an in-place algorithm, meaning it does not require additional memory to store the sorted array. It only swaps the elements within the original array.
- Quick sort is not a stable algorithm, meaning it does not preserve the relative order of equal elements in the array. For example, if the array is [2, 1, 2, 3], and the first 2 is the pivot, then the final sorted array could be [1, 2, 2, 3] or [1, 2, 3, 2], depending on how the swaps are performed.
- A pseudocode for quick sort is:

```
function quick_sort(array, low, high)
  if low < high
    pivot_index = partition(array, low, high) // partition the array and return the pivot index
    quick_sort(array, low, pivot_index - 1) // recursively sort the left subarray
    quick_sort(array, pivot_index + 1, high) // recursively sort the right subarray
  end if
end function

function partition(array, low, high)
  pivot = array[high] // choose the last element as the pivot
  i = low - 1 // initialize the index of the smaller element
  for j = low to high - 1 // loop through the array from low to high - 1
    if array[j] <= pivot // if the current element is less than or equal to the pivot
      i = i + 1 // increment the index of the smaller element
      swap array[i] and array[j] // swap the smaller element with the current element
    end if
  end for
  swap array[i + 1] and array[high] // swap the pivot with the element next to the smaller element
  return i + 1 // return the pivot index
end function
```