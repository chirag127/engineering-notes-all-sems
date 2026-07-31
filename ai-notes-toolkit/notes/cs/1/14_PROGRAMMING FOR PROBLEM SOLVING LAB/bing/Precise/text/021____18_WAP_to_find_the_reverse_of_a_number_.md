## 18. WAP to find the reverse of a number.

Here is an algorithm to find the reverse of a number:

1. Initialize a variable `reverse` to 0.
2. While the number is greater than 0:
    1. Multiply `reverse` by 10.
    2. Add the last digit of the number to `reverse`.
    3. Remove the last digit from the number by dividing it by 10.
3. The value of `reverse` is the reverse of the original number.

Here is an example of a program in C language that implements this algorithm:

```c
#include <stdio.h>

int main()
{
    int n, reverse = 0, remainder;

    printf("Enter an integer: ");
    scanf("%d", &n);

    while(n != 0)
    {
        remainder = n % 10;
        reverse = reverse * 10 + remainder;
        n /= 10;
    }

    printf("Reversed number = %d", reverse);

    return 0;
}
```

This program prompts the user to enter an integer, then calculates its reverse using the algorithm described above. The reversed number is then printed to the screen.