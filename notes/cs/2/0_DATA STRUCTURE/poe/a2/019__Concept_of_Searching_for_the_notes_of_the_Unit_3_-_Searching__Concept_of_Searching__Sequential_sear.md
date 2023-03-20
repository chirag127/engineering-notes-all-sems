 Here is the formal content in Markdown format without any feeling or friendliness:

### Concept of Searching for the notes of the Unit 3 - Searching:

- Concept of Searching: Searching is a technique to find the location of a particular data/element in a data structure. It involves traversing the data structure and comparing each element with the search key until a match is found.
- Sequential Search: It is a basic search technique. It involves traversing the data structure sequentially and comparing each element with the search key until a match is found. Time complexity is O(n).
- Index Sequential Search: It is similar to sequential search but with an additional array (index). The index array stores the locations of each element in the data structure. Time complexity is O(n+k) where k is the index location of the search key.
- Binary Search: It is a efficient search technique that works on sorted data structures. It divides the data structure in half and compares the middle element with the search key. If a match is found, the location is returned. If not, the half with the search key is identified and the process repeats. Time complexity is O(log n).

Concept of Hashing:
- Hashing is a technique to map a large set of input values into a smaller set of indexes of an array. A hash function is used to calculate an index from a key value.
- Collision Resolution Techniques used: Chaining, Open Addressing (Linear Probing, Quadratic Probing, Double Hashing).

Sorting:
- Insertion Sort: Sorts the data structure by gradually creating a larger left half which is always sorted. Time complexity is O(n^2).
- Selection Sort: Finds the minimum element and places it at the beginning. Repeats the process for the remaining elements. Time complexity is O(n^2).
- Bubble Sort: Compares adjacent elements and swaps them if out of order. Repeats the process until the data structure is sorted. Time complexity is O(n^2).
- Quick Sort: Picks an element as pivot and partitions the data structure into two halves - elements less than pivot and elements greater than pivot. Repeats the process recursively on the two halves. Time complexity is O(n log n).
- Merge Sort: Divides the data structure into halves until each subarray contains one element. The subarrays are then merged in a sorted order. Time complexity is O(n log n).
- Heap Sort: Converts the data structure into a max heap (or min heap) and extracts the maximum (or minimum) element, placing it at the end of the sorted array. Repeats the process until the heap is empty. Time complexity is O(n log n).
- Radix Sort: Does digit by digit sort starting from the least significant digit. Uses counting sort to sort the digits. Time complexity is O(wn) where w is the number of digits in the largest element.