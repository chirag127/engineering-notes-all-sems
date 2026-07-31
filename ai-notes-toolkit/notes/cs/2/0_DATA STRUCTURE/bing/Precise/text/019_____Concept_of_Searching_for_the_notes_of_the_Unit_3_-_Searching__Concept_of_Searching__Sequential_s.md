### Unit 3 - Searching and Sorting

#### Concept of Searching
Searching is the process of finding a specific element or value in a data structure. There are several algorithms that can be used to search for an element in a data structure, including sequential search, index sequential search, and binary search.

- **Sequential search**: This is the simplest search algorithm, where the search starts at the first element of the data structure and continues until the desired element is found or the end of the data structure is reached.

- **Index Sequential Search**: This search algorithm is similar to sequential search, but it uses an index to speed up the search process. The index is a data structure that stores the keys of the elements in the data structure, along with their positions. The search starts by looking up the desired key in the index, and then the search continues in the data structure from the position indicated by the index.

- **Binary Search**: This search algorithm is used on sorted data structures. It works by repeatedly dividing the data structure in half and checking if the desired element is in the left or right half. The search continues in the half where the element could be until it is found or it is determined that the element is not in the data structure.

#### Concept of Hashing & Collision resolution Techniques used in Hashing
Hashing is a technique used to map keys to values in a data structure called a hash table. A hash function is used to compute an index into the hash table for each key. Since different keys can map to the same index, collisions can occur. There are several techniques to resolve collisions in a hash table, including chaining, open addressing, and double hashing.

- **Chaining**: In this technique, each element of the hash table is a linked list. When a collision occurs, the new key-value pair is added to the linked list at the corresponding index.

- **Open Addressing**: In this technique, when a collision occurs, the algorithm looks for the next available slot in the hash table to store the key-value pair. There are several methods to determine the next available slot, including linear probing, quadratic probing, and double hashing.

- **Double Hashing**: This technique uses a second hash function to compute the step size for probing the hash table when a collision occurs. The step size is the distance between the slots that are checked when looking for an available slot.

#### Sorting
Sorting is the process of arranging the elements of a data structure in a specific order. There are several sorting algorithms, including insertion sort, selection sort, bubble sort, quick sort, merge sort, heap sort, and radix sort.

- **Insertion Sort**: This sorting algorithm works by iterating through the data structure and inserting each element into its correct position in the sorted list.

- **Selection Sort**: This sorting algorithm works by iterating through the data structure and selecting the smallest element and swapping it with the first element. The process is repeated for the remaining elements.

- **Bubble Sort**: This sorting algorithm works by repeatedly iterating through the data structure and swapping adjacent elements if they are in the wrong order.

- **Quick Sort**: This sorting algorithm works by selecting a pivot element and partitioning the data structure around the pivot, such that elements less than the pivot are on the left and elements greater than the pivot are on the right. The process is then repeated for the left and right partitions.

- **Merge Sort**: This sorting algorithm works by dividing the data structure into two halves, sorting each half, and then merging the two sorted halves back together.

- **Heap Sort**: This sorting algorithm works by building a heap data structure from the elements of the data structure and then repeatedly extracting the maximum element from the heap and inserting it at the end of the sorted list.

- **Radix Sort**: This sorting algorithm works by sorting the elements based on their individual digits or characters. The process is repeated for each digit or character position, starting from the least significant position.
