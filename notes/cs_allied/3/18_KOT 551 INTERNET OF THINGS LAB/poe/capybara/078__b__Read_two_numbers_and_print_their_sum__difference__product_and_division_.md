#### b) Read two numbers and print their sum, difference, product and division.

When it comes to programming, there are a few basic operations that you need to know how to do with numbers. One of those is performing mathematical calculations such as addition, subtraction, multiplication, and division. In this section, we will focus on reading two numbers and printing their sum, difference, product, and division. Here are the steps to follow:

1. First, we need to read two numbers from the user. We can do this by using the `input()` function in Python. Here is an example:

   ```python
   num1 = input("Enter first number: ")
   num2 = input("Enter second number: ")
   ```
   
   This will prompt the user to enter two numbers, which will be stored in the `num1` and `num2` variables.

2. Next, we need to convert the input strings to numbers so that we can perform calculations on them. We can do this using the `int()` or `float()` functions in Python. Here is an example:

   ```python
   num1 = int(num1)
   num2 = int(num2)
   ```

   Note that we are using the `int()` function here because we want to perform integer arithmetic. If we wanted to perform floating-point arithmetic, we would use the `float()` function instead.

3. Now that we have our two numbers, we can perform the desired calculations. Here are the formulas for each operation:

   - Sum: `num1 + num2`
   - Difference: `num1 - num2`
   - Product: `num1 * num2`
   - Division: `num1 / num2`

   We can print the results using the `print()` function in Python. Here is an example:

   ```python
   print("Sum:", num1 + num2)
   print("Difference:", num1 - num2)
   print("Product:", num1 * num2)
   print("Division:", num1 / num2)
   ```

   This will output the results of the calculations to the console.

And that's it! With these steps, you should now be able to read two numbers and print their sum, difference, product, and division in Python. Remember to always convert your input strings to numbers before performing calculations, and to use the appropriate arithmetic operators for each operation.