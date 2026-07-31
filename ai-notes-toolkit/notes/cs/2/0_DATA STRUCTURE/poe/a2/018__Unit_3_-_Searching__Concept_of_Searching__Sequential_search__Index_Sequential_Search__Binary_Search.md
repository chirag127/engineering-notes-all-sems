 Here is the formal content in Markdown format without any emojis or external links:

## Unit 3 - Searching: Concept of Searching, Sequential search, Index Sequential Search, Binary Search. Concept of Hashing & Collision resolution Techniques used in Hashing. Sorting: Insertion Sort, Selection, Bubble Sort, Quick Sort, Merge Sort, Heap Sort and Radix Sort.

Searching:
- Concept of Searching: The process of retrieving required data/information from a collection of data/information.
- Sequential Search: The simplest search technique. Searches one by one in the given data until the desired data is found. Time complexity is O(n).
- Index Sequential Search: Maintains an index of data. The index is searched first to get the actual location of data. If data is not found in index, sequential search is performed.
- Binary Search: Effective on sorted data. Divides the array into two halves and checks which half contains the data. The process continues on the selected half. Time complexity is O(log n).

Hashing:
- Concept of Hashing: A technique to convert a range of key values into indexes of an array.
- Collision Resolution Techniques: Methods to handle collisions when two keys map to the same index:
-- Open Addressing: Probing (linear and quadratic), double hashing.
-- Chaining: Separate chaining, open hashing.

Sorting:
- Insertion Sort: Builds the final sorted array one item at a time. Inefficient for large data sets.
- Selection Sort: Finds the minimum element and places it at the beginning. Repeats the process for the remaining elements.
- Bubble Sort: Compares adjacent elements and swaps them if out of order. Repeats the process until the list is sorted.
- Quick Sort: Picks a pivot element and partitions the array into two subarrays - elements less than pivot and elements greater than pivot. Applies the process recursively on the subarrays.
- Merge Sort: Divides the array into two halves, sorts them recursively and merges them.
- Heap Sort: Builds a max heap of the array and then extracts the max element repeatedly.
- Radix Sort: Does stable sorting by distributing input among buckets according to digit values.