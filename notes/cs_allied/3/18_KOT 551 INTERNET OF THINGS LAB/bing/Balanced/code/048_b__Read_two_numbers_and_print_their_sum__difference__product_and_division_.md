```
# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string value.
- To convert the string value to a numerical value, we can use the int() or float() function, depending on whether we want an integer or a decimal number.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators (+, -, *, /) in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value to the standard output.

## Example:

# Read two numbers from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the string values to numerical values
num1 = float(num1)
num2 = float(num2)

# Calculate the sum, difference, product and division of the two numbers
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

# Print the results
print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", difference)
print("The product of the two numbers is", product)
print("The division of the two numbers is", division)
```