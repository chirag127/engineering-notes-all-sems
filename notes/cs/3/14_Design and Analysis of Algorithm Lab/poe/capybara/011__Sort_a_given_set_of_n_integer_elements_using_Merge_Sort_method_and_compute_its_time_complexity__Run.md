## Merge Sort Algorithm

Merge Sort is a popular sorting algorithm that uses the divide and conquer methodology. It is one of the most efficient algorithms for large data sets. The algorithm involves the following steps:

1. Divide the given unsorted array into n subarrays, each of size one.
2. Repeatedly merge subarrays to produce new sorted subarrays until there is only one subarray remaining.
3. The remaining subarray is the sorted array.

The algorithm has a time complexity of O(n log n) in all three cases: worst, average, and best. 

## Time Complexity Analysis

The time complexity of Merge Sort can be analyzed in the following three cases:

### Worst Case

In the worst case, the time complexity is O(n log n). This occurs when the array is in reverse order. In this case, every pair of subarrays needs to be merged, and each merge operation takes O(n) time. 

### Average Case

In the average case, the time complexity is also O(n log n). This occurs when the array is randomly ordered. The algorithm still needs to perform the same number of merge operations as in the worst case, but the constant factor is smaller.

### Best Case

In the best case, the time complexity is also O(n log n). This occurs when the array is already sorted. In this case, the algorithm simply merges the subarrays without any additional sorting required.

## Program Execution

To execute the Merge Sort algorithm, we need to perform the following steps:

1. Read the input data from a file or generate it randomly using a number generator.
2. Implement the Merge Sort algorithm to sort the data.
3. Record the time taken to sort the data for different values of n.
4. Plot a graph of time taken versus n.

## Conclusion

Merge Sort is an efficient sorting algorithm that uses the divide and conquer methodology. It has a time complexity of O(n log n) in all three cases: worst, average, and best. The algorithm can be used to sort large data sets. The time taken to sort the data can be measured and plotted as a graph against the size of the data set. This information can be used to optimize the algorithm for different scenarios.