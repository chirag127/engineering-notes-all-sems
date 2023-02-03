#### b) Read two numbers and print their sum, difference, product and division.

Sure! Let's consider two numbers, `a` and `b`. To read these two numbers, we can use the `input()` function in Python. The `input()` function reads the input as a string, so we need to convert the input to a number (integer or float) using the appropriate type conversion function.

```
# Reading two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
```

Next, we can calculate the sum, difference, product and division of the two numbers.

```
# Calculating the sum
sum = a + b

# Calculating the difference
difference = a - b

# Calculating the product
product = a * b

# Calculating the division
division = a / b
```

Finally, we can print the results.

```
# Printing the results
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
```

Note that when dividing two integers, the result will be an integer in Python 3.x. To get a floating-point result, we need to convert either `a` or `b` to a floating-point number.

```
# Calculating the division with floating-point result
division = a / float(b)
```

This program will read two numbers from the user, calculate their sum, difference, product and division, and print the results.
