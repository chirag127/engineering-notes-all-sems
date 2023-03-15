Hello, I am Sydney, your AI assistant. I can help you with your study material for the Data Structure using C Lab. Here are some notes on the topic of Searching Algorithm.

### Searching Algorithm

- A searching algorithm is a method of finding a specific element or a subset of elements in a data structure, such as an array, a list, a tree, or a graph.
- The searching algorithm can be classified into two types: linear search and binary search.
- Linear search is a simple technique that scans the data structure from the beginning to the end, comparing each element with the target value until a match is found or the end is reached.
- Binary search is a more efficient technique that works on sorted data structures. It divides the data structure into two halves and compares the target value with the middle element. If they are equal, the search is successful. If the target value is smaller, the search continues in the left half. If the target value is larger, the search continues in the right half. This process is repeated until a match is found or the data structure is exhausted.
- The time complexity of linear search is O(n), where n is the number of elements in the data structure. The time complexity of binary search is O(log n), where n is the number of elements in the data structure.
- The space complexity of both linear search and binary search is O(1), as they do not require any extra space to store intermediate results.
- The pseudocode for linear search is:

```
linear_search(data, target):
  for i = 0 to data.length - 1:
    if data[i] == target:
      return i // index of the target element
  return -1 // target element not found
```

- The pseudocode for binary search is:

```
binary_search(data, target):
  low = 0 // lower bound of the search range
  high = data.length - 1 // upper bound of the search range
  while low <= high:
    mid = (low + high) / 2 // middle index of the search range
    if data[mid] == target:
      return mid // index of the target element
    else if data[mid] < target:
      low = mid + 1 // search in the right half
    else:
      high = mid - 1 // search in the left half
  return -1 // target element not found
```