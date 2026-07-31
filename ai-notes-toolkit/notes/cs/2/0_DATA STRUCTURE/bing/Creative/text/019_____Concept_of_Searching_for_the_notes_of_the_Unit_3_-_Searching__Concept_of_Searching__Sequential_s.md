Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Data Structure. Here is the content for the topic of Concept of Searching for the notes of the Unit 3.

### Concept of Searching

- Searching is the process of finding an element in a collection of data that satisfies a given condition or matches a given value.
- Searching can be performed on different types of data structures, such as arrays, lists, trees, graphs, etc.
- Searching can be classified into two categories: linear searching and binary searching.

#### Linear Searching

- Linear searching is the simplest method of searching, where the elements are searched one by one from the beginning or the end of the data structure until the desired element is found or the end is reached.
- Linear searching can be performed on any type of data structure, whether it is sorted or unsorted, sequential or linked.
- Linear searching has a time complexity of O(n), where n is the number of elements in the data structure.

#### Binary Searching

- Binary searching is a method of searching that works on sorted data structures, where the elements are arranged in ascending or descending order.
- Binary searching uses the divide and conquer technique, where the data structure is divided into two halves at each step and the desired element is compared with the middle element of the current half.
- If the desired element is equal to the middle element, the search is successful. If the desired element is smaller than the middle element, the search continues in the left half. If the desired element is larger than the middle element, the search continues in the right half.
- Binary searching has a time complexity of O(log n), where n is the number of elements in the data structure.

#### Index Sequential Searching

- Index sequential searching is a method of searching that works on sorted data structures, where the elements are arranged in ascending or descending order.
- Index sequential searching uses an index table, which is a smaller data structure that stores the key values and the corresponding positions of some elements in the original data structure.
- Index sequential searching first searches the index table for the desired element using binary search. If the desired element is found in the index table, the search is successful. If the desired element is not found in the index table, the search continues in the original data structure using linear search in the range specified by the index table.
- Index sequential searching has a time complexity of O(log m + k), where m is the number of elements in the index table and k is the number of elements in the original data structure between two consecutive index entries.

### Concept of Hashing

- Hashing is a technique of mapping a large set of data elements to a smaller set of data elements, called hash table, using a function, called hash function.
- Hashing is used to perform fast and efficient searching, insertion and deletion operations on the data elements.
- Hashing has a time complexity of O(1), where 1 is the constant time required to compute the hash function.

#### Hash Function

- A hash function is a function that takes a data element as input and returns an integer value, called hash value or hash code, as output.
- A hash function should be simple, fast and uniform, meaning that it should distribute the data elements evenly across the hash table.
- A hash function can be designed using various methods, such as division method, multiplication method, folding method, etc.

#### Hash Table

- A hash table is a data structure that stores the data elements along with their hash values in an array, called hash array.
- A hash table has a fixed size, which is usually chosen to be a prime number or a power of two.
- A hash table uses a collision resolution technique to handle the situation when two or more data elements have the same hash value, called collision.

#### Collision Resolution Techniques

- Collision resolution techniques are methods of resolving the collisions that occur in a hash table.
- Collision resolution techniques can be classified into two categories: open addressing and chaining.

##### Open Addressing

- Open addressing is a collision resolution technique that uses the hash array itself to store the data elements that have collided.
- Open addressing uses a probe sequence, which is a sequence of positions in the hash array, to find an empty slot for the data element that has collided.
- Open addressing can be implemented using various methods, such as linear probing, quadratic probing, double hashing, etc.

##### Chaining

- Chaining is a collision resolution technique that uses a separate data structure, such as a linked list, to store the data elements that have collided.
- Chaining uses the hash array to store the pointers to the linked lists, which contain the data elements that have the same hash value.
- Chaining avoids the problem of clustering, which is the tendency of the