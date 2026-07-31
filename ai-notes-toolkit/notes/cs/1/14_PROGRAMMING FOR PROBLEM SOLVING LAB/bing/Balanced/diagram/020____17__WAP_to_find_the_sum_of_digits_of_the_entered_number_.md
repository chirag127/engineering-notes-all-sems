Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to find the sum of digits of the entered number. Here is the content in markdown format:

## 17. WAP to find the sum of digits of the entered number.

- The problem statement is to write a program that takes a positive integer as input and calculates the sum of its digits.
- For example, if the input is 123, the output should be 6, because 1 + 2 + 3 = 6.
- To solve this problem, we need to use a loop and a variable to store the sum.
- We can use the modulo operator (%) to extract the last digit of the number and add it to the sum.
- We can use the integer division operator (//) to remove the last digit of the number and repeat the process until the number becomes zero.
- Here is the pseudocode for the algorithm:

```
# initialize sum to zero
sum = 0
# read the input number
number = input("Enter a positive integer: ")
# convert the input to an integer
number = int(number)
# loop until the number is zero
while number > 0:
  # extract the last digit using modulo operator
  digit = number % 10
  # add the digit to the sum
  sum = sum + digit
  # remove the last digit using integer division operator
  number = number // 10
# print the sum
print("The sum of digits is:", sum)
```

- Here is the Python code for the program:

```python
# initialize sum to zero
sum = 0
# read the input number
number = input("Enter a positive integer: ")
# convert the input to an integer
number = int(number)
# loop until the number is zero
while number > 0:
  # extract the last digit using modulo operator
  digit = number % 10
  # add the digit to the sum
  sum = sum + digit
  # remove the last digit using integer division operator
  number = number // 10
# print the sum
print("The sum of digits is:", sum)
```

- Here is a sample output of the program:

```
Enter a positive integer: 456
The sum of digits is: 15
```

- This is the end of the content. I hope you find it useful and informative. If you have any questions or feedback, please let me know. Thank you for using my service.