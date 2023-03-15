## Program for Insertion Sort

Insertion sort is a simple sorting algorithm that works by building the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

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

This program sorts an array of integers using the insertion sort algorithm. The function `insertionSort` takes as input an array of integers and its size, and sorts the array in ascending order. The function `printArray` is used to print the sorted array.

The time complexity of insertion sort is O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being simple to implement and understand, and it can be efficient for small datasets or partially sorted data.

This program can be used as a reference for the Design and Analysis of Algorithm Lab in the subject of Real Time System. It is important to understand the working of the insertion sort algorithm and its time complexity in order to analyze its performance and compare it with other sorting algorithms.