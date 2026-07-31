## 17. WAP to find the sum of digits of the entered number.

- A program to find the sum of digits of the entered number is a program that takes a number as input from the user and calculates the sum of its digits.
- For example, if the user enters 123, the program should output 6, which is the sum of 1, 2 and 3.
- To write such a program, we need to use the following steps:

  - Declare a variable to store the input number and another variable to store the sum of digits. Initialize the sum variable to zero.
  - Use a loop to iterate over the digits of the input number. In each iteration, extract the last digit of the number using the modulo operator (%) and add it to the sum variable. Then, divide the number by 10 to remove the last digit.
  - Repeat the loop until the number becomes zero.
  - Display the sum variable as the output.

- Here is an example of such a program in Python:

```python
# Python program to find the sum of digits of the entered number

# Take input from the user
num = int(input("Enter a number: "))

# Initialize sum to zero
sum = 0

# Loop over the digits of the number
while num > 0:
  # Extract the last digit using modulo operator
  digit = num % 10
  # Add the digit to the sum
  sum = sum + digit
  # Remove the last digit by dividing by 10
  num = num // 10

# Display the sum
print("The sum of digits is", sum)
```

- Here is an example of the output of the program:

```text
Enter a number: 123
The sum of digits is 6
```