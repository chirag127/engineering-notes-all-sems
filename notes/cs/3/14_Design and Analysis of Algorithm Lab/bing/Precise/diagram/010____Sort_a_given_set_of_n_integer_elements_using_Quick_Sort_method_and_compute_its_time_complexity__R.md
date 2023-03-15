## Quick Sort

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort is as follows:
- Worst case: O(n^2)
- Average case: O(n log n)
- Best case: O(n log n)

To demonstrate the time complexity of Quick Sort, we can run the algorithm on varied values of n > 5000 and record the time taken to sort. The elements can be read from a file or generated using a random number generator. The time taken to sort can then be plotted on a graph versus n on a graph sheet.

Here is an example implementation of Quick Sort in Java:

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

This implementation of Quick Sort uses the last element as the pivot. The partition function takes the pivot element and places it in its correct position in the sorted array, and places all smaller elements to the left of the pivot and all greater elements to the right of the pivot.

The time complexity of Quick Sort can be analyzed as follows:
- Worst case: The worst case occurs when the partition process always picks the greatest or smallest element as the pivot. This would result in an unbalanced partition and the time complexity would be O(n^2).
- Average case: The average case occurs when the partition process picks the median element as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).
- Best case: The best case occurs when the partition process always picks the median element as the pivot. This would result in a balanced partition and the time complexity would be O(n log n).

In conclusion, Quick Sort is an efficient sorting algorithm that uses the divide-and-conquer approach. Its time complexity can vary depending on the selection of the pivot element, but on average it has a time complexity of O(n log n).