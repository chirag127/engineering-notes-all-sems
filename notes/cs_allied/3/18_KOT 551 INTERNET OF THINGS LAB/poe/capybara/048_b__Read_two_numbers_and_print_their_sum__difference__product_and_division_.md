# Read two numbers and print their sum, difference, product and division

When it comes to programming, arithmetic operations are crucial, and carrying out these operations is an essential skill for all programmers. One of the fundamental operations is performing arithmetic operations on two numbers. In this topic, we will learn how to read two numbers from the user and perform the following arithmetic operations on them:

- Sum
- Difference
- Product
- Division

Here's how to perform these operations in your program:

1. Read two numbers from the user.
   - You can use the input() function to read the two numbers as strings.
   - Convert the input strings to integers using the int() function.

2. Calculate the sum of the two numbers.
   - Add the two numbers together using the + operator.
   - Store the result in a variable.

3. Calculate the difference between the two numbers.
   - Subtract the second number from the first number using the - operator.
   - Store the result in a variable.

4. Calculate the product of the two numbers.
   - Multiply the two numbers together using the * operator.
   - Store the result in a variable.

5. Calculate the quotient of the two numbers.
   - Divide the first number by the second number using the / operator.
   - Store the result in a variable.

6. Print the results.
   - Use the print() function to display the results.
   - Use the format() function to format the output string.

Here's an example program that reads two numbers from the user and performs the arithmetic operations:

```python
# Read two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform arithmetic operations
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
quot = num1 / num2

# Display the results
print("Sum: {}".format(sum))
print("Difference: {}".format(diff))
print("Product: {}".format(prod))
print("Quotient: {}".format(quot))
```

In conclusion, reading two numbers and performing arithmetic operations on them is a fundamental skill for any programmer. By following the steps outlined above, you can easily read two numbers from the user and perform arithmetic operations on them in your programs.