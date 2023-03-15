## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program, which is a common abbreviation used in computer science and programming courses.
- The problem statement asks us to write a program that can take an input of temperature in Centigrade (also known as Celsius) and convert it into Fahrenheit using the given formula.
- The formula C/5=(F-32)/9 is derived from the relation between the two temperature scales, which is F = (9/5)C + 32.
- To write a program, we need to choose a programming language, such as Python, C, Java, etc. For this example, we will use Python, which is a popular and easy-to-learn language.
- A Python program consists of statements that are executed sequentially by the interpreter. A statement can be an expression, an assignment, a function call, a control structure, etc.
- To accept the temperature in Centigrade from the user, we can use the input() function, which returns a string. We need to convert the string into a numeric value, such as a float, using the float() function.
- To convert the temperature into Fahrenheit, we can use the formula and assign the result to a variable, such as fahrenheit. We can use arithmetic operators, such as /, -, and * to perform calculations.
- To display the output, we can use the print() function, which prints the value of the argument to the standard output. We can use string formatting, such as f-strings, to insert variables into strings.
- To write a complete program, we need to follow the syntax and indentation rules of Python. We also need to add comments, which are lines that start with #, to explain the purpose and logic of the code.
- A possible solution for the problem is:

```python
# WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

# Ask the user to enter the temperature in Centigrade and store it in a variable called centigrade
centigrade = float(input("Enter the temperature in Centigrade: "))

# Convert the temperature into Fahrenheit using the formula and store it in a variable called fahrenheit
fahrenheit = (9/5) * centigrade + 32

# Print the output using string formatting
print(f"The temperature in Fahrenheit is {fahrenheit} degrees.")
```