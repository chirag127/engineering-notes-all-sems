## 30. WAP to swap two elements using the concept of pointers.

- A pointer is a variable that stores the address of another variable in memory.
- To swap two elements using pointers, we need to pass the addresses of the elements to a function that will swap their values using a temporary variable.
- The function will use the dereference operator (*) to access the values pointed by the pointers and assign them to the temporary variable and vice versa.
- The function will not return anything, but the changes will be reflected in the original variables as they are passed by reference.
- Here is an example of a C program that swaps two integers using pointers:

```c
#include <stdio.h>

// A function that swaps the values of two integers pointed by a and b
void swap(int *a, int *b) {
  // Declare a temporary variable
  int temp;
  // Assign the value pointed by a to temp
  temp = *a;
  // Assign the value pointed by b to the value pointed by a
  *a = *b;
  // Assign the value of temp to the value pointed by b
  *b = temp;
}

int main() {
  // Declare and initialize two integers
  int x = 10, y = 20;
  // Print their values before swapping
  printf("Before swapping: x = %d, y = %d\n", x, y);
  // Call the swap function and pass the addresses of x and y
  swap(&x, &y);
  // Print their values after swapping
  printf("After swapping: x = %d, y = %d\n", x, y);
  return 0;
}
```

- The output of the program will be:

```
Before swapping: x = 10, y = 20
After swapping: x = 20, y = 10
```