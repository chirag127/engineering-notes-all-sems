## Program for Insertion Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Insertion sort is a simple sorting algorithm that works by comparing each element of an array with the previous elements and inserting it in the correct position.
- The algorithm starts from the second element of the array and iterates until the last element.
- For each element, it compares it with the elements on its left and shifts them to the right until it finds the correct position to insert the element.
- The algorithm maintains a sorted subarray on the left of the current element and an unsorted subarray on the right of the current element.
- The algorithm has a time complexity of O(n^2) in the worst case and O(n) in the best case, where n is the number of elements in the array.
- The algorithm is stable, meaning that it preserves the relative order of equal elements in the array.
- The algorithm is adaptive, meaning that it performs better on partially sorted arrays than on random arrays.
- The algorithm is in-place, meaning that it does not require extra space to sort the array.
- The algorithm is suitable for small arrays or arrays that are nearly sorted.

- The following is a pseudocode for insertion sort:

```
insertion_sort(array)
  for i = 1 to length(array) - 1
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key
      array[j + 1] = array[j]
      j = j - 1
    array[j + 1] = key
  return array
```

- The following is a C program for insertion sort:

```
#include <stdio.h>

void insertion_sort(int array[], int n)
{
  int i, j, key;
  for (i = 1; i < n; i++)
  {
    key = array[i];
    j = i - 1;
    while (j >= 0 && array[j] > key)
    {
      array[j + 1] = array[j];
      j = j - 1;
    }
    array[j + 1] = key;
  }
}

void print_array(int array[], int n)
{
  int i;
  for (i = 0; i < n; i++)
  {
    printf("%d ", array[i]);
  }
  printf("\n");
}

int main()
{
  int array[] = {5, 2, 4, 6, 1, 3};
  int n = sizeof(array) / sizeof(array[0]);
  printf("Unsorted array: ");
  print_array(array, n);
  insertion_sort(array, n);
  printf("Sorted array: ");
  print_array(array, n);
  return 0;
}
```

- The following is the output of the C program:

```
Unsorted array: 5 2 4 6 1 3
Sorted array: 1 2 3 4 5 6
```