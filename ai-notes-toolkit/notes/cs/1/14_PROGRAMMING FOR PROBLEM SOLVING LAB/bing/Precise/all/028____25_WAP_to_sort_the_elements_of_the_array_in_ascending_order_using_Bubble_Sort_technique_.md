## 25. WAP to sort the elements of the array in ascending order using Bubble Sort technique.

Bubble sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order. The algorithm continues to do this until the entire array is sorted in ascending order. Here is an example of how to implement bubble sort in C:

```c
#include <stdio.h>

void bubbleSort(int arr[], int n)
{
    int i, j, temp;
    for (i = 0; i < n-1; i++)
    {
        for (j = 0; j < n-i-1; j++)
        {
            if (arr[j] > arr[j+1])
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main()
{
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr)/sizeof(arr[0]);
    bubbleSort(arr, n);
    printf("Sorted array: \n");
    for (int i=0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
    return 0;
}
```

This code defines a function `bubbleSort` that takes an array of integers and its size as arguments. The function uses two nested loops to iterate over the array. In each iteration, the function compares adjacent elements and swaps them if the first element is greater than the second. This process continues until the entire array is sorted.

The `main` function initializes an array of integers and calls the `bubbleSort` function to sort the array. The sorted array is then printed to the standard output.