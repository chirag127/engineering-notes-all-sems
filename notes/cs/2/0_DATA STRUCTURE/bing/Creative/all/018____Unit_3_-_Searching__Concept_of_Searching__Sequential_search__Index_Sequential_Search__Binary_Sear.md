# Unit 3 - Searching and Sorting

## Searching
- Searching is the process of finding a particular element or value in a collection of elements or values.
- Searching can be performed on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Searching can be classified into two categories: linear searching and binary searching.

### Linear Searching
- Linear searching is the simplest method of searching, where the search element is compared with each element of the collection sequentially until a match is found or the end of the collection is reached.
- Linear searching can be performed on sorted or unsorted collections, but it is inefficient for large collections as it requires O(n) time in the worst case, where n is the number of elements in the collection.
- Examples of linear searching algorithms are sequential search and index sequential search.

#### Sequential Search
- Sequential search is a linear searching algorithm that starts from the first element of the collection and compares it with the search element. If they match, the search is successful and the position of the element is returned. If they do not match, the algorithm moves to the next element and repeats the process until a match is found or the end of the collection is reached.
- Sequential search can be implemented using a loop or a recursion.
- Sequential search is simple and easy to implement, but it is slow and inefficient for large collections.

#### Index Sequential Search
- Index sequential search is a linear searching algorithm that uses an index to speed up the search process. An index is a separate data structure that stores the key values and the positions of some elements of the collection. The index is usually sorted in ascending or descending order of the key values.
- Index sequential search first searches the index for the search element using binary search. If the search element is found in the index, the position of the corresponding element in the collection is returned. If the search element is not found in the index, the algorithm determines the range of the collection where the search element may be present using the nearest index values. Then, the algorithm performs a sequential search on that range until a match is found or the end of the range is reached.
- Index sequential search is faster than sequential search, but it requires extra space and time to create and maintain the index. The index also needs to be updated whenever the collection is modified.

### Binary Searching
- Binary searching is a method of searching that works on sorted collections. It uses the divide and conquer technique to reduce the search space by half in each iteration.
- Binary searching compares the search element with the middle element of the collection. If they match, the search is successful and the position of the element is returned. If the search element is smaller than the middle element, the algorithm discards the right half of the collection and repeats the process on the left half. If the search element is larger than the middle element, the algorithm discards the left half of the collection and repeats the process on the right half. This process continues until a match is found or the collection becomes empty.
- Binary search can be implemented using a loop or a recursion.
- Binary search is efficient and fast for large collections, as it requires O(log n) time in the worst case, where n is the number of elements in the collection. However, binary search requires the collection to be sorted in advance, which may take O(n log n) time in the worst case.

## Hashing
- Hashing is a technique of mapping a large set of keys or values to a smaller set of indices or addresses, using a function called a hash function. The smaller set is called a hash table, which is an array of fixed size.
- Hashing is useful for implementing fast and efficient searching, insertion, deletion, and retrieval operations on collections of data. The hash function transforms the key or value into an index or address, which can be used to access the corresponding element in the hash table in constant time.
- Hashing can also be used for data compression, encryption, checksums, etc.

### Hash Function
- A hash function is a function that maps a key or value to an index or address in the hash table. The hash function should be deterministic, meaning that it should always produce the same output for the same input. The hash function should also be uniform, meaning that it should distribute the keys or values evenly across the hash table, to avoid collisions.
- A hash function can be simple or complex, depending on the type and range of the keys or values, and the size and structure of the hash table. Some examples of hash functions are:

  - Division method: h(k) = k mod m, where k is the key, m is the size of the hash table, and h(k) is the index or address.
  - Multiplication method: h(k)