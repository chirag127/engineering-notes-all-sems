# Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values in Python. They are binary operators, which means they operate on two operands. The following are the arithmetic operators in Python:

- **Addition (+)**: This operator adds two or more numbers together. For example, `5 + 3` returns `8`.
- **Subtraction (-)**: This operator subtracts one number from another. For example, `5 - 3` returns `2`.
- **Multiplication (*)**: This operator multiplies two or more numbers together. For example, `5 * 3` returns `15`.
- **Division (/)**: This operator divides one number by another. For example, `5 / 3` returns `1.6666666666666667`. Note that this operator always returns a floating-point number, even if the operands are integers.
- **Modulus (%)**: This operator returns the remainder of the division of one number by another. For example, `5 % 3` returns `2`. This operator is useful for checking if a number is divisible by another or for finding the last digit of a number.
- **Exponentiation (**)**: This operator raises one number to the power of another. For example, `5 ** 3` returns `125`. This operator has a higher precedence than the other arithmetic operators, which means it is evaluated before them.
- **Floor division (//)**: This operator performs an integer division, which means it returns the quotient of the division of one number by another, rounded down to the nearest integer. For example, `5 // 3` returns `1`. This operator is useful for finding the number of times a number can be divided by another without a remainder.

Here are some examples of using arithmetic operators in Python:

```python
# Addition
print(5 + 3) # 8
print(5 + 3 + 2) # 10
print(5.0 + 3) # 8.0

# Subtraction
print(5 - 3) # 2
print(5 - 3 - 2) # 0
print(5.0 - 3) # 2.0

# Multiplication
print(5 * 3) # 15
print(5 * 3 * 2) # 30
print(5.0 * 3) # 15.0

# Division
print(5 / 3) # 1.6666666666666667
print(5 / 3 / 2) # 0.8333333333333334
print(5.0 / 3) # 1.6666666666666667

# Modulus
print(5 % 3) # 2
print(5 % 3 % 2) # 0
print(5.0 % 3) # 2.0

# Exponentiation
print(5 ** 3) # 125
print(5 ** 3 ** 2) # 1953125
print(5.0 ** 3) # 125.0

# Floor division
print(5 // 3) # 1
print(5 // 3 // 2) # 0
print(5.0 // 3) # 1.0
```