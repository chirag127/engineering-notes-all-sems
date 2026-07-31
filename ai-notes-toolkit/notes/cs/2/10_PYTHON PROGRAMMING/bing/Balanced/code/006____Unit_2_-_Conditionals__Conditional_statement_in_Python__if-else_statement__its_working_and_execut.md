Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write the content in markdown format on the topic of Unit 2 - Conditionals. Here is the content:

# Unit 2 - Conditionals

## Conditional statement in Python (if-else statement, its working and execution)

- A conditional statement is a statement that executes a block of code based on a condition.
- In Python, the `if` statement is used to create a conditional statement.
- The syntax of the `if` statement is:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The condition is an expression that evaluates to a Boolean value (`True` or `False`).
- The block of code under the `if` clause is indented by four spaces or a tab.
- The `else` clause is optional and executes only if the condition is `False`.
- The `if` statement checks the condition and executes the corresponding block of code.
- Example:

```python
x = 10
if x > 0:
    print("x is positive")
else:
    print("x is negative or zero")
```

- Output:

```text
x is positive
```

## Nested-if statement and Elif statement in Python

- A nested-if statement is an `if` statement inside another `if` statement.
- The syntax of a nested-if statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
    if condition2:
        # block of code to execute if condition2 is True
    else:
        # block of code to execute if condition2 is False
else:
    # block of code to execute if condition1 is False
```

- The nested-if statement checks the condition1 first, and if it is `True`, it checks the condition2.
- The nested-if statement can have multiple levels of nesting, but it is not recommended to use more than three levels of nesting as it makes the code less readable and more prone to errors.
- Example:

```python
x = 10
y = 5
if x > y:
    print("x is greater than y")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is less than or equal to y")
```

- Output:

```text
x is greater than y
x is even
```

- An `elif` statement is a shorthand for an `else if` statement.
- The syntax of an `elif` statement is:

```python
if condition1:
    # block of code to execute if condition1 is True
elif condition2:
    # block of code to execute if condition2 is True
elif condition3:
    # block of code to execute if condition3 is True
...
else:
    # block of code to execute if none of the conditions are True
```

- The `elif` statement checks the conditions in order, and executes the first block of code whose condition is `True`.
- The `elif` statement can have multiple clauses, but only one of them can execute at a time.
- The `else` clause is optional and executes only if none of the conditions are `True`.
- The `elif` statement is useful when there are multiple mutually exclusive conditions to check.
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

```text
B
```

## Expression Evaluation & Float Representation

- An expression is a combination of values, variables, operators, and functions that produces a result when evaluated.
- In Python, expressions are evaluated according to the rules of precedence and associativity of operators.
- The precedence of operators determines the order in which they are evaluated in an expression. Operators with higher precedence are evaluated before operators with lower precedence.
- The associativity of operators determines the order in which they are evaluated when they have the same precedence. Operators can be either left-associative or right-associative. Left-associative operators are evaluated from left to right, and right-associative operators are evaluated from right to left.
- The table below shows the precedence and associativity of some common operators in Python:

| Operator | Description | Precedence | Associativity |
|----------|-------------|------------|---------------|
| `**`