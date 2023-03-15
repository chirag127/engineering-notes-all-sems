# Binary Search

- Binary search is an efficient algorithm for finding an element within a sorted array  .
- Binary search works by repeatedly dividing in half the portion of the list that could contain the element, until you've narrowed down the possible locations to just one.
- Binary search compares the element to the middle element of the array. If they are not equal, the half in which the element cannot lie is eliminated and the search continues on the remaining half, again taking the middle element and comparing it until the element is found.
- Binary search has a time complexity of O(log n), where n is the number of elements in the array .
- Binary search requires that the array is sorted in ascending or descending order before applying the algorithm .
- Binary search can be implemented using iterative or recursive methods.
- Binary search is useful for building more complex algorithms in computer science, such as interpolation search, exponential search, and binary search trees.