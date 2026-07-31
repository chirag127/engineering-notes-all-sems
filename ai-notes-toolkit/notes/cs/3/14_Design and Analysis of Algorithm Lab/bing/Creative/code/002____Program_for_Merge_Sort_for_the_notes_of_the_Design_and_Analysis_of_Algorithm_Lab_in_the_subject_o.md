## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Merge sort is a divide-and-conquer algorithm that recursively splits an array into two subarrays and then merges them in sorted order.
- The algorithm can be implemented using the following steps:

  1. If the array has only one element, return it as it is already sorted.
  2. Otherwise, divide the array into two equal or nearly equal subarrays and call merge sort on each subarray recursively.
  3. Merge the two sorted subarrays into one sorted array by comparing the first elements of each subarray and taking the smaller one into the output array. Repeat this until both subarrays are exhausted.
  4. Return the merged array as the final output.

- The time complexity of merge sort is O(n log n) in the worst, average, and best cases, where n is the number of elements in the array. This is because the algorithm divides the array into log n levels and performs O(n) work at each level.
- The space complexity of merge sort is O(n) in the worst case, as the algorithm requires an auxiliary array of the same size as the input array to store the merged output.
- The following is a possible C++ program for merge sort:

```cpp
// A function to merge two sorted subarrays into one sorted array
void merge(int arr[], int left, int mid, int right) {
  // Find the sizes of the two subarrays
  int n1 = mid - left + 1;
  int n2 = right - mid;

  // Create temporary arrays to store the subarrays
  int L[n1], R[n2];

  // Copy the subarrays into the temporary arrays
  for (int i = 0; i < n1; i++)
    L[i] = arr[left + i];
  for (int j = 0; j < n2; j++)
    R[j] = arr[mid + 1 + j];

  // Initialize indices for the subarrays and the output array
  int i = 0, j = 0, k = left;

  // Merge the subarrays into the output array by comparing the first elements of each subarray
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

  // Copy the remaining elements of the left subarray, if any
  while (i < n1) {
    arr[k] = L[i];
    i++;
    k++;
  }

  // Copy the remaining elements of the right subarray, if any
  while (j < n2) {
    arr[k] = R[j];
    j++;
    k++;
  }
}

// A function to implement merge sort on an array
void mergeSort(int arr[], int left, int right) {
  // Base case: if the array has only one element, return
  if (left >= right)
    return;

  // Find the middle point of the array
  int mid = left + (right - left) / 2;

  // Recursively call merge sort on the left and right subarrays
  mergeSort(arr, left, mid);
  mergeSort(arr, mid + 1, right);

  // Merge the two sorted subarrays
  merge(arr, left, mid, right);
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++)
    cout << arr[i] << " ";
  cout << endl;
}

// A main function to test the program
int main() {
  // Create an example array
  int arr[] = {12, 11, 13, 5, 6, 7};
  int size = sizeof(arr) / sizeof(arr[0]);

  // Print the original array
  cout << "Given array is: " << endl;
  printArray(arr, size);

  // Call merge sort on the array
  mergeSort(arr, 0, size - 1);

  // Print the sorted array
  cout << "Sorted array is: " << endl;
  printArray(arr, size);

  return 0;
}
```