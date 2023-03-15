## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Quick sort is a divide-and-conquer algorithm that sorts an array of elements by recursively partitioning it into smaller subarrays and sorting them independently.
- The algorithm works as follows:
  - Choose a pivot element from the array, typically the first or the last element.
  - Rearrange the array such that all the elements smaller than the pivot are on the left side of the pivot, and all the elements larger than the pivot are on the right side of the pivot. This is called partitioning the array.
  - Recursively apply the same algorithm to the left and right subarrays, excluding the pivot element, until the subarrays are of size one or zero.
- The average time complexity of quick sort is O(n log n), where n is the number of elements in the array. The worst-case time complexity is O(n^2), which occurs when the array is already sorted or nearly sorted, and the pivot is chosen as the first or the last element.
- The space complexity of quick sort is O(log n), which is the maximum depth of the recursion stack.
- Quick sort is an in-place algorithm, which means it does not require additional memory to store the sorted array. However, it is not a stable algorithm, which means it does not preserve the relative order of equal elements in the array.
- Here is an example of a C program that implements quick sort:

```c
// A function to swap two elements in an array
void swap(int* a, int* b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to partition an array around a pivot element
int partition(int arr[], int low, int high) {
  // Choose the last element as the pivot
  int pivot = arr[high];
  // Initialize the index of the smaller element
  int i = low - 1;
  // Loop through the array from low to high - 1
  for (int j = low; j < high; j++) {
    // If the current element is smaller than or equal to the pivot
    if (arr[j] <= pivot) {
      // Increment the index of the smaller element
      i++;
      // Swap the current element with the smaller element
      swap(&arr[i], &arr[j]);
    }
  }
  // Swap the pivot element with the element at i + 1
  swap(&arr[i + 1], &arr[high]);
  // Return the index of the pivot element
  return i + 1;
}

// A function to sort an array using quick sort
void quickSort(int arr[], int low, int high) {
  // If the low index is smaller than the high index
  if (low < high) {
    // Partition the array and get the index of the pivot element
    int pi = partition(arr, low, high);
    // Recursively sort the left subarray
    quickSort(arr, low, pi - 1);
    // Recursively sort the right subarray
    quickSort(arr, pi + 1, high);
  }
}

// A function to print an array
void printArray(int arr[], int size) {
  for (int i = 0; i < size; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the program
int main() {
  // An example array
  int arr[] = {10, 7, 8, 9, 1, 5};
  // The size of the array
  int n = sizeof(arr) / sizeof(arr[0]);
  // Print the original array
  printf("Original array: \n");
  printArray(arr, n);
  // Sort the array using quick sort
  quickSort(arr, 0, n - 1);
  // Print the sorted array
  printf("Sorted array: \n");
  printArray(arr, n);
  // Return 0 to indicate success
  return 0;
}
```