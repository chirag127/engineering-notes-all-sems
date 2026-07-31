Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to sort the elements of the array in ascending order using Bubble Sort technique. Here is the content in markdown format:

## 25.WAP to sort the elements of the array in ascending order using Bubble Sort technique.

- Bubble Sort is a simple sorting algorithm that compares adjacent elements in an array and swaps them if they are in the wrong order.
- The algorithm repeats this process until the array is sorted.
- The algorithm can be implemented in any programming language, but here we will use C as an example.
- The steps of the algorithm are as follows:

  - Declare an array of integers and initialize it with some values.
  - Declare a variable to store the size of the array.
  - Declare two loop variables i and j for iterating over the array.
  - Declare a temporary variable to store the value of an element during swapping.
  - Start a loop from i = 0 to i < size - 1, where size is the size of the array.
  - Inside the loop, start another loop from j = 0 to j < size - i - 1.
  - Inside the inner loop, compare the elements at index j and j + 1 in the array.
  - If the element at index j is greater than the element at index j + 1, swap them using the temporary variable.
  - End the inner loop.
  - End the outer loop.
  - Print the sorted array.

- The code for the algorithm in C is as follows:

```c
#include <stdio.h>

int main()
{
  // Declare an array of integers and initialize it with some values
  int arr[] = {5, 3, 8, 2, 6, 1, 9, 4, 7};
  // Declare a variable to store the size of the array
  int size = sizeof(arr) / sizeof(arr[0]);
  // Declare two loop variables i and j for iterating over the array
  int i, j;
  // Declare a temporary variable to store the value of an element during swapping
  int temp;
  // Start a loop from i = 0 to i < size - 1, where size is the size of the array
  for (i = 0; i < size - 1; i++)
  {
    // Inside the loop, start another loop from j = 0 to j < size - i - 1
    for (j = 0; j < size - i - 1; j++)
    {
      // Inside the inner loop, compare the elements at index j and j + 1 in the array
      if (arr[j] > arr[j + 1])
      {
        // If the element at index j is greater than the element at index j + 1, swap them using the temporary variable
        temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
    }
  }
  // Print the sorted array
  printf("The sorted array is:\n");
  for (i = 0; i < size; i++)
  {
    printf("%d ", arr[i]);
  }
  printf("\n");
  return 0;
}
```
- The output of the code is as follows:

```text
The sorted array is:
1 2 3 4 5 6 7 8 9
```