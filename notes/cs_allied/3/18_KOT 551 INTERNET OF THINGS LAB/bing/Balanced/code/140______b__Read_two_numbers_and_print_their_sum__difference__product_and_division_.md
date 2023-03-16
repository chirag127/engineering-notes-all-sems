#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string value that can be converted to a numeric type using `int()` or `float()`.
- For example, we can write:

```python
# Read two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input strings to integers
num1 = int(num1)
num2 = int(num2)
```

- To print their sum, difference, product and division, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform the corresponding operations on the operands and return the result.
- For example, we can write:

```python
# Print the sum of the two numbers
print("The sum is", num1 + num2)

# Print the difference of the two numbers
print("The difference is", num1 - num2)

# Print the product of the two numbers
print("The product is", num1 * num2)

# Print the division of the two numbers
print("The division is", num1 / num2)
```

- Note that the division operator `/` in Python returns a floating-point value, even if the operands are integers. To get an integer division, we can use the floor division operator `//`, which returns the quotient of the division without the remainder.
- For example, we can write:

```python
# Print the integer division of the two numbers
print("The integer division is", num1 // num2)
```

- Here is the complete code for the program:

```python
# Read two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the input strings to integers
num1 = int(num1)
num2 = int(num2)

# Print the sum of the two numbers
print("The sum is", num1 + num2)

# Print the difference of the two numbers
print("The difference is", num1 - num2)

# Print the product of the two numbers
print("The product is", num1 * num2)

# Print the division of the two numbers
print("The division is", num1 / num2)

# Print the integer division of the two numbers
print("The integer division is", num1 // num2)
```

- Here is an example of the output of the program:

```
Enter the first number: 10
Enter the second number: 5
The sum is 15
The difference is 5
The product is 50
The division is 2.0
The integer division is 2
```