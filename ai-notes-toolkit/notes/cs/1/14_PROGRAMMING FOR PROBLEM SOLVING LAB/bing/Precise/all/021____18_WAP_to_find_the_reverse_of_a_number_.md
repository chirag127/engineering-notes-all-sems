## 18. WAP to find the reverse of a number

Here is an algorithm to find the reverse of a number:

1. Initialize a variable `rev` to 0, which will store the reverse of the number.
2. While the number is greater than 0, repeat the following steps:
    1. Multiply `rev` by 10 and add the last digit of the number to it.
    2. Remove the last digit from the number by dividing it by 10.
3. `rev` now contains the reverse of the original number.

Here is an example of a program in C language that implements the above algorithm:

```c
#include <stdio.h>

int main()
{
    int n, rev = 0, remainder;
    printf("Enter an integer: ");
    scanf("%d", &n);
    while (n != 0)
    {
        remainder = n % 10;
        rev = rev * 10 + remainder;
        n /= 10;
    }
    printf("Reversed number = %d", rev);
    return 0;
}
```

This program takes an integer as input from the user and stores it in the variable `n`. The `while` loop runs until `n` is not equal to 0. In each iteration of the loop, the last digit of `n` is obtained using the modulus operator (`%`) and added to `rev` after multiplying `rev` by 10. Then, the last digit is removed from `n` by dividing it by 10. Finally, the reversed number is printed using the `printf` function.