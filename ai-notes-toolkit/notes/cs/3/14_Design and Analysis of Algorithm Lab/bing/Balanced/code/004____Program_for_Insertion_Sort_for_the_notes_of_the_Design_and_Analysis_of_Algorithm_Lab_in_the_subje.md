## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by inserting each element of the unsorted array into its correct position in the sorted array.
- The algorithm starts from the second element of the array and compares it with the first element. If the second element is smaller than the first element, it swaps them. Otherwise, it leaves them as they are.
- Then, the algorithm moves to the third element and compares it with the first and second elements. If the third element is smaller than any of the previous elements, it inserts it into its correct position by shifting the larger elements to the right. Otherwise, it leaves it as it is.
- The algorithm repeats this process for each element of the array until the entire array is sorted.
- The algorithm can be implemented in any programming language that supports arrays and comparison operators. Here is an example of the algorithm in C language:

```c
// Function to sort an array using insertion sort
void insertionSort(int arr[], int n) {
  // Loop from the second element to the last element
  for (int i = 1; i < n; i++) {
    // Store the current element in a temporary variable
    int key = arr[i];
    // Initialize the index of the previous element
    int j = i - 1;
    // Loop backwards from the current element and compare it with the previous elements
    while (j >= 0 && arr[j] > key) {
      // Shift the larger element to the right
      arr[j + 1] = arr[j];
      // Decrement the index of the previous element
      j = j - 1;
    }
    // Insert the current element into its correct position
    arr[j + 1] = key;
  }
}
```
- The time complexity of insertion sort is O(n^2) in the worst case, when the array is in reverse order. In the best case, when the array is already sorted, the time complexity is O(n). The average case time complexity is also O(n^2).
- The space complexity of insertion sort is O(1), as it only requires a constant amount of auxiliary space for the temporary variable and the loop indices.
- Insertion sort is a stable sorting algorithm, as it preserves the relative order of equal elements in the array.
- Insertion sort is an adaptive sorting algorithm, as it performs faster for partially sorted arrays than for random arrays.
- Insertion sort is suitable for small arrays or arrays that are nearly sorted, as it has a low overhead and a simple implementation. However, it is not efficient for large arrays or arrays that are very unsorted, as it requires many comparisons and shifts.