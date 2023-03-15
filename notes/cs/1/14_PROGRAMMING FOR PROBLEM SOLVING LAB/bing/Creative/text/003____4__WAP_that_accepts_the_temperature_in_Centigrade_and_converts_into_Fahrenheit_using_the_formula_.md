## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program, which is a common abbreviation used in computer science and programming courses.
- The problem statement asks us to write a program that can take a temperature value in Centigrade (also known as Celsius) and convert it into Fahrenheit using the given formula.
- The formula is derived from the fact that the freezing point of water is 0°C or 32°F, and the boiling point of water is 100°C or 212°F. Therefore, the difference between the two scales is 100°C = 180°F, or 1°C = 1.8°F.
- To write a program, we need to choose a programming language, such as Python, Java, C, etc. For this example, we will use Python, which is a popular and easy-to-learn language.
- A Python program consists of statements that are executed one by one by the interpreter. A statement can be an expression, an assignment, a function call, a control structure, etc.
- To accept the temperature in Centigrade from the user, we can use the input() function, which returns a string. We need to convert the string into a float (a decimal number) using the float() function, so that we can perform arithmetic operations on it.
- To convert the temperature into Fahrenheit, we can use the formula given in the problem statement. We can assign the result to a variable, such as f, using the = operator.
- To display the result to the user, we can use the print() function, which prints the value of its argument to the standard output. We can use string formatting to insert the values of the variables into the output string, using the {} placeholders and the .format() method.
- The program can be written as follows:

```python
# WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

# Accept the temperature in Centigrade from the user
c = float(input("Enter the temperature in Centigrade: "))

# Convert the temperature into Fahrenheit using the formula
f = (c * 9 / 5) + 32

# Display the result to the user
print("The temperature in Fahrenheit is: {:.2f}".format(f))
```

- The program can be tested with different input values, such as 0, 100, 37, etc. The output should match the expected values, such as 32, 212, 98.6, etc.