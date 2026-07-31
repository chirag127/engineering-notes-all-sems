# Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

## Simple Search

- A simple search is a method of finding an element in a list by checking each element in the list one by one until the element is found or the list is exhausted.
- A simple search is also known as a linear search or a sequential search.
- A simple search can be implemented using a loop or a recursion in Python.
- A simple search works on any list, whether it is sorted or not.
- A simple search has a time complexity of O(n), where n is the number of elements in the list. This means that the worst-case scenario is that the element is not in the list or is the last element in the list, and the search has to check all n elements.
- A simple search has a space complexity of O(1), which means that it does not use any extra memory apart from the input list and the element to be searched.

## Binary Search

- A binary search is a method of finding an element in a sorted list by repeatedly dividing the list into two halves and checking if the element is in the left half or the right half.
- A binary search is also known as a logarithmic search or a half-interval search.
- A binary search can be implemented using an iterative or a recursive approach in Python.
- A binary search works only on a sorted list, otherwise it may not find the element or give incorrect results.
- A binary search has a time complexity of O(log n), where n is the number of elements in the list. This means that the worst-case scenario is that the element is not in the list or is the middle element in the list, and the search has to perform log n comparisons.
- A binary search has a space complexity of O(1) for the iterative approach and O(log n) for the recursive approach, which means that it uses constant memory for the iterative approach and logarithmic memory for the recursive approach.