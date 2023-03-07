

## Sort a given set of n integer elements using Quick Sort method

Quick Sort is a sorting algorithm that is based on the Divide and Conquer approach. It is one of the most popular sorting algorithms with an average time complexity of O(n log n). It is also an in-place sorting algorithm, meaning that it does not require extra space to sort the elements. 

The basic idea behind Quick Sort is to divide the array into two parts, one of which is sorted and the other is unsorted. The algorithm then recursively sorts the unsorted part of the array until the entire array is sorted.

### How the algorithm works

Quick Sort works by selecting a pivot element from the array and partitioning the array into two parts based on the pivot element. All the elements in the left part of the pivot are smaller than the pivot element, and all the elements in the right part of the pivot are greater than the pivot element. The algorithm then recursively sorts the left and right parts of the array until the array is completely sorted.

### Time complexity

The time complexity of the Quick Sort algorithm depends on the way the pivot element is chosen. The best case time complexity of Quick Sort is O(n log n), while the worst case time complexity is O(n2). The average time complexity of Quick Sort is also O(n log n).

### Demonstration using Java

The following Java program demonstrates how Quick Sort works. It takes an array of integers as input and sorts them using Quick Sort.

```java
// QuickSort.java

public class QuickSort {
    public static void main(String[] args) {
        int[] arr = {5, 3, 8, 2, 9, 1};
        quickSort(arr, 0, arr.length-1);
        for(int i=0; i<arr.length; i++)
            System.out.print(arr[i] + " ");
    }
 
    public static void quickSort(int[] arr, int low, int high) {
        if (arr == null || arr.length == 0)
            return;
 
        if (low >= high)
            return;
 
        // pick the pivot
        int middle = low + (high - low) / 2;
        int pivot = arr[middle];
 
        // make left < pivot and right > pivot
        int i = low, j = high;
        while (i <= j) {
            while (arr[i] < pivot) {
                i++;
            }
 
            while (arr[j] > pivot) {
                j--;
            }
 
            if (i <= j) {
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }
        }
 
        // recursively sort two sub parts
        if (low < j)
            quickSort(arr, low, j);
 
        if (high > i)
            quickSort(arr, i, high);
    }
}
```

### Time complexity analysis

The time complexity of Quick Sort depends on the way the pivot element is chosen. The worst case time complexity of Quick Sort is O(n2), which occurs when the pivot element is either the smallest or the largest element in the array. The best case time complexity of Quick Sort is O(n log n), which occurs when the pivot element is the median of the array. The average time complexity of Quick Sort is also O(n log n).

### Running the program for varied values of n

To measure the time taken to sort an array of size n, the program can be run for different values of n and the time taken to sort the array can be recorded. A graph of the time taken versus n can then be plotted to visualize the time complexity of Quick Sort.

### Advantages

- Quick Sort is an in-place sorting algorithm, meaning that it does not require extra space to sort the elements.
- It has an average time complexity of O(n log n), which makes it faster than other sorting algorithms like Bubble Sort and Insertion Sort.
- It is a recursive algorithm, which makes it easier to implement.

### Disadvantages

- The worst case time complexity of Quick Sort is O(n2), which makes it slower than other sorting algorithms like Merge Sort and Heap Sort.
- It is not a stable sorting algorithm, meaning that the relative order of elements with equal values is not preserved.
- The choice of the pivot element can affect the time complexity of the algorithm.