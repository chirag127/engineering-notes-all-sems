Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to check whether the entered number is prime or not. Here is the content in markdown format:

## 16.WAP to check whether the entered number is prime or not.

A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers, but 4, 6, 8, 9, 10 are not.

To check whether a given number is prime or not, we can use the following algorithm:

- Step 1: Input the number n from the user.
- Step 2: Initialize a variable flag to 1. This variable will store the result of the check.
- Step 3: If n is less than or equal to 1, set flag to 0 and go to step 6. This is because 1 and negative numbers are not prime.
- Step 4: Loop from 2 to the square root of n. For each iteration, check if n is divisible by the current loop variable. If yes, set flag to 0 and break the loop. This is because if n has a divisor other than 1 and itself, it is not prime.
- Step 5: End the loop.
- Step 6: If flag is 1, print "n is a prime number". Else, print "n is not a prime number".
- Step 7: Stop.

Here is the program in C language that implements the above algorithm:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int n, flag = 1;
    printf("Enter a number: ");
    scanf("%d", &n);

    if (n <= 1)
    {
        flag = 0;
    }
    else
    {
        for (int i = 2; i <= sqrt(n); i++)
        {
            if (n % i == 0)
            {
                flag = 0;
                break;
            }
        }
    }

    if (flag == 1)
    {
        printf("%d is a prime number.\n", n);
    }
    else
    {
        printf("%d is not a prime number.\n", n);
    }

    return 0;
}
```