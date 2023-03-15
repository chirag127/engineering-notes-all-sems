## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

Here is the algorithm for insertion sort:

1. Start from the second element of the array (element at index 1).
2. Compare the current element with the element before it.
3. If the current element is smaller than the element before it, swap them.
4. Continue comparing the current element with the elements before it and swapping them until the current element is in its correct position.
5. Move to the next element and repeat the process until the last element is reached.

Here is an example of a program for insertion sort in C:

```c
#include <stdio.h>

void insertionSort(int arr[], int n)
{
    int i, key, j;
    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i - 1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

void printArray(int arr[], int n)
{
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, n);
    printArray(arr, n);

    return 0;
}
```

This program sorts an array of integers using the insertion sort algorithm. The `insertionSort` function takes an array and its size as arguments and sorts the array in ascending order. The `printArray` function is used to print the sorted array.