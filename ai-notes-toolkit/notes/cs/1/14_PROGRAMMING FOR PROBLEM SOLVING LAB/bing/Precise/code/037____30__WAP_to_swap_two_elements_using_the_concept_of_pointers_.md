## 30. WAP to swap two elements using the concept of pointers.

Here is an example of a program that swaps two elements using the concept of pointers:

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

In this program, the `swap` function takes two pointers to integers as arguments. The function uses a temporary variable to store the value of the first integer, then assigns the value of the second integer to the first integer, and finally assigns the value of the temporary variable to the second integer. This effectively swaps the values of the two integers.

In the `main` function, we define two integers `x` and `y` and print their values before swapping. Then we call the `swap` function, passing the addresses of `x` and `y` as arguments. This allows the `swap` function to modify the values of `x` and `y` directly. Finally, we print the values of `x` and `y` after swapping.
