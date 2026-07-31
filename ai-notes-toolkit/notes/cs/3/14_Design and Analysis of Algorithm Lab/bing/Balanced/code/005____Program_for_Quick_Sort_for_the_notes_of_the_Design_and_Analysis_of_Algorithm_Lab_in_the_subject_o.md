## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a sorting algorithm that uses the divide and conquer strategy to sort a list of elements.
- The basic idea of quick sort is to choose a pivot element from the list, and partition the list into two sublists: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted list, and the sublists are recursively sorted using the same procedure.
- The algorithm terminates when the list has one or zero elements, which are already sorted.
- The pseudocode for quick sort is as follows:

```
procedure quick_sort(list, low, high)
  if low < high then
    pivot_index = partition(list, low, high) // choose a pivot and partition the list
    quick_sort(list, low, pivot_index - 1) // sort the left sublist
    quick_sort(list, pivot_index + 1, high) // sort the right sublist
  end if
end procedure
```

- The partition function takes a list and a range of indices, and returns the index of the pivot element after partitioning the list.
- The partition function can be implemented in different ways, but one common method is to choose the last element of the list as the pivot, and use two pointers to scan the list from left to right and right to left, swapping elements that are out of order with respect to the pivot.
- The pseudocode for the partition function using this method is as follows:

```
function partition(list, low, high)
  pivot = list[high] // choose the last element as the pivot
  i = low - 1 // initialize the left pointer
  for j = low to high - 1 do // loop through the list from left to right
    if list[j] < pivot then // if the current element is smaller than the pivot
      i = i + 1 // increment the left pointer
      swap list[i] and list[j] // swap the elements at the left and right pointers
    end if
  end for
  swap list[i + 1] and list[high] // place the pivot in its correct position
  return i + 1 // return the index of the pivot
end function
```

- The time complexity of quick sort depends on the choice of the pivot element and the distribution of the elements in the list.
- In the best case, the pivot element is always the median of the list, and the list is evenly partitioned into two sublists of equal size. In this case, the recurrence relation for the time complexity is:

```
T(n) = 2T(n/2) + O(n)
```

- Using the master theorem, we can solve this recurrence and get the best case time complexity of quick sort as O(n log n).
- In the worst case, the pivot element is always the smallest or the largest element of the list, and the list is unevenly partitioned into one sublist of size n - 1 and one sublist of size 0. In this case, the recurrence relation for the time complexity is:

```
T(n) = T(n - 1) + O(n)
```

- Solving this recurrence, we get the worst case time complexity of quick sort as O(n^2).
- In the average case, the pivot element is chosen randomly or by some heuristic, and the list is partitioned into two sublists of varying sizes. In this case, the expected time complexity of quick sort is O(n log n).
- The space complexity of quick sort is O(log n), which is the space required for the recursive call stack.
- Quick sort is an efficient and widely used sorting algorithm, but it has some drawbacks, such as:
  - It is not stable, meaning that it does not preserve the relative order of equal elements in the list.
  - It is sensitive to the choice of the pivot element, which can affect its performance significantly.
  - It is not adaptive, meaning that it does not take advantage of the existing order in the list.
  - It is not suitable for sorting large data sets that cannot fit in memory, as it requires random access to the list elements.