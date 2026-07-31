#### b) Read two numbers and print their sum, difference, product and division.

When it comes to programming, mathematical operations are an essential part of it. In this topic, we will learn how to read two numbers from the user and perform basic arithmetic operations like addition, subtraction, multiplication, and division.

Here are the steps to read two numbers and perform operations on them:

1. First, we need to ask the user to enter two numbers. We can use the `input()` function to prompt the user to enter the numbers. 

2. Once we have the numbers, we need to convert them into integers as the `input()` function always returns a string. We can use the `int()` function to do this.

3. Now that we have the two numbers, we can perform arithmetic operations on them. Let's start by adding them. We can use the `+` operator to add the two numbers.

4. Next, we can subtract the second number from the first number using the `-` operator.

5. Multiplying the two numbers is also easy. We can use the `*` operator to multiply them.

6. Finally, we can divide the first number by the second number using the `/` operator. However, we need to be careful as division by zero is not allowed.

7. Once we have performed all the operations, we can print the results to the console. We can use the `print()` function to display the results.

Here is the Python code that reads two numbers and prints their sum, difference, product, and division:

```python
# Ask the user to enter two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Perform arithmetic operations
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2

# Check if the second number is zero before dividing
if num2 == 0:
    print("Cannot divide by zero")
else:
    div = num1 / num2

# Display the results
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
if num2 != 0:
    print("Division:", div)
```

In conclusion, the above code demonstrates how to read two numbers from the user, perform arithmetic operations on them, and display the results. It is essential to understand the basic arithmetic operators and how to use them in Python to perform mathematical operations.