# b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string value that can be converted to a numeric type such as int or float.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform the corresponding operations on the operands and return the result.
- To print the result, we can use the print() function in Python, which displays the value passed to it on the standard output device, such as the console or the screen.
- Here is an example of a Python program that reads two numbers and prints their sum, difference, product and division:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate and print the sum, difference, product and division
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("The sum of the two numbers is", sum)
print("The difference of the two numbers is", difference)
print("The product of the two numbers is", product)
print("The division of the two numbers is", division)
```

- Here is an example of the output of the program, assuming the user entered 10 and 5 as the two numbers:

```
Enter the first number: 10
Enter the second number: 5
The sum of the two numbers is 15
The difference of the two numbers is 5
The product of the two numbers is 50
The division of the two numbers is 2.0
```