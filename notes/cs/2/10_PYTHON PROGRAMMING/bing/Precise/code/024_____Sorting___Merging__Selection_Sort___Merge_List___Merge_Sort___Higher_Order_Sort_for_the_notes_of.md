### Sorting & Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

#### Selection Sort
Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part. The algorithm maintains two sublists, one sorted and one unsorted. The sorted sublist is built up from left to right at the front of the list, and the unsorted sublist is reduced from right to left.

The steps of the algorithm are as follows:
1. Find the minimum element in the unsorted sublist.
2. Swap the minimum element with the first element of the unsorted sublist.
3. Move the boundary of the sorted sublist one element to the right.

This process is repeated until the entire list is sorted.

#### Merge List
Merging two lists involves combining the elements of two sorted lists into a single sorted list. This can be done by repeatedly comparing the first elements of the two lists and moving the smaller element to the new list until one of the lists is empty. The remaining elements of the non-empty list are then appended to the new list.

#### Merge Sort
Merge sort is a recursive sorting algorithm that works by dividing the list into two halves, sorting each half, and then merging the two sorted halves back together. The algorithm can be described as follows:
1. If the list has zero or one element, return the list as is (it is already sorted).
2. Divide the list into two halves.
3. Recursively sort each half.
4. Merge the two sorted halves back together.

Merge sort has a time complexity of O(n log n) in the average and worst cases, making it an efficient sorting algorithm for large lists.

#### Higher Order Sort
Higher order sort refers to sorting algorithms that take a comparison function as an argument. This allows the user to specify the sorting criteria, such as sorting by a specific field or in reverse order. Examples of higher order sort functions in Python include the `sorted` function and the `list.sort` method, both of which take a `key` argument that specifies the comparison function.