### Sequential Search

Sequential search is a simple searching algorithm used to find a particular element in a list or an array. It is also known as linear search. It works by sequentially checking each element of the array until a match is found or the end of the array is reached.

#### Steps involved in sequential search algorithm:

1. Start from the first element of the array.
2. Compare the target element with the current element of the array.
3. If the elements match, return the index of the current element.
4. If the elements do not match, move to the next element of the array.
5. Repeat steps 2 to 4 until a match is found or the end of the array is reached.

#### Advantages of Sequential search:

- It is simple and easy to implement.
- It works with unsorted arrays as well.
- It is efficient for small arrays.

#### Disadvantages of Sequential search:

- It has a time complexity of O(n) which makes it inefficient for large arrays.
- It is not suitable for sorted arrays as the elements can be searched more efficiently using binary search.

### Index Sequential Search

Index Sequential Search is an optimization of the sequential search algorithm. It works by dividing the list into blocks of fixed size and creating an index for each block. The index contains the starting position of each block and the maximum value in the block. This allows for faster searching by reducing the number of comparisons required.

#### Steps involved in Index Sequential search algorithm:

1. Divide the list into blocks of fixed size.
2. Create an index for each block containing the starting position and the maximum value in the block.
3. Search the index to determine which block the target element is in.
4. Perform a sequential search within the block to find the target element.

#### Advantages of Index Sequential Search:

- It is faster than the sequential search algorithm.
- It works well with large arrays.
- It is suitable for both sorted and unsorted arrays.

#### Disadvantages of Index Sequential Search:

- It requires extra memory to store the index.
- It has a higher overhead cost than the sequential search algorithm.

### Binary Search

Binary search is a more efficient search algorithm than sequential search. It works by dividing the array into two halves and eliminating one half of the array based on the comparison of the target element with the middle element of the array. This process is repeated until the target element is found or the array is exhausted.

#### Steps involved in Binary search algorithm:

1. Start with the middle element of the array.
2. Compare the target element with the middle element of the array.
3. If the target element is equal to the middle element, return the index of the middle element.
4. If the target element is less than the middle element, search the left half of the array.
5. If the target element is greater than the middle element, search the right half of the array.
6. Repeat steps 2 to 5 until the target element is found or the array is exhausted.

#### Advantages of Binary search:

- It has a time complexity of O(log n) which makes it efficient for large arrays.
- It works well with sorted arrays.

#### Disadvantages of Binary search:

- It requires a sorted array for efficient searching.
- It is not suitable for small arrays.

### Concept of Hashing

Hashing is a technique used to store and retrieve data quickly. It works by mapping a large data set to a smaller data set using a hash function. The hash function converts the key of each data element into a unique index value which is used to store the data element in an array.

### Collision Resolution Techniques used in Hashing

Collision occurs when two or more data elements have the same hash value. Collision resolution techniques are used to resolve this issue. Some of the commonly used collision resolution techniques are:

#### 1. Open Addressing

In open addressing, the collision is resolved by searching for an empty slot in the hash table and storing the data element in that slot. There are three types of open addressing:

- Linear Probing
- Quadratic Probing
- Double Hashing

#### 2. Chaining

In chaining, the collision is resolved by storing the data elements with the same hash value in a linked list at the corresponding index of the hash table.

### Sorting

Sorting is the process of arranging a list of elements in a specific order. It is an important operation in data structures as it helps in efficient searching and retrieval of data. Some of the commonly used sorting algorithms are:

#### 1. Insertion Sort

Insertion Sort works by iterating through the list and inserting each element into its correct position in the sorted list.

#### 2. Selection Sort

Selection Sort works by selecting the smallest element in the unsorted list and swapping it with the first element of the unsorted list.

#### 3. Bubble Sort

Bubble Sort works by comparing adjacent elements of the list and swapping them if they are in the wrong order.

#### 4. Quick Sort

Quick Sort works by