## Quick Sort Algorithm

Quick Sort is a sorting algorithm that follows the divide and conquer method. It is one of the most efficient sorting algorithms with an average time complexity of O(n log n). It works by selecting a pivot element and partitioning the array into two sub-arrays, one with elements smaller than the pivot and the other with elements greater than the pivot. The pivot element is then placed in its correct position and the algorithm is recursively applied to the sub-arrays.

### Steps for Quick Sort

1. Select a pivot element from the array. The pivot can be selected randomly or as the first or last element of the array.
2. Partition the array into two sub-arrays, one with elements smaller than the pivot and the other with elements greater than the pivot.
3. Recursively apply the Quick Sort algorithm to the sub-arrays.
4. Combine the sorted sub-arrays.

### Time Complexity Analysis

The time complexity of Quick Sort depends on the selection of the pivot element. The worst-case time complexity occurs when the pivot element is either the smallest or largest element in the array, resulting in unbalanced partitions. In the worst-case scenario, the time complexity of Quick Sort is O(n^2).

The average-case time complexity of Quick Sort is O(n log n). This is because, on average, the pivot element will be selected such that the partitions are balanced, resulting in a logarithmic number of partitions.

The best-case time complexity of Quick Sort is O(n), which occurs when the pivot element is the median element of the array, resulting in balanced partitions.

### Java Implementation

Here is a Java implementation of the Quick Sort algorithm:

```java
public class QuickSort {
    
    public static void quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int pivotIndex = partition(arr, left, right);
            quickSort(arr, left, pivotIndex - 1);
            quickSort(arr, pivotIndex + 1, right);
        }
    }
    
    private static int partition(int[] arr, int left, int right) {
        int pivot = arr[right];
        int i = left - 1;
        for (int j = left; j < right; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, right);
        return i + 1;
    }
    
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public static void main(String[] args) {
        int[] arr = {5, 2, 8, 3, 9, 4};
        quickSort(arr, 0, arr.length - 1);
        for (int i : arr) {
            System.out.print(i + " ");
        }
    }
}
```

### Time Complexity Analysis using Graph

To analyze the time complexity of Quick Sort, we can plot a graph of the time taken to sort a given set of n integer elements. The elements can be read from a file or can be generated using the random number generator.

Here is an example of how to plot a graph in Java:

```java
import java.util.Random;

import org.knowm.xchart.*;

public class QuickSortGraph {
    
    public static void main(String[] args) {
        Random random = new Random();
        int[] nValues = {5000, 10000, 15000, 20000};
        long[] timeTaken = new long[nValues.length];
        
        for (int i = 0; i < nValues.length; i++) {
            int[] arr = new int[nValues[i]];
            for (int j = 0; j < arr.length; j++) {
                arr[j] = random.nextInt();
            }
            long startTime = System.nanoTime();
            QuickSort.quickSort(arr, 0, arr.length - 1);
            long endTime = System.nanoTime();
            timeTaken[i] = endTime - startTime;
        }
        
        XYChart chart = new XYChartBuilder().width(800).height(600).title("Quick Sort Time Complexity").xAxisTitle("n").yAxisTitle("Time (ns)").build();
        chart.addSeries("Quick Sort", nValues, timeTaken);
        new SwingWrapper<>(chart).displayChart();
    }
}
```

By running the above code, we can generate a graph that plots the time taken to sort different values of n using the Quick Sort algorithm.

### Conclusion

In this note, we learned about the Quick Sort algorithm and its time complexity analysis. We also saw how to implement Quick Sort in Java and how to plot a graph to analyze its time complexity.