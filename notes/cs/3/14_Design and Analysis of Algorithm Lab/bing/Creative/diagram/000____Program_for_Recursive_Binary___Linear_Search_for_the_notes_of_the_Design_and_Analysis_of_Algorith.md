## Program for Recursive Binary & Linear Search for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

### Binary Search

- Binary search is a searching algorithm that is used to find the position of an element (target value) in a sorted array. The array should be sorted prior to applying a binary search.
- Binary search is also called a half interval search or logarithmic search.
- Binary search is a recursive algorithm. The high level approach is that we examine the middle element of the list. The value of the middle element determines whether to terminate the algorithm (found the key), recursively search the left half of the list, or recursively search the right half of the list.
- Binary search has a time complexity of O(log n), where n is the number of elements in the array.
- Binary search can be implemented in two ways: iterative method and recursive method .

#### Iterative Method

- The iterative method uses a while loop to repeatedly divide the array into two subarrays until the target value is found or the array is exhausted.
- The pseudocode for the iterative method is:

```
binarySearch(arr, x)
  low = 0
  high = arr.length - 1
  while low <= high
    mid = (low + high) / 2
    if x == arr[mid]
      return mid
    else if x < arr[mid]
      high = mid - 1
    else
      low = mid + 1
  return -1
```

#### Recursive Method

- The recursive method uses a function call to itself to divide the array into two subarrays until the target value is found or the array is exhausted.
- The pseudocode for the recursive method is:

```
binarySearch(arr, x, low, high)
  if low > high
    return -1
  mid = (low + high) / 2
  if x == arr[mid]
    return mid
  else if x < arr[mid]
    return binarySearch(arr, x, low, mid - 1)
  else
    return binarySearch(arr, x, mid + 1, high)
```

### Linear Search

- Linear search is a searching algorithm that is used to find the position of an element (target value) in an array. The array can be sorted or unsorted.
- Linear search is also called a sequential search.
- Linear search is a simple algorithm that scans the array from left to right and compares each element with the target value until it is found or the array is exhausted.
- Linear search has a time complexity of O(n), where n is the number of elements in the array.
- Linear search can be implemented in two ways: iterative method and recursive method.

#### Iterative Method

- The iterative method uses a for loop to traverse the array and compare each element with the target value.
- The pseudocode for the iterative method is:

```
linearSearch(arr, x)
  for i = 0 to arr.length - 1
    if x == arr[i]
      return i
  return -1
```

#### Recursive Method

- The recursive method uses a function call to itself to traverse the array and compare each element with the target value.
- The pseudocode for the recursive method is:

```
linearSearch(arr, x, i)
  if i >= arr.length
    return -1
  if x == arr[i]
    return i
  return linearSearch(arr, x, i + 1)
```

: https://guides.codepath.com/compsci/Binary-Search
: https://www.educba.com/binary-search-with-recursion/
: https://www.tutorialspoint.com/binary-search-recursive-and-iterative-in-c-program
: https://www.geeksforgeeks.org/binary-search/
: https://iq.opengenus.org/binary-search-iterative-recursive/
: https://www.programiz.com/dsa/binary-search
: https://www.geeksforgeeks.org/linear-search/
: https://www.javatpoint.com/linear-search-in-java