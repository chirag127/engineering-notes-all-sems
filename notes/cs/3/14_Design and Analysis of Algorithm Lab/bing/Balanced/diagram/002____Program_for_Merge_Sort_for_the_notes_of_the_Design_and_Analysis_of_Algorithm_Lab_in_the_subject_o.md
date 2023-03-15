## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two halves and then merges them in sorted order.
- The algorithm can be described as follows:

  - If the array has only one element, return it as it is already sorted.
  - Otherwise, divide the array into two equal or nearly equal parts and call merge sort on each part.
  - Merge the two sorted subarrays by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat until one of the subarrays is empty, then copy the remaining elements of the other subarray into the output array.
  - Return the output array as the sorted array.

- The time complexity of merge sort is O(n log n) in the worst case, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels, and each level takes O(n) time to merge the subarrays.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the output array.
- Merge sort is a stable sorting algorithm, meaning that it preserves the relative order of equal elements in the input array.
- Merge sort is suitable for sorting large arrays or lists that are stored on disk or in external memory, as it can efficiently access sequential data and minimize the number of disk accesses.
- Here is an example of a C program that implements merge sort:

```c
// A function to merge two sorted subarrays
void merge(int arr[], int left, int mid, int right) {
  // Find the sizes of the subarrays
  int n1 = mid - left + 1;
  int n2 = right - mid;

  // Create temporary arrays to store the subarrays
  int L[n1], R[n2];

  // Copy the data to the temporary arrays
  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

  // Initialize indices for the subarrays and the output array
  int i = 0, j = 0, k = left;

  // Merge the subarrays by comparing the first elements of each subarray
  while (i < n1 && j < n2) {
    if (L[i] <= R[j]) {
      arr[k] = L[i];
      i++;
    } else {
      arr[k] = R[j];
      j++;
    }
    k++;
  }

  // Copy the remaining elements of L[], if any
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  // Copy the remaining elements of R[], if any
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

// A function to implement merge sort
void mergeSort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left >= right)
    return;

  // Find the middle point of the array
  int mid = (left + right) / 2;

  // Recursively sort the left and right halves of the array
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);

  // Merge the sorted halves
  merge(arr, left, mid, right);
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// A main function to test the program
int main() {
  // Create an example array
  int arr[] = {12, 11, 13, 5, 6, 7};
  int size = sizeof(arr) / sizeof(arr[0]);

  // Print the original array
  printf("Given array is \n");
  printArray(arr, size);

  // Sort the array using merge sort
  mergeSort(arr, 0, size - 1);

  // Print the sorted array
  printf("\nSorted array is \n");
  printArray(arr, size);

  return 0;
}
```