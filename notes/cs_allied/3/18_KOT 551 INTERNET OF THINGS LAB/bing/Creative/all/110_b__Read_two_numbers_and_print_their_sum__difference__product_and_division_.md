# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numerical type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value of the expression inside the parentheses to the standard output.
- For example, if we want to read two numbers x and y, and print their sum, difference, product and division, we can write the following code in Python:

```python
# Read two numbers from the user input and convert them to float
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Print the sum, difference, product and division of x and y
print("The sum of x and y is", x + y)
print("The difference of x and y is", x - y)
print("The product of x and y is", x * y)
print("The division of x and y is", x / y)
```

- The output of the code will depend on the values entered by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of x and y is 15.0
The difference of x and y is 5.0
The product of x and y is 50.0
The division of x and y is 2.0
```