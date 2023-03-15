### Search: Simple Search and Estimating Search Time, Binary Search and Estimating Binary Search Time

- Search is a process of finding a specific item or value in a collection of data.
- There are different types of search algorithms that can be used for different data structures and scenarios.
- The efficiency of a search algorithm can be measured by the number of comparisons or operations it performs to find the target value.

#### Simple Search

- Simple search, also known as linear search or sequential search, is the most basic search algorithm.
- It works by iterating over each element in the data structure and comparing it with the target value.
- If a match is found, the algorithm returns the index or position of the element. If no match is found, the algorithm returns -1 or None.
- Simple search can be used with any iterable data structure in Python, such as strings, lists, tuples, etc.
- The syntax of simple search in Python is:

```python
def simple_search(data, target):
  # data is the iterable data structure to search in
  # target is the value to search for
  for i in range(len(data)): # loop over each element in data
    if data[i] == target: # compare the element with the target
      return i # return the index of the element if a match is found
  return -1 # return -1 if no match is found
```

- The time complexity of simple search is O(n), where n is the number of elements in the data structure.
- This means that the worst-case scenario is that the algorithm has to check every element in the data structure to find the target or conclude that it is not present.
- The best-case scenario is that the algorithm finds the target in the first element, which takes O(1) time.
- The average-case scenario is that the algorithm finds the target in the middle of the data structure, which takes O(n/2) time, which is still O(n) in big O notation.

#### Binary Search

- Binary search, also known as logarithmic search or half-interval search, is a more efficient search algorithm than simple search.
- It works by dividing the data structure into two halves and comparing the target value with the middle element of each half.
- If the target value is equal to the middle element, the algorithm returns the index or position of the element.
- If the target value is less than the middle element, the algorithm discards the right half and repeats the process on the left half.
- If the target value is greater than the middle element, the algorithm discards the left half and repeats the process on the right half.
- Binary search can only be used with sorted data structures in Python, such as lists or tuples that are arranged in ascending or descending order.
- The syntax of binary search in Python is:

```python
def binary_search(data, target):
  # data is the sorted iterable data structure to search in
  # target is the value to search for
  low = 0 # the lowest index of the data structure
  high = len(data) - 1 # the highest index of the data structure
  while low <= high: # loop until the low and high indices cross
    mid = (low + high) // 2 # find the middle index of the current half
    if data[mid] == target: # compare the middle element with the target
      return mid # return the index of the element if a match is found
    elif data[mid] < target: # if the target is greater than the middle element
      low = mid + 1 # discard the left half and update the low index
    else: # if the target is less than the middle element
      high = mid - 1 # discard the right half and update the high index
  return -1 # return -1 if no match is found
```

- The time complexity of binary search is O(log n), where n is the number of elements in the data structure.
- This means that the worst-case scenario is that the algorithm has to divide the data structure into two halves log n times to find the target or conclude that it is not present.
- The best-case scenario is that the algorithm finds the target in the middle element, which takes O(1) time.
- The average-case scenario is that the algorithm finds the target in some middle element, which takes O(log n) time.