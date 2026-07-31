# b) Read two numbers and print their sum, difference, product and division.

To solve this problem, we need to follow these steps:

1. Read two numbers from the user. This can be done using the `input()` function in Python.
2. Convert the input values to integers using the `int()` function.
3. Calculate the sum of the two numbers by adding them together using the `+` operator.
4. Calculate the difference of the two numbers by subtracting one from the other using the `-` operator.
5. Calculate the product of the two numbers by multiplying them together using the `*` operator.
6. Calculate the division of the two numbers by dividing one by the other using the `/` operator.
7. Print the results of the calculations.

Here is an example of how the code might look:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

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

This code will read two numbers from the user, perform the necessary calculations, and print the results. The user can then see the sum, difference, product, and division of the two numbers they entered.