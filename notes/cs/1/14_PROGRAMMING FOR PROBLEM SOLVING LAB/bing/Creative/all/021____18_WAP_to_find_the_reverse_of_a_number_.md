## 18.WAP to find the reverse of a number.

- A program to find the reverse of a number is a program that takes a number as input and outputs the number with its digits in the opposite order.
- For example, if the input number is 123, the output should be 321. If the input number is -456, the output should be -654.
- One way to write such a program is to use a loop and a variable to store the reversed number. The algorithm is as follows:

  - Initialize a variable called reverse to 0.
  - While the input number is not 0, do the following steps:
    - Multiply reverse by 10 and add the last digit of the input number to it. This will append the last digit of the input number to the reverse variable.
    - Divide the input number by 10 and discard the remainder. This will remove the last digit of the input number.
  - Return the reverse variable as the output.

- Here is an example of how the program works for the input number 123:

  - reverse = 0, input = 123
  - reverse = 0 * 10 + 3 = 3, input = 123 / 10 = 12
  - reverse = 3 * 10 + 2 = 32, input = 12 / 10 = 1
  - reverse = 32 * 10 + 1 = 321, input = 1 / 10 = 0
  - output = reverse = 321

- Here is a possible implementation of the program in Python:

```python
# WAP to find the reverse of a number

# Input a number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the reverse
reverse = 0

# Loop until the input number is not 0
while num != 0:
  # Append the last digit of the input number to the reverse
  reverse = reverse * 10 + num % 10
  # Remove the last digit of the input number
  num = num // 10

# Print the output
print("The reverse of the number is:", reverse)
```

- Here is a sample output of the program:

```text
Enter a number: 123
The reverse of the number is: 321
```