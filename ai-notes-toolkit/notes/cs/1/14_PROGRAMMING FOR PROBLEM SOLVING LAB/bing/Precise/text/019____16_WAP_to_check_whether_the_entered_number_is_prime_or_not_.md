## 16. WAP to check whether the entered number is prime or not.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. To check if a number is prime or not, we can follow these steps:

1. Take input from the user and store it in a variable, let's say `n`.
2. Initialize a variable `flag` to 0.
3. Run a loop from 2 to `n/2`.
4. For each iteration, check if `n` is divisible by the current loop variable.
5. If `n` is divisible, set `flag` to 1 and break the loop.
6. After the loop, check the value of `flag`.
7. If `flag` is 0, the number is prime. Otherwise, it is not prime.

Here is an example code in C language that implements the above algorithm:

```c
#include <stdio.h>
int main()
{
    int n, i, flag = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for(i = 2; i <= n/2; ++i)
    {
        if(n%i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (n == 1) 
    {
        printf("1 is neither prime nor composite.");
    }
    else 
    {
        if (flag == 0)
            printf("%d is a prime number.", n);
        else
            printf("%d is not a prime number.", n);
    }

    return 0;
}
```