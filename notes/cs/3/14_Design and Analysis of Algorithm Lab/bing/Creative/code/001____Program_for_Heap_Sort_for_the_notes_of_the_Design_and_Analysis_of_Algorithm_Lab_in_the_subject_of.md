## Program for Heap Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Heap sort is a comparison-based sorting algorithm that uses a binary heap data structure to sort a given array of elements.
- A binary heap is a complete binary tree that satisfies the heap property, which means that every node is greater than or equal to its children (max-heap) or less than or equal to its children (min-heap).
- The basic idea of heap sort is to build a max-heap or a min-heap from the input array, and then repeatedly extract the root element (which is the maximum or minimum element) and place it at the end of the sorted array, until the heap is empty.
- The algorithm can be implemented as follows:

```
// A function to swap two elements in an array
void swap(int arr[], int i, int j) {
  int temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

// A function to heapify a subtree rooted at index i in an array of size n
// This function assumes that the subtrees rooted at i's children are already heapified
void heapify(int arr[], int n, int i) {
  // Find the largest among the root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest]) {
    largest = left;
  }

  if (right < n && arr[right] > arr[largest]) {
    largest = right;
  }

  // If the largest is not the root, swap it with the root and heapify the affected subtree
  if (largest != i) {
    swap(arr, i, largest);
    heapify(arr, n, largest);
  }
}

// A function to perform heap sort on an array of size n
void heapSort(int arr[], int n) {
  // Build a max-heap from the input array
  for (int i = n / 2 - 1; i >= 0; i--) {
    heapify(arr, n, i);
  }

  // Extract the root element and place it at the end of the sorted array
  // Repeat this process until the heap is empty
  for (int i = n - 1; i > 0; i--) {
    swap(arr, 0, i);
    heapify(arr, i, 0);
  }
}
```

- The time complexity of heap sort is O(n log n) in the worst, average and best cases, as the heapify function takes O(log n) time and is called n times in the algorithm.
- The space complexity of heap sort is O(1), as it only requires a constant amount of auxiliary space to perform the swaps.
- Heap sort is an in-place and unstable sorting algorithm, as it does not preserve the relative order of equal elements in the input array.
- Heap sort is suitable for sorting large data sets, as it can handle them efficiently and does not require additional memory. However, it is not very adaptive, as it does not take advantage of the existing order in the input array.