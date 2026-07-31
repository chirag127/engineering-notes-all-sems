# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string that can be converted to a numerical type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the argument to the standard output device, such as the screen or a file.
- An example of a Python program that reads two numbers and prints their sum, difference, product and division is:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the sum, difference, product and division of the two numbers
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

# Print the results
print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", diff)
print("The product of the two numbers is", prod)
print("The division of the two numbers is", div)
```