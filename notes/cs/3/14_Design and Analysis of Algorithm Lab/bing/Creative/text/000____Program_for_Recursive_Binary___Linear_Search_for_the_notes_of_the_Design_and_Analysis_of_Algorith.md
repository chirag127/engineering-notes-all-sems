## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Binary search is a searching algorithm that finds the position of a target value in a sorted array. It is also called a half-interval search or logarithmic search  .
- Binary search works by comparing the target value with the middle element of the array. If they are equal, the search is successful and the position is returned. If they are not equal, the search continues in either the left or the right half of the array, depending on whether the target value is smaller or larger than the middle element  .
- Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a loop to repeat the comparison and narrowing of the search range until the target value is found or the array is exhausted. The recursive method uses a function that calls itself with a smaller subarray as an argument until the base case is reached   .
- The pseudocode for the recursive binary search algorithm is as follows  :

```
binarySearch(array, target, low, high)
  // base case: the search range is empty
  if low > high
    return -1 // not found
  // find the middle index of the search range
  mid = (low + high) / 2
  // compare the target value with the middle element
  if target == array[mid]
    return mid // found
  else if target < array[mid]
    // search in the left half of the array
    return binarySearch(array, target, low, mid - 1)
  else
    // search in the right half of the array
    return binarySearch(array, target, mid + 1, high)
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array. The space complexity of binary search is O(1) for the iterative method and O(log n) for the recursive method, due to the stack space used by the recursive calls     .
- Linear search is a searching algorithm that finds the position of a target value in an array by checking each element in order. It is also called a sequential search or a brute-force search  .
- Linear search works by comparing the target value with each element of the array until it is found or the array is exhausted. If the target value is found, the search is successful and the position is returned. If the target value is not found, the search is unsuccessful and -1 is returned  .
- Linear search can also be implemented in two ways: iterative and recursive. The iterative method uses a loop to repeat the comparison until the target value is found or the array is exhausted. The recursive method uses a function that calls itself with the next element as an argument until the base case is reached  .
- The pseudocode for the recursive linear search algorithm is as follows :

```
linearSearch(array, target, index)
  // base case: the array is exhausted
  if index == array.length
    return -1 // not found
  // compare the target value with the current element
  if target == array[index]
    return index // found
  else
    // search in the next element of the array
    return linearSearch(array, target, index + 1)
```

- The time complexity of linear search is O(n), where n is the number of elements in the array. The space complexity of linear search is O(1) for the iterative method and O(n) for the recursive method, due to the stack space used by the recursive calls  .
- Binary search is more efficient than linear search for large and sorted arrays, as it reduces the search range by half at each step. Linear search is simpler and more suitable for small and unsorted arrays, as it does not require any sorting or extra space   [^7