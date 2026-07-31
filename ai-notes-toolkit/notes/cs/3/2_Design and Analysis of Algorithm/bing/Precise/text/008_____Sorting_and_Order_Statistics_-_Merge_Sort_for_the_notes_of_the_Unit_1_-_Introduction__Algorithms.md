### Sorting and Order Statistics - Merge Sort

Merge sort is a sorting algorithm that uses the divide-and-conquer approach to sort a list of elements. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining, which is the sorted list.

The steps of the merge sort algorithm are as follows:

1. If the list is of length 0 or 1, return the list as it is already sorted.
2. Divide the list into two smaller sublists by splitting it in half.
3. Recursively sort each of the two sublists by calling merge sort on them.
4. Merge the two sorted sublists back into one sorted list.

The time complexity of merge sort is O(n log n) in the worst case, which makes it a very efficient sorting algorithm. It is also a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted list.