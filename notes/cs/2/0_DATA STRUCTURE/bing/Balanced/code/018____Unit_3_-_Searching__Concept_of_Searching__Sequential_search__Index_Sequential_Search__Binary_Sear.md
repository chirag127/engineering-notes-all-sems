## Unit 3 - Searching and Sorting Algorithms

Searching and sorting algorithms are common algorithms that are used to manipulate data in various ways. Searching algorithms allow a set of data to be examined and for a specific item to be found. Sorting algorithms allow a data set to be sorted into a specific order.

### Concept of Searching

Searching is the process of finding a particular element or value in a collection of elements or values. The collection can be an array, a list, a tree, a graph, or any other data structure that can store multiple elements. The searching algorithm can be classified into two categories based on the type of operations they perform:

- Sequential search: This is the simplest and most basic form of searching. It involves checking each element of the collection one by one until the desired element is found or the end of the collection is reached. The time complexity of sequential search is O(n), where n is the number of elements in the collection. Sequential search is also known as linear search or brute-force search.
- Index sequential search: This is a variation of sequential search that uses an index to speed up the search process. An index is a data structure that stores the key values and the locations of the elements in the collection. The index is usually sorted in ascending or descending order of the key values. The searching algorithm first uses the index to find a range of elements that may contain the desired element, and then performs a sequential search within that range. The time complexity of index sequential search is O(log n + k), where n is the number of elements in the collection, and k is the number of elements in the range. Index sequential search is also known as indexed search or binary search with index.

- Binary search: This is a more efficient form of searching that works on a sorted collection of elements. It involves repeatedly dividing the collection into two halves and comparing the middle element with the desired element. If the middle element is equal to the desired element, the search is over. If the middle element is greater than the desired element, the search continues in the left half. If the middle element is less than the desired element, the search continues in the right half. The time complexity of binary search is O(log n), where n is the number of elements in the collection. Binary search is also known as logarithmic search or half-interval search.

### Concept of Hashing

Hashing is a technique that maps a large set of elements or values to a smaller set of elements or values, called hash values or hash codes. The mapping function that performs this transformation is called a hash function. The hash function takes an element or value as input and returns a hash value as output. The hash value is usually an integer that can be used as an index to access the element or value in a data structure, such as an array or a list. The data structure that stores the elements or values using hash values is called a hash table or a hash map.

Hashing is useful for implementing fast and efficient searching and lookup operations. By using a hash function, the searching algorithm can directly access the element or value in the hash table without having to compare it with other elements or values. The time complexity of hashing is O(1), which is constant and independent of the number of elements or values in the set.

However, hashing also has some drawbacks and challenges. One of the main challenges is to design a good hash function that can distribute the elements or values uniformly and randomly across the hash table, and avoid collisions. A collision occurs when two or more elements or values have the same hash value, and thus map to the same location in the hash table. Collisions can reduce the performance and accuracy of hashing, and cause data loss or corruption.

### Collision Resolution Techniques

Collision resolution techniques are methods that handle and resolve collisions in hashing. There are two main types of collision resolution techniques:

- Open addressing: This technique tries to find an alternative location for the element or value that causes a collision in the hash table. The alternative location is usually determined by applying a probe function to the original hash value. The probe function can be linear, quadratic, or double hashing. Linear probing involves incrementing the hash value by a constant until an empty location is found. Quadratic probing involves incrementing the hash value by a quadratic function until an empty location is found. Double hashing involves applying a second hash function to the element or value and adding it to the original hash value until an empty location is found. Open addressing is also known as closed hashing or probing.
- Chaining: This technique allows multiple elements or values to be stored at the same location in the hash table. The location is usually implemented as a linked