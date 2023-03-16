#### b) Read two numbers and print their sum, difference, product and division.

To solve this problem, we need to follow these steps:

1. Read the first number from the user and store it in a variable.
2. Read the second number from the user and store it in another variable.
3. Calculate the sum of the two numbers by adding the values of the two variables and store the result in a new variable.
4. Calculate the difference of the two numbers by subtracting the value of the second variable from the value of the first variable and store the result in a new variable.
5. Calculate the product of the two numbers by multiplying the values of the two variables and store the result in a new variable.
6. Calculate the division of the two numbers by dividing the value of the first variable by the value of the second variable and store the result in a new variable.
7. Print the values of the sum, difference, product, and division variables.

Here is an example of how this can be done in Python:

```python
# Read the first number from the user
num1 = float(input("Enter the first number: "))

# Read the second number from the user
num2 = float(input("Enter the second number: "))

# Calculate the sum of the two numbers
sum = num1 + num2

# Calculate the difference of the two numbers
difference = num1 - num2

# Calculate the product of the two numbers
product = num1 * num2

# Calculate the division of the two numbers
division = num1 / num2

# Print the results
print("The sum of the two numbers is:", sum)
print("The difference of the two numbers is:", difference)
print("The product of the two numbers is:", product)
print("The division of the two numbers is:", division)
```