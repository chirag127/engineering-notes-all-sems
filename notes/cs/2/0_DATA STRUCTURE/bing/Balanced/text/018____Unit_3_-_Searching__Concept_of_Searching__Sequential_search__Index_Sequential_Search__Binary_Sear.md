## Unit 3 - Searching and Sorting Algorithms

### Concept of Searching
- Searching is the process of finding an element or a value in a data structure, such as an array or a list.
- Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is used.
- Based on the type of operations, searching algorithms are generally classified into two categories:
  - Sequential search: The algorithm checks each element in the data structure one by one until it finds the target element or reaches the end of the data structure.
  - Binary search: The algorithm divides the sorted data structure into two halves and compares the target element with the middle element of each half. It repeats this process until it finds the target element or the data structure becomes empty.

### Concept of Hashing and Collision Resolution Techniques
- Hashing is a technique of mapping a large set of data elements to a smaller set of data elements, called hash table, using a function called hash function.
- Hashing is useful for fast and efficient search, insertion and deletion operations on the data elements.
- A collision occurs when two or more data elements are mapped to the same location in the hash table by the hash function.
- Collision resolution techniques are methods to handle the collisions and store the data elements in the hash table without losing any information.
- Some common collision resolution techniques are:
  - Linear probing: The algorithm tries to find the next available location in the hash table by moving linearly from the original location until it finds an empty slot or reaches the end of the hash table.
  - Quadratic probing: The algorithm tries to find the next available location in the hash table by moving quadratically from the original location until it finds an empty slot or reaches the end of the hash table.
  - Chaining: The algorithm uses a linked list to store the data elements that are mapped to the same location in the hash table. Each location in the hash table contains a pointer to the head of the linked list.

### Concept of Sorting
- Sorting is the process of arranging a set of data elements in a certain order, such as ascending or descending order.
- Sorting algorithms are algorithms that put elements of a list in a certain order.
- Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists.
- Some common sorting algorithms are :
  - Insertion sort: The algorithm iterates over the list and inserts each element into its correct position in the sorted part of the list.
  - Selection sort: The algorithm iterates over the list and selects the smallest (or largest) element and swaps it with the first (or last) element of the list. It repeats this process for the remaining unsorted part of the list.
  - Bubble sort: The algorithm iterates over the list and compares each pair of adjacent elements and swaps them if they are in the wrong order. It repeats this process until no swaps are needed.
  - Quick sort: The algorithm chooses a pivot element from the list and partitions the list into two sublists, one with elements smaller than the pivot and one with elements larger than the pivot. It then recursively sorts the sublists using the same method.
  - Merge sort: The algorithm divides the list into two halves and recursively sorts each half using the same method. It then merges the two sorted halves into one sorted list.
  - Heap sort: The algorithm builds a heap (a binary tree where each node is larger than its children) from the list and repeatedly removes the largest element from the heap and places it at the end of the list. It repeats this process until the heap is empty.
  - Radix sort: The algorithm sorts the list based on the individual digits or characters of the elements, starting from the least significant digit or character and moving to the most significant digit or character.