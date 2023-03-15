# Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case.

## Quick Sort
- Quick Sort is a sorting algorithm that uses the **divide and conquer** technique to sort a given array of integers.
- The basic idea is to choose a **pivot** element from the array, and partition the array into two subarrays: one with elements smaller than the pivot, and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted using the same procedure.
- The algorithm terminates when the array size is one or zero, which means it is already sorted.

## Time Complexity
- The time complexity of Quick Sort depends on how the pivot element is chosen, and how balanced the partitions are.
- In the **worst case**, the pivot element is always the smallest or the largest element in the array, which means one partition is empty and the other contains n-1 elements. This leads to a recursive call on an array of size n-1, which repeats until the array is sorted. The time complexity in this case is **O(n^2)**, where n is the number of elements in the array.
- In the **average case**, the pivot element is chosen randomly or by using some heuristic, which means the partitions are roughly equal in size. This leads to a recursive call on two subarrays of size n/2, which repeats until the array is sorted. The time complexity in this case is **O(n log n)**, where n is the number of elements in the array.
- In the **best case**, the pivot element is always the median of the array, which means the partitions are exactly equal in size. This leads to a recursive call on two subarrays of size n/2, which repeats until the array is sorted. The time complexity in this case is also **O(n log n)**, where n is the number of elements in the array.

## Java Implementation
- The following code snippet shows how to implement Quick Sort in Java, using a random pivot selection and a swap function to partition the array.

```java
// A utility function to swap two elements in an array
public static void swap(int[] arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to perform Quick Sort on a given array
public static void quickSort(int[] arr, int low, int high) {
  // Base case: array size is one or zero
  if (low >= high) {
    return;
  }

  // Choose a random pivot element and swap it with the last element
  int pivotIndex = (int) (Math.random() * (high - low + 1)) + low;
  swap(arr, pivotIndex, high);

  // Partition the array around the pivot element
  int i = low; // index for smaller elements
  int j = high - 1; // index for larger elements
  while (i <= j) {
    // Find the first element that is larger than or equal to the pivot
    while (i <= j && arr[i] < arr[high]) {
      i++;
    }
    // Find the last element that is smaller than or equal to the pivot
    while (i <= j && arr[j] > arr[high]) {
      j--;
    }
    // Swap the two elements if they are out of order
    if (i <= j) {
      swap(arr, i, j);
      i++;
      j--;
    }
  }
  // Swap the pivot element with the first element that is larger than it
  swap(arr, i, high);

  // Recursively sort the left and right subarrays
  quickSort(arr, low, i - 1);
  quickSort(arr, i + 1, high);
}
```

## Experiment and Graph
- To test the performance of Quick Sort, we can generate random arrays of different sizes (n > 5000) and measure the time taken to sort them using the Java implementation.
- We can use the `System.nanoTime()` method to get the current time in nanoseconds before and after the sorting, and calculate the difference as the elapsed time.
- We can repeat the experiment for different values of n