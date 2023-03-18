## Unit 3 - Searching and Sorting

In this unit, we will discuss the various searching and sorting techniques used in computer science. These techniques are fundamental to many algorithms and data structures, and are essential for efficient and effective programming.

### Searching Techniques

#### Concept of Searching

- Searching is the process of finding a particular item or element within a given data structure.
- The efficiency of a search algorithm is measured by its time complexity, which is determined by the number of operations required to perform the search.

#### Sequential Search

- Sequential search, also known as linear search, is a simple search algorithm that checks each element in a data structure in sequence until the desired element is found.
- The time complexity of sequential search is O(n), where n is the number of elements in the data structure.

#### Index Sequential Search

- Index sequential search is an improvement upon sequential search that uses an index to speed up the search process.
- The index is a data structure that contains pointers to blocks of elements in the data structure, allowing for faster access to elements.
- The time complexity of index sequential search is O(log n), where n is the number of elements in the data structure.

#### Binary Search

- Binary search is a search algorithm that works by repeatedly dividing the search interval in half.
- It requires that the data structure is sorted in ascending or descending order.
- The time complexity of binary search is O(log n), where n is the number of elements in the data structure.

#### Concept of Hashing

- Hashing is a technique used to map large amounts of data to smaller, fixed-size data structures.
- A hash function is used to generate a unique key for each element in the data structure.
- Hashing is used to improve the efficiency of searching by reducing the search space.

#### Collision Resolution Techniques used in Hashing

- Collision resolution is the process of handling situations where two or more elements are mapped to the same hash key.
- There are several collision resolution techniques, including chaining, open addressing, and coalesced hashing.

### Sorting Techniques

#### Insertion Sort

- Insertion sort is a simple sorting algorithm that works by repeatedly inserting an element into a sorted sublist until all elements are sorted.
- The time complexity of insertion sort is O(n^2), where n is the number of elements in the data structure.

#### Selection Sort

- Selection sort is a sorting algorithm that works by repeatedly selecting the smallest element from the unsorted portion of the data structure and swapping it with the first element of the unsorted portion.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the data structure.

#### Bubble Sort

- Bubble sort is a sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
- The time complexity of bubble sort is O(n^2), where n is the number of elements in the data structure.

#### Quick Sort

- Quick sort is a sorting algorithm that works by partitioning the data structure around a pivot element and recursively sorting the sublists on either side of the pivot.
- The time complexity of quick sort is O(n log n), where n is the number of elements in the data structure.

#### Merge Sort

- Merge sort is a sorting algorithm that works by recursively dividing the data structure in half, sorting the sublists, and merging them back together.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the data structure.

#### Heap Sort

- Heap sort is a sorting algorithm that works by building a heap data structure and repeatedly removing the largest element until all elements are sorted.
- The time complexity of heap sort is O(n log n), where n is the number of elements in the data structure.

#### Radix Sort

- Radix sort is a sorting algorithm that works by sorting elements based on their digits or characters.
- It can be used to sort integers, strings, and other data types.
- The time complexity of radix sort is O(nk), where n is the number of elements in the data structure and k is the maximum number of digits or characters in the elements.