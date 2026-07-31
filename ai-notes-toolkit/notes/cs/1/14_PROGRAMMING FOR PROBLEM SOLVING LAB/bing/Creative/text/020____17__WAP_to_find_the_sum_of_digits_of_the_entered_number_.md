## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a program that takes a positive integer as input and calculates the sum of its individual digits.
- For example, if the input is 123, the output should be 6, because 1 + 2 + 3 = 6.
- To write such a program, we need to use the following steps:

  - Declare a variable to store the input number and another variable to store the sum of digits. Initialize the sum variable to zero.
  - Use a loop to iterate over the input number until it becomes zero. In each iteration, do the following:
    - Extract the last digit of the input number by using the modulo operator (%). For example, 123 % 10 = 3.
    - Add the extracted digit to the sum variable. For example, sum = sum + 3.
    - Divide the input number by 10 to remove the last digit. For example, 123 / 10 = 12.
  - After the loop ends, print the sum variable as the output.

- Here is an example of a program to find the sum of digits of the entered number in Python:

```python
# Python program to find the sum of digits of the entered number

# Take input from the user
num = int(input("Enter a positive integer: "))

# Initialize sum to zero
sum = 0

# Loop until num becomes zero
while num > 0:
  # Extract the last digit
  digit = num % 10
  # Add the digit to the sum
  sum = sum + digit
  # Remove the last digit
  num = num // 10

# Print the sum
print("The sum of digits is:", sum)
```

- Here is an example of a program to find the sum of digits of the entered number in C:

```c
// C program to find the sum of digits of the entered number

#include <stdio.h>

int main()
{
  // Declare variables to store the input number and the sum of digits
  int num, sum;

  // Take input from the user
  printf("Enter a positive integer: ");
  scanf("%d", &num);

  // Initialize sum to zero
  sum = 0;

  // Loop until num becomes zero
  while (num > 0)
  {
    // Extract the last digit
    int digit = num % 10;
    // Add the digit to the sum
    sum = sum + digit;
    // Remove the last digit
    num = num / 10;
  }

  // Print the sum
  printf("The sum of digits is: %d\n", sum);

  return 0;
}
```