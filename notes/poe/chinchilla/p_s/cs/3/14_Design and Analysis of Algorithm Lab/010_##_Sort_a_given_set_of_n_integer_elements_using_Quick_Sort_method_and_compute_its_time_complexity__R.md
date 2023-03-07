## Sort a given set of n integer elements using Quick Sort method and compute its time complexity.

Quick Sort is a widely used sorting algorithm in computer science. It is a divide and conquer algorithm that is used to sort a given set of elements. In this algorithm, the partition of an array is done based on a pivot element. 

### Algorithm:
The following steps are involved in Quick Sort:

1. Choose a pivot element from the array.
2. Partition the array by rearranging the elements such that all the elements less than the pivot element come before the pivot element, and all the elements greater than the pivot element come after it.
3. Recursively apply the first two steps to the sub-arrays on either side of the pivot element.

### Time Complexity:
The time complexity of Quick Sort depends on the choice of the pivot element. In the worst case scenario, when the pivot element divides the array into two sub-arrays of unequal size, the time complexity of Quick Sort is O(n^2). However, in the average and best case scenarios, the time complexity is O(n*logn).

### Java Implementation:
The Java implementation of Quick Sort is as follows:

```
public class QuickSort {
    public static void quickSort(int[] arr, int start, int end) {
        if (start < end) {
            int pivotPos = partition(arr, start, end);
            quickSort(arr, start, pivotPos - 1);
            quickSort(arr, pivotPos + 1, end);
        }
    }

    public static int partition(int[] arr, int start, int end) {
        int pivot = arr[end];
        int i = start - 1;

        for (int j = start; j <= end - 1; j++) {
            if (arr[j] <= pivot) {
                i++;
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        int temp = arr[i + 1];
        arr[i + 1] = arr[end];
        arr[end] = temp;

        return i + 1;
    }
}
```

### Running Time Analysis:
To record the time taken to sort various sets of n>5000 elements, we can use Java's `System.currentTimeMillis()` method before and after the sorting algorithm is executed. The difference between the two times gives us the time taken to sort the elements.

We can then plot a graph of the time taken versus the number of elements on a non-graph sheet. This will help us visualize how the running time of the Quick Sort algorithm increases with the number of elements.

### Conclusion:
In conclusion, Quick Sort is an efficient sorting algorithm that has a worst-case time complexity of O(n^2) and an average and best-case time complexity of O(n*logn). By recording the time taken to sort various sets of elements and plotting the results on a graph, we can analyze the running time of the algorithm and its performance.