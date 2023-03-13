## 22.WAP that inputs two arrays and saves sum of corresponding elements of these arrays in a third array and prints them.

- This is a program that performs the operation of adding two arrays element-wise and storing the result in a third array.
- To write this program, we need to follow these steps:
  - Declare and initialize three arrays of the same size, say `a`, `b`, and `c`.
  - Use a loop to iterate over the elements of the arrays, say `i` from `0` to `n-1`, where `n` is the size of the arrays.
  - In each iteration, add the corresponding elements of `a` and `b` and store the result in `c`, i.e. `c[i] = a[i] + b[i]`.
  - After the loop, print the elements of `c` using another loop or a built-in function.
- Here is an example of the program in C language:

```c
#include <stdio.h>
#define SIZE 5 // define the size of the arrays

int main()
{
  int a[SIZE] = {1, 2, 3, 4, 5}; // initialize the first array
  int b[SIZE] = {6, 7, 8, 9, 10}; // initialize the second array
  int c[SIZE]; // declare the third array
  int i; // declare the loop variable

  // loop to add the elements of a and b and store in c
  for (i = 0; i < SIZE; i++)
  {
    c[i] = a[i] + b[i];
  }

  // loop to print the elements of c
  for (i = 0; i < SIZE; i++)
  {
    printf("%d ", c[i]);
  }
  printf("\n");

  return 0;
}
```

- The output of the program is:

```
7 9 11 13 15
```

- Some mnemonics and learning tricks for this program are:
  - Remember that the size of the arrays must be the same, otherwise the addition will not be possible.
  - Remember that the index of the arrays starts from 0 and ends at n-1, where n is the size of the arrays.
  - Remember that the loop variable must be initialized, updated, and checked in the loop condition, otherwise the loop may not work properly.
  - Remember that the addition of two arrays is done element-wise, i.e. the first element of the first array is added to the first element of the second array, and so on.
  - Remember that the result of the addition is stored in the third array, not in the first or the second array.
  - Remember that the elements of the third array must be printed after the addition is done, otherwise the output will not be correct.