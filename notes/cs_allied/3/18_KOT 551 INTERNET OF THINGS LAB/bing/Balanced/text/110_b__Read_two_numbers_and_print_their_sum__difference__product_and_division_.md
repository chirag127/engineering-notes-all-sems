# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the `input()` function in Python, which returns a string value that can be converted to a numeric type using `int()` or `float()`.
- For example, we can write:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
```

- To print their sum, difference, product and division, we can use the arithmetic operators `+`, `-`, `*` and `/` in Python, which perform addition, subtraction, multiplication and division respectively.
- For example, we can write:

```python
# Print the sum, difference, product and division of the two numbers
print("The sum of the two numbers is", num1 + num2)
print("The difference of the two numbers is", num1 - num2)
print("The product of the two numbers is", num1 * num2)
print("The division of the two numbers is", num1 / num2)
```

- Note that the division operator `/` returns a floating-point value, even if the operands are integers. To get an integer division, we can use the floor division operator `//`, which returns the quotient of the division without the remainder.
- For example, we can write:

```python
# Print the integer division of the two numbers
print("The integer division of the two numbers is", num1 // num2)
```

- Here is the complete program that reads two numbers and prints their sum, difference, product and division:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Print the sum, difference, product and division of the two numbers
print("The sum of the two numbers is", num1 + num2)
print("The difference of the two numbers is", num1 - num2)
print("The product of the two numbers is", num1 * num2)
print("The division of the two numbers is", num1 / num2)
print("The integer division of the two numbers is", num1 // num2)
```

- Here is an example of the output of the program, assuming the user enters 10 and 5 as the two numbers:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15
The difference of the two numbers is 5
The product of the two numbers is 50
The division of the two numbers is 2.0
The integer division of the two numbers is 2
```