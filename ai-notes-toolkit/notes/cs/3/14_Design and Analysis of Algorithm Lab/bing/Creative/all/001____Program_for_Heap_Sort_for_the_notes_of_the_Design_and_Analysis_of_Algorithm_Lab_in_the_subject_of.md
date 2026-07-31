## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted output array.
- The algorithm can be implemented as follows:

  - Build a max-heap or a min-heap from the input array by using a bottom-up approach, starting from the last non-leaf node and moving upwards. This can be done in O(n) time, where n is the number of elements in the array.
  - Repeat the following steps until the heap size is reduced to one:
    - Swap the root element (which is the maximum or minimum element) with the last element in the heap.
    - Reduce the heap size by one and adjust the heap to maintain the heap property by using a top-down approach, starting from the root node and moving downwards. This can be done in O(log n) time, where n is the current heap size.
    - The extracted element is placed at the end of the sorted output array.

- The overall time complexity of heap sort is O(n log n), where n is the number of elements in the array. The space complexity is O(1), as no extra space is required apart from the input array.
- Heap sort is an in-place and unstable sorting algorithm, which means that it does not require extra space to store the sorted output and it does not preserve the relative order of equal elements.
- Heap sort is suitable for sorting large data sets, as it has a good asymptotic performance and it can be easily parallelized. However, it is not very efficient for sorting small data sets, as it has a high constant factor and it does not take advantage of the existing order in the input array.
- The following is an example of a C program that implements heap sort:

```c
// A function to swap two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to heapify a subtree rooted at index i
// n is the size of the heap
void heapify(int arr[], int n, int i) {
  // Find the largest among the root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest])
    largest = left;

  if (right < n && arr[right] > arr[largest])
    largest = right;

  // Swap and continue heapifying if the root is not the largest
  if (largest != i) {
    swap(&arr[i], &arr[largest]);
    heapify(arr, n, largest);
  }
}

// A function to perform heap sort
void heapSort(int arr[], int n) {
  // Build a max-heap from the input array
  for (int i = n / 2 - 1; i >= 0; i--)
    heapify(arr, n, i);

  // Extract the root element and place it at the end of the sorted output array
  for (int i = n - 1; i > 0; i--) {
    swap(&arr[0], &arr[i]);
    // Heapify the reduced heap
    heapify(arr, i, 0);
  }
}

// A function to print an array
void printArray(int arr[], int n) {
  for (int i = 0; i < n; i++)
    printf("%d ", arr[i]);
  printf("\n");
}

// A main function to test the program
int main() {
  int arr[] = {12, 11, 13, 5, 6, 7};
  int n = sizeof(arr) / sizeof(arr[0]);

  printf("Input array: \n");
  printArray(arr, n);

  heapSort(arr, n);

  printf("Sorted array: \n");
  printArray(arr, n);

  return 0;
}
```