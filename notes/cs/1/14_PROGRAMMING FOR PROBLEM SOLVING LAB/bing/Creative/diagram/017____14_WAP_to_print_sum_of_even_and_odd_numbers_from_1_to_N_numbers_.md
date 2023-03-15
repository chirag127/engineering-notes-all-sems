## 14.WAP to print sum of even and odd numbers from 1 to N numbers.

- A program to print sum of even and odd numbers from 1 to N numbers is a program that takes a positive integer N as input and calculates the sum of all the even numbers and all the odd numbers from 1 to N, and prints them as output.
- To write such a program, we need to use the following steps:

  - Declare and initialize two variables, `even_sum` and `odd_sum`, to store the sum of even and odd numbers respectively. Set them to zero initially.
  - Declare and initialize another variable, `n`, to store the input value of N. Read the value of N from the user using a suitable input function, such as `scanf` in C or `input` in Python.
  - Use a loop structure, such as `for` or `while`, to iterate from 1 to N. For each iteration, check if the current number is even or odd using a conditional statement, such as `if-else` or `switch-case`.
  - If the current number is even, add it to the `even_sum` variable. If the current number is odd, add it to the `odd_sum` variable.
  - After the loop ends, print the values of `even_sum` and `odd_sum` using a suitable output function, such as `printf` in C or `print` in Python.

- Here is an example of such a program written in C language:

```c
#include <stdio.h>
int main()
{
  // Declare and initialize the variables
  int even_sum = 0, odd_sum = 0, n;
  // Read the input value of N
  printf("Enter a positive integer: ");
  scanf("%d", &n);
  // Use a for loop to iterate from 1 to N
  for (int i = 1; i <= n; i++)
  {
    // Check if the current number is even or odd
    if (i % 2 == 0)
    {
      // Add the even number to the even_sum
      even_sum += i;
    }
    else
    {
      // Add the odd number to the odd_sum
      odd_sum += i;
    }
  }
  // Print the sums
  printf("Sum of even numbers = %d\n", even_sum);
  printf("Sum of odd numbers = %d\n", odd_sum);
  return 0;
}
```

- Here is an example of such a program written in Python language:

```python
# Declare and initialize the variables
even_sum = 0
odd_sum = 0
# Read the input value of N
n = int(input("Enter a positive integer: "))
# Use a for loop to iterate from 1 to N
for i in range(1, n + 1):
  # Check if the current number is even or odd
  if i % 2 == 0:
    # Add the even number to the even_sum
    even_sum += i
  else:
    # Add the odd number to the odd_sum
    odd_sum += i
# Print the sums
print("Sum of even numbers =", even_sum)
print("Sum of odd numbers =", odd_sum)
```