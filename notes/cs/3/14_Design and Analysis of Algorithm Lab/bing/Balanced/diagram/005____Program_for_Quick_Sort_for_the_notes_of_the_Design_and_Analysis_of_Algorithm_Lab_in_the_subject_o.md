## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the **divide and conquer** strategy to partition the array into two subarrays and recursively sort them.
- The main idea of quick sort is to choose a **pivot** element from the array and move all the elements that are smaller than the pivot to the left of the pivot and all the elements that are larger than the pivot to the right of the pivot.
- The pivot can be chosen in different ways, such as the first element, the last element, the median element, or a random element of the array.
- After partitioning the array, the pivot is placed in its correct position in the sorted array and the subarrays on the left and right of the pivot are sorted recursively using the same procedure.
- The algorithm can be implemented using the following pseudocode:

```
procedure quick_sort(A, low, high)
  if low < high then
    pivot_index = partition(A, low, high) // partition the array and return the pivot index
    quick_sort(A, low, pivot_index - 1) // sort the left subarray
    quick_sort(A, pivot_index + 1, high) // sort the right subarray
  end if
end procedure

procedure partition(A, low, high)
  pivot = A[high] // choose the last element as the pivot
  i = low - 1 // initialize the index of the smaller element
  for j = low to high - 1 do // loop through the array
    if A[j] <= pivot then // if the current element is smaller than or equal to the pivot
      i = i + 1 // increment the index of the smaller element
      swap A[i] and A[j] // swap the current element with the smaller element
    end if
  end for
  swap A[i + 1] and A[high] // swap the pivot with the element next to the smaller element
  return i + 1 // return the pivot index
end procedure
```

- The time complexity of quick sort is **O(n log n)** on average and **O(n^2)** in the worst case, where n is the number of elements in the array.
- The space complexity of quick sort is **O(log n)**, which is the depth of the recursion stack.
- Quick sort is an **in-place** and **unstable** sorting algorithm, meaning that it does not require extra space to store the sorted array and it does not preserve the relative order of equal elements.
- Quick sort is suitable for sorting large arrays that can fit in memory and that have a good distribution of elements. It is not suitable for sorting arrays that are already sorted, nearly sorted, or have many duplicate elements, as these cases can lead to the worst-case performance of quick sort.