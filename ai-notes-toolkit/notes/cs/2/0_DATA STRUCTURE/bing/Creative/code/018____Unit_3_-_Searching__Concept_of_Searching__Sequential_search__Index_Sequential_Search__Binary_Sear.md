Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 3 - Searching and Sorting.

## Unit 3 - Searching and Sorting

### Concept of Searching
- Searching is the process of finding a specific element or value in a collection of elements or values.
- Searching can be done on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Searching can be classified into two categories: linear searching and binary searching.

### Linear Searching
- Linear searching is the simplest method of searching, where the elements are searched one by one from the beginning or the end of the collection.
- Linear searching can be done on any type of data structure, whether it is sorted or unsorted, sequential or random access.
- Linear searching has a time complexity of O(n), where n is the number of elements in the collection.

### Binary Searching
- Binary searching is a method of searching that works on sorted data structures, where the elements are arranged in ascending or descending order.
- Binary searching uses the divide and conquer technique, where the collection is divided into two halves and the search value is compared with the middle element of each half.
- If the search value is equal to the middle element, the search is successful. If the search value is less than the middle element, the search continues in the left half. If the search value is greater than the middle element, the search continues in the right half.
- Binary searching has a time complexity of O(log n), where n is the number of elements in the collection.

### Concept of Hashing
- Hashing is a technique of mapping a large set of keys or values to a smaller set of indices or addresses, using a mathematical function called a hash function.
- Hashing is used to implement data structures such as hash tables, which allow fast insertion, deletion, and retrieval of elements.
- Hashing can also be used to implement various applications such as cryptography, compression, checksums, etc.

### Collision Resolution Techniques
- A collision occurs when two or more keys or values map to the same index or address in the hash table.
- Collisions reduce the performance of hashing and can lead to data loss or corruption.
- Collision resolution techniques are methods of handling collisions and ensuring that every key or value has a unique index or address in the hash table.
- Some common collision resolution techniques are:

  - Chaining: In this technique, each index or address in the hash table points to a linked list of elements that map to that index or address. To insert, delete, or retrieve an element, the hash function is used to find the index or address, and then the linked list is traversed to find the element.
  - Linear Probing: In this technique, each index or address in the hash table contains at most one element. To insert an element, the hash function is used to find the index or address, and if it is occupied, the next available index or address is searched in a linear fashion. To delete or retrieve an element, the same process is followed.
  - Quadratic Probing: In this technique, each index or address in the hash table contains at most one element. To insert an element, the hash function is used to find the index or address, and if it is occupied, the next available index or address is searched in a quadratic fashion, using a formula such as h(k) + i^2, where h(k) is the hash function, i is the number of collisions, and k is the key or value. To delete or retrieve an element, the same process is followed.
  - Double Hashing: In this technique, each index or address in the hash table contains at most one element. To insert an element, the hash function is used to find the index or address, and if it is occupied, a second hash function is used to find the next available index or address, using a formula such as h1(k) + i * h2(k), where h1(k) and h2(k) are two different hash functions, i is the number of collisions, and k is the key or value. To delete or retrieve an element, the same process is followed.

### Concept of Sorting
- Sorting is the process of arranging a collection of elements or values in a specific order, such as ascending or descending, alphabetical or numerical, etc.
- Sorting can be done on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Sorting can be classified into two categories: internal sorting and external sorting.

### Internal Sorting
- Internal sorting is a method of sorting that works on data structures that can fit entirely in the main memory or RAM of the computer.
- Internal sorting can be further classified