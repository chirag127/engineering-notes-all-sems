#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string that can be converted to a numeric type such as `int` or `float`.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the `print()` function in Python, which displays the value of the expression inside the parentheses to the standard output.
- For example, the following code reads two numbers from the user and prints their sum, difference, product and division:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print the sum, difference, product and division of the two numbers
print("The sum of the two numbers is", num1 + num2)
print("The difference of the two numbers is", num1 - num2)
print("The product of the two numbers is", num1 * num2)
print("The division of the two numbers is", num1 / num2)
```

- The output of the code may look like this:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15
The difference of the two numbers is 5
The product of the two numbers is 50
The division of the two numbers is 2.0
```