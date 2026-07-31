### Binary Search

Binary search algorithm is a commonly used searching algorithm that works efficiently on sorted arrays. The algorithm works by repeatedly dividing the search interval in half until the desired value is found or until the interval becomes empty. 

The binary search algorithm has the following steps:

1. Compare the target value with the middle element of the array.
2. If the target value matches the middle element, return the index of the middle element.
3. If the target value is less than the middle element, narrow the search to the lower half of the array.
4. If the target value is greater than the middle element, narrow the search to the upper half of the array.
5. Repeat steps 1-4 until the target value is found or the search interval becomes empty.

Binary search has a time complexity of O(log N), which is much faster than sequential search for large arrays.

### Sorting

Sorting is the process of arranging data in a particular order, typically in ascending or descending order. There are many sorting algorithms available, each with its own advantages and disadvantages.

#### Insertion Sort

Insertion sort is a simple sorting algorithm that works by repeatedly inserting the next element into its correct position in the already sorted part of the array. The algorithm has a time complexity of O(N^2).

#### Selection Sort

Selection sort works by repeatedly selecting the smallest element from the unsorted part of the array and placing it at the beginning of the sorted part. The algorithm has a time complexity of O(N^2).

#### Bubble Sort

Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order. The algorithm has a time complexity of O(N^2).

#### Quick Sort

Quick sort is a divide-and-conquer algorithm that works by selecting a pivot element and partitioning the array into two sub-arrays, one with elements smaller than the pivot and one with elements larger than the pivot. The algorithm then recursively sorts the sub-arrays. The average case time complexity is O(N log N), but the worst case is O(N^2).

#### Merge Sort

Merge sort is a divide-and-conquer algorithm that works by dividing the array into two halves, sorting each half, and then merging the two sorted halves. The algorithm has a time complexity of O(N log N).

#### Heap Sort

Heap sort works by building a binary heap from the array and repeatedly extracting the maximum element from the heap until the array is sorted. The algorithm has a time complexity of O(N log N).

#### Radix Sort

Radix sort works by sorting the elements by their individual digits or bits. The algorithm has a time complexity of O(NK), where K is the maximum number of digits or bits in the elements.

### Hashing

Hashing is a technique for storing and retrieving data in a hash table using a hash function. A hash function maps a key to an index in the hash table, where the corresponding value is stored. 

#### Collision Resolution Techniques

Collision resolution techniques are used to handle cases where two or more keys map to the same index in the hash table. There are several collision resolution techniques available, including:

- Linear Probing: If a collision occurs, the algorithm searches for the next available slot in the hash table.
- Quadratic Probing: If a collision occurs, the algorithm searches for the next available slot using a quadratic function.
- Chaining: If a collision occurs, the algorithm stores the values in a linked list at the index in the hash table.

Overall, understanding the various searching and sorting algorithms, as well as hashing and collision resolution techniques, is essential for building efficient and effective data structures.