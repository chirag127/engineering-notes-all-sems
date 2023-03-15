## Unit 2 - Conditionals

### Conditional statement in Python
- Conditional statements are used to control the flow of execution of a program based on certain conditions.
- The `if` statement is used to execute a block of code if a specified condition is `True`.
- The syntax for an `if` statement is as follows:
```
if condition:
    # code to execute if condition is True
```
- The condition is evaluated, and if it is `True`, the code block indented under the `if` statement is executed.
- If the condition is `False`, the code block is skipped and the program continues to the next line of code after the `if` block.

### The `else` statement
- The `else` statement is used in conjunction with the `if` statement to provide an alternative block of code to execute if the condition in the `if` statement is `False`.
- The syntax for an `if-else` statement is as follows:
```
if condition:
    # code to execute if condition is True
else:
    # code to execute if condition is False
```
- If the condition is `True`, the code block under the `if` statement is executed. If the condition is `False`, the code block under the `else` statement is executed.

### The `elif` statement
- The `elif` statement is used to chain multiple `if` statements together.
- It is used to test multiple conditions and execute different code blocks depending on which condition is `True`.
- The syntax for an `if-elif-else` statement is as follows:
```
if condition1:
    # code to execute if condition1 is True
elif condition2:
    # code to execute if condition2 is True
else:
    # code to execute if none of the conditions are True
```
- The conditions are evaluated in order. If `condition1` is `True`, the code block under the first `if` statement is executed. If `condition1` is `False`, `condition2` is evaluated. If `condition2` is `True`, the code block under the first `elif` statement is executed. If `condition2` is `False`, the code block under the `else` statement is executed.

### Nested `if` statements
- `if` statements can be nested inside other `if` statements to create more complex conditional logic.
- The syntax for a nested `if` statement is as follows:
```
if condition1:
    # code to execute if condition1 is True
    if condition2:
        # code to execute if condition1 and condition2 are both True
```
- If `condition1` is `True`, the code block under the first `if` statement is executed. Within this code block, `condition2` is evaluated. If `condition2` is also `True`, the code block under the second `if` statement is executed.

### Expression Evaluation & Float Representation
- In Python, expressions are evaluated according to the rules of operator precedence.
- Operators with higher precedence are evaluated before operators with lower precedence.
- Parentheses can be used to override the default order of operations and group expressions together.
- Floats are represented using a fixed number of bits, which can result in small rounding errors when performing arithmetic operations.
- It is important to be aware of these errors and take them into account when writing programs that rely on precise floating-point calculations.