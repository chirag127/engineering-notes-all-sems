# Unit 3 - Searching and Sorting Algorithms

## Concept of Searching
Searching is the process of finding an element or a value in a data structure, such as an array or a list. Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Based on the type of operations, these algorithms are generally classified into two categories:

- Sequential Search: In this, the data structure is traversed sequentially and every element is checked. For example, linear search and interpolation search are sequential search algorithms.
- Interval Search: In this, the data structure is divided into smaller substructures and the search is performed in a specific interval. For example, binary search and exponential search are interval search algorithms.

## Concept of Hashing and Collision Resolution Techniques
Hashing is a technique of mapping a large set of data items to a smaller set of data items, called hash table, using a function called hash function. The hash function maps each data item to a unique index, called hash code or hash value, in the hash table. Hashing is useful for fast and efficient search and insertion operations.

However, sometimes two or more data items may have the same hash code, which is called a collision. Collision reduces the performance of hashing and may cause data loss. Therefore, collision resolution techniques are used to handle the collisions and store the data items properly in the hash table. Some of the common collision resolution techniques are:

- Linear Probing: In this, the next available slot in the hash table is used to store the data item that causes collision.
- Quadratic Probing: In this, a quadratic function is used to calculate the next available slot in the hash table for the data item that causes collision.
- Chaining: In this, each slot in the hash table is a linked list of data items that have the same hash code. The data item that causes collision is added to the end of the linked list.

## Concept of Sorting
Sorting is the process of arranging a set of data items in a specific order, such as ascending or descending order. Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of the elements in the respective data structures. Sorting algorithms are important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted order.

Some of the common sorting algorithms are:

- Insertion Sort: In this, the array is divided into two parts: sorted and unsorted. The first element is considered as sorted and the rest as unsorted. The unsorted element is inserted into the correct position in the sorted part by shifting the larger elements to the right.
- Selection Sort: In this, the array is divided into two parts: sorted and unsorted. The smallest element in the unsorted part is selected and swapped with the leftmost element in the unsorted part. The sorted part is extended by one element and the unsorted part is reduced by one element.
- Bubble Sort: In this, the array is traversed from left to right and the adjacent elements are compared and swapped if they are in the wrong order. This process is repeated until no swaps are required, which means the array is sorted.
- Quick Sort: In this, a pivot element is chosen from the array and the array is partitioned into two subarrays: one with elements smaller than the pivot and one with elements larger than the pivot. The subarrays are then sorted recursively using the same algorithm.
- Merge Sort: In this, the array is divided into two halves and each half is sorted recursively using the same algorithm. The sorted halves are then merged together by comparing and merging the elements in order.
- Heap Sort: In this, the array is converted into a binary heap data structure, which is a complete binary tree that satisfies the heap property. The heap property means that the parent node is either greater than or equal to (max-heap) or less than or equal to (min-heap) its child nodes. The root node of the heap is the largest (max-heap) or the smallest (min-heap) element in the array. The root node is removed from the heap and placed at the end of the array. The heap is then adjusted to maintain the heap property and the process is repeated until the heap is empty and the array is sorted.
- Radix Sort: In this, the array is sorted based on the individual digits of the elements, starting from the least significant digit to the most significant digit. The elements