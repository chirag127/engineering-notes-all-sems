## 16. WAP to check whether the entered number is prime or not.

A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers. To check if a number is prime or not, we can follow these steps:

1. Take input from the user and store it in a variable.
2. Initialize a flag variable to 0.
3. Run a loop from 2 to the square root of the entered number.
4. Check if the entered number is divisible by the loop variable.
5. If it is divisible, set the flag variable to 1 and break the loop.
6. After the loop, check the value of the flag variable.
7. If the flag variable is 0, the entered number is prime. Otherwise, it is not prime.

Here is an example code in C language that implements the above algorithm:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int n, i, flag = 0;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    for(i = 2; i <= sqrt(n); i++)
    {
        if(n % i == 0)
        {
            flag = 1;
            break;
        }
    }

    if (n <= 1)
        printf("%d is not a prime number.", n);
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