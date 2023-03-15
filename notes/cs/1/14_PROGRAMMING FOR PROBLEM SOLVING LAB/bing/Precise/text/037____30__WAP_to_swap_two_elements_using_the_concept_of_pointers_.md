## 30. WAP to swap two elements using the concept of pointers.

Here is an example of a program that swaps two elements using the concept of pointers in C language:

```c
#include <stdio.h>

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x = 5, y = 10;
    printf("Before swapping: x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After swapping: x = %d, y = %d\n", x, y);
    return 0;
}
```

- In this program, the `swap` function takes two pointers to integers as arguments.
- The function uses a temporary variable `temp` to store the value of the first integer pointed to by `a`.
- Then, the value of the first integer is changed to the value of the second integer pointed to by `b`.
- Finally, the value of the second integer is changed to the value stored in the temporary variable `temp`.
- In the `main` function, two integers `x` and `y` are declared and initialized.
- The `swap` function is called with the addresses of `x` and `y` as arguments, using the `&` operator.
- After the function call, the values of `x` and `y` are swapped.
