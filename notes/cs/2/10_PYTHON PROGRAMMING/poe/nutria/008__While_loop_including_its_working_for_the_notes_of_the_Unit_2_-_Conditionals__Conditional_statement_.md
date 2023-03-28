
### While loop
A while loop is a looping construct in Python that allows a program to execute a block of code repeatedly until a certain condition is met. The syntax of a while loop is:

```
while <condition>:
    <statement(s)>
```

The condition is evaluated before each iteration of the loop, and if it evaluates to `True`, the loop body is executed. If it evaluates to `False`, the loop is terminated and execution continues with the statement following the loop.

#### Conditional statement in Python (if-else statement)
The `if-else` statement is a conditional statement in Python that evaluates a condition and executes a block of code based on the result. The syntax of the `if-else` statement is:

```
if <condition>:
    <statement(s)>
else:
    <statement(s)>
```

The `if` statement evaluates the condition and if it evaluates to `True`, the statements in the `if` block are executed. Otherwise, the statements in the `else` block are executed.

#### Nested-if statement
A nested-if statement is a conditional statement in Python that evaluates multiple conditions and executes a block of code based on the result. The syntax of the nested-if statement is:

```
if <condition1>:
    <statement(s)>
elif <condition2>:
    <statement(s)>
elif <condition3>:
    <statement(s)>
...
else:
    <statement(s)>
```

The `if-elif` statements evaluate the conditions in order and if one of them evaluates to `True`, the statements in the corresponding block are executed. If none of the conditions evaluate to `True`, the statements in the `else` block are executed.

#### Elif statement in Python
The `elif` statement is a conditional statement in Python that evaluates multiple conditions and executes a block of code based on the result. The syntax of the `elif` statement is:

```
if <condition1>:
    <statement(s)>
elif <condition2>:
    <statement(s)>
elif <condition3>:
    <statement(s)>
...
```

The `elif` statements evaluate the conditions in order and if one of them evaluates to `True`, the statements in the corresponding block are executed. If none of the conditions evaluate to `True`, the statement following the `elif` statement is executed.

#### Expression Evaluation & Float Representation
Expression evaluation is the process of evaluating an expression in Python to determine its value. Expressions can be evaluated using the `eval()` function, which takes a string as an argument and returns the value of the expression.

Float representation is the way in which a number is represented in Python as a floating-point number. Floats are represented as a sequence of digits, with a decimal point and an optional exponent. For example, the number `3.14` is represented as `3.14e0`.