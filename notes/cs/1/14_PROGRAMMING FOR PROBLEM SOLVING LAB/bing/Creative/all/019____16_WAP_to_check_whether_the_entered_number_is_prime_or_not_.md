## 16.WAP to check whether the entered number is prime or not.

A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, etc. are prime numbers.

To check whether the entered number is prime or not, we can use the following algorithm:

- Step 1: Input the number n from the user.
- Step 2: Initialize a variable flag to 0.
- Step 3: If n is less than or equal to 1, then go to step 8. Otherwise, go to step 4.
- Step 4: Initialize a variable i to 2.
- Step 5: If i is less than or equal to the square root of n, then go to step 6. Otherwise, go to step 9.
- Step 6: If n is divisible by i, then set flag to 1 and go to step 9. Otherwise, go to step 7.
- Step 7: Increment i by 1 and go to step 5.
- Step 8: Print "Invalid input" and stop.
- Step 9: If flag is 0, then print "The number is prime" and stop. Otherwise, print "The number is not prime" and stop.

Here is an example of a program in C language that implements the above algorithm:

```c
#include <stdio.h>
#include <math.h>

int main()
{
    int n, flag = 0, i;
    printf("Enter a number: ");
    scanf("%d", &n);
    if (n <= 1)
    {
        printf("Invalid input\n");
        return 0;
    }
    for (i = 2; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
    {
        printf("The number is prime\n");
    }
    else
    {
        printf("The number is not prime\n");
    }
    return 0;
}
```