## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

A WAP (Write a Program) is a common term used to describe the task of writing a computer program to solve a specific problem or perform a specific task. In this case, the task is to write a program that accepts a temperature value in degrees Centigrade and converts it into degrees Fahrenheit using the given formula: C/5=(F-32)/9.

Here are the steps to write this program:

1. Accept the temperature value in degrees Centigrade from the user.
2. Use the given formula to convert the temperature from Centigrade to Fahrenheit. The formula can be rearranged to solve for F: F = (9/5)*C + 32.
3. Display the result to the user.

Here is an example of how this program could be written in Python:

```python
# Accept the temperature value in degrees Centigrade from the user
C = float(input("Enter the temperature in degrees Centigrade: "))

# Use the given formula to convert the temperature from Centigrade to Fahrenheit
F = (9/5)*C + 32

# Display the result to the user
print("The temperature in degrees Fahrenheit is:", F)
```

This program prompts the user to enter a temperature value in degrees Centigrade, converts it into degrees Fahrenheit using the given formula, and displays the result to the user. The user can then use this program to easily convert temperatures between the two units.