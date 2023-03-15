### Searching Algorithm for the notes of the Data Structure using C Lab in the subject of Data Structure using C

- A searching algorithm is a method of finding a specific element or a subset of elements in a data structure that satisfies some criteria.
- There are two main types of searching algorithms: linear search and binary search.
- Linear search is a simple algorithm that scans the data structure from the beginning to the end, comparing each element with the target value until it is found or the end is reached.
- Binary search is a more efficient algorithm that works on sorted data structures. It divides the data structure into two halves and compares the target value with the middle element. If they are equal, the search is done. If the target value is smaller, the search continues in the left half. If the target value is larger, the search continues in the right half. This process is repeated until the target value is found or the data structure is exhausted.
- The pseudocode for linear search is:

```
linear_search(data, target):
  for i = 0 to data.length - 1:
    if data[i] == target:
      return i // target found at index i
  return -1 // target not found
```

- The pseudocode for binary search is:

```
binary_search(data, target):
  low = 0 // lower bound of the search range
  high = data.length - 1 // upper bound of the search range
  while low <= high:
    mid = (low + high) / 2 // middle index of the search range
    if data[mid] == target:
      return mid // target found at index mid
    else if data[mid] < target:
      low = mid + 1 // search in the right half
    else:
      high = mid - 1 // search in the left half
  return -1 // target not found
```

- The time complexity of linear search is O(n), where n is the number of elements in the data structure. The time complexity of binary search is O(log n), where n is the number of elements in the sorted data structure.
- The space complexity of both algorithms is O(1), as they do not require any extra space to store intermediate results.