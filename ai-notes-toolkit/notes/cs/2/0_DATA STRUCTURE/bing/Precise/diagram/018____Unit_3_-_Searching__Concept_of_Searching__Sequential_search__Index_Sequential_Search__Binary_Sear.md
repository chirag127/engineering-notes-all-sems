## Unit 3 - Searching and Sorting

### Searching
- **Concept of Searching**: Searching refers to the process of finding a specific element or value in a data structure or a collection of data.
- **Sequential search**: Also known as linear search, it involves checking each element of the data structure one by one until the desired element is found.
- **Index Sequential Search**: This method involves creating an index for the data structure and using it to narrow down the search range, making the search faster.
- **Binary Search**: This method involves repeatedly dividing the search range in half until the desired element is found. It requires the data structure to be sorted.

### Hashing
- **Concept of Hashing**: Hashing is a technique used to map data of arbitrary size to data of fixed size, called hash values or hash codes.
- **Collision resolution Techniques used in Hashing**: When two or more data elements are mapped to the same hash value, a collision occurs. Common techniques to resolve collisions include chaining, open addressing, and double hashing.

### Sorting
- **Insertion Sort**: This method involves inserting each element into its correct position in the sorted list by comparing it with the previous elements.
- **Selection Sort**: This method involves finding the smallest element in the unsorted list and swapping it with the first element, then finding the smallest element in the remaining unsorted list and swapping it with the second element, and so on.
- **Bubble Sort**: This method involves repeatedly swapping adjacent elements if they are in the wrong order until the list is sorted.
- **Quick Sort**: This method involves selecting a pivot element and partitioning the list around the pivot, then recursively sorting the sublists on either side of the pivot.
- **Merge Sort**: This method involves dividing the list into two halves, recursively sorting each half, and then merging the two sorted halves back together.
- **Heap Sort**: This method involves building a heap data structure from the list and repeatedly extracting the maximum element from the heap and inserting it at the end of the sorted list.
- **Radix Sort**: This method involves sorting the list based on the individual digits of the elements, starting from the least significant digit and moving to the most significant digit. It is a non-comparison based sorting algorithm.
