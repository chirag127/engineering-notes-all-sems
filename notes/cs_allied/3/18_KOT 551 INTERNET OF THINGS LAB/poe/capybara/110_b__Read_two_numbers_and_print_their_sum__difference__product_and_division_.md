## Read two numbers and print their sum, difference, product and division.

When programming, it is common to perform mathematical operations on numbers. One of the most basic operations is to add, subtract, multiply or divide two numbers. In this guide, you will learn how to read two numbers from the user and print their sum, difference, product and division.

### Reading Input from the User
Before you can perform any calculations, you need to read the input from the user. In Python, you can use the `input()` function to read a line of text from the user. To read a number, you can use the `int()` or `float()` function to convert the input to an integer or a float, respectively.

```python
# Reading input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
```

### Performing Mathematical Operations
Once you have read the input from the user, you can perform mathematical operations on the numbers. To add two numbers, you can use the `+` operator. To subtract two numbers, you can use the `-` operator. To multiply two numbers, you can use the `*` operator. To divide two numbers, you can use the `/` operator.

```python
# Performing mathematical operations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
```

### Printing the Results
After performing the mathematical operations, you can print the results to the screen using the `print()` function. You can use string formatting to include the values of the variables in the output.

```python
# Printing the results
print("Sum: {}".format(sum))
print("Difference: {}".format(difference))
print("Product: {}".format(product))
print("Division: {}".format(division))
```

### Example
Here's an example program that reads two numbers from the user and prints their sum, difference, product and division:

```python
# Read two numbers and print their sum, difference, product and division

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Sum: {}".format(sum))
print("Difference: {}".format(difference))
print("Product: {}".format(product))
print("Division: {}".format(division))
```

### Conclusion
In this guide, you learned how to read two numbers from the user and print their sum, difference, product and division. These basic mathematical operations are essential to many programming tasks, and being able to perform them is an important skill for any programmer.