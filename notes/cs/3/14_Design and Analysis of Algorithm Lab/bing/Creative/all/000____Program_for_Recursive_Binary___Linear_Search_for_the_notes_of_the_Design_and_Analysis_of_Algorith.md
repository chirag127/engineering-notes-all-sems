## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Binary search is a searching algorithm that finds the position of a target value in a sorted array. It is also called a half-interval search or logarithmic search .
- Binary search works by comparing the target value with the middle element of the array. If they are equal, the search is successful and the position is returned. If the target value is smaller than the middle element, the search continues in the left half of the array. If the target value is larger than the middle element, the search continues in the right half of the array  .
- Binary search can be implemented in two ways: iterative and recursive. The iterative method uses a while loop to repeatedly update the low and high indices of the search range. The recursive method uses a function that calls itself with the new low and high indices until the base case is reached  .
- The pseudocode for the iterative binary search is:

```
binarySearch(array, target):
  low = 0
  high = array.length - 1
  while low <= high:
    mid = (low + high) / 2
    if target == array[mid]:
      return mid
    else if target < array[mid]:
      high = mid - 1
    else:
      low = mid + 1
  return -1
```

- The pseudocode for the recursive binary search is:

```
binarySearch(array, target, low, high):
  if low > high:
    return -1
  mid = (low + high) / 2
  if target == array[mid]:
    return mid
  else if target < array[mid]:
    return binarySearch(array, target, low, mid - 1)
  else:
    return binarySearch(array, target, mid + 1, high)
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array. The space complexity of binary search is O(1) for the iterative method and O(log n) for the recursive method, due to the stack space used by the recursive calls  .
- Linear search is a searching algorithm that finds the position of a target value in an array by checking each element from left to right. It is also called a sequential search.
- Linear search works by comparing the target value with each element of the array. If they are equal, the search is successful and the position is returned. If the target value is not found in the array, the search is unsuccessful and -1 is returned .
- Linear search can be implemented in two ways: iterative and recursive. The iterative method uses a for loop to iterate over the array elements. The recursive method uses a function that calls itself with the next index until the base case is reached .
- The pseudocode for the iterative linear search is:

```
linearSearch(array, target):
  for i = 0 to array.length - 1:
    if target == array[i]:
      return i
  return -1
```

- The pseudocode for the recursive linear search is:

```
linearSearch(array, target, index):
  if index >= array.length:
    return -1
  if target == array[index]:
    return index
  else:
    return linearSearch(array, target, index + 1)
```

- The time complexity of linear search is O(n), where n is the number of elements in the array. The space complexity of linear search is O(1) for the iterative method and O(n) for the recursive method, due to the stack space used by the recursive calls .
- Binary search is faster and more efficient than linear search, but it requires the array to be sorted. Linear search is simpler and more flexible, but it requires more comparisons and iterations .