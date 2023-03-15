### Unit 3 - Searching and Sorting

#### Concept of Searching
Searching is the process of finding a specific element or value in a data structure. There are several algorithms that can be used to search for an element in a data structure, including sequential search, index sequential search, and binary search.

- **Sequential search**: This is the simplest search algorithm, where the search starts at the first element and checks each element in the data structure until the desired element is found or the end of the data structure is reached.

- **Index Sequential Search**: This search algorithm is similar to sequential search, but it uses an index to speed up the search process. The index contains a list of key values and their corresponding locations in the data structure. The search starts by looking up the desired key value in the index, and then searching the data structure starting at the location specified in the index.

- **Binary Search**: This search algorithm is used on sorted data structures. It starts by comparing the desired key value to the middle element of the data structure. If the desired key value is less than the middle element, the search continues on the left half of the data structure. If the desired key value is greater than the middle element, the search continues on the right half of the data structure. This process is repeated until the desired element is found or it is determined that the element is not in the data structure.

#### Concept of Hashing & Collision resolution Techniques used in Hashing
Hashing is a technique used to map a large set of data to a smaller set of data, called the hash table. The hash function is used to map the data to the hash table. When two or more data elements are mapped to the same location in the hash table, a collision occurs. There are several techniques that can be used to resolve collisions, including chaining, open addressing, and double hashing.

- **Chaining**: In this technique, each location in the hash table contains a linked list of elements that are mapped to that location. When a collision occurs, the new element is added to the linked list.

- **Open Addressing**: In this technique, when a collision occurs, the algorithm searches for the next available location in the hash table to store the new element.

- **Double Hashing**: In this technique, a second hash function is used to determine the distance to the next available location in the hash table when a collision occurs.

#### Sorting
Sorting is the process of arranging a set of data in a specific order. There are several sorting algorithms, including insertion sort, selection sort, bubble sort, quick sort, merge sort, heap sort, and radix sort.

- **Insertion Sort**: This sorting algorithm works by inserting each element into its correct position in the sorted list.

- **Selection Sort**: This sorting algorithm works by selecting the smallest element from the unsorted list and swapping it with the first element of the unsorted list.

- **Bubble Sort**: This sorting algorithm works by repeatedly swapping adjacent elements if they are in the wrong order.

- **Quick Sort**: This sorting algorithm works by selecting a pivot element and partitioning the data around the pivot, such that elements less than the pivot are on the left and elements greater than the pivot are on the right. The algorithm then recursively sorts the left and right partitions.

- **Merge Sort**: This sorting algorithm works by dividing the data into two halves, sorting each half, and then merging the two sorted halves.

- **Heap Sort**: This sorting algorithm works by building a heap data structure from the data and then repeatedly extracting the maximum element from the heap and inserting it into the sorted list.

- **Radix Sort**: This sorting algorithm works by sorting the data based on the individual digits of the data, starting with the least significant digit and moving to the most significant digit.