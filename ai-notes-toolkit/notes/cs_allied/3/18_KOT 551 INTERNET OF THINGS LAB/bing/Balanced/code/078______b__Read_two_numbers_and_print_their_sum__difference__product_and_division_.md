#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string that can be converted to a numeric type such as `int` or `float`.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the `print()` function in Python, which displays the value of the argument to the standard output.
- Here is an example of a Python program that reads two numbers and prints their sum, difference, product and division:

```python
# Read two numbers from the user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum, difference, product and division of the two numbers
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

# Print the results
print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", diff)
print("The product of the two numbers is", prod)
print("The division of the two numbers is", div)
```

- Here is an example of the output of the program:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15.0
The difference of the two numbers is 5.0
The product of the two numbers is 50.0
The division of the two numbers is 2.0
```