## 5. WAP that swaps values of two variables using a third variable.

Swapping the values of two variables means exchanging their values. For example, if variable `a` has the value `5` and variable `b` has the value `10`, after swapping, `a` will have the value `10` and `b` will have the value `5`.

Here is an example of a program that swaps the values of two variables using a third variable in the C programming language:

```c
#include <stdio.h>

int main()
{
    int a = 5, b = 10, temp;

    printf("Before swapping: a = %d, b = %d\n", a, b);

    temp = a;
    a = b;
    b = temp;

    printf("After swapping: a = %d, b = %d\n", a, b);

    return 0;
}
```

In this program, we use a third variable `temp` to temporarily store the value of `a`. Then, we assign the value of `b` to `a` and the value of `temp` (which is the original value of `a`) to `b`. This way, the values of `a` and `b` are swapped.

This method of swapping values using a third variable is commonly used in many programming languages. It is simple and easy to understand. However, there are other methods to swap values without using a third variable, such as using arithmetic operations or bitwise XOR. These methods can be more efficient in some cases, but they may be more difficult to understand for beginners.