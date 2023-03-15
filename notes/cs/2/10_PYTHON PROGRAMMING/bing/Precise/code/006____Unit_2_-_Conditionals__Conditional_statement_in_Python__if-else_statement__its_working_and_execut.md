## Unit 2 - Conditionals

### Conditional statement in Python
- Conditional statements are used to control the flow of execution in a program.
- The `if` statement is used to test a condition and execute a block of code if the condition is `True`.
- The `else` statement is used to execute a block of code if the condition in the `if` statement is `False`.
- The syntax for an `if-else` statement is as follows:
```
if condition:
    # code block to execute if condition is True
else:
    # code block to execute if condition is False
```

### Nested-if statement and Elif statement in Python
- A nested `if` statement is an `if` statement inside another `if` statement.
- The `elif` statement is used to test multiple conditions in a more concise way than using nested `if` statements.
- The syntax for an `elif` statement is as follows:
```
if condition1:
    # code block to execute if condition1 is True
elif condition2:
    # code block to execute if condition1 is False and condition2 is True
else:
    # code block to execute if all conditions are False
```

### Expression Evaluation & Float Representation
- In Python, expressions are evaluated according to the rules of operator precedence.
- Floats are represented using the IEEE 754 standard, which specifies a binary format for representing floating-point numbers.
- Due to the limitations of this representation, some decimal numbers cannot be represented exactly as floats, leading to small rounding errors in calculations.