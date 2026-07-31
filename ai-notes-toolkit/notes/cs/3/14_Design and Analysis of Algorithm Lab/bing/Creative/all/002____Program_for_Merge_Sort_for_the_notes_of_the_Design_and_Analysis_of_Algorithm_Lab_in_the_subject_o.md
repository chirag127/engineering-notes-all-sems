## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into one sorted array.
- The algorithm can be implemented using the following steps:

  - If the array has only one element, return the array as it is already sorted.
  - Otherwise, divide the array into two equal or nearly equal parts, called the left and right subarrays.
  - Recursively sort the left and right subarrays using merge sort.
  - Merge the sorted left and right subarrays into one sorted array using a helper function that takes two sorted arrays and returns a new sorted array that contains all the elements from both arrays in ascending order.
  - Return the merged array as the final sorted array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level takes O(n) time to merge the subarrays.
- The space complexity of merge sort is O(n), as the algorithm requires an auxiliary array of the same size as the original array to store the merged subarrays.
- The following is a possible pseudocode implementation of merge sort in C:

```c
// A function that merges two sorted subarrays into one sorted array
// Input: arr - the original array, l - the starting index of the left subarray, m - the ending index of the left subarray, r - the ending index of the right subarray
// Output: none, but the original array is modified to contain the sorted elements from l to r
void merge(int arr[], int l, int m, int r) {
  // Create an auxiliary array of size r - l + 1
  int n = r - l + 1;
  int aux[n];

  // Initialize two pointers i and j to point to the start of the left and right subarrays respectively
  int i = l;
  int j = m + 1;

  // Initialize a pointer k to point to the start of the auxiliary array
  int k = 0;

  // Loop until either i or j reaches the end of their subarray
  while (i <= m && j <= r) {
    // Compare the elements at i and j and copy the smaller one to the auxiliary array
    if (arr[i] <= arr[j]) {
      aux[k] = arr[i];
      i++;
    } else {
      aux[k] = arr[j];
      j++;
    }
    // Increment k to point to the next position in the auxiliary array
    k++;
  }

  // Copy the remaining elements from the left subarray to the auxiliary array if any
  while (i <= m) {
    aux[k] = arr[i];
    i++;
    k++;
  }

  // Copy the remaining elements from the right subarray to the auxiliary array if any
  while (j <= r) {
    aux[k] = arr[j];
    j++;
    k++;
  }

  // Copy the elements from the auxiliary array back to the original array from l to r
  for (i = l; i <= r; i++) {
    arr[i] = aux[i - l];
  }
}

// A function that implements merge sort on an array
// Input: arr - the array to be sorted, l - the starting index of the array, r - the ending index of the array
// Output: none, but the array is modified to be sorted in ascending order
void mergeSort(int arr[], int l, int r) {
  // Base case: if the array has only one element, return
  if (l == r) {
    return;
  }

  // Find the middle index of the array
  int m = (l + r) / 2;

  // Recursively sort the left and right subarrays
  mergeSort(arr, l, m);
  mergeSort(arr, m + 1, r);

  // Merge the sorted subarrays
  merge(arr, l, m, r);
}
```