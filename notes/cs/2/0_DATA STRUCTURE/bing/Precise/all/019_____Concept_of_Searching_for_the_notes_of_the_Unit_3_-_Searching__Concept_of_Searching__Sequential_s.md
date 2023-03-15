# Unit 3 - Searching and Sorting

## Concept of Searching
Searching is the process of finding a specific element or value in a data structure. There are several algorithms that can be used to search for an element in a data structure, including sequential search, index sequential search, and binary search.

### Sequential Search
Sequential search, also known as linear search, is a simple search algorithm that involves iterating through each element in a data structure until the desired element is found. This algorithm has a time complexity of O(n), where n is the number of elements in the data structure.

### Index Sequential Search
Index sequential search is a search algorithm that involves creating an index for the data structure to improve the efficiency of the search. The index is typically created by dividing the data structure into smaller sections and storing the key values of the first element in each section. This allows the algorithm to quickly determine which section the desired element is likely to be in, reducing the number of elements that need to be searched. The time complexity of this algorithm depends on the size of the index and the data structure.

### Binary Search
Binary search is a search algorithm that involves repeatedly dividing the data structure in half until the desired element is found. This algorithm is only effective on sorted data structures and has a time complexity of O(log n), where n is the number of elements in the data structure.

## Concept of Hashing
Hashing is a technique used to map data to a fixed-size table, known as a hash table. This is done by using a hash function to generate an index for each element based on its key value. Hashing can be used to improve the efficiency of search and retrieval operations.

### Collision Resolution Techniques
When multiple elements are mapped to the same index in a hash table, a collision occurs. There are several techniques that can be used to resolve collisions, including chaining, open addressing, and double hashing.

## Sorting
Sorting is the process of arranging data in a specific order. There are several algorithms that can be used to sort data, including insertion sort, selection sort, bubble sort, quick sort, merge sort, heap sort, and radix sort.

### Insertion Sort
Insertion sort is a simple sorting algorithm that involves iterating through each element in the data structure and inserting it into its correct position in the sorted list. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

### Selection Sort
Selection sort is a sorting algorithm that involves iterating through each element in the data structure and selecting the smallest element to swap with the current element. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

### Bubble Sort
Bubble sort is a simple sorting algorithm that involves repeatedly swapping adjacent elements if they are in the wrong order. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

### Quick Sort
Quick sort is a sorting algorithm that involves selecting a pivot element and partitioning the data structure around the pivot, such that elements less than the pivot are on one side and elements greater than the pivot are on the other. This process is then repeated on the two partitions until the data structure is sorted. The time complexity of this algorithm is O(n log n) on average, where n is the number of elements in the data structure.

### Merge Sort
Merge sort is a sorting algorithm that involves dividing the data structure into two smaller sub-arrays, sorting each sub-array, and then merging the two sorted sub-arrays back together. This algorithm has a time complexity of O(n log n), where n is the number of elements in the data structure.

### Heap Sort
Heap sort is a sorting algorithm that involves building a binary heap from the data structure and then repeatedly removing the maximum element from the heap and inserting it into the sorted list. This algorithm has a time complexity of O(n log n), where n is the number of elements in the data structure.

### Radix Sort
Radix sort is a sorting algorithm that involves sorting data by the individual digits or letters of the key values. This algorithm has a time complexity of O(nk), where n is the number of elements in the data structure and k is the maximum number of digits or letters in the key values.