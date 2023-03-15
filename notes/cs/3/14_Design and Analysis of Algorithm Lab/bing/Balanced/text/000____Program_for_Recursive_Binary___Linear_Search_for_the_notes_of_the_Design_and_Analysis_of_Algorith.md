## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A **recursive binary search** is an algorithm that searches for a target value in a sorted array by repeatedly dividing the search interval in half and comparing the target value with the middle element of the subarray.
- A **recursive linear search** is an algorithm that searches for a target value in an array by checking each element from left to right until the target value is found or the end of the array is reached.
- Both algorithms use **recursion**, which is a technique of defining a problem in terms of smaller instances of the same problem.
- The **time complexity** of recursive binary search is O(log n), where n is the size of the array, because the search interval is halved at each recursive call.
- The **time complexity** of recursive linear search is O(n), where n is the size of the array, because each element is checked once in the worst case.
- The **space complexity** of both algorithms is O(log n), where n is the size of the array, because the maximum depth of the recursive call stack is log n.
- The **advantages** of recursive binary search are that it is faster than linear search for large arrays and that it does not require extra space for storing the indices of the subarray.
- The **disadvantages** of recursive binary search are that it requires the array to be sorted and that it may cause stack overflow for very large arrays or deep recursion.
- The **advantages** of recursive linear search are that it does not require the array to be sorted and that it is simple to implement.
- The **disadvantages** of recursive linear search are that it is slower than binary search for large arrays and that it may cause stack overflow for very large arrays or deep recursion.

- The **pseudocode** for recursive binary search is:

```
function binary_search(array, low, high, target)
  if low > high
    return -1 // target not found
  mid = (low + high) / 2 // integer division
  if array[mid] == target
    return mid // target found
  else if array[mid] > target
    return binary_search(array, low, mid - 1, target) // search in left subarray
  else
    return binary_search(array, mid + 1, high, target) // search in right subarray
```

- The **pseudocode** for recursive linear search is:

```
function linear_search(array, index, target)
  if index == array.length
    return -1 // target not found
  if array[index] == target
    return index // target found
  else
    return linear_search(array, index + 1, target) // search in next element
```