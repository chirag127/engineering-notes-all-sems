### Unit 3 - Searching and Sorting

#### Concept of Searching
Searching is the process of finding a specific element or value in a data structure. There are several searching algorithms that can be used to find an element in a data structure, including sequential search, index sequential search, and binary search.

##### Sequential Search
Sequential search, also known as linear search, is a simple searching algorithm that involves iterating through each element in a data structure until the desired element is found. This algorithm has a time complexity of O(n), where n is the number of elements in the data structure.

##### Index Sequential Search
Index sequential search is a searching algorithm that involves creating an index for the data structure to improve the search time. The index is used to narrow down the search range, reducing the number of elements that need to be checked. This algorithm has a time complexity of O(log n), where n is the number of elements in the data structure.

##### Binary Search
Binary search is a searching algorithm that involves dividing the data structure in half and checking if the desired element is in the left or right half. This process is repeated until the desired element is found. This algorithm has a time complexity of O(log n), where n is the number of elements in the data structure.

#### Concept of Hashing & Collision Resolution Techniques
Hashing is a technique used to map data to a fixed-size table, called a hash table. The data is mapped using a hash function, which generates an index for the data. If two or more pieces of data generate the same index, a collision occurs. Collision resolution techniques are used to resolve these collisions, including chaining and open addressing.

#### Sorting
Sorting is the process of arranging data in a specific order. There are several sorting algorithms that can be used to sort data, including insertion sort, selection sort, bubble sort, quick sort, merge sort, heap sort, and radix sort.

##### Insertion Sort
Insertion sort is a simple sorting algorithm that involves iterating through the data and inserting each element into its correct position in the sorted list. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

##### Selection Sort
Selection sort is a sorting algorithm that involves finding the smallest element in the data structure and swapping it with the first element. This process is repeated until the entire data structure is sorted. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

##### Bubble Sort
Bubble sort is a sorting algorithm that involves comparing adjacent elements and swapping them if they are in the wrong order. This process is repeated until the entire data structure is sorted. This algorithm has a time complexity of O(n^2), where n is the number of elements in the data structure.

##### Quick Sort
Quick sort is a sorting algorithm that involves selecting a pivot element and partitioning the data around the pivot. The pivot is then placed in its correct position in the sorted list, and the process is repeated for the sublists on either side of the pivot. This algorithm has a time complexity of O(n log n), where n is the number of elements in the data structure.

##### Merge Sort
Merge sort is a sorting algorithm that involves dividing the data structure into two halves, sorting each half, and then merging the two halves back together. This algorithm has a time complexity of O(n log n), where n is the number of elements in the data structure.

##### Heap Sort
Heap sort is a sorting algorithm that involves building a binary heap from the data and then repeatedly removing the maximum element from the heap and inserting it into the sorted list. This algorithm has a time complexity of O(n log n), where n is the number of elements in the data structure.

##### Radix Sort
Radix sort is a sorting algorithm that involves sorting the data based on the individual digits of the elements. This algorithm has a time complexity of O(nk), where n is the number of elements in the data structure and k is the number of digits in the largest element.