## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

Selection sort is a simple sorting algorithm that sorts an array by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part. Here is the algorithm for selection sort:

1. Find the minimum element in the unsorted array.
2. Swap the found minimum element with the first element of the unsorted part.
3. Move the boundary of the unsorted part one element to the right.
4. Repeat steps 1-3 until the entire array is sorted.

Here is an example of a selection sort program in C:

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr)/sizeof(arr[0]);
    selectionSort(arr, n);
    printf("Sorted array: \n");
    for (int i=0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

This program sorts an array of integers using the selection sort algorithm. The `selectionSort` function takes as input the array to be sorted and its size, and sorts the array in place. The `main` function initializes an array of integers, calls the `selectionSort` function to sort the array, and then prints the sorted array.

Selection sort has a time complexity of O(n^2), where n is the number of elements in the array. This makes it inefficient for large datasets. However, it has the advantage of being easy to understand and implement.