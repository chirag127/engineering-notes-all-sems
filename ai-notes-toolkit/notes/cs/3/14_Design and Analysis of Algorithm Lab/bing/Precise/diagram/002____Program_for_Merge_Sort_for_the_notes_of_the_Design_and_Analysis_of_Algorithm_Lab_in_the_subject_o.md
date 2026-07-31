## Program for Merge Sort

Merge sort is a sorting algorithm that uses the divide and conquer approach to sort a list of elements. It works by dividing the unsorted list into n sub-lists, each containing one element, and then repeatedly merging sub-lists to produce new sorted sub-lists until there is only one sub-list remaining, which will be the sorted list.

Here is the algorithm for merge sort:

1. If the list is of length 0 or 1, return the list.
2. Divide the list into two smaller sub-lists by splitting it in half.
3. Recursively sort each of the two sub-lists by calling merge sort on them.
4. Merge the two sub-lists back into one sorted list.

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

This program first defines the `merge` function, which takes in an array, the left index, the middle index, and the right index, and merges the two sub-arrays defined by these indices. The `mergeSort` function then uses this `merge` function to recursively sort the array by dividing it in half and sorting each half, then merging the two halves back together. The `main` function demonstrates how to use the `mergeSort` function to sort an array of integers.

This is the basic idea behind the merge sort algorithm and an example implementation in C. It is an efficient sorting algorithm with a time complexity of O(n log n) in the worst case. It is commonly used in the Design and Analysis of Algorithm Lab in the subject of Real Time System.