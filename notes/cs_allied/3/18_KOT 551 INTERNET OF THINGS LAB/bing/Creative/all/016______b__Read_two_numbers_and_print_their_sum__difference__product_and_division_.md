#### b) Read two numbers and print their sum, difference, product and division.

- To read two numbers, we can use the input() function in Python, which returns a string. We can convert the string to a numerical type, such as int or float, using the int() or float() function respectively.
- To print the sum, difference, product and division of two numbers, we can use the arithmetic operators +, -, *, and / in Python, which perform addition, subtraction, multiplication, and division respectively. We can use the print() function to display the results on the screen.
- For example, if we want to read two numbers x and y, and print their sum, difference, product and division, we can write the following code in Python:

```python
# Read two numbers
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Print their sum, difference, product and division
print("The sum of", x, "and", y, "is", x + y)
print("The difference of", x, "and", y, "is", x - y)
print("The product of", x, "and", y, "is", x * y)
print("The division of", x, "and", y, "is", x / y)
```

- If we run this code and enter 10 and 5 as the input, we will get the following output:

```text
Enter the first number: 10
Enter the second number: 5
The sum of 10.0 and 5.0 is 15.0
The difference of 10.0 and 5.0 is 5.0
The product of 10.0 and 5.0 is 50.0
The division of 10.0 and 5.0 is 2.0
```