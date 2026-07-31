## 30. WAP to swap two elements using the concept of pointers.

Here is a C program that demonstrates how to swap two elements using the concept of pointers:

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

In this program, the `swap` function takes two pointers to integers as arguments. The function uses a temporary variable `temp` to store the value of the first integer, then assigns the value of the second integer to the first integer, and finally assigns the value of `temp` to the second integer. This effectively swaps the values of the two integers.

In the `main` function, we define two integers `x` and `y` and print their values before swapping. Then we call the `swap` function, passing the addresses of `x` and `y` as arguments. This allows the `swap` function to modify the values of `x` and `y` directly. Finally, we print the values of `x` and `y` after swapping.

This program demonstrates how pointers can be used to pass the addresses of variables to a function, allowing the function to modify the values of those variables directly. This is a powerful feature of the C language that allows for more efficient and flexible code.