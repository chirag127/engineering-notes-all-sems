### Arithmetic Operators

Arithmetic operators are used to perform mathematical operations on numeric values. They are binary operators, which means they operate on two operands. The following are the arithmetic operators in Python:

- `+` : Addition. It adds the values on either side of the operator. For example, `3 + 5` gives `8`.
- `-` : Subtraction. It subtracts the right operand from the left operand. For example, `10 - 7` gives `3`.
- `*` : Multiplication. It multiplies the values on either side of the operator. For example, `4 * 6` gives `24`.
- `/` : Division. It divides the left operand by the right operand. It returns a floating-point number. For example, `15 / 3` gives `5.0`.
- `%` : Modulus. It returns the remainder of the division of the left operand by the right operand. For example, `17 % 5` gives `2`.
- `**` : Exponentiation. It raises the left operand to the power of the right operand. For example, `2 ** 3` gives `8`.
- `//` : Floor division. It performs integer division and returns the largest integer less than or equal to the result. For example, `9 // 2` gives `4`.

The order of precedence of the arithmetic operators is as follows:

- Parentheses `()` have the highest precedence and can be used to change the order of evaluation.
- Exponentiation `**` has the next highest precedence.
- Multiplication `*`, division `/`, floor division `//`, and modulus `%` have the same precedence and are evaluated from left to right.
- Addition `+` and subtraction `-` have the lowest precedence and are also evaluated from left to right.

Some examples of using arithmetic operators in Python are:

```python
# Addition
print(5 + 3) # 8
print(2.5 + 4.7) # 7.2
print('Hello' + 'World') # HelloWorld

# Subtraction
print(10 - 4) # 6
print(7.8 - 3.2) # 4.6
# print('Python' - 'Py') # Error: unsupported operand type(s) for -: 'str' and 'str'

# Multiplication
print(6 * 4) # 24
print(3.5 * 2.0) # 7.0
print('Hi' * 3) # HiHiHi

# Division
print(12 / 4) # 3.0
print(15 / 2) # 7.5
# print('Bye' / 2) # Error: unsupported operand type(s) for /: 'str' and 'int'

# Modulus
print(17 % 5) # 2
print(12.5 % 4.2) # 3.7
# print('Mod' % 2) # Error: not all arguments converted during string formatting

# Exponentiation
print(2 ** 3) # 8
print(4.0 ** 0.5) # 2.0
# print('Exp' ** 2) # Error: unsupported operand type(s) for ** or pow(): 'str' and 'int'

# Floor division
print(9 // 2) # 4
print(8.4 // 2.1) # 4.0
# print('Floor' // 2) # Error: unsupported operand type(s) for //: 'str' and 'int'
```