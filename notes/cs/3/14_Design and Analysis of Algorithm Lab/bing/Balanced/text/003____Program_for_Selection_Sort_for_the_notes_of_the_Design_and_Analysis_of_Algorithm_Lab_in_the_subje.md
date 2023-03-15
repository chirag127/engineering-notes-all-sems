## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and places it at the beginning.
- The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted subarray, finds the smallest element, and swaps it with the leftmost element of the unsorted subarray, moving the boundary of the sorted subarray by one element to the right.
- The algorithm repeats this process until the entire array is sorted.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the array, as it performs n-1 comparisons for each of the n elements.
- The space complexity of selection sort is O(1), as it only requires a constant amount of auxiliary space to store the index of the minimum element.
- Selection sort is not a stable sorting algorithm, as it may change the relative order of elements with equal values.
- Selection sort is not an adaptive sorting algorithm, as it does not take advantage of the existing order in the input array.
- Selection sort is suitable for small arrays or arrays that are nearly sorted, as it performs fewer swaps than other sorting algorithms.
- Selection sort is easy to implement and understand, but it is inefficient for large or random arrays, as it performs many unnecessary comparisons.

- A pseudocode for selection sort is given below:

```
procedure selection_sort(A : array of items)
   n := length(A)
   for i := 0 to n - 2 do
      min_index := i
      for j := i + 1 to n - 1 do
         if A[j] < A[min_index] then
            min_index := j
         end if
      end for
      if min_index != i then
         swap A[i] and A[min_index]
      end if
   end for
end procedure
```

- A diagram for selection sort is given below:

![Selection sort diagram](https://upload.wikimedia.org/wikipedia/commons/9/94/Selection-Sort-Animation.gif)

- A C program for selection sort is given below:

```
#include <stdio.h>

// A function to swap two elements
void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort on an array
void selection_sort(int arr[], int n) {
  int i, j, min_index;
  // Iterate over the unsorted subarray
  for (i = 0; i < n - 1; i++) {
    // Find the minimum element in the unsorted subarray
    min_index = i;
    for (j = i + 1; j < n; j++) {
      if (arr[j] < arr[min_index]) {
        min_index = j;
      }
    }
    // Swap the minimum element with the leftmost element of the unsorted subarray
    if (min_index != i) {
      swap(&arr[i], &arr[min_index]);
    }
  }
}

// A function to print an array
void print_array(int arr[], int n) {
  int i;
  for (i = 0; i < n; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
}

// A main function to test the selection sort function
int main() {
  int arr[] = {64, 25, 12, 22, 11};
  int n = sizeof(arr) / sizeof(arr[0]);
  printf("Unsorted array: \n");
  print_array(arr, n);
  selection_sort(arr, n);
  printf("Sorted array: \n");
  print_array(arr, n);
  return 0;
}
```