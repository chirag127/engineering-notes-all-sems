Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to find the sum of digits of the entered number. Here is the content in markdown format:

## 17. WAP to find the sum of digits of the entered number.

- The problem statement is to write a program that takes a positive integer as input and returns the sum of its digits.
- For example, if the input is 123, the output should be 6, because 1 + 2 + 3 = 6.
- One possible algorithm to solve this problem is as follows:

  - Initialize a variable sum to 0.
  - Repeat the following steps until the input number is 0:
    - Find the remainder of the input number when divided by 10. This is the last digit of the number.
    - Add the remainder to the sum variable.
    - Divide the input number by 10 and update it. This removes the last digit of the number.
  - Return the sum variable as the output.

- Here is an example of how the algorithm works for the input 123:

  - sum = 0
  - remainder = 123 % 10 = 3
  - sum = sum + remainder = 0 + 3 = 3
  - number = number / 10 = 123 / 10 = 12
  - remainder = 12 % 10 = 2
  - sum = sum + remainder = 3 + 2 = 5
  - number = number / 10 = 12 / 10 = 1
  - remainder = 1 % 10 = 1
  - sum = sum + remainder = 5 + 1 = 6
  - number = number / 10 = 1 / 10 = 0
  - The loop ends and the output is 6.

- Here is a possible implementation of the algorithm in Python:

```python
# WAP to find the sum of digits of the entered number

# Take a positive integer as input
number = int(input("Enter a positive integer: "))

# Initialize a variable sum to 0
sum = 0

# Repeat until the number is 0
while number > 0:
  # Find the remainder of the number when divided by 10
  remainder = number % 10
  # Add the remainder to the sum
  sum = sum + remainder
  # Divide the number by 10 and update it
  number = number // 10

# Print the output
print("The sum of digits is", sum)
```

- Here is a sample run of the program:

```
Enter a positive integer: 123
The sum of digits is 6
```

- Here are some points to remember when writing such programs:

  - Use the modulo operator (%) to find the remainder of a number when divided by another number.
  - Use the integer division operator (//) to divide a number by another number and get the quotient as an integer.
  - Use a while loop to repeat a block of code until a condition is false.
  - Use the input() function to take user input as a string and the int() function to convert it to an integer.
  - Use the print() function to display the output.