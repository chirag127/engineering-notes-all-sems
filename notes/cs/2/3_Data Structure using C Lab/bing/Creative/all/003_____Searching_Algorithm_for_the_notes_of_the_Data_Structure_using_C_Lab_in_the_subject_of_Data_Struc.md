# Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding an element or retrieving an element from any data structure where it is stored.
- There are different types of searching algorithms, such as linear search, binary search, interpolation search, etc.
- The choice of the searching algorithm depends on the data structure, the size of the data, the sorting order of the data, and the complexity of the algorithm.
- In this note, we will focus on two basic searching algorithms: linear search and binary search.

## Linear Search
- Linear search is a simple and brute-force method of searching for an element in an array or a list .
- It works by traversing the array or list sequentially and comparing every element with the target value until a match is found or the end of the array or list is reached.
- The algorithm for linear search is as follows:

```
linear_search(array, size, target)
  for i = 0 to size - 1
    if array[i] == target
      return i // element found at index i
  return -1 // element not found
```

- The time complexity of linear search is O(n), where n is the number of elements in the array or list.
- The space complexity of linear search is O(1), as it does not require any extra space.
- Linear search is suitable for small and unsorted data sets, as it does not require any prior sorting or ordering of the data.

## Binary Search
- Binary search is a more efficient and faster method of searching for an element in a sorted array or list .
- It works by repeatedly dividing the array or list into two halves and checking if the target value is in the left half or the right half.
- The algorithm for binary search is as follows:

```
binary_search(array, low, high, target)
  while low <= high
    mid = (low + high) / 2 // find the middle index
    if array[mid] == target
      return mid // element found at index mid
    else if array[mid] < target
      low = mid + 1 // search in the right half
    else
      high = mid - 1 // search in the left half
  return -1 // element not found
```

- The time complexity of binary search is O(log n), where n is the number of elements in the array or list.
- The space complexity of binary search is O(1), as it does not require any extra space.
- Binary search is suitable for large and sorted data sets, as it reduces the search space by half in each iteration.