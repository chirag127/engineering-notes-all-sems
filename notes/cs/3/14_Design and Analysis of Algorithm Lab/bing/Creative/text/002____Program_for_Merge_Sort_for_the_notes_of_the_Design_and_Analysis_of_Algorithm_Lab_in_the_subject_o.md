## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that splits an array into two halves and recursively sorts each half, then merges the sorted halves into a single sorted array.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return the array as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal parts, called the left and right subarrays.
  3. Recursively apply merge sort to the left and right subarrays, and obtain the sorted left and right subarrays.
  4. Merge the sorted left and right subarrays using a helper function that takes two sorted arrays and returns a single sorted array.
  5. Return the merged array as the final sorted array.

- The time complexity of merge sort is O(n log n) in the average and worst cases, where n is the number of elements in the array. The space complexity is O(n) as the algorithm requires an auxiliary array to store the merged subarrays.
- The following is a possible pseudocode implementation of merge sort in C:

```c
// A helper function that merges two sorted arrays into one sorted array
void merge(int arr[], int left, int mid, int right) {
  // Create a temporary array to store the merged array
  int temp[right - left + 1];

  // Initialize the indices for the left, right, and merged subarrays
  int i = left; // index for the left subarray
  int j = mid + 1; // index for the right subarray
  int k = 0; // index for the merged subarray

  // Loop until either the left or the right subarray is exhausted
  while (i <= mid && j <= right) {
    // Compare the current elements of the left and right subarrays
    // and copy the smaller one to the merged subarray
    if (arr[i] <= arr[j]) {
      temp[k] = arr[i];
      i++;
    } else {
      temp[k] = arr[j];
      j++;
    }
    k++;
  }

  // Copy the remaining elements of the left subarray, if any
  while (i <= mid) {
    temp[k] = arr[i];
    i++;
    k++;
  }

  // Copy the remaining elements of the right subarray, if any
  while (j <= right) {
    temp[k] = arr[j];
    j++;
    k++;
  }

  // Copy the merged subarray back to the original array
  for (i = left; i <= right; i++) {
    arr[i] = temp[i - left];
  }
}

// A recursive function that implements merge sort
void merge_sort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left == right) {
    return;
  }

  // Otherwise, find the middle point of the array
  int mid = (left + right) / 2;

  // Recursively sort the left and right subarrays
  merge_sort(arr, left, mid);
  merge_sort(arr, mid + 1, right);

  // Merge the sorted subarrays
  merge(arr, left, mid, right);
}
```