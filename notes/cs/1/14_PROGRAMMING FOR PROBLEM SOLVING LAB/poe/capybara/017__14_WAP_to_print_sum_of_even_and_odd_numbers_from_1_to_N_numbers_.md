## 14. WAP to print sum of even and odd numbers from 1 to N numbers.

In this program, we will write a code to print the sum of even and odd numbers from 1 to N numbers. Here are the steps to write the program:

1. First, we will take input from the user for the value of N.
2. We will then initialize two variables, one for the sum of even numbers and the other for the sum of odd numbers. We will set both variables to 0.
3. We will then use a for loop to iterate through numbers from 1 to N.
4. Inside the loop, we will check if the current number is even or odd.
5. If the number is even, we will add it to the sum of even numbers variable.
6. If the number is odd, we will add it to the sum of odd numbers variable.
7. Finally, we will print the sum of even numbers and the sum of odd numbers.

Here is the code for the program:

```
#include <stdio.h>

int main()
{
    int n, i, sum_even = 0, sum_odd = 0;

    printf("Enter the value of N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        if (i % 2 == 0)
        {
            sum_even += i;
        }
        else
        {
            sum_odd += i;
        }
    }

    printf("Sum of even numbers from 1 to %d is %d\n", n, sum_even);
    printf("Sum of odd numbers from 1 to %d is %d\n", n, sum_odd);

    return 0;
}
```

In this program, we have used the modulus operator to check if a number is even or odd. The modulus operator returns the remainder of a division operation. If a number is divisible by 2, then its remainder will be 0, which means it is even. If the remainder is 1, then the number is odd.

This program can be used to find the sum of even and odd numbers for any value of N. It is a simple program and can be used as a starting point for more complex programs that involve finding the sum of even or odd numbers in a range of numbers.