## 16.WAP to check whether the entered number is prime or not.

A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers, but 4, 6, 8, 9, 10 are not.

To check whether a given number is prime or not, we can use the following algorithm:

- Step 1: Input the number n from the user.
- Step 2: Initialize a variable flag to 0.
- Step 3: If n is less than or equal to 1, then go to step 8. Otherwise, go to step 4.
- Step 4: For each integer i from 2 to n-1, do the following:
  - Step 4.1: If n is divisible by i, then set flag to 1 and break the loop.
- Step 5: If flag is 0, then go to step 6. Otherwise, go to step 7.
- Step 6: Print n is a prime number and stop.
- Step 7: Print n is not a prime number and stop.
- Step 8: Print n is neither prime nor composite and stop.

Here is an example of a program in C language that implements this algorithm:

```c
#include <stdio.h>
int main()
{
  int n, i, flag = 0;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  if (n <= 1)
  {
    printf("%d is neither prime nor composite.\n", n);
  }
  else
  {
    for (i = 2; i < n; i++)
    {
      if (n % i == 0)
      {
        flag = 1;
        break;
      }
    }
    if (flag == 0)
    {
      printf("%d is a prime number.\n", n);
    }
    else
    {
      printf("%d is not a prime number.\n", n);
    }
  }
  return 0;
}
```