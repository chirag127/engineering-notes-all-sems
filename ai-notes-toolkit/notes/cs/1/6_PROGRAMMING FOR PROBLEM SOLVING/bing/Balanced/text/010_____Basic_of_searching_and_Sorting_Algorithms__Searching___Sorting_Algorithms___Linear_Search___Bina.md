### Basic of Searching and Sorting Algorithms

Searching and sorting algorithms are fundamental techniques for manipulating data in a computer program. They are widely used in various applications, such as databases, web search engines, cryptography, and artificial intelligence. In this section, we will introduce some of the most common searching and sorting algorithms, and explain how they work and compare their performance.

#### Searching Algorithms

A searching algorithm is a method for finding a specific element or a set of elements that satisfy some criteria in a collection of data. The collection of data can be stored in different data structures, such as arrays, lists, trees, or graphs. The searching algorithm can be classified into two types: linear search and binary search.

##### Linear Search

Linear search is the simplest searching algorithm. It works by scanning the data collection from the beginning to the end, and checking each element one by one until it finds the target element or reaches the end of the collection. Linear search can be applied to any data structure that supports sequential access, such as arrays or lists. The pseudocode for linear search is as follows:

```
function linear_search(data, target):
  for i from 0 to data.length - 1:
    if data[i] == target:
      return i // target found at index i
  return -1 // target not found
```

The time complexity of linear search is O(n), where n is the number of elements in the data collection. This means that the worst-case scenario is that the algorithm has to scan the entire collection to find the target or determine that it does not exist. The best-case scenario is that the algorithm finds the target at the first element, and only takes one comparison. The average-case scenario is that the algorithm takes n/2 comparisons.

##### Binary Search

Binary search is a more efficient searching algorithm than linear search, but it requires that the data collection is sorted in ascending or descending order. It works by dividing the data collection into two halves, and comparing the target element with the middle element of the current half. If the target is equal to the middle element, then the search is successful. If the target is smaller than the middle element, then the search continues in the left half. If the target is larger than the middle element, then the search continues in the right half. This process is repeated until the target is found or the current half becomes empty. Binary search can be applied to any data structure that supports random access, such as arrays. The pseudocode for binary search is as follows:

```
function binary_search(data, target):
  low = 0 // lower bound of the search range
  high = data.length - 1 // upper bound of the search range
  while low <= high:
    mid = (low + high) / 2 // middle index of the current range
    if data[mid] == target:
      return mid // target found at index mid
    else if data[mid] < target:
      low = mid + 1 // search in the right half
    else:
      high = mid - 1 // search in the left half
  return -1 // target not found
```

The time complexity of binary search is O(log n), where n is the number of elements in the data collection. This means that the worst-case scenario is that the algorithm has to divide the collection into two halves log n times to find the target or determine that it does not exist. The best-case scenario is that the algorithm finds the target at the middle element, and only takes one comparison. The average-case scenario is that the algorithm takes log n comparisons.

#### Sorting Algorithms

A sorting algorithm is a method for rearranging the elements in a data collection in a specific order, such as ascending or descending. Sorting algorithms are useful for organizing data, improving the efficiency of other algorithms, and facilitating data analysis. There are many different sorting algorithms, each with different advantages and disadvantages. In this section, we will introduce some of the most common sorting algorithms, such as bubble sort, insertion sort, and selection sort.

##### Bubble Sort

Bubble sort is the simplest sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order, until the data collection is sorted. Bubble sort can be applied to any data structure that supports sequential access and swapping, such as arrays or lists. The pseudocode for bubble sort is as follows:

```
function bubble_sort(data):
  for i from 0 to data.length - 2:
    for j from 0 to data.length - i - 2:
      if data[j] > data[j + 1]: // compare adjacent elements
        swap(data[j], data[j + 1]) // swap them if out of order
```

The time complexity of bubble sort is O(n^2), where n is