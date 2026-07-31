### Search : Simple Search and Estimating Search Time , Binary Search and Estimating Binary Search Time

- Search is a common operation that involves finding an element in a collection that satisfies a given condition or matches a given value.
- There are different algorithms for performing search, depending on the type and structure of the collection, and the desired efficiency and accuracy of the search.
- In this section, we will discuss two basic search algorithms: simple search and binary search, and how to estimate their running time.

#### Simple Search

- Simple search, also known as linear search or sequential search, is a brute-force algorithm that checks every element in the collection until it finds the target element or reaches the end of the collection.
- Simple search can be applied to any collection, regardless of its order or structure.
- The pseudocode for simple search is as follows:

```
# Assume collection is a list of elements, and target is the value to be searched
def simple_search(collection, target):
  # Loop through the collection from the first element to the last
  for i in range(len(collection)):
    # If the current element matches the target, return its index
    if collection[i] == target:
      return i
  # If the loop ends without finding the target, return -1 to indicate failure
  return -1
```

- The running time of simple search depends on the size of the collection and the position of the target element (if it exists).
- In the best case, the target element is the first element in the collection, and the algorithm only needs one comparison to find it. The best case running time is O(1).
- In the worst case, the target element is the last element in the collection, or does not exist in the collection, and the algorithm needs to check every element in the collection. The worst case running time is O(n), where n is the number of elements in the collection.
- In the average case, the target element is somewhere in the middle of the collection, and the algorithm needs to check about half of the elements in the collection. The average case running time is also O(n), since the constant factor of 1/2 can be ignored in the asymptotic notation.

#### Binary Search

- Binary search, also known as logarithmic search or bisection search, is a divide-and-conquer algorithm that exploits the order of a sorted collection to find the target element more efficiently than simple search.
- Binary search can only be applied to a collection that is sorted in ascending or descending order.
- The pseudocode for binary search is as follows:

```
# Assume collection is a list of elements sorted in ascending order, and target is the value to be searched
def binary_search(collection, target):
  # Initialize the lower and upper bounds of the search range
  low = 0
  high = len(collection) - 1
  # Loop until the search range is empty
  while low <= high:
    # Find the middle element of the current search range
    mid = (low + high) // 2
    # If the middle element matches the target, return its index
    if collection[mid] == target:
      return mid
    # If the middle element is smaller than the target, narrow the search range to the right half
    elif collection[mid] < target:
      low = mid + 1
    # If the middle element is larger than the target, narrow the search range to the left half
    else:
      high = mid - 1
  # If the loop ends without finding the target, return -1 to indicate failure
  return -1
```

- The running time of binary search depends on the size of the collection and the position of the target element (if it exists).
- In the best case, the target element is the middle element of the collection, and the algorithm only needs one comparison to find it. The best case running time is O(1).
- In the worst case, the target element is one of the endpoints of the collection, or does not exist in the collection, and the algorithm needs to halve the search range until it becomes empty. The worst case running time is O(log n), where n is the number of elements in the collection.
- In the average case, the target element is somewhere in the middle of the collection, and the algorithm needs to halve the search range about log n times to find it. The average case running time is also O(log n), since the constant factor of 1/2 can be ignored in the asymptotic notation.