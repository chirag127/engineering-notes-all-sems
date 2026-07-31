## Program for Selection Sort for the notes of the Design and Analysis of Algorithm Lab in the subject of Real Time System

- Selection sort is a simple and easy-to-understand sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list.
- Selection sort is an in-place sorting algorithm, which means it does not require any additional memory to sort the list.
- Selection sort has a best-case and average-case time complexity of O(n^2), making it efficient for small data sets. It is easy to modify to sort in ascending or descending order.
- Selection sort is not difficult to analyze compared to other sorting algorithms, since none of the loops depend on the data in the array. Selecting the minimum requires scanning n elements (taking n-1 comparisons) and then swapping it into the first position. Finding the next minimum requires scanning the remaining n-1 elements and so on, for (n-1) + (n-2) + ... + 2 + 1 = n(n-1)/2 comparisons. Each of these scans requires one swap for n-1 elements. Therefore, the total number of comparisons is n(n-1)/2 and the total number of swaps is n-1.
- The pseudocode for selection sort is as follows:

```
selection_sort(array)
  for i from 0 to length(array) - 2
    min_index = i
    for j from i + 1 to length(array) - 1
      if array[j] < array[min_index]
        min_index = j
    swap array[i] and array[min_index]
```

- The following diagram illustrates the selection sort algorithm on an example array of 8 elements:

![Selection sort diagram](https://www.simplilearn.com/ice9/free_resources_article_thumb/Selection-Sort-Algorithm.jpg)

- The following is an example of a C program for selection sort:

```
#include <stdio.h>

// A function to swap two elements
void swap(int *a, int *b)
{
  int temp = *a;
  *a = *b;
  *b = temp;
}

// A function to perform selection sort
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

// A function to print an array of size n
void print_array(int array[], int n)
{
  int i;
  for (i=0; i < n; i++)
    printf("%d ", array[i]);
  printf("\n");
}

// Driver program to test above functions
int main()
{
  int array[] = {64, 25, 12, 22, 11};
  int n = sizeof(array)/sizeof(array[0]);
  selection_sort(array, n);
  printf("Sorted array: \n");
  print_array(array, n);
  return 0;
}
```

- The output of the program is:

```
Sorted array: 
11 12 22 25 64
```