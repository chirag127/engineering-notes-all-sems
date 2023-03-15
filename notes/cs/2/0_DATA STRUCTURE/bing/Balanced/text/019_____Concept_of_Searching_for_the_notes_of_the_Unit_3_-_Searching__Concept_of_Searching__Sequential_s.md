### Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information from the set of items stored in the form of elements in the computer memory.
- These sets of items are in various forms, such as an array, tree, graph, or linked list.
- Based on the type of search operation, these algorithms are generally classified into two categories: Sequential Search and Binary Search.

### Sequential Search

- Sequential Search is a method of searching where the list or array is traversed sequentially and every element is checked.
- It has the best case time complexity of O(1) when the element is present at the first position.
- It has the worst case time complexity of O(n) when the element is present at the last position or not present at all.
- It is also known as Linear Search or Serial Search.
- It is a simple and easy to implement algorithm, but it is inefficient for large lists.
- It can be applied to any type of list, whether sorted or unsorted, fixed or variable length.

### Index Sequential Search

- Index Sequential Search is a method of searching where the list is divided into smaller sublists, each of which has an index associated with it.
- The index contains the first element and the last element of each sublist.
- The index is searched first using binary search to find the sublist that may contain the element.
- Then, the sublist is searched using sequential search to find the exact position of the element.
- It has the best case time complexity of O(1) when the element is present at the first position of the first sublist.
- It has the worst case time complexity of O(log n + k) where n is the number of sublists and k is the size of the sublist.
- It is also known as Indexed Linear Search or Indexed Sequential Access Method (ISAM).
- It is an improvement over sequential search, but it requires extra space for the index and it is not suitable for dynamic lists.
- It can be applied to sorted lists of fixed length.

### Binary Search

- Binary Search is a method of searching where the list is divided into two halves repeatedly until the element is found or the list is exhausted.
- The list must be sorted in ascending or descending order before applying binary search.
- The middle element of the list is compared with the search key and based on the result, the search is continued in the left half or the right half of the list.
- It has the best case time complexity of O(1) when the element is present at the middle position of the list.
- It has the worst case time complexity of O(log n) where n is the number of elements in the list.
- It is also known as Half-Interval Search or Logarithmic Search.
- It is a fast and efficient algorithm, but it requires the list to be sorted and it is not suitable for dynamic lists.
- It can be applied to sorted lists of any length.