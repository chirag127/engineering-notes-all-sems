# Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

## Selection Sort
- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element in the unsorted part of the list and moves it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the list.
- The space complexity of selection sort is O(1), as it only requires a constant amount of auxiliary space.

## Merge List
- Merge list is a function that takes two sorted lists as input and returns a new list that contains all the elements from both lists in sorted order.
- The function uses a two-pointer technique to compare the elements from both lists and append the smaller one to the new list.
- The function repeats this process until one of the lists is exhausted and then appends the remaining elements from the other list to the new list.
- The time complexity of merge list is O(m + n), where m and n are the lengths of the two lists.
- The space complexity of merge list is O(m + n), as it requires a new list to store the merged elements.

## Merge Sort
- Merge sort is a divide and conquer sorting algorithm that recursively splits the list into smaller sublists until they are of size one or zero, and then merges them back in sorted order using the merge list function.
- The algorithm divides the list into two halves, calls itself for the two halves, and then merges the two sorted halves using the merge list function.
- The algorithm repeats this process until the list is sorted.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list.
- The space complexity of merge sort is O(n), as it requires a temporary list to store the merged elements.

## Higher Order Sort
- Higher order sort is a sorting algorithm that takes a comparison function as an argument and uses it to sort the list according to a custom criterion.
- The algorithm can use any of the existing sorting algorithms, such as selection sort or merge sort, and pass the comparison function to them as a parameter.
- The comparison function should take two elements as input and return a negative value if the first element is smaller than the second, a positive value if the first element is larger than the second, and zero if the elements are equal.
- The time complexity of higher order sort depends on the underlying sorting algorithm and the comparison function.
- The space complexity of higher order sort depends on the underlying sorting algorithm and the comparison function.