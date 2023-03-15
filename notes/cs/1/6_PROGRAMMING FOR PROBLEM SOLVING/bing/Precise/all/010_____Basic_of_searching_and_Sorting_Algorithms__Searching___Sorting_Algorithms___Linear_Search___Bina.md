# Basic of Searching and Sorting Algorithms: Searching & Sorting Algorithms (Linear Search, Binary Search, Bubble Sort, Insertion and Selection Sort)

## Searching Algorithms

### Linear Search
- Linear search is the simplest search algorithm.
- It works by iterating through an array or list of elements, comparing each element to the search key.
- If the element is equal to the search key, the index of the element is returned.
- If the search key is not found in the array or list, the algorithm returns -1.
- The time complexity of linear search is O(n), where n is the number of elements in the array or list.

### Binary Search
- Binary search is an efficient search algorithm that works on sorted arrays or lists.
- It works by repeatedly dividing the search interval in half.
- If the search key is less than the middle element of the interval, the search continues in the lower half of the interval.
- If the search key is greater than the middle element, the search continues in the upper half of the interval.
- If the search key is equal to the middle element, the index of the element is returned.
- If the search key is not found in the array or list, the algorithm returns -1.
- The time complexity of binary search is O(log n), where n is the number of elements in the array or list.

## Sorting Algorithms

### Bubble Sort
- Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
- The algorithm continues until no more swaps are needed, indicating that the array or list is sorted.
- The time complexity of bubble sort is O(n^2), where n is the number of elements in the array or list.

### Insertion Sort
- Insertion sort is a simple sorting algorithm that works by building the final sorted array or list one item at a time.
- It works by iterating through the array or list, and for each element, the algorithm moves it to its correct position in the sorted array or list by repeatedly swapping it with the preceding element until it is in the correct position.
- The time complexity of insertion sort is O(n^2), where n is the number of elements in the array or list.

### Selection Sort
- Selection sort is a simple sorting algorithm that works by repeatedly selecting the minimum element from the unsorted part of the array or list and swapping it with the first element of the unsorted part.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the array or list.