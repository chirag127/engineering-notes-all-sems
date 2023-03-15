## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A recursive binary search is an algorithm that searches for a target value in a sorted array by repeatedly dividing the array into two halves and comparing the middle element with the target.
- A recursive linear search is an algorithm that searches for a target value in an array by checking each element from left to right until the target is found or the end of the array is reached.
- Both algorithms use recursion, which is a technique of defining a problem in terms of smaller instances of the same problem.
- The pseudocode for recursive binary search is:

```
function binary_search(array, low, high, target)
  if low > high then
    return -1 // target not found
  end if
  mid = (low + high) / 2 // integer division
  if array[mid] == target then
    return mid // target found
  else if array[mid] < target then
    return binary_search(array, mid + 1, high, target) // search in right half
  else
    return binary_search(array, low, mid - 1, target) // search in left half
  end if
end function
```

- The pseudocode for recursive linear search is:

```
function linear_search(array, index, target)
  if index >= array.length then
    return -1 // target not found
  end if
  if array[index] == target then
    return index // target found
  else
    return linear_search(array, index + 1, target) // search in next element
  end if
end function
```

- The time complexity of recursive binary search is O(log n), where n is the size of the array, because it halves the search space in each recursive call.
- The time complexity of recursive linear search is O(n), where n is the size of the array, because it checks each element in the array once.
- The space complexity of recursive binary search is O(log n), where n is the size of the array, because it uses a call stack to store the recursive calls.
- The space complexity of recursive linear search is O(n), where n is the size of the array, because it uses a call stack to store the recursive calls.