## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- A recursive binary search is an algorithm that searches for a target value in a sorted array by repeatedly dividing the array into two halves and comparing the middle element with the target.
- A recursive linear search is an algorithm that searches for a target value in an array by checking each element from left to right until the target is found or the end of the array is reached.
- Both algorithms use recursion, which is a technique of solving a problem by breaking it down into smaller subproblems of the same type and solving them using the same algorithm.
- The pseudocode for the recursive binary search is:

```
function binarySearch(array, low, high, target)
  if low > high then
    return -1 // target not found
  end if
  mid = (low + high) / 2 // calculate the middle index
  if array[mid] == target then
    return mid // target found at mid
  else if array[mid] > target then
    return binarySearch(array, low, mid - 1, target) // search in the left half
  else
    return binarySearch(array, mid + 1, high, target) // search in the right half
  end if
end function
```

- The pseudocode for the recursive linear search is:

```
function linearSearch(array, index, target)
  if index >= array.length then
    return -1 // target not found
  end if
  if array[index] == target then
    return index // target found at index
  else
    return linearSearch(array, index + 1, target) // search in the next element
  end if
end function
```

- The time complexity of the recursive binary search is O(log n), where n is the size of the array, because it halves the search space in each recursive call.
- The time complexity of the recursive linear search is O(n), where n is the size of the array, because it checks each element in the array once.
- The space complexity of both algorithms is O(log n), where n is the size of the array, because of the recursive call stack.