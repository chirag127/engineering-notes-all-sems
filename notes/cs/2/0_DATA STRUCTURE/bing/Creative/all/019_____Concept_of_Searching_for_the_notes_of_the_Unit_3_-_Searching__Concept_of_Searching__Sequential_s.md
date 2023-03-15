# Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information from the set of items stored in the form of elements in the computer memory .
- Based on the type of search operation, these algorithms are generally classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked.
  - Interval Search: In this, the list or array is divided into smaller segments of equal size and then a search is performed on the segment that may contain the item.

## Sequential Search

- Sequential search is the simplest and most basic search algorithm.
- It is also known as linear search.
- It works by comparing each element of the list or array with the search key until a match is found or the end of the list is reached.
- It can be applied to any type of data structure, such as array, linked list, tree, or graph.
- It has the best case time complexity of O(1) when the element is found at the first position.
- It has the worst case time complexity of O(n) when the element is not found or found at the last position.
- It has the average case time complexity of O(n/2) when the element is found at the middle position.
- It is suitable for small and unsorted lists or arrays.

## Index Sequential Search

- Index sequential search is a variation of sequential search that uses an index to speed up the search process.
- It is also known as indexed sequential search or index search.
- It works by dividing the list or array into smaller segments of equal size and creating an index table that stores the first element and the position of each segment.
- It then compares the search key with the first element of each segment in the index table until a segment is found that may contain the item.
- It then performs a sequential search on that segment to find the exact position of the item.
- It can be applied to any type of data structure, such as array, linked list, tree, or graph.
- It has the best case time complexity of O(1) when the element is found at the first position of the first segment.
- It has the worst case time complexity of O(log n + n/m) when the element is not found or found at the last position of the last segment, where n is the size of the list or array and m is the size of the segment.
- It has the average case time complexity of O(log n + n/2m) when the element is found at the middle position of the middle segment.
- It is suitable for large and sorted lists or arrays.

## Binary Search

- Binary search is a popular and efficient search algorithm that uses the divide and conquer technique.
- It works by repeatedly dividing the sorted list or array into two halves and comparing the search key with the middle element of each half until a match is found or the list becomes empty.
- It can be applied to any type of data structure that allows random access, such as array or binary tree.
- It has the best case time complexity of O(1) when the element is found at the middle position of the list or array.
- It has the worst case time complexity of O(log n) when the element is not found or found at the first or last position of the list or array.
- It has the average case time complexity of O(log n) when the element is found at any other position of the list or array.
- It is suitable for large and sorted lists or arrays.