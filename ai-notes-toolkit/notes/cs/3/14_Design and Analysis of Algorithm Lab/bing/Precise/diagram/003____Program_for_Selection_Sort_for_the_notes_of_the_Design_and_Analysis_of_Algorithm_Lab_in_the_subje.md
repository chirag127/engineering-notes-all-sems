## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is an in-place comparison-based sorting algorithm. Here is a step-by-step guide on how the algorithm works:

1. The algorithm divides the input list into two parts: the sublist of items already sorted, which is built up from left to right at the front (left) of the list, and the sublist of items remaining to be sorted that occupy the rest of the list.
2. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list.
3. The algorithm proceeds by finding the smallest (or largest, depending on the sorting order) element in the unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in sorted order), and moving the sublist boundaries one element to the right.

Here is an example of a selection sort program in C:

```c
#include <stdio.h>

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

void selectionSort(int arr[], int n)
{
    int i, j, min_idx;

    for (i = 0; i < n-1; i++)
    {
        min_idx = i;
        for (j = i+1; j < n; j++)
          if (arr[j] < arr[min_idx])
            min_idx = j;

        swap(&arr[min_idx], &arr[i]);
    }
}

void printArray(int arr[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

int main()
{
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
```

This program sorts an array of integers using the selection sort algorithm. The `swap` function is used to exchange the values of two variables. The `selectionSort` function implements the selection sort algorithm, and the `printArray` function is used to print the sorted array.

Selection sort has a time complexity of O(n^2) in the worst, average, and best cases, where n is the number of elements in the input list. This makes it inefficient on large lists and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.