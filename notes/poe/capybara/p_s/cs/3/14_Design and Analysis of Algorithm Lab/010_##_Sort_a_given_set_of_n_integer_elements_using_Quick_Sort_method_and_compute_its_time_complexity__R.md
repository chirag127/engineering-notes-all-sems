## Sort a given set of n integer elements using Quick Sort method and compute its time complexity

Quick Sort is a popular sorting algorithm that is widely used in computer science. It is an efficient sorting algorithm that sorts an array by partitioning it into two smaller arrays, one with elements less than the pivot and the other with elements greater than the pivot. The pivot is the element around which the array is partitioned.

### Steps in Quick Sort Algorithm

1. Choose a pivot from the array. This can be done randomly or by selecting the first or last element of the array.
2. Partition the array such that all elements less than the pivot are on one side and all elements greater than the pivot are on the other side.
3. Recursively apply the above two steps to the sub-arrays of elements less than and greater than the pivot until the entire array is sorted.

### Time Complexity Analysis

The time complexity of Quick Sort is O(n log n) in the average and best case scenarios. However, in the worst case scenario, the time complexity is O(n^2). This happens when the array is already sorted or reverse sorted and the pivot is chosen as the first or last element. To overcome this, we can choose the pivot randomly or choose the median of three elements as the pivot.

### Running the Program

To run the program, we can generate an array of n integers using the random number generator or read the elements from a file. We can then apply Quick Sort on the array and record the time taken to sort it. We can repeat this process for different values of n greater than 5000 and plot a graph of the time taken versus n.

### Demonstration using Java

Here is an example Java code to implement Quick Sort:

```java
public static void quickSort(int[] arr, int low, int high){
    if (low < high){
        int pivot = partition(arr, low, high);
        quickSort(arr, low, pivot - 1);
        quickSort(arr, pivot + 1, high);
    }
}

public static int partition(int[] arr, int low, int high){
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++){
        if (arr[j] < pivot){
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

We can call the `quickSort` method with the array, starting and ending indices as parameters to sort the array using Quick Sort.

### Conclusion

Quick Sort is an efficient sorting algorithm that can be used to sort large arrays of integers. It has an average and best case time complexity of O(n log n) and a worst case time complexity of O(n^2). By using a random pivot or choosing the median of three elements as the pivot, we can reduce the probability of worst case scenario. We can also demonstrate how the divide and conquer method works using Java code and analyze the time complexity for different scenarios.