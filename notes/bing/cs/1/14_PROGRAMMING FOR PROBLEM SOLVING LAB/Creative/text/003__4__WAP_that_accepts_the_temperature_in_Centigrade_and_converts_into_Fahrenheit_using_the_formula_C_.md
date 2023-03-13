## 4. WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

- WAP stands for Write a Program, which is a common abbreviation used in computer science and programming.
- The problem statement asks us to write a program that can take a temperature value in Centigrade (also known as Celsius) and convert it into Fahrenheit using the given formula.
- Centigrade and Fahrenheit are two different units of measuring temperature. They are related by the formula C/5=(F-32)/9, where C is the temperature in Centigrade and F is the temperature in Fahrenheit.
- To write a program that can perform this conversion, we need to follow these steps:

  1. Declare a variable to store the temperature in Centigrade and assign it a value. For example, `C = 25`.
  2. Declare another variable to store the temperature in Fahrenheit and initialize it to zero. For example, `F = 0`.
  3. Apply the formula C/5=(F-32)/9 to calculate the value of F from C. For example, `F = (C * 9 / 5) + 32`.
  4. Print the value of F to the output. For example, `print(F)`.
  5. Test the program with different values of C and verify the results.

- Here is an example of a program written in Python that can perform this task:

```python
# WAP that accepts the temperature in Centigrade and converts into Fahrenheit using the formula C/5=(F-32)/9.

# Declare a variable to store the temperature in Centigrade and assign it a value
C = 25

# Declare another variable to store the temperature in Fahrenheit and initialize it to zero
F = 0

# Apply the formula C/5=(F-32)/9 to calculate the value of F from C
F = (C * 9 / 5) + 32

# Print the value of F to the output
print(F)
```

- The output of this program is:

```text
77.0
```

- This means that 25 degrees Centigrade is equivalent to 77 degrees Fahrenheit.