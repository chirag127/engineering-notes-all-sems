## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the array and puts it at the beginning.
- The algorithm maintains two subarrays in a given array: one that is already sorted and one that is unsorted.
- The algorithm repeatedly selects the smallest element from the unsorted subarray and swaps it with the leftmost element, and moves the subarray boundaries one element to the right.
- The algorithm has a time complexity of O(n^2), where n is the number of elements in the array.
- The algorithm is not stable, meaning that it does not preserve the relative order of equal elements.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.

- The following is a pseudocode for selection sort:

```
selection_sort(array)
  for i from 0 to n-1
    min_index = i
    for j from i+1 to n
      if array[j] < array[min_index]
        min_index = j
    swap array[i] and array[min_index]
```

- The following is a C program for selection sort:

```c
#include <stdio.h>

// A function to swap two elements
void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort on an array
void selection_sort(int array[], int n)
{
  int i, j, min_index;

  // One by one move boundary of unsorted subarray
  for (i = 0; i < n-1; i++)
  {
    // Find the minimum element in unsorted array
    min_index = i;
    for (j = i+1; j < n; j++)
      if (array[j] < array[min_index])
        min_index = j;

    // Swap the found minimum element with the first element
    swap(&array[min_index], &array[i]);
  }
}

// A function to print an array
void print_array(int array[], int n)
{
  int i;
  for (i = 0; i < n; i++)
    printf("%d ", array[i]);
  printf("\n");
}

// A main function to test the program
int main()
{
  int array[] = {64, 25, 12, 22, 11};
  int n = sizeof(array)/sizeof(array[0]);
  printf("Unsorted array: \n");
  print_array(array, n);
  selection_sort(array, n);
  printf("Sorted array: \n");
  print_array(array, n);
  return 0;
}
```

- The output of the program is:

```
Unsorted array: 
64 25 12 22 11 
Sorted array: 
11 12 22 25 64 
```