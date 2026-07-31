## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Merge sort is a sorting algorithm that uses the divide and conquer approach. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which is the sorted list.

Here is an example of a merge sort program in C:

```c
#include <stdio.h>
void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
    int L[n1], R[n2];
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2)
    {
        if (L[i] <= R[j])
        {
            arr[k] = L[i];
            i++;
        }
        else
        {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1)
    {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2)
    {
        arr[k] = R[j];
        j++;
        k++;
    }
}
void mergeSort(int arr[], int l, int r)
{
    if (l < r)
    {
        int m = l + (r - l) / 2;
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
        merge(arr, l, m, r);
    }
}
void printArray(int A[], int size)
{
    int i;
    for (i = 0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}
int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr) / sizeof(arr[0]);
    printf("Given array is \n");
    printArray(arr, arr_size);
    mergeSort(arr, 0, arr_size - 1);
    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
```

This program first defines a function `merge` that takes an array, the left index, the middle index, and the right index as arguments. It then creates two temporary arrays `L` and `R` to store the left and right halves of the array. The function then merges the two halves back into the original array in sorted order.

The `mergeSort` function takes an array, the left index, and the right index as arguments. It recursively divides the array into two halves until the base case is reached, where the sub-array has only one element. It then calls the `merge` function to merge the two halves back into the original array in sorted order.

The `main` function initializes an array and calls the `mergeSort` function to sort the array. It then prints the sorted array.

This is an example of how merge sort can be implemented in C. It is an efficient sorting algorithm with a time complexity of O(n log n) in the worst case. It is also a stable sorting algorithm, meaning that the relative order of equal elements is preserved. It is commonly used in computer science and can be applied to a wide range of problems.