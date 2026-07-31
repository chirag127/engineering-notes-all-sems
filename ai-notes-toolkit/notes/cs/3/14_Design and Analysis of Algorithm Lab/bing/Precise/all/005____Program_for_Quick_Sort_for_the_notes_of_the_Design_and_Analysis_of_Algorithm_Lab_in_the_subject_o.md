## Program for Quick Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Quick Sort is a sorting algorithm that uses the divide and conquer approach. It works by selecting a pivot element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The function then recursively sorts the sub-arrays.

Here is an example of a Quick Sort program in C:

```c
#include <stdio.h>

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

int partition (int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);

    for (int j = low; j <= high- 1; j++)
    {
        if (arr[j] <= pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
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
    int arr[] = {10, 7, 8, 9, 1, 5};
    int n = sizeof(arr)/sizeof(arr[0]);
    quickSort(arr, 0, n-1);
    printf("Sorted array: \n");
    printArray(arr, n);
    return 0;
}
```

This program first includes the necessary libraries and defines a `swap` function to swap two elements. The `partition` function takes the array, the starting index, and the ending index as arguments and returns the partition index. The `quickSort` function takes the array, the starting index, and the ending index as arguments and recursively sorts the sub-arrays. The `printArray` function takes the array and its size as arguments and prints the array. The `main` function defines an array, calculates its size, calls the `quickSort` function to sort the array, and then calls the `printArray` function to print the sorted array.

Quick Sort has an average-case time complexity of O(n log n) and a worst-case time complexity of O(n^2). It is an in-place sorting algorithm, meaning it only requires a constant amount of additional memory. It is also a comparison-based sorting algorithm, meaning it only needs to know the order of elements, not their actual values. Quick Sort is not a stable sorting algorithm, meaning the relative order of equal elements is not preserved. However, it can be made stable with some modifications.

Quick Sort is widely used in practice due to its efficiency and simplicity. It is often used as the default sorting algorithm in many programming languages and libraries. However, it is not always the best choice for all situations, and other sorting algorithms may be more suitable depending on the specific use case. It is important to understand the trade-offs and choose the appropriate sorting algorithm for the task at hand.