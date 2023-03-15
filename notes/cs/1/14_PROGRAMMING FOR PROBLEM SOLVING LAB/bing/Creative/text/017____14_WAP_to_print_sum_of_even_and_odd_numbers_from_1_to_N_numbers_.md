## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

- A program to print sum of even and odd numbers from 1 to N numbers is a program that takes a positive integer N as input and calculates the sum of all the even numbers and all the odd numbers from 1 to N, and prints them as output.
- To write such a program, we need to use the following steps:
  - Declare and initialize two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively. Set them to zero initially.
  - Declare and initialize another variable, `num`, to store the input value of N. Read the value of N from the user using `scanf` function or any other input method.
  - Use a `for` loop to iterate from 1 to N, and check each number if it is even or odd using the modulo operator (`%`). The modulo operator returns the remainder of the division of two numbers. If the remainder is zero, the number is even, otherwise it is odd.
  - Inside the loop, if the number is even, add it to the `even_sum` variable using the `+=` operator. If the number is odd, add it to the `odd_sum` variable using the same operator.
  - After the loop ends, print the values of `even_sum` and `odd_sum` using `printf` function or any other output method.
- Here is an example of such a program in C language:

```c
#include <stdio.h>
int main()
{
  // Declare and initialize the variables
  int even_sum = 0, odd_sum = 0, num;
  // Read the input value of N
  printf("Enter a positive integer: ");
  scanf("%d", &num);
  // Use a for loop to iterate from 1 to N
  for (int i = 1; i <= num; i++)
  {
    // Check if the number is even or odd using modulo operator
    if (i % 2 == 0)
    {
      // Add the even number to the even_sum variable
      even_sum += i;
    }
    else
    {
      // Add the odd number to the odd_sum variable
      odd_sum += i;
    }
  }
  // Print the sums of even and odd numbers
  printf("Sum of even numbers = %d\n", even_sum);
  printf("Sum of odd numbers = %d\n", odd_sum);
  return 0;
}
```