# Unit 2 - Conditionals

## Conditional statement in Python (if-else statement, its working and execution)

- A conditional statement is a statement that executes a block of code based on a condition.
- A condition is an expression that evaluates to either True or False.
- In Python, a conditional statement has the following syntax:

```python
if condition:
    # block of code to execute if condition is True
else:
    # block of code to execute if condition is False
```

- The if keyword introduces the condition, followed by a colon (:).
- The block of code under the if keyword is indented by four spaces or a tab. This block is called the if-block.
- The else keyword introduces the alternative block of code, followed by a colon (:).
- The block of code under the else keyword is indented by the same amount as the if-block. This block is called the else-block.
- Only one of the blocks (if-block or else-block) is executed, depending on the value of the condition.
- If the condition is True, the if-block is executed and the else-block is skipped.
- If the condition is False, the else-block is executed and the if-block is skipped.
- For example, the following code prints "Hello, world!" if the variable x is equal to 10, and prints "Goodbye, world!" otherwise.

```python
x = 10
if x == 10:
    print("Hello, world!")
else:
    print("Goodbye, world!")
```

## Nested-if statement and Elif statement in Python

- A nested-if statement is a conditional statement that contains another conditional statement inside its block of code.
- A nested-if statement can be used to check for multiple conditions and execute different blocks of code accordingly.
- For example, the following code prints "Positive" if the variable x is greater than zero, prints "Negative" if x is less than zero, and prints "Zero" if x is equal to zero.

```python
x = 0
if x > 0:
    print("Positive")
else:
    if x < 0:
        print("Negative")
    else:
        print("Zero")
```

- An elif statement is a shorthand way of writing a nested-if statement that has only one condition in each block of code.
- An elif statement has the following syntax:

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

- The elif keyword stands for "else if", and introduces another condition to check, followed by a colon (:).
- The block of code under the elif keyword is indented by the same amount as the if-block.
- An elif statement can have multiple elif clauses, each with a different condition and a different block of code.
- The else clause is optional, and executes if none of the conditions are True.
- Only one of the blocks (if-block, elif-block, or else-block) is executed, depending on the value of the conditions.
- The conditions are checked in order, from top to bottom, until one of them is True or all of them are False.
- For example, the following code is equivalent to the previous nested-if example, but uses an elif statement instead.

```python
x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
```

## Expression Evaluation & Float Representation

- An expression is a combination of values, variables, operators, and functions that produces a result when evaluated.
- For example, the expression 2 + 3 * 4 evaluates to 14, because the multiplication operator (*) has higher precedence than the addition operator (+), and is evaluated first.
- The order of precedence of operators in Python is as follows, from highest to lowest:

  - Parentheses ()
  - Exponentiation **
  - Unary operators +, -
  - Multiplication *, division /, floor division //, modulo %
  - Addition +, subtraction -
  - Comparison operators ==, !=, <, >, <=, >=
  - Logical operators not, and, or

- Operators with the same precedence are evaluated from left to right, except for exponentiation, which is evaluated from right to left.
- For example, the expression 2 ** 3 ** 2 evaluates to 512, because the rightmost exponentiation is evaluated first