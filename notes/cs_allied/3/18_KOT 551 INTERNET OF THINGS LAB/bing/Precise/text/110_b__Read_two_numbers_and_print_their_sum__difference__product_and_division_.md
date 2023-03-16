# b) Read two numbers and print their sum, difference, product and division.

1. To read two numbers, we can use the `input()` function in Python. This function reads a line from the input and returns it as a string.
2. We can then convert the string to an integer using the `int()` function.
3. Once we have the two numbers, we can perform the required operations on them.
4. To find the sum of the two numbers, we can use the `+` operator.
5. To find the difference between the two numbers, we can use the `-` operator.
6. To find the product of the two numbers, we can use the `*` operator.
7. To find the division of the two numbers, we can use the `/` operator.
8. Finally, we can print the results using the `print()` function.

Here is an example code that implements the above steps:

```python
# Read the first number
num1 = int(input("Enter the first number: "))

# Read the second number
num2 = int(input("Enter the second number: "))

# Find the sum
sum = num1 + num2

# Find the difference
diff = num1 - num2

# Find the product
product = num1 * num2

# Find the division
division = num1 / num2

# Print the results
print("Sum:", sum)
print("Difference:", diff)
print("Product:", product)
print("Division:", division)
```