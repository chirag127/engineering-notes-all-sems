Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write a program to find the sum of digits of the entered number. Here is the content in markdown format:

## 17. WAP to find the sum of digits of the entered number.

- The problem statement is to write a program that takes a positive integer as input and returns the sum of its digits.
- For example, if the input is 123, the output should be 6, because 1 + 2 + 3 = 6.
- To solve this problem, we need to use a loop to extract each digit of the number and add it to a variable that stores the sum.
- We can use the modulo operator (%) to get the rightmost digit of the number and the integer division operator (//) to remove the rightmost digit from the number.
- We can repeat this process until the number becomes zero, which means we have processed all the digits.
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
  # get the rightmost digit using modulo operator
  digit = number % 10
  # add the digit to the sum
  sum = sum + digit
  # remove the rightmost digit using integer division operator
  number = number // 10
# print the sum
print("The sum of digits is", sum)
```

- Here is an example of the program output:

```
Enter a positive integer: 456
The sum of digits is 15
```

- Here are some points to remember:

  - The input should be a positive integer, otherwise the program may not work correctly.
  - The modulo operator (%) returns the remainder of the division, which is the rightmost digit of the number.
  - The integer division operator (//) returns the quotient of the division, which is the number without the rightmost digit.
  - The loop condition is number > 0, which means the loop will stop when the number becomes zero.
  - The sum variable is initialized to zero and updated in each iteration of the loop.
  - The print statement is outside the loop, so it will print the final sum after the loop ends.