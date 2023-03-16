#### b) Read two numbers and print their sum, difference, product and division.

1. To read two numbers, you can use the `input()` function in Python. This function reads a line from input, converts it to a string, and returns it.
2. You can then convert the string to an integer or a float using the `int()` or `float()` functions, respectively.
3. Once you have the two numbers, you can perform the arithmetic operations of addition, subtraction, multiplication, and division using the `+`, `-`, `*`, and `/` operators, respectively.
4. Finally, you can print the results of these operations using the `print()` function.

Here is an example code that reads two numbers and prints their sum, difference, product, and division:

```python
# Read two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Calculate the sum, difference, product, and division
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

# Print the results
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
```