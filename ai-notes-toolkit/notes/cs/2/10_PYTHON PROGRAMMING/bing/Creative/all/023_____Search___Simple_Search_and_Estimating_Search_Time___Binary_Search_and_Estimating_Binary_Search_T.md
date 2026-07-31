# Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

## Simple Search

- A simple search is also known as a linear search or a sequential search.
- It is a method of finding an element in a list by checking each element one by one until a match is found or the end of the list is reached.
- It is the simplest and most intuitive way of searching, but also the slowest and least efficient.
- The pseudocode for a simple search is:

```
def simple_search(list, target):
  for i in range(len(list)):
    if list[i] == target:
      return i # return the index of the match
  return -1 # return -1 if no match is found
```

## Estimating Search Time for Simple Search

- To estimate the search time for a simple search, we need to consider the worst-case scenario, which is when the target element is not in the list or at the end of the list.
- In this case, we need to compare the target with every element in the list, which takes O(n) time, where n is the length of the list.
- The average-case scenario is when the target element is in the middle of the list, which takes O(n/2) time, which is still O(n) in big-O notation.
- The best-case scenario is when the target element is at the beginning of the list, which takes O(1) time, but this is very rare and does not affect the overall performance of the algorithm.
- Therefore, the search time for a simple search is O(n) in the worst case, average case, and big-O notation.

## Binary Search

- A binary search is a more efficient way of searching for an element in a sorted list.
- It is based on the idea of dividing and conquering, which means reducing the search space by half at each step until the target element is found or the search space is empty.
- It is faster and more efficient than a simple search, but it requires the list to be sorted in advance, which may take extra time and space.
- The pseudocode for a binary search is:

```
def binary_search(list, target):
  low = 0 # the lowest index of the search space
  high = len(list) - 1 # the highest index of the search space
  while low <= high: # while the search space is not empty
    mid = (low + high) // 2 # the middle index of the search space
    if list[mid] == target: # if the target is found at the middle
      return mid # return the index of the match
    elif list[mid] < target: # if the target is larger than the middle
      low = mid + 1 # discard the lower half of the search space
    else: # if the target is smaller than the middle
      high = mid - 1 # discard the upper half of the search space
  return -1 # return -1 if no match is found
```

## Estimating Search Time for Binary Search

- To estimate the search time for a binary search, we need to consider the worst-case scenario, which is when the target element is not in the list or at the boundaries of the list.
- In this case, we need to halve the search space at each step until it becomes empty, which takes O(log n) time, where n is the length of the list.
- The average-case scenario is when the target element is in the middle of the list, which takes O(log n) time as well, since the search space is halved at each step.
- The best-case scenario is when the target element is at the middle of the list, which takes O(1) time, but this is very rare and does not affect the overall performance of the algorithm.
- Therefore, the search time for a binary search is O(log n) in the worst case, average case, and big-O notation.