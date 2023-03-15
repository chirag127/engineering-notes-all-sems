## Unit 2 - Conditionals

### Conditional statement in Python
- Conditional statements are used to control the flow of execution of a program based on certain conditions.
- The `if` statement is used to execute a block of code if a certain condition is true.
- The `else` statement is used to execute a block of code if the condition in the `if` statement is false.
- The syntax for the `if-else` statement is as follows:
```
if condition:
    # code block to be executed if condition is true
else:
    # code block to be executed if condition is false
```
- The condition is evaluated to a boolean value, either `True` or `False`.
- If the condition is `True`, the code block under the `if` statement is executed.
- If the condition is `False`, the code block under the `else` statement is executed.

### Nested-if statement and Elif statement in Python
- A nested `if` statement is an `if` statement inside another `if` statement.
- It is used to test multiple conditions and execute different code blocks based on the results of those tests.
- The syntax for a nested `if` statement is as follows:
```
if condition1:
    # code block to be executed if condition1 is true
    if condition2:
        # code block to be executed if condition1 and condition2 are true
    else:
        # code block to be executed if condition1 is true and condition2 is false
else:
    # code block to be executed if condition1 is false
```
- The `elif` statement is used as a shorthand for `else if`.
- It is used to test multiple conditions in a more concise and readable way.
- The syntax for the `elif` statement is as follows:
```
if condition1:
    # code block to be executed if condition1 is true
elif condition2:
    # code block to be executed if condition1 is false and condition2 is true
else:
    # code block to be executed if condition1 and condition2 are false
```

### Expression Evaluation & Float Representation
- In Python, expressions are evaluated according to the rules of operator precedence.
- Operators with higher precedence are evaluated before operators with lower precedence.
- Parentheses can be used to override the default order of evaluation.
- Floats are represented using the IEEE 754 standard.
- Due to the limitations of this representation, some decimal numbers cannot be represented exactly as floats.
- This can lead to small rounding errors when performing arithmetic operations with floats.