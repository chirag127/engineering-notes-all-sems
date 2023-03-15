## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here are the steps for implementing insertion sort:

1. Start by iterating through the array from the second element to the last element.
2. For each element, compare it with the elements before it.
3. If the current element is smaller than the previous element, swap them.
4. Continue swapping until the current element is in its correct position.
5. Repeat the process for the next element until the entire array is sorted.

Here is an example of insertion sort implemented in C:

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

void printArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes in an array and its size as arguments and sorts the array in ascending order. The `printArray` function is used to print the sorted array.

Insertion sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being simple to implement and can be useful for small datasets or partially sorted data. It is also a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted output.