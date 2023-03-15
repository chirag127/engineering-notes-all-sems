# Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

## Selection Sort
- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element in the unsorted part of the list and moves it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2) in the worst case, where n is the number of elements in the list.
- The space complexity of selection sort is O(1) as it only requires a constant amount of auxiliary space.

## Merge List
- Merge list is a function that takes two sorted lists as input and returns a single sorted list that contains all the elements from both lists.
- The function uses a pointer for each list and compares the elements at the current positions of the pointers.
- The function appends the smaller element to the output list and advances the pointer of the corresponding list.
- The function repeats this process until one of the lists is exhausted and then appends the remaining elements of the other list to the output list.
- The time complexity of merge list is O(m + n) in the worst case, where m and n are the lengths of the input lists.
- The space complexity of merge list is O(m + n) as it requires a new list to store the output.

## Merge Sort
- Merge sort is a divide and conquer sorting algorithm that recursively splits the list into smaller sublists until each sublist has at most one element and then merges the sublists in sorted order.
- The algorithm divides the list into two halves, calls itself for the two halves, and then merges the two sorted halves using the merge list function.
- The algorithm repeats this process until the list is sorted.
- The time complexity of merge sort is O(n log n) in the worst case, where n is the number of elements in the list.
- The space complexity of merge sort is O(n) as it requires a linear amount of auxiliary space.

## Higher Order Sort
- Higher order sort is a sorting algorithm that takes a comparison function as an argument and uses it to sort the list according to a custom order.
- The comparison function is a function that takes two elements as input and returns a negative value, zero, or a positive value depending on whether the first element is less than, equal to, or greater than the second element.
- The algorithm can use any sorting technique, such as selection sort or merge sort, and apply the comparison function to determine the order of the elements.
- The time complexity of higher order sort depends on the sorting technique and the comparison function used.
- The space complexity of higher order sort depends on the sorting technique and the comparison function used.