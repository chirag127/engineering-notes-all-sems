## Unit 2 - Conditionals

### Conditional statement in Python
- Conditional statements are used to control the flow of execution of a program based on certain conditions.
- The `if` statement is used to execute a block of code if a specified condition is `True`.
- The `else` statement is used to execute a block of code if the condition in the `if` statement is `False`.
- The syntax for an `if` statement is as follows:
```
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```
- The condition is evaluated and if it is `True`, the code block under the `if` statement is executed. If the condition is `False`, the code block under the `else` statement is executed.

### Nested-if statement and Elif statement in Python
- A nested `if` statement is an `if` statement inside another `if` statement.
- The syntax for a nested `if` statement is as follows:
```
if condition1:
    # code to execute if condition1 is True
    if condition2:
        # code to execute if condition2 is True
    else:
        # code to execute if condition2 is False
else:
    # code to execute if condition1 is False
```
- The `elif` statement is used to check multiple conditions in a more concise way.
- The syntax for an `elif` statement is as follows:
```
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
else:
    # code to execute if none of the conditions are True
```
- The conditions are evaluated in order and the first condition that is `True` is executed. If none of the conditions are `True`, the code block under the `else` statement is executed.

### Expression Evaluation & Float Representation
- In Python, expressions are evaluated according to the rules of operator precedence.
- The order of precedence is as follows: parentheses, exponentiation, multiplication and division, addition and subtraction.
- Floats are represented using the IEEE 754 standard.
- Due to the limitations of this representation, some decimal numbers cannot be represented exactly and may result in small rounding errors.
- It is important to be aware of these limitations when working with floats in Python.