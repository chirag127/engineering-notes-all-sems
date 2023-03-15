### Unit 3 - Searching and Sorting

#### Searching
- **Concept of Searching**: Searching refers to the process of finding a specific element or value in a data structure or a collection of data.
- **Sequential search**: A sequential search is a method of searching where the search starts at the beginning of the list and continues until the desired element is found or the end of the list is reached.
- **Index Sequential Search**: Index sequential search is a search method that uses an index to speed up the search process. The index contains key values and pointers to the location of the data in the data structure.
- **Binary Search**: Binary search is a search algorithm that works by repeatedly dividing the search interval in half. The search begins by comparing the middle element of the array with the target value. If the target value matches the middle element, its position in the array is returned. If the target value is less than the middle element, the search continues in the lower half of the array. If the target value is greater than the middle element, the search continues in the upper half of the array.
- **Concept of Hashing**: Hashing is a technique used to map data of arbitrary size to data of fixed size. The values returned by a hash function are called hash values, hash codes, or simply hashes.
- **Collision resolution Techniques used in Hashing**: Collision resolution techniques are used to handle situations where two or more keys hash to the same index in the hash table. Some common collision resolution techniques include chaining, open addressing, and double hashing.

#### Sorting
- **Insertion Sort**: Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
- **Selection Sort**: Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part.
- **Bubble Sort**: Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
- **Quick Sort**: Quick sort is an efficient sorting algorithm that uses the divide and conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot.
- **Merge Sort**: Merge sort is an efficient, general-purpose, comparison-based sorting algorithm. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining.
- **Heap Sort**: Heap sort is a comparison-based sorting algorithm that works by dividing the input into a sorted and an unsorted region, and iteratively shrinking the unsorted region by extracting the largest element and moving that to the sorted region.
- **Radix Sort**: Radix sort is a non-comparative sorting algorithm that sorts data with integer keys by grouping the keys by the individual digits which share the same significant position and value.
