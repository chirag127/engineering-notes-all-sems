## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here is an example of how the insertion sort algorithm works:

1. Start by iterating over the array, starting from the second element (index 1).
2. Compare the current element with the previous element.
3. If the current element is smaller than the previous element, swap the two elements.
4. Continue comparing the current element with the previous elements until it is no longer smaller than the previous element or until the first element is reached.
5. Repeat the process for the next element in the array until the entire array is sorted.

Here is an example of a program that implements the insertion sort algorithm in C:

```c
#include <stdio.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes an array and its length as arguments and sorts the array in place.