## 30. WAP to swap two elements using the concept of pointers.

- A pointer is a variable that stores the address of another variable in memory.
- To swap two elements using pointers, we need to pass the addresses of the elements to a function that will swap their values using a temporary variable.
- The function will use the dereference operator (*) to access the values pointed by the pointers and assign them to the temporary variable and vice versa.
- The function will not return anything, but the changes will be reflected in the original variables as they are passed by reference.
- Here is an example of a C program that swaps two integers using pointers:

```c
#include <stdio.h>

// A function that swaps the values of two integers pointed by x and y
void swap(int *x, int *y)
{
    // Declare a temporary variable
    int temp;

    // Store the value pointed by x in temp
    temp = *x;

    // Assign the value pointed by y to the location pointed by x
    *x = *y;

    // Assign the value of temp to the location pointed by y
    *y = temp;
}

int main()
{
    // Declare and initialize two integers
    int a = 10, b = 20;

    // Print the original values of a and b
    printf("Before swapping: a = %d, b = %d\n", a, b);

    // Call the swap function and pass the addresses of a and b
    swap(&a, &b);

    // Print the swapped values of a and b
    printf("After swapping: a = %d, b = %d\n", a, b);

    return 0;
}
```

- The output of the program is:

```
Before swapping: a = 10, b = 20
After swapping: a = 20, b = 10
```