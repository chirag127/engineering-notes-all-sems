# Unit 2 - Conditionals

## Conditional statement in Python (if-else statement, its working and execution)

- A conditional statement is a statement that can be either true or false depending on the values of the variables or expressions involved.
- In Python, a conditional statement is written using the `if` keyword, followed by a condition (a logical expression that evaluates to either `True` or `False`), and a colon (`:`). The condition is usually enclosed in parentheses, but this is optional.
- After the colon, a block of code (called the body of the `if` statement) is indented by four spaces or a tab. This block of code will only execute if the condition is true. Otherwise, it will be skipped.
- Optionally, an `else` keyword can be used after the body of the `if` statement, followed by another colon and another block of code (called the body of the `else` statement). This block of code will only execute if the condition is false. Otherwise, it will be skipped.
- The `else` keyword must be aligned with the `if` keyword, and the body of the `else` statement must be indented by the same amount as the body of the `if` statement.
- An example of a conditional statement in Python is:

```python
# A program that checks if a number is positive, negative, or zero
number = int(input("Enter a number: ")) # Get a number from the user
if (number > 0): # Check if the number is positive
    print("The number is positive.") # Print a message if the condition is true
else: # Otherwise
    if (number < 0): # Check if the number is negative
        print("The number is negative.") # Print a message if the condition is true
    else: # Otherwise
        print("The number is zero.") # Print a message if the condition is true
```

- The working and execution of a conditional statement in Python is as follows:
  - The interpreter evaluates the condition after the `if` keyword. If the condition is true, it executes the body of the `if` statement and skips the rest of the statement. If the condition is false, it skips the body of the `if` statement and checks if there is an `else` keyword.
  - If there is an `else` keyword, the interpreter executes the body of the `else` statement and skips the rest of the statement. If there is no `else` keyword, the interpreter skips the rest of the statement.
  - The interpreter moves on to the next statement after the conditional statement.

## Nested-if statement and Elif statement in Python

- A nested-if statement is a conditional statement that contains another conditional statement inside its body. This allows for more complex logic and multiple conditions to be checked.
- A nested-if statement can have any number of levels of nesting, but it is advisable to avoid too much nesting as it can make the code difficult to read and debug.
- An example of a nested-if statement in Python is:

```python
# A program that checks if a year is a leap year
year = int(input("Enter a year: ")) # Get a year from the user
if (year % 4 == 0): # Check if the year is divisible by 4
    if (year % 100 == 0): # Check if the year is divisible by 100
        if (year % 400 == 0): # Check if the year is divisible by 400
            print("The year is a leap year.") # Print a message if all conditions are true
        else: # Otherwise
            print("The year is not a leap year.") # Print a message if the last condition is false
    else: # Otherwise
        print("The year is a leap year.") # Print a message if the second condition is false
else: # Otherwise
    print("The year is not a leap year.") # Print a message if the first condition is false
```

- An elif statement is a shorthand way of writing a nested-if statement that has multiple branches. It stands for "else if" and is used to check another condition after the first condition is false.
- An elif statement can have any number of branches, but only one of them will execute depending on which condition is true first. The last branch can be an `else` statement, which will execute if none of the conditions are true.
- An example of an elif statement in Python is:

```python
# A program that assigns grades based on marks
marks = int(input("Enter your marks: ")) # Get marks from the user
if (marks >= 90): # Check