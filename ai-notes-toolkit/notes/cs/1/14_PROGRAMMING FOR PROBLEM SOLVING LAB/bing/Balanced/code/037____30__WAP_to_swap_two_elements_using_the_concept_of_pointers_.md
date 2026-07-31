## 30. WAP to swap two elements using the concept of pointers.

- A pointer is a variable that stores the address of another variable.
- To swap two elements using pointers, we need to pass the addresses of the elements to a function that will swap their values.
- The function will use a temporary variable to store the value of one element, then assign the value of the other element to the first element, and then assign the value of the temporary variable to the second element.
- The function will not return anything, as the changes will be reflected in the original variables.
- The syntax of the function is:

```c
void swap(int *a, int *b)
{
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}
```

- The main function will declare two variables and initialize them with some values.
- It will also declare two pointers and assign them the addresses of the variables using the & operator.
- It will print the values of the variables before and after calling the swap function.
- The syntax of the main function is:

```c
#include <stdio.h>
int main()
{
    int x = 10, y = 20;
    int *p, *q;
    p = &x;
    q = &y;
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(p, q);
    printf("After swapping: x = %d, y = %d\n", x, y);
    return 0;
}
```

- The output of the program is:

```c
Before swapping: x = 10, y = 20
After swapping: x = 20, y = 10
```