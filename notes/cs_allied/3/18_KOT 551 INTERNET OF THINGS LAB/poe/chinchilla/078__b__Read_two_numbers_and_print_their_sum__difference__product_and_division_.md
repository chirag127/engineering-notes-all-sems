#### b) Read two numbers and print their sum, difference, product and division.

When working with numerical data in programming, it is often necessary to perform mathematical operations such as addition, subtraction, multiplication, and division. In this section, we will learn how to read two numbers from the user and print their sum, difference, product, and division.

To read user input in Python, we use the `input()` function, which prompts the user to enter a value and returns it as a string. To convert the string input into a numerical value, we use type conversion functions such as `int()` or `float()`.

Here are the steps to read two numbers and perform mathematical operations on them:

1. Prompt the user to enter the first number using the `input()` function and store it in a variable, say `num1`.

2. Prompt the user to enter the second number using the `input()` function and store it in a variable, say `num2`.

3. Convert the string input of `num1` and `num2` into numerical values using the `int()` or `float()` function.

4. Compute the sum of `num1` and `num2` using the `+` operator and store it in a variable, say `sum`.

5. Compute the difference of `num1` and `num2` using the `-` operator and store it in a variable, say `diff`.

6. Compute the product of `num1` and `num2` using the `*` operator and store it in a variable, say `prod`.

7. Compute the division of `num1` and `num2` using the `/` operator and store it in a variable, say `div`.

8. Print the results of the mathematical operations using the `print()` function and the appropriate string formatting. For example, to print the sum of `num1` and `num2`, we can use the following code:

```python
print("The sum of {} and {} is {}".format(num1, num2, sum))
```

Here, the curly braces `{}` are placeholders that will be replaced with the values of `num1`, `num2`, and `sum` respectively.

9. Run the program and enter two numbers when prompted. The program will compute the sum, difference, product, and division of the two numbers and print the results.

Here is the complete code to read two numbers and print their sum, difference, product and division:

```python
# Prompt the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Convert the string input to numerical values
num1 = float(num1)
num2 = float(num2)

# Compute the mathematical operations
sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2

# Print the results
print("The sum of {} and {} is {}".format(num1, num2, sum))
print("The difference between {} and {} is {}".format(num1, num2, diff))
print("The product of {} and {} is {}".format(num1, num2, prod))
print("The division of {} and {} is {}".format(num1, num2, div))
```

Remember to test your code with different input values to ensure that it works correctly in all cases.