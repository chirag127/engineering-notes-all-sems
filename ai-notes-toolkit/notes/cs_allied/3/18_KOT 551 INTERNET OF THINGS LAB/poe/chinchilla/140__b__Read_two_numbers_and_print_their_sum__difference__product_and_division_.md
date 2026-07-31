#### b) Read two numbers and print their sum, difference, product and division.

To perform basic arithmetic operations in Python, we need to know how to read input from the user and print output to the screen. In this section, we will learn how to read two numbers from the user and print their sum, difference, product, and division.

Here are the steps to perform the above-mentioned operations:

1. **Reading input from the user:** To read input from the user, we use the `input()` function in Python. The syntax of the `input()` function is as follows:

   ```python
   variable_name = input("Enter a value: ")
   ```

   Here, `variable_name` is the name of the variable that will store the value entered by the user, and `"Enter a value: "` is the prompt that will be displayed on the screen when the user is prompted to enter a value.

2. **Converting input to numbers:** By default, the `input()` function reads input as a string. To perform arithmetic operations, we need to convert the input to numbers. We can do this using the `int()` or `float()` function in Python. The `int()` function is used to convert a string to an integer, and the `float()` function is used to convert a string to a floating-point number. Here's an example:

   ```python
   x = int(input("Enter a number: "))
   y = float(input("Enter another number: "))
   ```

   Here, `x` is an integer variable that will store the first number entered by the user, and `y` is a floating-point variable that will store the second number entered by the user.

3. **Performing arithmetic operations:** Once we have read the input and converted it to numbers, we can perform arithmetic operations on them. Here are the formulas to perform the four basic arithmetic operations:

   - Sum: `x + y`
   - Difference: `x - y`
   - Product: `x * y`
   - Division: `x / y`

4. **Printing output to the screen:** To display the output to the user, we use the `print()` function in Python. The syntax of the `print()` function is as follows:

   ```python
   print("Output:", variable_name)
   ```

   Here, `"Output: "` is the prompt that will be displayed on the screen before the output, and `variable_name` is the name of the variable that contains the output.

Here's an example program that reads two numbers from the user and prints their sum, difference, product, and division:

```python
# Read two numbers from the user
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

# Perform arithmetic operations
sum = x + y
diff = x - y
prod = x * y
div = x / y

# Print output to the screen
print("Sum:", sum)
print("Difference:", diff)
print("Product:", prod)
print("Division:", div)
```

When you run this program, it will prompt the user to enter two numbers. Once the user enters the numbers, the program will perform the four basic arithmetic operations and print the results to the screen.