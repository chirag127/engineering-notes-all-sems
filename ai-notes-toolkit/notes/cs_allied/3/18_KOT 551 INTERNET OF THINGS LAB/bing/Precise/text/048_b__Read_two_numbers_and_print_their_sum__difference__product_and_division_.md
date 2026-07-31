# b) Read two numbers and print their sum, difference, product and division.

1. To read two numbers, you can use the `input()` function in Python. This function reads a line from input, converts it to a string, and returns the result.
2. To convert the input string to a number, you can use the `int()` or `float()` functions, depending on whether you want to work with integers or floating-point numbers.
3. To calculate the sum of the two numbers, you can use the `+` operator.
4. To calculate the difference between the two numbers, you can use the `-` operator.
5. To calculate the product of the two numbers, you can use the `*` operator.
6. To calculate the division of the two numbers, you can use the `/` operator.
7. To print the results, you can use the `print()` function.

Here is an example of how this can be done in Python:

```python
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
```