### Concept of Searching

Searching is a fundamental operation in computer science and is used to find specific data elements in a collection of data. There are several searching algorithms available, which can be broadly categorized into two types: linear search and binary search.

#### Sequential search
- Sequential search is a simple searching algorithm that works by sequentially checking each element in a collection until a match is found.
- It has a time complexity of O(n), where n is the number of elements in the collection.
- It is not suitable for large collections as it takes a long time to search for an element.

#### Index Sequential Search
- Index Sequential Search is an improvement over the sequential search algorithm.
- It involves dividing the collection into blocks or pages and creating an index of the starting position of each block or page.
- The algorithm first searches the index to find the block or page where the element is likely to be located and then performs a sequential search within that block or page.
- It has a time complexity of O(sqrt(n)).

#### Binary Search
- Binary search is a more efficient searching algorithm that works by repeatedly dividing the collection in half until the element is found.
- It has a time complexity of O(log n), which makes it suitable for large collections.
- The collection must be sorted in ascending or descending order for binary search to work.

### Concept of Hashing

Hashing is a technique used to efficiently store and retrieve data in a collection. It involves converting the data into an index or key using a hash function and then storing the data in an array at the index corresponding to the key.

#### Collision Resolution Techniques used in Hashing
- Collision occurs when two or more keys map to the same index in the array.
- There are several techniques used to resolve collisions in hashing, including chaining and open addressing.
- Chaining involves storing the data in linked lists at the index corresponding to the key.
- Open addressing involves finding the next available index in the array to store the data when a collision occurs.

### Sorting

Sorting is the process of arranging data in a specific order, such as ascending or descending order. There are several sorting algorithms available, which can be broadly categorized into two types: comparison-based sorting and non-comparison-based sorting.

#### Insertion Sort
- Insertion sort is a simple sorting algorithm that works by repeatedly inserting each element in the collection into its correct position in the sorted sub-collection.
- It has a time complexity of O(n^2), which makes it suitable for small collections.

#### Selection Sort
- Selection sort is a sorting algorithm that works by repeatedly selecting the smallest element in the unsorted sub-collection and swapping it with the first element in the sub-collection.
- It has a time complexity of O(n^2), which makes it suitable for small collections.

#### Bubble Sort
- Bubble sort is a sorting algorithm that works by repeatedly swapping adjacent elements in the collection if they are in the wrong order.
- It has a time complexity of O(n^2), which makes it suitable for small collections.

#### Quick Sort
- Quick sort is a comparison-based sorting algorithm that works by dividing the collection into two sub-collections, one with elements smaller than a pivot element and the other with elements larger than the pivot element.
- It has a time complexity of O(n log n), which makes it suitable for large collections.

#### Merge Sort
- Merge sort is a comparison-based sorting algorithm that works by dividing the collection into two halves, sorting each half recursively, and then merging the two halves together.
- It has a time complexity of O(n log n), which makes it suitable for large collections.

#### Heap Sort
- Heap sort is a comparison-based sorting algorithm that works by creating a binary heap from the collection and repeatedly extracting the largest element from the heap and placing it at the end of the collection.
- It has a time complexity of O(n log n), which makes it suitable for large collections.

#### Radix Sort
- Radix sort is a non-comparison-based sorting algorithm that works by sorting the collection based on the individual digits or characters in the elements.
- It has a time complexity of O(dn), where d is the number of digits or characters in the elements, which makes it suitable for large collections with small values.