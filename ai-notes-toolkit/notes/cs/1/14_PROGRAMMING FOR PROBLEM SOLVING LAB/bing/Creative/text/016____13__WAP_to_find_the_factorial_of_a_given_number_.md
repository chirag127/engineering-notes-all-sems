## 13. WAP to find the factorial of a given number.

- The factorial of a positive integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example, 5! = 5 x 4 x 3 x 2 x 1 = 120.
- The factorial of zero, 0!, is defined as 1 by convention.
- The factorial function can be implemented using a loop or recursion in most programming languages.
- Here is an example of a program to find the factorial of a given number in Python:

```python
# Define a function to calculate the factorial of a number
def factorial(n):
  # Initialize the result variable to 1
  result = 1
  # Loop from 1 to n and multiply the result by each number
  for i in range(1, n + 1):
    result = result * i
  # Return the result
  return result

# Take a number as input from the user
n = int(input("Enter a number: "))
# Call the factorial function and print the result
print("The factorial of", n, "is", factorial(n))
```

- Here is an example of a program to find the factorial of a given number in C:

```c
// Include the standard input/output library
#include <stdio.h>
// Define a function to calculate the factorial of a number
int factorial(int n)
{
  // Initialize the result variable to 1
  int result = 1;
  // Loop from 1 to n and multiply the result by each number
  for (int i = 1; i <= n; i++)
  {
    result = result * i;
  }
  // Return the result
  return result;
}

// Define the main function
int main()
{
  // Declare a variable to store the input number
  int n;
  // Prompt the user to enter a number
  printf("Enter a number: ");
  // Read the input from the standard input
  scanf("%d", &n);
  // Call the factorial function and print the result
  printf("The factorial of %d is %d\n", n, factorial(n));
  // Return 0 to indicate successful termination
  return 0;
}
```