# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numeric type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- For example, if we want to read two numbers x and y, and print their sum, difference, product and division, we can write the following code:

```python
# Read two numbers from the user input
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Print the sum, difference, product and division of the two numbers
print("The sum of the two numbers is", x + y)
print("The difference of the two numbers is", x - y)
print("The product of the two numbers is", x * y)
print("The division of the two numbers is", x / y)
```

- The output of the code will depend on the values entered by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15
The difference of the two numbers is 5
The product of the two numbers is 50
The division of the two numbers is 2.0
```

- Note that the division operator / always returns a float value, even if the operands are integers. To perform integer division, which discards the fractional part, we can use the // operator instead. For example, 10 // 5 will return 2, not 2.0.