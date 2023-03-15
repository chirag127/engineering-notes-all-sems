## Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort depends on the implementation. In the worst case, the time complexity is O(n^2), where n is the number of elements in the array. This occurs when the pivot element is the smallest or largest element in the array, causing one of the partitions to be empty. In the average case, the time complexity is O(n log n).

To demonstrate the time complexity of Quick Sort, we can run the algorithm on varied values of n > 5000 and record the time taken to sort. We can then plot a graph of the time taken versus n on a graph sheet.

The elements to be sorted can be read from a file or generated using a random number generator. Here is an example implementation of Quick Sort in Java:

```java
public class QuickSort {
    public static void quickSort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (arr[j] <= pivot) {
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
}
```

This implementation of Quick Sort uses the last element as the pivot. The `partition` function takes the array, the starting index, and the ending index as arguments, and returns the index of the pivot element. The `quickSort` function recursively sorts the sub-arrays on either side of the pivot.

The worst-case time complexity of this implementation is O(n^2), while the average-case time complexity is O(n log n). The best-case time complexity is also O(n log n), which occurs when the pivot element is the median of the array, causing the partitions to be of equal size.