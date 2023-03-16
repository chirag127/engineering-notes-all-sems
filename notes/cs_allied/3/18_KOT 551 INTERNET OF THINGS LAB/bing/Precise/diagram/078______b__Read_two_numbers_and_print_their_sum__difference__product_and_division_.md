#### b) Read two numbers and print their sum, difference, product and division.

To solve this problem, we need to follow these steps:

1. Read two numbers from the user. This can be done using the `input()` function in Python or `scanf()` function in C.
2. Calculate the sum of the two numbers by adding them together.
3. Calculate the difference of the two numbers by subtracting the second number from the first.
4. Calculate the product of the two numbers by multiplying them together.
5. Calculate the division of the two numbers by dividing the first number by the second.
6. Print the results of the sum, difference, product, and division.

Here is an example of how this can be done in Python:

```python
# Read two numbers from the user
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

This code reads two numbers from the user, calculates their sum, difference, product, and division, and then prints the results. It is important to note that the division operation may result in an error if the second number is zero, as division by zero is undefined. In such a case, an appropriate error message should be displayed to the user.