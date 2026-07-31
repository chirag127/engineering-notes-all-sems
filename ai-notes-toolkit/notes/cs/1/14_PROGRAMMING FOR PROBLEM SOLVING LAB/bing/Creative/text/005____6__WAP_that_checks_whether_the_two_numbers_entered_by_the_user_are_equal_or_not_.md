## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (write a program) is a task that requires writing a computer code that performs a specific function or solves a problem.
- To check whether the two numbers entered by the user are equal or not, the WAP needs to do the following steps:
  - Take input from the user for two numbers, say x and y, and store them in variables.
  - Compare the values of x and y using the equality operator (==) which returns true if they are equal and false otherwise.
  - Display the result of the comparison using a print statement or any other output method.
- An example of a WAP that checks whether the two numbers entered by the user are equal or not in Python is:

```python
# Take input from the user for two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Compare the values of x and y using the equality operator
result = x == y

# Display the result of the comparison
print("The two numbers are equal:", result)
```

- An example of a WAP that checks whether the two numbers entered by the user are equal or not in C is:

```c
// Include the standard input/output library
#include <stdio.h>

// Define the main function
int main()
{
  // Declare and initialize two integer variables
  int x, y;

  // Take input from the user for two numbers
  printf("Enter the first number: ");
  scanf("%d", &x);
  printf("Enter the second number: ");
  scanf("%d", &y);

  // Compare the values of x and y using the equality operator
  int result = x == y;

  // Display the result of the comparison
  printf("The two numbers are equal: %d\n", result);

  // Return 0 to indicate successful execution
  return 0;
}
```