### Sorting Algorithms-Non-Recursive

Sorting algorithms are a set of instructions that take an array or list as an input and arrange the items into a particular order. Sorts are most commonly in numerical or a form of alphabetical (called lexicographical) order, and can be in ascending (A-Z, 0-9) or descending (Z-A, 9-0) order.

A non-recursive sorting algorithm is one that does not use recursion to sort the input. Recursion is a technique where a function calls itself with a smaller or simpler input until a base case is reached. Recursion can be useful for breaking down complex problems into smaller subproblems, but it also has some drawbacks, such as extra memory usage and possible stack overflow.

Some examples of non-recursive sorting algorithms are:

- **Selection sort**: This algorithm finds the smallest (or largest) element in the array and swaps it with the first (or last) element, then repeats the process for the remaining subarray. The time complexity of this algorithm is O(n^2), where n is the number of elements in the array.
- **Insertion sort**: This algorithm iterates over the array and inserts each element into its correct position in the sorted subarray that precedes it. The time complexity of this algorithm is O(n^2) in the worst case, but it can be faster for nearly sorted arrays.
- **Bubble sort**: This algorithm compares adjacent pairs of elements in the array and swaps them if they are out of order, then repeats the process until no more swaps are needed. The time complexity of this algorithm is O(n^2) in the worst case, but it can be improved by using a flag to indicate whether any swaps were made in the last pass.
- **Non-recursive merge sort**: This algorithm is a variation of the recursive merge sort, which divides the array into two halves, sorts them recursively, and then merges them in sorted order. The non-recursive version uses a loop and a stack to simulate the recursion, and avoids the extra memory and function calls of the recursive version. The time complexity of this algorithm is O(n log n), where n is the number of elements in the array.

These are some of the non-recursive sorting algorithms that can be implemented in C. To learn more about them, you can refer to the following sources:

: Recursive vs non-recursive sorting algorithms - Stack Overflow
: Sorting Algorithms Explained - freeCodeCamp.org
: Non-Recursive Merge Sort | Baeldung on Computer Science