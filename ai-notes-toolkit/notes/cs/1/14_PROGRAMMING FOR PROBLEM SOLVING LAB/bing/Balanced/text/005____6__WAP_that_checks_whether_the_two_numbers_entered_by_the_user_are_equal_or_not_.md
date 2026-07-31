## 6. WAP that checks whether the two numbers entered by the user are equal or not.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- To check whether the two numbers entered by the user are equal or not, we need to compare the values of the two numbers and return a boolean value (True or False) based on the result of the comparison.
- One possible way to write a WAP that checks whether the two numbers entered by the user are equal or not is:

```python
# Ask the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Compare the two numbers and store the result in a variable
are_equal = (num1 == num2)

# Print the result
print("The two numbers are equal:", are_equal)
```

- The above program uses the following concepts:
  - Input and output: The input() function allows the user to enter data from the keyboard and returns a string. The float() function converts the string to a floating-point number. The print() function displays the data on the screen.
  - Variables and assignment: A variable is a name that refers to a value stored in the memory. The assignment operator (=) assigns a value to a variable.
  - Comparison and boolean: The comparison operator (==) compares the values of two operands and returns True if they are equal and False otherwise. A boolean is a data type that can have only two values: True or False.