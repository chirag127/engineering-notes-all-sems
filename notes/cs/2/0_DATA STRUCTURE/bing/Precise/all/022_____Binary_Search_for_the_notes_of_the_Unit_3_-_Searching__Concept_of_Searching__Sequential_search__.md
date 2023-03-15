# Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until the remaining portion is reduced to zero or one element.

Here are the key points to remember about binary search:

1. Binary search operates on a sorted list of elements.
2. It compares the target value to the middle element of the list.
3. If the target value is equal to the middle element, the search is successful.
4. If the target value is less than the middle element, the search continues in the lower half of the list.
5. If the target value is greater than the middle element, the search continues in the upper half of the list.
6. The process is repeated until the target value is found or the list is exhausted.
7. The time complexity of binary search is O(log n), where n is the number of elements in the list.
