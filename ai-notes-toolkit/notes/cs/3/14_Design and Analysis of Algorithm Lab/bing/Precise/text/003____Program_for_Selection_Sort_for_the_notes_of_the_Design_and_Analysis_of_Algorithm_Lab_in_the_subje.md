## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. Here are the steps to implement selection sort:

1. Start from the first element of the array and find the minimum element in the unsorted part of the array.
2. Swap the minimum element with the first element of the unsorted part.
3. Move the boundary of the unsorted part one element to the right.
4. Repeat the above steps until the entire array is sorted.

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

This program first defines a `swap` function that swaps the values of two variables. The `selectionSort` function takes an array and its size as arguments and sorts the array using the selection sort algorithm. The `printArray` function prints the elements of the array. In the `main` function, we define an array, call the `selectionSort` function to sort it, and then print the sorted array using the `printArray` function.

Selection sort has a time complexity of O(n^2) in the worst case, where n is the number of elements in the array. This makes it inefficient for large datasets. However, it is easy to understand and implement, and can be useful for small datasets or as a part of more complex algorithms.