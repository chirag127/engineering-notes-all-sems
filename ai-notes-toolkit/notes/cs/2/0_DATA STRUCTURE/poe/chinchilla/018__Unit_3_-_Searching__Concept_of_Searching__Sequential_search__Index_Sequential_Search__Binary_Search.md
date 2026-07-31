## Unit 3 - Searching and Sorting

In this unit, we will learn about searching and sorting algorithms. Searching is a process of finding a specific item from a collection of items. Sorting is the process of arranging the items in a particular order. Both searching and sorting are fundamental to computer science and are used extensively in various applications.

### Searching

#### Concept of Searching

- Searching is the process of finding an element in a collection of elements.
- Searching is a fundamental operation in computer science and is used extensively in various applications.
- The efficiency of a search algorithm is measured by its time complexity, which is the amount of time it takes to perform a search operation.

#### Sequential Search

- Sequential search, also known as linear search, is a simple search algorithm that checks each element in a collection until the desired element is found.
- The time complexity of sequential search is O(n), where n is the number of elements in the collection.
- Sequential search is efficient for small collections, but it becomes inefficient for large collections.

#### Index Sequential Search

- Index sequential search is an improvement over sequential search that uses an index to speed up the search operation.
- The index contains the starting position of each block of elements in the collection.
- The time complexity of index sequential search is O(log n), where n is the number of elements in the collection.

#### Binary Search

- Binary search is a search algorithm that works by repeatedly dividing the search interval in half.
- Binary search is efficient for large collections and has a time complexity of O(log n), where n is the number of elements in the collection.
- The collection must be sorted in ascending or descending order for binary search to work.

### Hashing

#### Concept of Hashing

- Hashing is a technique used to store and retrieve data in a hash table.
- A hash function is used to map each item to a unique index in the hash table.
- Hashing is a fast and efficient way to store and retrieve data.

#### Collision Resolution Techniques Used in Hashing

- Collision occurs when two or more items are mapped to the same index in the hash table.
- Collision resolution techniques are used to handle collisions in hashing.
- Some collision resolution techniques are chaining, linear probing, quadratic probing, and double hashing.

### Sorting

#### Insertion Sort

- Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time.
- The time complexity of insertion sort is O(n^2), where n is the number of elements in the collection.

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the collection and moving it to the beginning of the sorted part.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the collection.

#### Bubble Sort

- Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
- The time complexity of bubble sort is O(n^2), where n is the number of elements in the collection.

#### Quick Sort

- Quick sort is a divide-and-conquer sorting algorithm that works by partitioning the collection into two sub-collections, sorting each sub-collection recursively, and then combining the sorted sub-collections.
- The time complexity of quick sort is O(n log n), where n is the number of elements in the collection.

#### Merge Sort

- Merge sort is a divide-and-conquer sorting algorithm that works by dividing the collection into two sub-collections, sorting each sub-collection recursively, and then merging the sorted sub-collections.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the collection.

#### Heap Sort

- Heap sort is a comparison-based sorting algorithm that works by building a binary heap from the collection and repeatedly removing the root element from the heap and inserting it into the sorted part of the collection.
- The time complexity of heap sort is O(n log n), where n is the number of elements in the collection.

#### Radix Sort

- Radix sort is a non-comparison-based sorting algorithm that works by sorting the elements by their digits.
- Radix sort is efficient for collections with a large number of elements.
- The time complexity of radix sort is O(kn), where k is the maximum number of digits in the collection and n is the number of elements in the collection.

In conclusion, searching and sorting algorithms are fundamental to computer science and are used extensively in various applications. The efficiency of a search or sort algorithm is measured by its time complexity, which is the amount of time it takes to perform the operation. It is important to choose the appropriate algorithm for a particular application to ensure efficiency and accuracy.