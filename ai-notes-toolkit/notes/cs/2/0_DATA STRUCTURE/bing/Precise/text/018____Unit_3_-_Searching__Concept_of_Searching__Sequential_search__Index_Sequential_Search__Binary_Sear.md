## Unit 3 - Searching and Sorting

### Searching
- **Concept of Searching**: Searching refers to the process of finding a specific element or value in a data structure or collection of data.
- **Sequential Search**: Also known as linear search, this method involves iterating through the data structure element by element until the desired value is found.
- **Index Sequential Search**: This method involves creating an index for the data structure to improve search efficiency. The index contains key values and pointers to the location of the data in the structure.
- **Binary Search**: This method involves repeatedly dividing the data structure in half and comparing the middle element to the desired value until the value is found or the search interval is empty. The data structure must be sorted for this method to work.
- **Concept of Hashing**: Hashing involves using a hash function to map data to a specific location in a hash table. This can improve search efficiency as the data can be accessed directly using the hash value.
- **Collision resolution Techniques used in Hashing**: When two or more data elements are mapped to the same location in the hash table, a collision occurs. Various techniques can be used to resolve collisions, including chaining, open addressing, and rehashing.

### Sorting
- **Insertion Sort**: This method involves iterating through the data structure and inserting each element into its correct position in the sorted list.
- **Selection Sort**: This method involves finding the smallest element in the data structure and swapping it with the first element, then finding the smallest element in the remaining data and swapping it with the second element, and so on until the entire data structure is sorted.
- **Bubble Sort**: This method involves repeatedly comparing adjacent elements and swapping them if they are out of order until the entire data structure is sorted.
- **Quick Sort**: This method involves selecting a pivot element and partitioning the data structure around the pivot, then recursively sorting the partitions.
- **Merge Sort**: This method involves dividing the data structure into two halves, recursively sorting each half, and then merging the two sorted halves back together.
- **Heap Sort**: This method involves building a heap data structure from the data and repeatedly removing the maximum element from the heap and inserting it into the sorted list.
- **Radix Sort**: This method involves sorting the data based on the individual digits or characters of the elements, starting with the least significant digit or character and moving to the most significant.
