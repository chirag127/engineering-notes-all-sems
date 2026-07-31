# Unit 3 - Searching and Sorting

## Sorting

Sorting is the process of arranging a set of items in a specific order. The order can be numerical, lexicographical, or any user-defined order. There are several sorting algorithms, each with its own advantages and disadvantages. Here are some of the most commonly used sorting algorithms:

### Insertion Sort

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

The algorithm iterates over the list and removes one element per iteration, finds the location within the sorted part of the list where it belongs, and inserts it there. It repeats until no input elements remain.

### Selection Sort

Selection sort is a simple sorting algorithm that works by dividing the input into two parts: the sorted part and the unsorted part. The algorithm iterates over the unsorted part and finds the smallest element, then swaps it with the first element of the unsorted part. It repeats until the unsorted part is empty.

### Bubble Sort

Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order. The algorithm gets its name from the way smaller elements "bubble" to the top of the list.

### Quick Sort

Quick sort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

### Merge Sort

Merge sort is a divide-and-conquer sorting algorithm that works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.

### Heap Sort

Heap sort is a comparison-based sorting algorithm that works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region.

### Radix Sort

Radix sort is a non-comparative sorting algorithm that works by sorting data with integer keys by grouping the keys by the individual digits which share the same significant position and value.

## Searching

Searching is the process of finding a specific item in a collection of items. There are several searching algorithms, each with its own advantages and disadvantages. Here are some of the most commonly used searching algorithms:

### Sequential Search

Sequential search is a simple searching algorithm that works by iterating over the list and checking each element until the desired element is found.

### Index Sequential Search

Index sequential search is a searching algorithm that works by creating an index for the list and using it to speed up the search process.

### Binary Search

Binary search is a searching algorithm that works by repeatedly dividing the search interval in half. If the value of the search key is less than the item in the middle of the interval, the algorithm narrows the interval to the lower half. Otherwise, it narrows it to the upper half. The algorithm repeats until the value is found or the interval is empty.

### Concept of Hashing

Hashing is the process of mapping data of arbitrary size to data of a fixed size. The values returned by a hash function are called hash values, hash codes, or simply hashes.

### Collision Resolution Techniques used in Hashing

Collision resolution is the process of handling situations where two or more keys hash to the same index in a hash table. Some common collision resolution techniques include chaining, open addressing, and coalesced hashing.
