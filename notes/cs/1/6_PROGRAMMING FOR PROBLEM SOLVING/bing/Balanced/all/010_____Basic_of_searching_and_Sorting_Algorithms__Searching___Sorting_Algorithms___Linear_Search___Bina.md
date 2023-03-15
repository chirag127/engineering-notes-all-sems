# Basic of Searching and Sorting Algorithms

Searching and sorting algorithms are fundamental techniques for manipulating data in a computer program. They are widely used in various applications, such as databases, web search engines, cryptography, and artificial intelligence. In this section, we will introduce some of the most common searching and sorting algorithms, and analyze their performance and complexity.

## Searching Algorithms

Searching algorithms are methods for finding a specific element or a set of elements that satisfy some criteria in a collection of data. The collection of data can be stored in different data structures, such as arrays, lists, trees, or graphs. Depending on the data structure and the criteria, different searching algorithms may be more suitable or efficient.

### Linear Search

Linear search is the simplest searching algorithm. It works by scanning the data collection from the beginning to the end, and comparing each element with the target value. If a match is found, the algorithm returns the index or the position of the element. If no match is found, the algorithm returns a special value, such as -1, to indicate failure.

The pseudocode for linear search is:

```
function linear_search(array, target):
  for i from 0 to array.length - 1:
    if array[i] == target:
      return i
  return -1
```

The time complexity of linear search is O(n), where n is the number of elements in the data collection. This means that the worst-case scenario is that the algorithm has to scan the entire collection to find the target or to determine that it does not exist. The best-case scenario is that the target is the first element in the collection, and the algorithm only needs one comparison. The average-case scenario is that the target is somewhere in the middle of the collection, and the algorithm needs n/2 comparisons.

The space complexity of linear search is O(1), which means that the algorithm does not use any extra memory apart from the input data and a few variables.

Linear search is easy to implement and does not require any prior knowledge or sorting of the data. However, it is inefficient for large or unsorted data collections, as it may take a long time to find the target or to conclude that it does not exist.

### Binary Search

Binary search is a more efficient searching algorithm for sorted data collections. It works by repeatedly dividing the data collection into two halves, and comparing the middle element with the target value. If the target is equal to the middle element, the algorithm returns the index or the position of the element. If the target is smaller than the middle element, the algorithm discards the right half of the collection and repeats the process on the left half. If the target is larger than the middle element, the algorithm discards the left half of the collection and repeats the process on the right half. This process continues until the target is found or the collection becomes empty.

The pseudocode for binary search is:

```
function binary_search(array, target):
  low = 0
  high = array.length - 1
  while low <= high:
    mid = (low + high) / 2
    if array[mid] == target:
      return mid
    else if array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1
```

The time complexity of binary search is O(log n), where n is the number of elements in the data collection. This means that the worst-case scenario is that the algorithm has to divide the collection log n times to find the target or to determine that it does not exist. The best-case scenario is that the target is the middle element in the collection, and the algorithm only needs one comparison. The average-case scenario is that the target is somewhere in the collection, and the algorithm needs log n comparisons.

The space complexity of binary search is O(1), which means that the algorithm does not use any extra memory apart from the input data and a few variables.

Binary search is more efficient than linear search for large or sorted data collections, as it can find the target or conclude that it does not exist in fewer comparisons. However, it requires that the data collection is sorted in ascending or descending order, and that the data structure allows random access, such as arrays. Binary search may not work well for data collections that are frequently modified, as the sorting may become invalid.

## Sorting Algorithms

Sorting algorithms are methods for rearranging the elements in a data collection in a specific order, such as ascending, descending, alphabetical, or numerical. Sorting algorithms can be classified into two categories: comparison-based and non-comparison-based. Comparison-based sorting algorithms use comparisons between elements to determine their relative order, such as bubble sort, insertion sort, and selection sort. Non-comparison-based sorting algorithms use