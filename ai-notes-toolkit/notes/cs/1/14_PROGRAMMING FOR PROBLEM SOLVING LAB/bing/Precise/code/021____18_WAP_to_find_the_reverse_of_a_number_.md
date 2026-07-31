## 18. WAP to find the reverse of a number

Here is an algorithm to find the reverse of a number:

1. Initialize a variable `rev` to 0, which will store the reversed number.
2. While the number is greater than 0, repeat the following steps:
    1. Multiply `rev` by 10 and add the last digit of the number to it.
    2. Remove the last digit from the number by dividing it by 10.
3. The variable `rev` now contains the reversed number.

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

This program takes an integer as input from the user and outputs its reverse. The `while` loop iterates until the number becomes 0. In each iteration, the last digit of the number is obtained using the modulus operator (`%`) and added to `rev` after multiplying it by 10. The last digit is then removed from the number by dividing it by 10. This process continues until the number becomes 0, at which point `rev` contains the reversed number. The reversed number is then printed to the screen.