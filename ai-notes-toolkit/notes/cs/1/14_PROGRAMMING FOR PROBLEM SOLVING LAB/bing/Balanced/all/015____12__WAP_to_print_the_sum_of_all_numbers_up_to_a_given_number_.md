## 12. WAP to print the sum of all numbers up to a given number.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a desired output or functionality.
- To print the sum of all numbers up to a given number, we need to use a loop that iterates from 1 to the given number and adds each number to a variable that stores the sum.
- We also need to print the sum variable after the loop ends.
- Here is an example of a WAP to print the sum of all numbers up to a given number in Python:

```python
# Input the given number
n = int(input("Enter a number: "))

# Initialize the sum variable to 0
sum = 0

# Loop from 1 to n
for i in range(1, n + 1):
  # Add i to the sum variable
  sum = sum + i

# Print the sum variable
print("The sum of all numbers up to", n, "is", sum)
```

- Here is an example of a WAP to print the sum of all numbers up to a given number in C:

```c
// Include the standard input/output library
#include <stdio.h>

// Define the main function
int main()
{
  // Declare and input the given number
  int n;
  printf("Enter a number: ");
  scanf("%d", &n);

  // Declare and initialize the sum variable to 0
  int sum = 0;

  // Declare a loop variable
  int i;

  // Loop from 1 to n
  for (i = 1; i <= n; i++)
  {
    // Add i to the sum variable
    sum = sum + i;
  }

  // Print the sum variable
  printf("The sum of all numbers up to %d is %d\n", n, sum);

  // Return 0 to indicate successful execution
  return 0;
}
```