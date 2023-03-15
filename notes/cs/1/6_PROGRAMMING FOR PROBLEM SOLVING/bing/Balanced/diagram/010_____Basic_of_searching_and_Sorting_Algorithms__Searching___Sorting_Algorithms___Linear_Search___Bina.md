### Basic of searching and sorting algorithms

Searching and sorting algorithms are common algorithms that are used to manipulate data in various ways. They are often used in coding interviews and exams to test the understanding and implementation of different data structures and algorithms.

#### Searching algorithms

Searching algorithms are designed to check for an element or retrieve an element from any data structure where it is stored. Based on the type of operations, these algorithms are generally classified into two categories:

- Sequential search: In this, the list or array is traversed sequentially and every element is checked. For example, linear search is a sequential search algorithm that compares the target element with each element of the list until a match is found or the list is exhausted.
- Interval search: In this, the list or array is divided into smaller segments based on some condition and the search is carried out in the selected segment. For example, binary search is an interval search algorithm that works on a sorted array and repeatedly divides the array into two halves until the target element is found or the array is empty.

#### Sorting algorithms

Sorting algorithms are used to rearrange a given array or list of elements according to a comparison operator on the elements. The comparison operator is used to decide the new order of the elements in the respective data structures. Some of the common sorting algorithms are:

- Bubble sort: This is a simple sorting algorithm that repeatedly swaps the adjacent elements if they are in wrong order. It has a time complexity of O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the array.
- Insertion sort: This is a sorting algorithm that builds the final sorted array one item at a time. It iterates over the array and inserts each element into its correct position in the sorted subarray. It has a time complexity of O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the array.
- Selection sort: This is a sorting algorithm that selects the smallest element from the unsorted subarray and places it at the beginning of the subarray. It repeats this process until the entire array is sorted. It has a time complexity of O(n^2) in the worst and average cases, where n is the number of elements in the array.

#### Diagram

The following diagram illustrates the working of linear search, binary search, bubble sort, insertion sort and selection sort on an example array of 10 elements:

![Diagram of searching and sorting algorithms](https://i.imgur.com/0w6Za1i.png)