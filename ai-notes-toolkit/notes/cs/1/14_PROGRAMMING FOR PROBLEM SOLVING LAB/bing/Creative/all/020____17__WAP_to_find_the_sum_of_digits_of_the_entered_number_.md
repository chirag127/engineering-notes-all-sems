## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a program that takes a number as input from the user and calculates the sum of its digits.
- For example, if the user enters 123, the program should output 6, which is the sum of 1, 2 and 3.
- To write such a program, we need to use the following steps:

  - Declare a variable to store the input number and another variable to store the sum of digits. Initialize the sum variable to zero.
  - Use a loop to iterate over the digits of the input number. In each iteration, extract the last digit of the number using the modulo operator (%) and add it to the sum variable. Then, divide the number by 10 using the integer division operator (//) to remove the last digit.
  - Repeat the loop until the number becomes zero.
  - Print the sum variable as the output.

- Here is an example of such a program in Python:

```python
# Declare a variable to store the input number
num = int(input("Enter a number: "))

# Declare a variable to store the sum of digits
sum = 0

# Use a loop to iterate over the digits of the input number
while num > 0:
  # Extract the last digit of the number using the modulo operator (%)
  digit = num % 10

  # Add the digit to the sum variable
  sum = sum + digit

  # Divide the number by 10 using the integer division operator (//) to remove the last digit
  num = num // 10

# Print the sum variable as the output
print("The sum of digits is", sum)
```

- Here is an example of the output of the program:

```
Enter a number: 123
The sum of digits is 6
```