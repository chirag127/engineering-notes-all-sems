# Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple and easy-to-understand sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
- Selection sort is an in-place sorting algorithm, which means it does not require any additional memory to sort the list.
- Selection sort has a best-case and average-case time complexity of O(n^2), making it efficient for small data sets. It is easy to modify to sort in ascending or descending order.
- Selection sort is described as an in-place comparison-based algorithm that divides the list into two parts, the sorted part on the left and the unsorted part on the right.
- Selection sort loops over indices in the array; for each index, selection sort calls indexOfMinimum and swap. If the length of the array is n, there are n indices in the array.
- Selection sort requires scanning n elements (taking n-1 comparisons) and then swapping it into the first position. Finding the minimum requires n-1 comparisons. Then sorting the rest of the list requires n-2 comparisons. In general, finding the minimum element of an n element list requires n-1 comparisons.
- Selection sort performs n swaps in the worst case, which is the same as the best case, and which is optimal for a sorting algorithm that uses swaps.
- Selection sort is not stable, meaning that the relative order of equal elements may not be preserved after sorting. It is also not adaptive, meaning that it does not take advantage of the existing order in the list.

## Pseudocode for Selection Sort

The following pseudocode shows the basic steps of selection sort algorithm:

```
selectionSort(array, size)
  for i from 0 to size-1
    minIndex = i
    for j from i+1 to size-1
      if array[j] < array[minIndex]
        minIndex = j
    swap array[i] and array[minIndex]
```

## Example of Selection Sort

The following example illustrates how selection sort works on an array of integers:

```
array = [64, 25, 12, 22, 11]

// Find the minimum element in array[0...4]
// and place it at beginning
minIndex = 0
array[0] = 64
array[1] = 25
array[2] = 12
array[3] = 22
array[4] = 11
11 < 64, so minIndex = 4
swap array[0] and array[4]
array = [11, 25, 12, 22, 64]

// Find the minimum element in array[1...4]
// and place it at beginning of array[1...4]
minIndex = 1
array[1] = 25
array[2] = 12
array[3] = 22
array[4] = 64
12 < 25, so minIndex = 2
swap array[1] and array[2]
array = [11, 12, 25, 22, 64]

// Find the minimum element in array[2...4]
// and place it at beginning of array[2...4]
minIndex = 2
array[2] = 25
array[3] = 22
array[4] = 64
22 < 25, so minIndex = 3
swap array[2] and array[3]
array = [11, 12, 22, 25, 64]

// Find the minimum element in array[3...4]
// and place it at beginning of array[3...4]
minIndex = 3
array[3] = 25
array[4] = 64
25 < 64, so minIndex = 3
swap array[3] and array[3]
array = [11, 12, 22, 25, 64]

// The array is now sorted
```

## References

: https://www.geeksforgeeks.org/selection-sort/
: https://www.simplilearn.com/tutorials/data-structure-tutorial/selection-sort-al