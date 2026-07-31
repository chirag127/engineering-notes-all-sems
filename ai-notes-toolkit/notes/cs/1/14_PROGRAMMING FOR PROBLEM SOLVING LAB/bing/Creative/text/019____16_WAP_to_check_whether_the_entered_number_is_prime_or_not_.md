## 16.WAP to check whether the entered number is prime or not.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- To check whether a given number is prime or not, we can use the following algorithm:
  - Step 1: Input the number n from the user.
  - Step 2: Initialize a variable flag to 0.
  - Step 3: If n is less than or equal to 1, then it is not a prime number. Go to step 7.
  - Step 4: For each integer i from 2 to n-1, do the following:
    - Step 4.1: If n is divisible by i, then it is not a prime number. Set flag to 1 and go to step 7.
  - Step 5: If flag is still 0, then n is a prime number.
  - Step 6: Output the result.
  - Step 7: Stop the algorithm.
- Here is an example of a program in C language that implements the above algorithm:

```c
#include <stdio.h>
int main()
{
  int n, i, flag = 0;
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  if (n <= 1)
  {
    printf("%d is not a prime number.\n", n);
  }
  else
  {
    for (i = 2; i < n; i++)
    {
      if (n % i == 0)
      {
        printf("%d is not a prime number.\n", n);
        flag = 1;
        break;
      }
    }
    if (flag == 0)
    {
      printf("%d is a prime number.\n", n);
    }
  }
  return 0;
}
```