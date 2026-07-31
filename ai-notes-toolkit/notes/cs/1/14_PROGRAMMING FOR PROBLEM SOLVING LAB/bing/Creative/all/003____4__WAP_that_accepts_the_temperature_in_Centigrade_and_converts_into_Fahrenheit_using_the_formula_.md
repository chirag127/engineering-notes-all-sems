## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- A WAP (Write a Program) is a task that requires writing a computer program that performs a specific function or solves a problem.
- The temperature in Centigrade (also known as Celsius) is a unit of measurement for temperature that is based on the freezing point (0°C) and boiling point (100°C) of water at standard atmospheric pressure.
- The temperature in Fahrenheit is another unit of measurement for temperature that is based on the freezing point (32°F) and boiling point (212°F) of water at standard atmospheric pressure.
- The formula C/5=(F-32)/9 is a mathematical equation that relates the temperature in Centigrade to the temperature in Fahrenheit. It can be derived from the fact that the difference between the freezing and boiling points of water is 100°C in Centigrade and 180°F in Fahrenheit, and that both scales have the same interval size of 1/180.
- To write a program that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9, we need to follow these steps:
  - Declare a variable to store the temperature in Centigrade and assign it a value from the user input.
  - Declare another variable to store the temperature in Fahrenheit and assign it the value obtained by applying the formula C/5=(F-32)/9 to the first variable.
  - Display the value of the second variable as the output of the program.
- An example of a program that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9 in Python is:

```python
# Declare a variable to store the temperature in Centigrade and assign it a value from the user input
C = float(input("Enter the temperature in Centigrade: "))

# Declare another variable to store the temperature in Fahrenheit and assign it the value obtained by applying the formula C/5=(F-32)/9 to the first variable
F = (C * 9 / 5) + 32

# Display the value of the second variable as the output of the program
print("The temperature in Fahrenheit is: ", F)
```