 Here is the content in markdown format:

## Sort a given set of n integer elements using Merge Sort method and compute its time complexity.

1. Merge Sort is a Divide and Conquer algorithm. It divides the input array into two halves, calls itself for the two halves and then merges the two sorted halves.
2. The steps are:
- Divide the unsorted array into two halves
- Sort the two halves recursively using Merge Sort
- Merge the two sorted halves into one sorted array

3. Pseudocode:
mergeSort(array, left, right) {
    if (left < right) {
        middle = (left + right) / 2;
        mergeSort(array, left, middle);
        mergeSort(array, middle + 1, right);
        merge(array, left, middle, right);
    }
}

4. The time complexity of Merge Sort is O(n log n) in all 3 cases (worst, average and best) as the algorithm always divides the array into two halves and takes logarithmic time to sort each half.

5. Run the program for varied values of n> 5000, and record the time taken to sort. Plot a graph of the time taken versus n. The elements can be read from a file or can be generated using the random number generator.

6. This demonstrates how the divide and conquer method works by dividing the problem into smaller subproblems, solving them recursively and then combining to get the solution to the original problem. The time complexity is also computed to be O(n log n) which is better than O(n^2) for other comparison-based sorting algorithms.

Does this look okay?