#### b) Read two numbers and print their sum, difference, product and division.

To solve this problem, we can follow these steps:

1. Read the first number from the user and store it in a variable, let's call it `num1`.
2. Read the second number from the user and store it in another variable, let's call it `num2`.
3. Calculate the sum of `num1` and `num2` and store the result in a variable, let's call it `sum`.
4. Calculate the difference between `num1` and `num2` and store the result in a variable, let's call it `difference`.
5. Calculate the product of `num1` and `num2` and store the result in a variable, let's call it `product`.
6. Calculate the division of `num1` by `num2` and store the result in a variable, let's call it `division`.
7. Print the values of `sum`, `difference`, `product`, and `division`.

Here is an example of how the code might look like in Python:

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

This code reads two numbers from the user, calculates their sum, difference, product, and division, and then prints the results. It is important to note that the division operation might result in an error if `num2` is equal to zero, as division by zero is undefined. In such a case, an appropriate error message should be displayed to the user.