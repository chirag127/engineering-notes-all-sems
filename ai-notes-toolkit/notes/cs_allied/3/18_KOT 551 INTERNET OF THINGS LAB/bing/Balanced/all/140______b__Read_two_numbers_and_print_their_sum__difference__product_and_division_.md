#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string value that can be converted to a numeric type using int() or float() functions.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators (+, -, *, /) in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value passed as an argument to the standard output device (such as the screen or a file).
- An example of a Python program that reads two numbers and prints their sum, difference, product and division is:

```python
# Read two numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

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

- The output of the program may look like:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15.0
The difference of the two numbers is 5.0
The product of the two numbers is 50.0
The division of the two numbers is 2.0
```