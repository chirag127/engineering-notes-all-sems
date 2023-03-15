## Program for Merge Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Merge sort is a sorting algorithm that uses the divide-and-conquer approach to sort a list of elements. The algorithm works by dividing the unsorted list into n sublists, each containing one element, and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining, which will be the sorted list.

Here is the algorithm for merge sort:

1. If the list is of length 0 or 1, return the list.
2. Divide the list into two smaller sublists by splitting it in half.
3. Recursively sort each of the two sublists by calling merge sort on them.
4. Merge the two sorted sublists back into one sorted list.

Here is an example implementation of merge sort in C:

```c
#include <stdio.h>

void merge(int arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 =  r - m;

    int L[n1], R[n2];

    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1+ j];

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
        int m = l+(r-l)/2;

        mergeSort(arr, l, m);
        mergeSort(arr, m+1, r);

        merge(arr, l, m, r);
    }
}

void printArray(int A[], int size)
{
    int i;
    for (i=0; i < size; i++)
        printf("%d ", A[i]);
    printf("\n");
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int arr_size = sizeof(arr)/sizeof(arr[0]);

    printf("Given array is \n");
    printArray(arr, arr_size);

    mergeSort(arr, 0, arr_size - 1);

    printf("\nSorted array is \n");
    printArray(arr, arr_size);
    return 0;
}
```

This program first defines a `merge` function that takes in an array, the left index, the middle index, and the right index, and merges the two subarrays `arr[l..m]` and `arr[m+1..r]` into one sorted array. The `mergeSort` function takes in an array, the left index, and the right index, and recursively sorts the array by dividing it into two subarrays, sorting each subarray, and then merging the two sorted subarrays back into one sorted array. The `main` function defines an array, prints the given array, calls the `mergeSort` function to sort the array, and then prints the sorted array.

This is an example of how merge sort can be implemented in C. The time complexity of merge sort is O(nlogn) in the worst case, which makes it an efficient sorting algorithm for large datasets. It is also a stable sorting algorithm, meaning that it maintains the relative order of equal elements in the sorted list. However, it requires additional space to store the subarrays during the merging process, which can make it less space-efficient than other sorting algorithms.