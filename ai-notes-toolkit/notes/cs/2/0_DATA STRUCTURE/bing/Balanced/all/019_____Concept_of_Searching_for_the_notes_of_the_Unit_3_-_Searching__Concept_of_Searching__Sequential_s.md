# Concept of Searching

- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- Searching in data structure can be done by applying searching algorithms to check for or extract the desired information.
- Based on the type of search operation, searching algorithms are generally classified into two categories:
  - Sequential Search: In this, the list or array is traversed sequentially and every element is checked.
  - Interval Search: In this, the list or array is divided into smaller segments of equal size and then a search is performed in a specific interval.
- Some of the common searching algorithms are:
  - Linear Search: It is the simplest form of sequential search that checks every element of the list until a match is found or the list is exhausted.
  - Binary Search: It is a form of interval search that works on a sorted list or array and repeatedly divides the search interval in half until the key is found or the interval is empty.
  - Interpolation Search: It is an improved form of binary search that estimates the position of the key based on the first and last element of the sorted list or array and then performs a binary search in the estimated interval.
  - Hashing: It is a technique that maps a large range of keys to a smaller range of indices using a hash function and then stores the elements in an array called a hash table.
  - Index Sequential Search: It is a technique that creates an index table for a sorted list or array and then performs a binary search on the index table to find the position of the key in the original list or array.