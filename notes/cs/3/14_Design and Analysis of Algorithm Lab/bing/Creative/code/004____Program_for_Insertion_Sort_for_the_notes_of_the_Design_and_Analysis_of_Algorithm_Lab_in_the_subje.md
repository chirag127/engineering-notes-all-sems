## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages:

- It is easy to implement and understand.
- It is stable, meaning that it preserves the relative order of equal elements.
- It is adaptive, meaning that it performs well on partially sorted arrays.
- It requires constant extra space, meaning that it only uses a fixed amount of memory beyond the input array.

The basic idea of insertion sort is to divide the array into two parts: a sorted part and an unsorted part. Initially, the sorted part consists of only the first element, and the unsorted part consists of the rest of the elements. Then, the algorithm repeatedly picks an element from the unsorted part and inserts it into the correct position in the sorted part, until the unsorted part is empty.

The algorithm can be described as follows:

- Set i to 1, the index of the second element in the array.
- Repeat until i reaches the end of the array:
  - Set key to the value of the element at index i.
  - Set j to i - 1, the index of the last element in the sorted part.
  - Repeat until j reaches -1 or the element at index j is less than or equal to key:
    - Move the element at index j to index j + 1, creating a space for key in the sorted part.
    - Decrease j by 1.
  - Insert key into the space at index j + 1.
  - Increase i by 1.

The following pseudocode shows the implementation of insertion sort:

```
procedure insertionSort(A : array of items)
   n = length(A)
   for i = 1 to n - 1
      key = A[i]
      j = i - 1
      while j >= 0 and A[j] > key
         A[j + 1] = A[j]
         j = j - 1
      end while
      A[j + 1] = key
   end for
end procedure
```

The following diagram illustrates the insertion sort algorithm on an example array:

![Insertion sort example](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

The time complexity of insertion sort is O(n^2) in the worst case, when the array is in reverse order, and O(n) in the best case, when the array is already sorted. The average case is also O(n^2), but with a smaller constant factor than the worst case. The space complexity of insertion sort is O(1), since it only uses a constant amount of extra space.