## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- A WAP (write a program) is a task that requires writing code in a specific programming language to achieve a desired output or functionality.
- In this task, the input is two arrays of the same size, which are collections of data elements of the same type, such as integers, characters, or strings.
- The output is a third array of the same size as the input arrays, which contains the sum of the corresponding elements of the input arrays at each index.
- For example, if the input arrays are [1, 2, 3] and [4, 5, 6], then the output array is [5, 7, 9].
- To write a program that performs this task, we need to follow these steps:

  - Declare and initialize the input arrays with some values, or take the input from the user using a loop or a function.
  - Declare an empty output array of the same size as the input arrays.
  - Use a loop to iterate over the elements of the input arrays, and for each iteration, add the corresponding elements of the input arrays and store the result in the output array at the same index.
  - Use another loop or a function to print the elements of the output array.

- Here is an example of a program that performs this task in C language:

```c
#include <stdio.h>
#define SIZE 3 // define the size of the arrays

int main()
{
  // declare and initialize the input arrays
  int arr1[SIZE] = {1, 2, 3};
  int arr2[SIZE] = {4, 5, 6};

  // declare an empty output array
  int arr3[SIZE];

  // use a loop to iterate over the elements of the input arrays
  for (int i = 0; i < SIZE; i++)
  {
    // add the corresponding elements of the input arrays and store the result in the output array
    arr3[i] = arr1[i] + arr2[i];
  }

  // use another loop to print the elements of the output array
  printf("The output array is:\n");
  for (int i = 0; i < SIZE; i++)
  {
    printf("%d ", arr3[i]);
  }
  printf("\n");

  return 0;
}
```

- The output of this program is:

```
The output array is:
5 7 9
```