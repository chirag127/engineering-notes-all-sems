## Unit 2 - Conditionals

- Conditional statements are used to control the flow of execution of a program based on some conditions.
- In Python, the most common conditional statement is the `if-else` statement, which has the following syntax:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The `condition` is a boolean expression that evaluates to either `True` or `False`.
- The `if` and `else` keywords are followed by a colon (`:`) and indented blocks of code.
- The indented block of code under the `if` clause is executed only if the condition is `True`, otherwise the indented block of code under the `else` clause is executed.
- For example, the following code prints a message based on the value of a variable `x`:

```python
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

- The output of this code is:

```
x is positive
```

- Nested-if statement is a conditional statement that contains another conditional statement inside it.
- The nested conditional statement can be either an `if-else` statement or an `elif` statement.
- The `elif` statement is used to check multiple conditions in a sequential manner, and has the following syntax:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
elif condition3:
    # block of code to execute if condition1 and condition2 are False and condition3 is True
...
else:
    # block of code to execute if all conditions are False
```

- The `elif` keyword is short for `else if`, and is followed by a colon (`:`) and an indented block of code.
- The `elif` clause is executed only if the previous condition is `False` and the current condition is `True`.
- The `else` clause is executed only if all the conditions are `False`.
- For example, the following code prints a message based on the value of a variable `grade`:

```python
grade = 85
if grade >= 90:
    print("Excellent")
elif grade >= 80:
    print("Good")
elif grade >= 70:
    print("Fair")
elif grade >= 60:
    print("Pass")
else:
    print("Fail")
```

- The output of this code is:

```
Good
```

- Expression evaluation is the process of computing the value of an expression by applying the rules of precedence and associativity of operators and operands.
- In Python, the order of precedence of operators from highest to lowest is:

  - Parentheses `()`
  - Exponentiation `**`
  - Unary operators `+`, `-`, `~`, `not`
  - Multiplication `*`, division `/`, floor division `//`, modulo `%`
  - Addition `+`, subtraction `-`
  - Bitwise operators `<<`, `>>`, `&`, `^`, `|`
  - Comparison operators `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in`
  - Logical operators `and`, `or`

- The associativity of operators determines the order of evaluation of operators with the same precedence level.
- In Python, most operators are left-associative, meaning they are evaluated from left to right, except for the exponentiation operator `**`, which is right-associative, meaning it is evaluated from right to left.
- For example, the following expression is evaluated as:

```python
2 ** 3 ** 2
```

- `(2 ** (3 ** 2))`
- `(2 ** 9)`
- `512`

- Float representation is the way of storing and displaying decimal numbers in a computer system.
- In Python, float numbers are represented using the IEEE 754 standard, which uses a fixed number of bits (usually 64) to store the sign, exponent, and fraction of a decimal number.
- The sign bit indicates whether the number is positive or negative, the exponent bits indicate the magnitude of the number, and the fraction bits indicate the precision of the number.
- For example, the float number `12.34` is represented as:

```
0 10000000010 10001011100011110101110
```

- The sign bit is `0`, indicating the number is positive.
- The exponent bits are `