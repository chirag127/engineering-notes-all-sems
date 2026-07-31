## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To check whether the two numbers entered by the user are equal or not, the program needs to do the following steps:
  - Ask the user to input two numbers and store them in variables, such as `num1` and `num2`.
  - Compare the values of `num1` and `num2` using the `==` operator, which returns `True` if they are equal and `False` otherwise.
  - Print the result of the comparison using the `print` function.
- An example of a WAP that checks whether the two numbers entered by the user are equal or not in Python is:

```python
# Ask the user to input two numbers and store them in variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the values of num1 and num2 using the == operator
result = num1 == num2

# Print the result of the comparison
print("The two numbers are equal:", result)
```

- The output of the program will depend on the user's input. For example, if the user enters `5` and `5`, the output will be:

```
Enter the first number: 5
Enter the second number: 5
The two numbers are equal: True
```

- If the user enters `3.14` and `3.15`, the output will be:

```
Enter the first number: 3.14
Enter the second number: 3.15
The two numbers are equal: False
```