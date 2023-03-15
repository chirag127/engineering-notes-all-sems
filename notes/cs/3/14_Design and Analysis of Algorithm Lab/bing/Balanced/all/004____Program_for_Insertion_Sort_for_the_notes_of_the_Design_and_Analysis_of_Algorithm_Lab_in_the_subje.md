## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by comparing each element of an array with the previous elements and inserting it in the correct position.
- The algorithm starts from the second element of the array and iterates until the last element, assuming that the first element is already sorted.
- At each iteration, the current element is compared with the previous elements in the sorted part of the array and shifted to the right until it finds its correct position.
- The algorithm has a time complexity of O(n^2) in the worst case, when the array is in reverse order, and O(n) in the best case, when the array is already sorted.
- The algorithm is stable, meaning that it preserves the relative order of equal elements, and in-place, meaning that it does not use extra space.
- The algorithm is suitable for small arrays or arrays that are nearly sorted, as it has a low overhead and a fast best case.
- The algorithm can be implemented in any programming language that supports arrays and comparison operators. Here is an example of the algorithm in C:

```c
// A function to sort an array using insertion sort
void insertionSort(int arr[], int n) {
  // Loop from the second element to the last element
  for (int i = 1; i < n; i++) {
    // Store the current element in a temporary variable
    int key = arr[i];
    // Initialize a variable to store the index of the previous element
    int j = i - 1;
    // Loop through the sorted part of the array and compare the key with each element
    while (j >= 0 && arr[j] > key) {
      // Shift the element to the right if it is greater than the key
      arr[j + 1] = arr[j];
      // Decrement the index of the previous element
      j--;
    }
    // Insert the key in the correct position
    arr[j + 1] = key;
  }
}
```