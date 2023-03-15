Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content for the topic of Concept of Searching for the notes of the Unit 3 - Searching: Concept of Searching, Sequential search, Index Sequential Search, Binary Search. Concept of Hashing & Collision resolution Techniques used in Hashing. Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort. in the subject of DATA STRUCTURE.

### Concept of Searching
- Searching is the process of finding a given value position in a list of values.
- It decides whether a search key is present in the data or not.
- It is the algorithmic process of finding a particular item in a collection of items.
- It can be done on internal data structure or on external data structure.
- There are different techniques of searching, such as sequential search, index sequential search, binary search, etc.

### Sequential Search
- Sequential search is the simplest method of searching.
- It involves scanning the list of elements one by one until the desired element is found or the list is exhausted.
- It can be applied to any type of list, sorted or unsorted, linear or linked.
- It has a time complexity of O(n) in the worst case, where n is the number of elements in the list.
- It is also known as linear search.

### Index Sequential Search
- Index sequential search is an improvement over sequential search.
- It involves creating an index table that stores the key values and the corresponding positions of some elements in the list.
- The index table is sorted in ascending order of the key values.
- To search for an element, the index table is searched first using binary search.
- If the element is found in the index table, its position is returned.
- If the element is not found in the index table, the range of the list where the element can be present is determined by comparing the element with the nearest index values.
- Then, the sequential search is applied to that range of the list.
- It has a time complexity of O(log m + k) in the worst case, where m is the number of elements in the index table and k is the number of elements in the range of the list.
- It is also known as indexed search.

### Binary Search
- Binary search is a method of searching that works on a sorted list.
- It involves dividing the list into two halves and comparing the middle element with the search key.
- If the middle element is equal to the search key, its position is returned.
- If the middle element is greater than the search key, the search is repeated on the left half of the list.
- If the middle element is less than the search key, the search is repeated on the right half of the list.
- This process is repeated until the element is found or the list becomes empty.
- It has a time complexity of O(log n) in the worst case, where n is the number of elements in the list.
- It is also known as half-interval search or logarithmic search.

### Concept of Hashing
- Hashing is a technique of mapping a large set of keys to a smaller set of values.
- It involves using a hash function that takes a key as input and returns a hash value as output.
- The hash value is used as an index to store the key-value pair in a hash table.
- Hashing allows fast access and insertion of data, as the hash value can be computed in constant time.
- However, hashing may also cause collisions, which occur when two or more keys have the same hash value.

### Collision Resolution Techniques
- Collision resolution techniques are methods of handling collisions in hashing.
- There are different techniques of collision resolution, such as chaining, linear probing, quadratic probing, double hashing, etc.
- Chaining involves creating a linked list of key-value pairs for each hash value.
- Linear probing involves finding the next available slot in the hash table by incrementing the hash value by one.
- Quadratic probing involves finding the next available slot in the hash table by incrementing the hash value by a