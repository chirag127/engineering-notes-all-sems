 Here is the content in markdown format:

## Sort a given set of n integer elements using Quick Sort method and compute its time complexity.

1. Quicksort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot.
2. There are three steps in quicksort:
- Pick an element as pivot
- Partition the array around the pivot
- Recursively sort the subarrays on left and right of pivot
3. Pseudocode:
quicksort(array, low, high) {
    if low < high:
        // pivot location
        pivot_index = partition(array, low, high)
        // sort left partition
        quicksort(array, low, pivot_index - 1)
        // sort right partition
        quicksort(array, pivot_index + 1, high)
}

4. Time complexity:
- Worst case: O(n^2) - when elements are sorted
- Average case: O(n log n)
- Best case: O(n log n) - when elements are randomly distributed

5. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus n on a graph sheet. The elements can be read from a file or can be generated using the random number generator.

6. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

7. This covers quicksort and its complexity analysis. It can be used as notes for the Design and Analysis of Algorithm Lab in the subject of Real Time System.