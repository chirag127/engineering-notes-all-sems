## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To write a WAP that checks whether the two numbers entered by the user are equal or not, we need to follow these steps:

  - Declare two variables to store the numbers entered by the user, such as `num1` and `num2`.
  - Use the `input()` function to get the user input and assign it to the variables. The `input()` function returns a string, so we need to convert it to a numeric type, such as `int` or `float`, using the `int()` or `float()` function.
  - Use the `==` operator to compare the two numbers and check if they are equal. The `==` operator returns `True` if the operands are equal, and `False` otherwise.
  - Use the `if` statement to execute a block of code if the condition is `True`, and the `else` statement to execute another block of code if the condition is `False`.
  - Use the `print()` function to display the result to the user.

- Here is an example of a WAP that checks whether the two numbers entered by the user are equal or not, written in Python:

```python
# Declare two variables to store the numbers entered by the user
num1 = int(input("Enter the first number: ")) # Convert the user input to an integer
num2 = int(input("Enter the second number: ")) # Convert the user input to an integer

# Compare the two numbers and check if they are equal
if num1 == num2: # If the condition is True
  print("The two numbers are equal.") # Display this message
else: # If the condition is False
  print("The two numbers are not equal.") # Display this message
```

- Here is an example of the output of the WAP, given the user input of 5 and 5:

```
Enter the first number: 5
Enter the second number: 5
The two numbers are equal.
```

- Here is another example of the output of the WAP, given the user input of 10 and 20:

```
Enter the first number: 10
Enter the second number: 20
The two numbers are not equal.
```