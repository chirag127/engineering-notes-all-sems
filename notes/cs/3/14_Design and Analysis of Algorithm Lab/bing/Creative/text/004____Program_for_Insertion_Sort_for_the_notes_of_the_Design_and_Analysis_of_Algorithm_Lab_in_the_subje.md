## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons .
- It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort .
- However, insertion sort provides several advantages:
  - It is easy to implement and understand.
  - It is stable, meaning that it preserves the relative order of equal elements.
  - It is adaptive, meaning that it performs well on partially sorted arrays.
  - It requires constant space and no auxiliary data structures.
  - It can sort the array as it receives it, making it suitable for online or streaming data.
- The basic idea of insertion sort is to divide the array into two parts: a sorted part and an unsorted part .
- Initially, the sorted part consists of only the first element, and the unsorted part consists of the rest of the elements.
- The algorithm then picks an element from the unsorted part and inserts it into the correct position in the sorted part, shifting the larger elements to the right if necessary.
- This process is repeated until the unsorted part is empty and the array is sorted.
- The pseudocode for insertion sort is as follows:

```
insertionSort(array)
  for i = 1 to length(array)
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
```

- The time complexity of insertion sort is O(n^2) in the worst case and average case, and O(n) in the best case, where n is the number of elements in the array .
- The worst case occurs when the array is in reverse order, and the best case occurs when the array is already sorted.
- The space complexity of insertion sort is O(1), as it only requires constant extra space for the key variable .