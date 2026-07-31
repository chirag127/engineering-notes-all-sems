## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (Write a Program) is a task that requires writing a computer program in a specific programming language to achieve a desired output or functionality.
- To check whether the two numbers entered by the user are equal or not, we need to perform the following steps:
  - Declare two variables to store the user input, such as `num1` and `num2`.
  - Prompt the user to enter the first number and assign it to `num1`.
  - Prompt the user to enter the second number and assign it to `num2`.
  - Compare the values of `num1` and `num2` using the `==` operator, which returns `true` if they are equal and `false` otherwise.
  - Display the result of the comparison using an `if-else` statement, which executes a block of code depending on whether the condition is `true` or `false`.
  - For example, if the condition is `true`, we can print "The numbers are equal." and if the condition is `false`, we can print "The numbers are not equal."
- Here is an example of a WAP that checks whether the two numbers entered by the user are equal or not in Python, which is a popular and easy-to-learn programming language:

```python
# Declare two variables to store the user input
num1 = 0
num2 = 0

# Prompt the user to enter the first number and assign it to num1
num1 = int(input("Enter the first number: "))

# Prompt the user to enter the second number and assign it to num2
num2 = int(input("Enter the second number: "))

# Compare the values of num1 and num2 using the == operator
if num1 == num2:
  # If the condition is true, print "The numbers are equal."
  print("The numbers are equal.")
else:
  # If the condition is false, print "The numbers are not equal."
  print("The numbers are not equal.")
```

- Here is an example of the output of the WAP when the user enters 5 and 5:

```
Enter the first number: 5
Enter the second number: 5
The numbers are equal.
```

- Here is an example of the output of the WAP when the user enters 5 and 6:

```
Enter the first number: 5
Enter the second number: 6
The numbers are not equal.
```