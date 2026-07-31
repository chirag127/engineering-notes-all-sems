# Basic of Searching and Sorting Algorithms

Searching and sorting algorithms are fundamental techniques for manipulating data in a computer. Searching algorithms are used to find a specific element or a set of elements that satisfy some criteria in a collection of data. Sorting algorithms are used to arrange the elements of a collection in a specific order, such as ascending, descending, alphabetical, etc.

## Searching Algorithms

There are many types of searching algorithms, but two of the most common ones are linear search and binary search.

### Linear Search

Linear search is the simplest searching algorithm. It works by scanning the collection of data from the beginning to the end, and comparing each element with the target value. If the element matches the target value, the search is successful and the index of the element is returned. If the element does not match the target value, the search continues with the next element. If the end of the collection is reached without finding the target value, the search is unsuccessful and -1 is returned.

The pseudocode for linear search is:

```
function linear_search(array, target):
  for i from 0 to array.length - 1:
    if array[i] == target:
      return i
  return -1
```

The time complexity of linear search is O(n), where n is the number of elements in the collection. This means that the worst-case scenario is that the algorithm has to scan the entire collection to find the target value or to determine that it does not exist. The best-case scenario is that the algorithm finds the target value at the first element, in which case it only performs one comparison. The average-case scenario is that the algorithm finds the target value somewhere in the middle of the collection, in which case it performs n/2 comparisons.

### Binary Search

Binary search is a more efficient searching algorithm than linear search, but it requires that the collection of data is sorted in ascending or descending order. It works by dividing the collection into two halves, and comparing the middle element with the target value. If the element matches the target value, the search is successful and the index of the element is returned. If the element is smaller than the target value (in ascending order) or larger than the target value (in descending order), the search continues with the right half of the collection. If the element is larger than the target value (in ascending order) or smaller than the target value (in descending order), the search continues with the left half of the collection. If the collection becomes empty without finding the target value, the search is unsuccessful and -1 is returned.

The pseudocode for binary search is:

```
function binary_search(array, target):
  low = 0
  high = array.length - 1
  while low <= high:
    mid = (low + high) / 2
    if array[mid] == target:
      return mid
    else if array[mid] < target: (in ascending order)
      low = mid + 1
    else:
      high = mid - 1
  return -1
```

The time complexity of binary search is O(log n), where n is the number of elements in the collection. This means that the worst-case scenario is that the algorithm has to divide the collection into two halves log n times to find the target value or to determine that it does not exist. The best-case scenario is that the algorithm finds the target value at the middle element, in which case it only performs one comparison. The average-case scenario is that the algorithm finds the target value somewhere in the middle of the collection, in which case it performs log n comparisons.

## Sorting Algorithms

There are many types of sorting algorithms, but three of the most common ones are bubble sort, insertion sort, and selection sort.

### Bubble Sort

Bubble sort is the simplest sorting algorithm. It works by repeatedly swapping adjacent elements that are out of order, until the collection is sorted. The algorithm passes through the collection n-1 times, where n is the number of elements in the collection. In each pass, the algorithm compares each pair of adjacent elements, and swaps them if they are in the wrong order. After the first pass, the largest element is at the end of the collection. After the second pass, the second largest element is at the second last position of the collection, and so on. The algorithm stops when no swaps are performed in a pass, which means that the collection is sorted.

The pseudocode for bubble sort is:

```
function bubble_sort(array):
  swapped = true
  while swapped:
    swapped = false
    for i from 0 to array.length - 2:
      if array[i] > array[i+1]: (in ascending order)
        swap array[i] and array[i+1]
        swapped = true
```