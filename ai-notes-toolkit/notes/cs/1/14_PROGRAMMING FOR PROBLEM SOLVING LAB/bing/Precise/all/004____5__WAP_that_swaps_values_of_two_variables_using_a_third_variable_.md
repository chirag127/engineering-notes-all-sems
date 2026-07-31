## 5. WAP that swaps values of two variables using a third variable.

Swapping the values of two variables means exchanging their values. For example, if variable `a` has the value `5` and variable `b` has the value `10`, after swapping, variable `a` will have the value `10` and variable `b` will have the value `5`.

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

In this program, we first declare three integer variables `a`, `b`, and `temp`. We assign the values `5` and `10` to `a` and `b` respectively. We then print the values of `a` and `b` before swapping.

Next, we use the `temp` variable to temporarily store the value of `a`. We then assign the value of `b` to `a` and the value of `temp` (which is the original value of `a`) to `b`. This effectively swaps the values of `a` and `b`.

Finally, we print the values of `a` and `b` after swapping.

This is one way to swap the values of two variables using a third variable. There are other ways to achieve the same result, such as using arithmetic operations or bitwise operations, but using a third variable is a simple and straightforward method.