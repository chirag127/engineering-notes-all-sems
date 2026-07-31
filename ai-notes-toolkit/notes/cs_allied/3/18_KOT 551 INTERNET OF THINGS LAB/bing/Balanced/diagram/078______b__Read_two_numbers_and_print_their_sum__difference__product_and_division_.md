#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string. We can convert the string to a numerical type, such as int or float, using the int() or float() function.
- To print the sum, difference, product and division of two numbers, we can use the print() function in Python, which displays the value of its argument to the standard output. We can use the arithmetic operators +, -, *, and / to perform the operations on the numbers.
- For example, if we want to read two numbers x and y, and print their sum, difference, product and division, we can write the following code in Python:

```python
# Read two numbers
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

# Print their sum, difference, product and division
print("The sum of", x, "and", y, "is", x + y)
print("The difference of", x, "and", y, "is", x - y)
print("The product of", x, "and", y, "is", x * y)
print("The division of", x, "and", y, "is", x / y)
```

- The output of the code will depend on the values entered by the user. For example, if the user enters 10 and 5, the output will be:

```
Enter the first number: 10
Enter the second number: 5
The sum of 10 and 5 is 15
The difference of 10 and 5 is 5
The product of 10 and 5 is 50
The division of 10 and 5 is 2.0
```