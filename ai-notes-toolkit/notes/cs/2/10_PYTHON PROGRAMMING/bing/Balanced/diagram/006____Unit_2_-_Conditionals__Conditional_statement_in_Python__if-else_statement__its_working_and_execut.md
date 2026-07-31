Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some content in markdown format that you can use for your study material.

## Unit 2 - Conditionals

### Conditional statement in Python

- A conditional statement is a statement that controls the flow of execution depending on some condition.
- In Python, the `if` statement is used to write a conditional statement.
- The syntax of the `if` statement is:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The `condition` is an expression that evaluates to a Boolean value, either `True` or `False`.
- The `if` and `else` keywords are followed by a colon (`:`) and indented by four spaces or a tab.
- The block of code under the `if` clause is executed only if the condition is `True`, otherwise the block of code under the `else` clause is executed.
- The `else` clause is optional and can be omitted if there is no alternative action to take when the condition is `False`.
- Example:

```python
x = 10
y = 5
if x > y:
    print("x is greater than y")
else:
    print("x is less than or equal to y")
```

- Output:

```
x is greater than y
```

### Nested-if statement and Elif statement in Python

- A nested-if statement is a conditional statement that contains another conditional statement inside it.
- The nested-if statement can be used to check for multiple conditions and execute different blocks of code accordingly.
- The syntax of the nested-if statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
    if condition2:
        # block of code to execute if condition1 and condition2 are True
    else:
        # block of code to execute if condition1 is True and condition2 is False
else:
    # block of code to execute if condition1 is False
```

- The nested-if statement can have more than one level of nesting, but it is not recommended to use too many levels as it can make the code difficult to read and understand.
- Example:

```python
x = 10
y = 5
z = 15
if x > y:
    print("x is greater than y")
    if x > z:
        print("x is the greatest of all")
    else:
        print("x is not the greatest of all")
else:
    print("x is less than or equal to y")
```

- Output:

```
x is greater than y
x is not the greatest of all
```

- An `elif` statement is a shorthand way of writing a nested-if statement that has only one block of code for each condition.
- The `elif` statement is used to check for multiple conditions in a sequential order and execute the first block of code that matches the condition.
- The syntax of the `elif` statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition1 is False and condition2 is True
elif condition3:
    # block of code to execute if condition1 and condition2 are False and condition3 is True
...
else:
    # block of code to execute if none of the conditions are True
```

- The `elif` keyword is short for "else if" and is followed by a colon (`:`) and indented by four spaces or a tab.
- The `else` clause is optional and can be omitted if there is no default action to take when none of the conditions are `True`.
- The `elif` statement can have any number of conditions, but only one block of code will be executed for the first condition that evaluates to `True`.
- Example:

```python
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")
```

- Output:

```
B
```

### Expression Evaluation & Float Representation

- An expression is a combination of values, variables, operators, and functions that produces a result when evaluated.
- In Python, expressions are evaluated according to the rules of precedence and associativity of the operators and functions involved.
- The precedence of an operator determines the order in which it is applied in an expression. Operators with higher precedence are applied before operators with lower precedence