## Quick Sort Method

Quick Sort is a sorting algorithm that uses the divide-and-conquer approach. It works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

The time complexity of Quick Sort is as follows:
- Worst case: O(n^2)
- Average case: O(n log n)
- Best case: O(n log n)

To demonstrate the time complexity of Quick Sort, the program can be run for varied values of n>5000 and the time taken to sort can be recorded. A graph of the time taken versus n can be plotted on a graph sheet.

The elements to be sorted can be read from a file or generated using a random number generator.

Here is an example of how Quick Sort can be implemented in Java:

```java
public static void quickSort(int[] arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi-1);
        quickSort(arr, pi+1, high);
    }
}

public static int partition(int[] arr, int low, int high) {
    int pivot = arr[high];
    int i = (low-1);
    for (int j=low; j<high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    int temp = arr[i+1];
    arr[i+1] = arr[high];
    arr[high] = temp;
    return i+1;
}
```

This is an example of how the divide-and-conquer method works in Quick Sort. The time complexity analysis shows that in the worst case, the time taken to sort is O(n^2), while in the average and best cases, the time taken is O(n log n).