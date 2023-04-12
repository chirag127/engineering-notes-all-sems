## Sort a given set of n integer elements using Quick Sort method and compute its time complexity. Run the program for varied values of n> 5000 and record the time taken to sort. Plot a graph of the time taken versus non graph sheet. The elements can be read from a file or can be generated using the random number generator. Demonstrate using Java how the divide and- conquer method works along with its time complexity analysis: worst case, average case and best case. for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick Sort is a sorting algorithm that uses the divide and conquer technique to sort a given array of integers.
- The basic idea of Quick Sort is to choose a pivot element from the array, such as the first or the last element, and partition the array into two subarrays: one with elements smaller than the pivot and one with elements larger than the pivot.
- The pivot element is then placed in its correct position in the sorted array, and the subarrays are recursively sorted using the same procedure.
- The time complexity of Quick Sort depends on the choice of the pivot element and the distribution of the elements in the array.
- The worst case time complexity of Quick Sort is O(n^2), which occurs when the pivot element is the smallest or the largest element in the array, or when the array is already sorted or reverse sorted. In this case, the partitioning step does not divide the array evenly, and one subarray has n-1 elements while the other has 0 elements. This leads to n-1 recursive calls, each taking O(n) time to partition the array.
- The average case time complexity of Quick Sort is O(n log n), which occurs when the pivot element is chosen randomly or by using some heuristic, such as the median of three elements. In this case, the partitioning step divides the array into two subarrays of roughly equal size, and the recursive calls take O(log n) time to sort each subarray. The total time taken is O(n log n) + O(n) = O(n log n), where O(n) is the time taken to partition the array.
- The best case time complexity of Quick Sort is also O(n log n), which occurs when the pivot element is the median of the array. In this case, the partitioning step divides the array into two subarrays of exactly equal size, and the recursive calls take O(log n) time to sort each subarray. The total time taken is O(n log n) + O(n) = O(n log n), where O(n) is the time taken to partition the array.
- To implement Quick Sort in Java, we can use the following code:

```java
// A utility function to swap two elements in an array
public static void swap(int[] arr, int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to partition the array around a pivot element
public static int partition(int[] arr, int low, int high) {
  // Choose the last element as the pivot
  int pivot = arr[high];
  // Initialize the index of the smaller element
  int i = low - 1;
  // Loop through the elements from low to high - 1
  for (int j = low; j < high; j++) {
    // If the current element is smaller than or equal to the pivot
    if (arr[j] <= pivot) {
      // Increment the index of the smaller element
      i++;
      // Swap the current element with the smaller element
      swap(arr, i, j);
    }
  }
  // Swap the pivot element with the element at i + 1
  swap(arr, i + 1, high);
  // Return the index of the pivot element
  return i + 1;
}

// A function to sort the array using Quick Sort
public static void quickSort(int[] arr, int low, int high) {
  // Base case: if the array has one or zero elements, it is already sorted
  if (low >= high) {
    return;
  }
  // Partition the array around a pivot element and get its index
  int pi = partition(arr, low, high);
  // Recursively sort the left subarray
  quickSort(arr, low, pi - 1);
  // Recursively sort the right subarray
  quickSort(arr, pi + 1, high);
}

// A function to generate an array of n random integers
public static int[] generateRandomArray(int n) {
  // Create a new array of size n
  int[] arr = new int

```
