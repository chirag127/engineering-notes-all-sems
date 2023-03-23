## Quick Sort Algorithm

Quick Sort is a commonly used sorting algorithm that follows the divide-and-conquer approach. It is an efficient algorithm for sorting large datasets. The algorithm works by selecting a pivot element from the dataset, partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot, and recursively applying the algorithm to each sub-array.

### Algorithm Steps

1. Choose an element in the array to be the pivot element.
2. Partition the array into two sub-arrays based on the pivot element. One sub-array contains elements smaller than the pivot element, and the other sub-array contains elements greater than the pivot element.
3. Recursively apply the algorithm to each sub-array.
4. Combine the sorted sub-arrays to obtain the final sorted array.

### Time Complexity

The time complexity of Quick Sort algorithm is as follows:

- Worst Case: O(n^2)
- Average Case: O(n log n)
- Best Case: O(n log n)

The worst case occurs when the pivot element is always the smallest or largest element in the array, resulting in unbalanced partitions. The average and best cases occur when the pivot element is chosen randomly or is the median element, resulting in balanced partitions.

### Demonstration using Java

Here is a sample implementation of Quick Sort algorithm using Java:

```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int partitionIndex = partition(arr, low, high);
        quickSort(arr, low, partitionIndex - 1);
        quickSort(arr, partitionIndex + 1, high);
    }
}

public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    return i + 1;
}
```

### Time Complexity Analysis

We can analyze the time complexity of Quick Sort algorithm using the following scenarios:

1. Worst Case: When the pivot element is always the smallest or largest element in the array, resulting in unbalanced partitions. This leads to the worst case time complexity of O(n^2).
2. Best Case: When the pivot element is the median element, resulting in balanced partitions. This leads to the best case time complexity of O(n log n).
3. Average Case: When the pivot element is chosen randomly, resulting in balanced partitions on average. This leads to the average case time complexity of O(n log n).

### Running the Program

To run the program for varied values of n>5000 and record the time taken to sort, we can use the following steps:

1. Generate an array of n random integers using the random number generator.
2. Call the quickSort() function with the array as input.
3. Record the time taken to sort the array using the System.currentTimeMillis() function.
4. Plot a graph of the time taken versus n using a graph sheet.

### Conclusion

Quick Sort is an efficient sorting algorithm that can be used for large datasets. The algorithm follows the divide-and-conquer approach and has a worst case time complexity of O(n^2), an average case time complexity of O(n log n), and a best case time complexity of O(n log n). By generating arrays of random integers with varied values of n>5000 and recording the time taken to sort, we can plot a graph of the time taken versus n to analyze the performance of the algorithm.