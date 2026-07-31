### Sorting and Order Statistics - Merge Sort

Merge sort is a sorting algorithm that uses the divide-and-conquer approach to sort a list of elements. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining, which will be the sorted list.

The steps of the merge sort algorithm are as follows:

1. If the list is of length 0 or 1, return the list as it is already sorted.
2. Divide the list into two smaller sublists by splitting it in half.
3. Recursively sort each of the two sublists by calling merge sort on them.
4. Merge the two sorted sublists back into one sorted list.

The time complexity of merge sort is O(n log n) in the worst case, where n is the number of elements in the list. This makes it a very efficient sorting algorithm for large datasets.

Merge sort has several advantages over other sorting algorithms. It is a stable sort, meaning that it maintains the relative order of equal elements. It is also easily parallelizable, as the sublists can be sorted independently. However, merge sort requires additional space to store the sublists during the sorting process, which can be a disadvantage for large datasets.

In summary, merge sort is an efficient and stable sorting algorithm that uses a divide-and-conquer approach to sort a list of elements. Its time complexity is O(n log n) in the worst case, making it a good choice for large datasets. However, it does require additional space for the sorting process.