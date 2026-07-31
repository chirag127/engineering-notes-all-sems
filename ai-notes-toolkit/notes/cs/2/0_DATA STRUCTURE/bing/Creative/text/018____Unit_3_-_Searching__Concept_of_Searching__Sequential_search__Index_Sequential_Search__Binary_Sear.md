## Unit 3 - Searching and Sorting

### Concept of Searching
- Searching is the process of finding a particular element or record in a collection of data.
- Searching is often performed on a sorted or indexed data structure to improve the efficiency and accuracy of the search.
- Searching can be classified into two types: linear search and binary search.

### Sequential Search
- Sequential search is a linear search technique that scans each element of the data structure one by one until the target element is found or the end of the data structure is reached.
- Sequential search is also known as linear search or brute-force search.
- Sequential search is simple and easy to implement, but it is inefficient and slow for large data sets.
- The time complexity of sequential search is O(n), where n is the number of elements in the data structure.

### Index Sequential Search
- Index sequential search is an improvement over sequential search that uses an index to speed up the search process.
- An index is a separate data structure that stores the key values and the corresponding locations of some or all elements in the data structure.
- Index sequential search first searches the index to find the range of locations where the target element may be present, and then performs a sequential search within that range.
- Index sequential search reduces the number of comparisons and accesses to the data structure, but it requires extra space and time to create and maintain the index.
- The time complexity of index sequential search depends on the size and structure of the index, but it is generally better than O(n).

### Binary Search
- Binary search is a divide-and-conquer technique that searches a sorted data structure by repeatedly dividing the search range into two halves and comparing the target element with the middle element of the current range.
- Binary search discards the half of the range that does not contain the target element and continues the search on the remaining half until the target element is found or the range becomes empty.
- Binary search is efficient and fast for large and sorted data sets, but it requires the data structure to be sorted and random access to be possible.
- The time complexity of binary search is O(log n), where n is the number of elements in the data structure.

### Concept of Hashing
- Hashing is a technique that maps a large and heterogeneous set of keys to a smaller and homogeneous set of values, called hash values or hash codes.
- Hashing is used to implement efficient and compact data structures, such as hash tables, that allow fast insertion, deletion, and retrieval of elements based on their keys.
- Hashing uses a hash function, which is a mathematical function that takes a key as input and returns a hash value as output.
- A good hash function should be easy to compute, uniform, and consistent, meaning that it should distribute the keys evenly over the hash values, and always return the same hash value for the same key.

### Collision Resolution Techniques used in Hashing
- A collision occurs when two or more keys are mapped to the same hash value by the hash function.
- Collisions reduce the performance and accuracy of hashing, and they need to be resolved by some techniques.
- Some common collision resolution techniques are:

  - Chaining: In chaining, each hash value is associated with a linked list of elements that have the same hash value. To insert, delete, or retrieve an element, the hash function is used to find the corresponding linked list, and then the linear search is performed on the list.
  - Linear Probing: In linear probing, each hash value is associated with a single element, and the elements are stored in an array. To insert an element, the hash function is used to find the initial position in the array, and if that position is occupied, the next available position is searched in a linear fashion. To delete or retrieve an element, the same process is followed, but the search stops when either the element is found or an empty position is encountered.
  - Quadratic Probing: In quadratic probing, the same idea as linear probing is used, but instead of searching the next available position in a linear fashion, a quadratic function is used to determine the next position. This reduces the clustering of elements that have similar hash values, but it may cause some positions to be skipped or revisited.
  - Double Hashing: In double hashing, two hash functions are used to find the position of an element in the array. The first hash function is used to find the initial position, and if that position is occupied, the second hash function is used to find the next position. The second hash function is applied repeatedly until an empty position is found or the array is full.

### Sorting
- Sorting is the process of arranging a collection of data in a specific order, such as ascending or descending, based on some criteria, such as numerical value, alphabetical order