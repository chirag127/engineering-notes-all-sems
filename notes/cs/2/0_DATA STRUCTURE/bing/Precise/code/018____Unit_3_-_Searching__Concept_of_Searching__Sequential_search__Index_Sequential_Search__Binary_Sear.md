## Unit 3 - Searching and Sorting

### Searching
Searching is the process of finding a specific element or value in a data structure or a collection of data. There are several searching algorithms that can be used to find an element in a data structure. Some of the most common searching algorithms are:

1. **Sequential search**: This is the simplest searching algorithm. It involves iterating through the entire data structure, comparing each element with the target value until the element is found or the end of the data structure is reached.

2. **Index Sequential Search**: This is an improvement over the sequential search algorithm. It involves creating an index for the data structure, which can be used to quickly locate the target value.

3. **Binary Search**: This is an efficient searching algorithm that can be used on sorted data structures. It involves repeatedly dividing the data structure in half and comparing the middle element with the target value until the element is found or the search interval is empty.

### Hashing
Hashing is a technique used to map data of arbitrary size to data of fixed size. It involves using a hash function to generate a hash value for the data, which can be used as an index to store the data in a hash table. Collision resolution techniques are used to handle situations where multiple data elements map to the same hash value. Some common collision resolution techniques are:

1. **Chaining**: This involves creating a linked list at each index of the hash table, and storing all the data elements that map to that index in the linked list.

2. **Open Addressing**: This involves finding an alternate index for the data element using a probing sequence, such as linear probing or quadratic probing.

### Sorting
Sorting is the process of arranging data in a specific order. There are several sorting algorithms that can be used to sort data. Some of the most common sorting algorithms are:

1. **Insertion Sort**: This is a simple sorting algorithm that involves iterating through the data structure, and inserting each element into its correct position in the sorted list.

2. **Selection Sort**: This is a simple sorting algorithm that involves iterating through the data structure, finding the smallest element, and swapping it with the first element. This process is repeated for the remaining elements.

3. **Bubble Sort**: This is a simple sorting algorithm that involves repeatedly iterating through the data structure, comparing adjacent elements, and swapping them if they are in the wrong order.

4. **Quick Sort**: This is an efficient sorting algorithm that involves selecting a pivot element, partitioning the data around the pivot, and recursively sorting the partitions.

5. **Merge Sort**: This is an efficient sorting algorithm that involves dividing the data into two halves, recursively sorting the halves, and merging the sorted halves.

6. **Heap Sort**: This is an efficient sorting algorithm that involves building a heap data structure from the data, and repeatedly extracting the maximum element from the heap and inserting it into the sorted list.

7. **Radix Sort**: This is a non-comparison based sorting algorithm that involves sorting the data based on the individual digits of the data elements.
