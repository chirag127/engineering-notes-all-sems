## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and puts it at the beginning.
- The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted.
- The algorithm works as follows:
  - Find the minimum element in the unsorted subarray and swap it with the leftmost element.
  - Move the subarray boundary one element to the right.
  - Repeat until the entire array is sorted.
- The time complexity of selection sort is O(n^2) in the worst, average, and best cases, where n is the number of elements in the array.
- The space complexity of selection sort is O(1), as it only requires a constant amount of auxiliary space.
- Selection sort is not a stable sorting algorithm, as it may change the relative order of elements with equal values.
- Selection sort is not suitable for large arrays, as it performs poorly compared to other sorting algorithms.
- Here is an example of a program for selection sort in C language:

```c
// A function to swap two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort on an array of size n
void selectionSort(int arr[], int n) {
  // The index of the minimum element in the unsorted subarray
  int min_idx;
  // Loop through all array elements
  for (int i = 0; i < n - 1; i++) {
    // Find the minimum element in the unsorted subarray
    min_idx = i;
    for (int j = i + 1; j < n; j++) {
      if (arr[j] < arr[min_idx]) {
        min_idx = j;
      }
    }
    // Swap the minimum element with the leftmost element
    swap(&arr[min_idx], &arr[i]);
  }
}

// A function to print an array of size n
void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the selection sort function
int main() {
  // An example array
  int arr[] = {64, 25, 12, 22, 11};
  // The size of the array
  int n = sizeof(arr) / sizeof(arr[0]);
  // Print the original array
  printf("Original array: \n");
  printArray(arr, n);
  // Perform selection sort
  selectionSort(arr, n);
  // Print the sorted array
  printf("Sorted array: \n");
  printArray(arr, n);
  return 0;
}
```