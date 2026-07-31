### Binary Search

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until the remaining portion is reduced to zero or one element.

Here are the key points to remember about binary search:

1. The list must be sorted in ascending or descending order.
2. The search begins by comparing the middle element of the list with the target value.
3. If the target value matches the middle element, its position in the list is returned.
4. If the target value is less than the middle element, the search continues in the lower half of the list. Otherwise, the search continues in the upper half of the list.
5. This process continues, eliminating half of the elements, and comparing the middle value of the remaining elements with the target value until the target value is found.
6. If the entire list has been searched without finding the target value, the algorithm returns that the value is not in the list.

Binary search has a time complexity of O(log n), making it much more efficient than linear search for large lists. However, it is important to note that the list must be sorted for binary search to work. If the list is not sorted, a sorting algorithm must be applied first, which will add to the overall time complexity of the search.