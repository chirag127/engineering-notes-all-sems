## Unit 2 - Conditionals

### Conditional statement in Python

- A conditional statement is a statement that controls the flow of execution depending on some condition.
- In Python, the conditional statement is written using the `if` keyword, followed by a boolean expression and a colon (:).
- The body of the `if` statement is a block of code that is executed only if the boolean expression evaluates to `True`.
- The body of the `if` statement is indented by four spaces or a tab from the `if` keyword.
- Example:

```python
# A program that checks if a number is positive
number = int(input("Enter a number: ")) # Get a number from the user
if number > 0: # Check if the number is positive
    print("The number is positive.") # Print a message if the condition is true
```

- The `if` statement can be followed by an optional `else` clause, which is executed if the boolean expression evaluates to `False`.
- The `else` keyword is aligned with the `if` keyword, and is followed by a colon (:).
- The body of the `else` clause is a block of code that is executed only if the boolean expression evaluates to `False`.
- Example:

```python
# A program that checks if a number is even or odd
number = int(input("Enter a number: ")) # Get a number from the user
if number % 2 == 0: # Check if the number is divisible by 2
    print("The number is even.") # Print a message if the condition is true
else: # Otherwise
    print("The number is odd.") # Print a message if the condition is false
```

### Nested-if statement and Elif statement in Python

- A nested-if statement is an `if` statement that is inside another `if` statement.
- A nested-if statement allows us to check for multiple conditions in a hierarchical manner.
- Example:

```python
# A program that checks if a number is positive, negative or zero
number = int(input("Enter a number: ")) # Get a number from the user
if number > 0: # Check if the number is positive
    print("The number is positive.") # Print a message if the condition is true
else: # Otherwise
    if number < 0: # Check if the number is negative
        print("The number is negative.") # Print a message if the condition is true
    else: # Otherwise
        print("The number is zero.") # Print a message if the condition is true
```

- An `elif` statement is a shorthand for an `else` followed by an `if` statement.
- An `elif` statement allows us to check for multiple conditions in a sequential manner, without nesting.
- An `elif` statement is written using the `elif` keyword, followed by a boolean expression and a colon (:).
- The body of the `elif` statement is a block of code that is executed only if the boolean expression evaluates to `True` and all the previous conditions are `False`.
- An `elif` statement can be followed by another `elif` statement or an `else` clause, but not by an `if` statement.
- Example:

```python
# A program that checks if a grade is A, B, C, D or F
grade = int(input("Enter a grade: ")) # Get a grade from the user
if grade >= 90: # Check if the grade is greater than or equal to 90
    print("The grade is A.") # Print a message if the condition is true
elif grade >= 80: # Check if the grade is greater than or equal to 80 and less than 90
    print("The grade is B.") # Print a message if the condition is true
elif grade >= 70: # Check if the grade is greater than or equal to 70 and less than 80
    print("The grade is C.") # Print a message if the condition is true
elif grade >= 60: # Check if the grade is greater than or equal to 60 and less than 70
    print("The grade is D.") # Print a message if the condition is true
else: # Otherwise
    print("The grade is F.") # Print a message if the condition is false
```

### Expression Evaluation & Float Representation

- An expression is a combination of values, variables, operators and functions that produces a result when evaluated.
- In Python, expressions are evaluated according to the rules of precedence and associativity of the operators and functions involved.
- The order of precedence of the operators in Python is as follows (from