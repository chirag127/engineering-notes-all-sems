## Between 90-100%-----Print ‘A’

- This topic is about how to write a program that takes a percentage as input and prints 'A' if the percentage is between 90 and 100, inclusive.
- To write such a program, we need to use some basic concepts of programming, such as variables, data types, input/output, conditional statements, and logical operators.
- Here are the steps to write the program in Python, a popular programming language:

  1. Declare a variable called `percentage` and assign it the value of the input from the user. We can use the `input()` function to get the input and the `float()` function to convert it to a decimal number.
  2. Use an `if` statement to check if the value of `percentage` is between 90 and 100, inclusive. We can use the logical operator `and` to combine two conditions: `percentage >= 90` and `percentage <= 100`.
  3. If the condition is true, print 'A' using the `print()` function. Otherwise, print nothing or a suitable message.
  4. End the program.

- Here is the code for the program in Python:

```python
# Declare a variable called percentage and assign it the value of the input from the user
percentage = float(input("Enter your percentage: "))

# Use an if statement to check if the value of percentage is between 90 and 100, inclusive
if percentage >= 90 and percentage <= 100:
  # If the condition is true, print 'A'
  print("A")
else:
  # Otherwise, print nothing or a suitable message
  print("Not in the range")
```

- Here is an example of the program output:

```
Enter your percentage: 95
A
```

- Here is another example of the program output:

```
Enter your percentage: 80
Not in the range
```