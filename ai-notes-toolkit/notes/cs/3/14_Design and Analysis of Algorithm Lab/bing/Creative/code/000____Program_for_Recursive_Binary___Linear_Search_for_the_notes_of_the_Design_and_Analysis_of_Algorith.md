## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Binary Search

Binary search is a searching algorithm that is used to find the position of an element (target value) in a sorted array. The array should be sorted prior to applying a binary search.

Binary search is a recursive algorithm. The high level approach is that we examine the middle element of the list. The value of the middle element determines whether to terminate the algorithm (found the key), recursively search the left half of the list, or recursively search the right half of the list.

Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a while loop to repeatedly update the low and high indices of the search range until the target value is found or the range becomes empty. The recursive method follows the divide and conquer approach, where the original problem is divided into smaller subproblems and solved recursively until the base case is reached  .

The pseudocode for the recursive binary search algorithm is as follows:

```
binarySearch(array, target, low, high)
  if low > high
    return -1 // target not found
  mid = (low + high) / 2 // calculate the middle index
  if target == array[mid]
    return mid // target found at mid
  else if target < array[mid]
    return binarySearch(array, target, low, mid - 1) // search in the left half
  else
    return binarySearch(array, target, mid + 1, high) // search in the right half
```

The time complexity of binary search is O(log n), where n is the size of the array. The space complexity of the recursive binary search is O(log n), due to the stack space used by the recursive calls. The space complexity of the iterative binary search is O(1), as no extra space is used.

### Linear Search

Linear search is a searching algorithm that is used to find the position of an element (target value) in an array. It does not require the array to be sorted. It works by comparing each element of the array with the target value until a match is found or the end of the array is reached.

Linear search can also be implemented in two ways: iterative and recursive. The iterative method uses a for loop to traverse the array and check each element. The recursive method calls itself with a smaller array until the target value is found or the array becomes empty.

The pseudocode for the recursive linear search algorithm is as follows:

```
linearSearch(array, target, index)
  if index == array.length
    return -1 // target not found
  if target == array[index]
    return index // target found at index
  else
    return linearSearch(array, target, index + 1) // search in the next element
```

The time complexity of linear search is O(n), where n is the size of the array. The space complexity of the recursive linear search is O(n), due to the stack space used by the recursive calls. The space complexity of the iterative linear search is O(1), as no extra space is used.