## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a program that takes a number as input from the user and calculates the sum of its individual digits.
- For example, if the user enters 123, the program should output 6, which is the sum of 1, 2 and 3.
- To write such a program, we need to use the following steps:

  1. Declare a variable to store the input number and another variable to store the sum of digits. Initialize the sum variable to zero.
  2. Use a loop to iterate over the input number until it becomes zero. In each iteration, do the following:
    - Extract the last digit of the number using the modulo operator (%). For example, 123 % 10 gives 3, which is the last digit of 123.
    - Add the extracted digit to the sum variable.
    - Divide the number by 10 to remove the last digit. For example, 123 / 10 gives 12, which is the number without the last digit.
  3. After the loop ends, display the sum variable as the output.

- Here is an example of such a program in Python:

```python
# WAP to find the sum of digits of the entered number

# Take input from the user
num = int(input("Enter a number: "))

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

# Display the sum
print("The sum of digits is", sum)
```

- Here is an example of such a program in C:

```c
// WAP to find the sum of digits of the entered number

#include <stdio.h>

int main()
{
  // Declare variables to store the input number and the sum of digits
  int num, sum;

  // Take input from the user
  printf("Enter a number: ");
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

  // Display the sum
  printf("The sum of digits is %d\n", sum);

  return 0;
}
```