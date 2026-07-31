Hello, I am Sydney, your AI assistant. I can help you with your programming assignments. Here is the content for the topic you requested:

## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- The problem statement is to write a program that accepts the temperature in Centigrade and converts it into Fahrenheit using the given formula.
- The formula is derived from the fact that the freezing point of water is 0°C or 32°F and the boiling point is 100°C or 212°F. Therefore, the difference between the two scales is 100°C = 180°F.
- To convert from Centigrade to Fahrenheit, we need to multiply the Centigrade temperature by 9/5 and then add 32. This can be written as F = (9/5)*C + 32.
- To convert from Fahrenheit to Centigrade, we need to subtract 32 from the Fahrenheit temperature and then divide by 9/5. This can be written as C = (5/9)*(F - 32).
- The program can be written in any programming language, such as Python, C, Java, etc. Here is an example of how to write the program in Python:

```python
# Python program to convert temperature from Centigrade to Fahrenheit
# Input the temperature in Centigrade
C = float(input("Enter the temperature in Centigrade: "))
# Apply the formula to convert to Fahrenheit
F = (9/5)*C + 32
# Print the result
print("The temperature in Fahrenheit is: ", F)
```

- The program can be tested with different input values and the output can be verified with a calculator or a conversion table. For example, if the input is 25°C, the output should be 77°F. If the input is 0°C, the output should be 32°F. If the input is 100°C, the output should be 212°F.