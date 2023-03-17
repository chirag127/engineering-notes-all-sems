## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

Here are some key points to help you understand how to write a program that converts temperature from Celsius to Fahrenheit:

- To convert temperature from Celsius to Fahrenheit, we need to use the formula C/5=(F-32)/9. This formula relates the temperature in Celsius (C) to the temperature in Fahrenheit (F).
- In the formula, C is the temperature in Celsius, and F is the temperature in Fahrenheit. We can rearrange the formula to solve for F, which gives us F = (C * 9/5) + 32.
- To write a program that converts temperature from Celsius to Fahrenheit, we need to accept the temperature in Celsius as input from the user. We can do this using the input() function in Python.
- Once we have the temperature in Celsius, we can use the formula F = (C * 9/5) + 32 to calculate the temperature in Fahrenheit.
- We can then print the temperature in Fahrenheit using the print() function in Python.
- It is important to handle errors and edge cases in our program. For example, we should ensure that the input temperature is a number, and we should handle cases where the input temperature is below absolute zero (-273.15°C).
- Here is an example program in Python that converts temperature from Celsius to Fahrenheit:

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)
```

- This program accepts the temperature in Celsius from the user, converts it to Fahrenheit using the formula F = (C * 9/5) + 32, and prints the result. Note that we use the float() function to convert the user input to a floating-point number, which allows us to handle decimal values.
- By following these key points and understanding the formula and program logic, you should be able to write a program that converts temperature from Celsius to Fahrenheit in any programming language.