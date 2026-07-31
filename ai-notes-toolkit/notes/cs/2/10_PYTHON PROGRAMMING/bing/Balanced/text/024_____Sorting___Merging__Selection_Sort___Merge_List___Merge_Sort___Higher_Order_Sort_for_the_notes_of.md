### Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

- Sorting is the process of arranging data in a specific order, such as ascending or descending, based on some criteria.
- Merging is the process of combining two or more sorted lists into one sorted list.
- There are different algorithms for sorting and merging data, each with different advantages and disadvantages.

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum or maximum element in the unsorted part of the list and moving it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest or largest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the list, because it requires n iterations to sort the list and each iteration requires n comparisons to find the minimum or maximum element.
- The space complexity of selection sort is O(1), because it only requires a constant amount of extra space to store the index of the minimum or maximum element.
- Selection sort is not a stable sorting algorithm, meaning that it does not preserve the relative order of equal elements in the list.
- Selection sort is not an adaptive sorting algorithm, meaning that it does not take advantage of the existing order in the list and performs the same number of operations regardless of the initial order of the elements.
- Selection sort is suitable for small lists or lists that are already nearly sorted, because it has a low overhead and performs fewer swaps than other algorithms.

#### Merge List

- Merge list is a simple merging algorithm that works by comparing the first elements of two sorted lists and appending the smaller or larger one to the output list, until one of the lists is exhausted.
- The algorithm then appends the remaining elements of the non-empty list to the output list.
- The time complexity of merge list is O(m + n), where m and n are the number of elements in the two lists, because it requires at most m + n comparisons to merge the lists.
- The space complexity of merge list is O(m + n), because it requires a new list of size m + n to store the output.
- Merge list is a stable merging algorithm, meaning that it preserves the relative order of equal elements in the lists.
- Merge list is not an adaptive merging algorithm, meaning that it does not take advantage of the existing order in the lists and performs the same number of operations regardless of the initial order of the elements.
- Merge list is suitable for merging two sorted lists of any size, because it has a linear time complexity and a simple implementation.

#### Merge Sort

- Merge sort is a recursive sorting algorithm that works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves using the merge list algorithm.
- The algorithm follows the divide and conquer paradigm, where a complex problem is broken down into smaller and simpler subproblems, which are then solved and combined to obtain the final solution.
- The algorithm uses a recursive function that takes the list and two indices, start and end, as parameters.
- The base case of the recursion is when the list has one or zero elements, in which case the list is already sorted and returned as it is.
- The recursive case of the recursion is when the list has more than one element, in which case the list is split into two halves by finding the middle index, mid, as the average of start and end.
- The algorithm then calls itself recursively on the left half, from start to mid, and on the right half, from mid + 1 to end, and obtains the sorted halves as the return values.
- The algorithm then merges the two sorted halves using the merge list algorithm and returns the merged list as the final output.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list, because it requires log n levels of recursion to divide the list into sublists of size one, and each level requires n comparisons to merge the sublists.
- The space complexity of merge sort is O(n), because it requires a new list of size n to store the output at each level of recursion.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the list.
- Merge sort is not an adaptive sorting algorithm, meaning that it does not