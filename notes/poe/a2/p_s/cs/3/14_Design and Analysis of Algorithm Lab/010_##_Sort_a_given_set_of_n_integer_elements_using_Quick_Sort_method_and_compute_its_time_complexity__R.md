 Here is the content in markdown format:

## Sort a given set of n integer elements using Quick Sort method and compute its time complexity.

Quicksort is a divide and conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. There are three steps in quicksort:

1. Pick an element as pivot: This element is called the pivot element
2. Partitioning: The array is rearranged such that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it. After this partitioning, the pivot is in its final position. This is called the partition operation.
3. Recursively applying the above steps to the sub-array: The sub-array to the left of the pivot is further sorted by recursively applying the quicksort algorithm using the left sub-array. Similarly, the sub-array to the right of the pivot is sorted using the quicksort algorithm with the right sub-array.

This recursive process continues on the left and right partitions until all items have been sorted.
The time complexity of quicksort is:

- Best case: O(nlogn) - When the pivot is always the median element
- Average case: O(nlogn)
- Worst case: O(n^2) - When the array is already sorted

To plot the time taken for sorting versus n:

1. Generate n random integers and store in an array
2. Record the start time
3. Sort the array using quicksort
4. Record the end time
5. Compute the time taken as end time - start time
6. Plot the time taken on the y-axis and n on the x-axis

The code for quicksort in Java can be:

public void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

public int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high - 1; j++) {
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