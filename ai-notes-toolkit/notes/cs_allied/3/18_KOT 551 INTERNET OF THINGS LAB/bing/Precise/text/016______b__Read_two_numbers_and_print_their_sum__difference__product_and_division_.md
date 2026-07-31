#### b) Read two numbers and print their sum, difference, product and division.

1. To read two numbers, you can use the `input()` function in Python. This function reads a line from input, converts it to a string, and returns it. You can then convert the string to an integer or a float using the `int()` or `float()` functions, respectively.

```python
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
```

2. To print the sum, difference, product, and division of the two numbers, you can use the `print()` function. The `+`, `-`, `*`, and `/` operators can be used to perform addition, subtraction, multiplication, and division, respectively.

```python
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
```

3. The above code will read two numbers from the user, and then print their sum, difference, product, and division. Make sure to handle the case where the second number is zero, as division by zero is not allowed. You can do this by adding an `if` statement to check if the second number is zero before performing the division.

```python
if num2 == 0:
    print("Cannot divide by zero")
else:
    print("Division:", num1 / num2)
```