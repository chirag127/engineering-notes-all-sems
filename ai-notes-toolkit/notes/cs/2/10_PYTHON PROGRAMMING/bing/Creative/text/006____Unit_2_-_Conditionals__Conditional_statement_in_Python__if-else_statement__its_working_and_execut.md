## Unit 2 - Conditionals

- Conditional statements are used to control the flow of execution in a program based on some conditions.
- The most common conditional statement in Python is the `if-else` statement, which has the following syntax:

```python
if condition:
    # execute this block of code if condition is True
else:
    # execute this block of code if condition is False
```

- The `condition` is a boolean expression that evaluates to either `True` or `False`.
- The `if` and `else` keywords are followed by a colon (`:`) and indented blocks of code.
- The indentation is important in Python, as it defines the scope of the code blocks.
- Only one of the code blocks will be executed, depending on the value of the condition.
- For example:

```python
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

- This code will print "x is positive" if x is greater than 0, and "x is negative or zero" otherwise.

- Nested-if statement is a conditional statement that contains another conditional statement inside it.
- The nested conditional statement can be either an `if-else` statement or an `elif` statement, which will be explained later.
- The syntax of a nested-if statement is:

```python
if condition1:
    # execute this block of code if condition1 is True
    if condition2:
        # execute this block of code if condition2 is True
    else:
        # execute this block of code if condition2 is False
else:
    # execute this block of code if condition1 is False
```

- The nested conditional statement is indented inside the outer conditional statement.
- The nested conditional statement will only be evaluated if the outer condition is True.
- For example:

```python
x = 10
y = 5
if x > 0:
    print("x is positive")
    if y > 0:
        print("y is also positive")
    else:
        print("y is negative or zero")
else:
    print("x is negative or zero")
```

- This code will print "x is positive" and "y is also positive" if x and y are both greater than 0, "x is positive" and "y is negative or zero" if x is greater than 0 and y is less than or equal to 0, and "x is negative or zero" if x is less than or equal to 0.

- Elif statement is a conditional statement that is used to check multiple conditions in a sequence.
- The `elif` keyword stands for "else if", and it is followed by a condition and a colon (`:`).
- The `elif` statement can be used after an `if` statement or another `elif` statement, but not after an `else` statement.
- The syntax of an `elif` statement is:

```python
if condition1:
    # execute this block of code if condition1 is True
elif condition2:
    # execute this block of code if condition1 is False and condition2 is True
elif condition3:
    # execute this block of code if condition1 and condition2 are False and condition3 is True
else:
    # execute this block of code if all conditions are False
```

- The `elif` statement allows us to check multiple conditions in a single conditional statement, without using nested-if statements.
- The `elif` statement will only be evaluated if the previous conditions are False.
- Only one of the code blocks will be executed, depending on which condition is True first.
- For example:

```python
x = 10
if x < 0:
    print("x is negative")
elif x == 0:
    print("x is zero")
elif x < 10:
    print("x is positive and less than 10")
else:
    print("x is positive and greater than or equal to 10")
```

- This code will print "x is positive and greater than or equal to 10" if x is 10, "x is zero" if x is 0, "x is negative" if x is less than 0, and "x is positive and less than 10" if x is between 0 and 10.

- Expression evaluation is the process of computing the value of an expression, which can consist of literals, variables, operators, and parentheses.
- The order of evaluation of an expression depends on the precedence and associativity of the operators involved.
- The precedence of an operator determines which operator is evaluated first in an expression that contains multiple operators.
-