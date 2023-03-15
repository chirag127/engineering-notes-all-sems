## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program.
- The formula for converting temperature from Centigrade to Fahrenheit is `C/5=(F-32)/9`.
- To convert a temperature from Centigrade to Fahrenheit, first subtract 32 from the Fahrenheit temperature.
- Then, multiply the result by 5/9.
- The resulting value is the temperature in Centigrade.

Here is an example of a program that accepts the temperature in Centigrade and converts it into Fahrenheit using the formula `C/5=(F-32)/9`:

```python
C = float(input("Enter the temperature in Centigrade: "))
F = (C * 9/5) + 32
print("The temperature in Fahrenheit is:", F)
```

In this program, the user is prompted to enter the temperature in Centigrade. The program then converts the temperature to Fahrenheit using the formula `C/5=(F-32)/9` and displays the result.