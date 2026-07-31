### Basic of Searching and Sorting Algorithms

Searching and sorting algorithms are fundamental techniques for manipulating data in a computer. Searching algorithms are used to find a specific element or a set of elements that satisfy some criteria in a collection of data. Sorting algorithms are used to arrange the elements of a collection in a specific order, such as ascending, descending, alphabetical, etc.

Some of the common searching and sorting algorithms are:

- Linear Search: This is the simplest searching algorithm that iterates over each element of a collection from left to right and compares it with the target element. If a match is found, the algorithm returns the index of the element. If no match is found, the algorithm returns -1. The time complexity of linear search is O(n), where n is the number of elements in the collection.

- Binary Search: This is a more efficient searching algorithm that works on a sorted collection of data. It divides the collection into two halves and compares the middle element with the target element. If they are equal, the algorithm returns the index of the element. If the target element is smaller than the middle element, the algorithm repeats the process on the left half of the collection. If the target element is larger than the middle element, the algorithm repeats the process on the right half of the collection. The algorithm terminates when either a match is found or the collection becomes empty. The time complexity of binary search is O(log n), where n is the number of elements in the collection.

- Bubble Sort: This is a simple sorting algorithm that repeatedly swaps adjacent elements of a collection if they are in the wrong order. The algorithm passes over the collection until no swaps are needed, which means the collection is sorted. The time complexity of bubble sort is O(n^2), where n is the number of elements in the collection.

- Insertion Sort: This is another simple sorting algorithm that builds the sorted collection one element at a time. The algorithm iterates over each element of the collection and inserts it into its correct position in the sorted collection. The time complexity of insertion sort is O(n^2), where n is the number of elements in the collection.

- Selection Sort: This is a sorting algorithm that selects the smallest (or largest) element of the collection and swaps it with the first (or last) element of the collection. The algorithm repeats this process for the remaining elements of the collection until the collection is sorted. The time complexity of selection sort is O(n^2), where n is the number of elements in the collection.