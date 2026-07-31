# Using for and while loops, handling divided by zero exception, and printing current time for 10 times with an interval of 1 second

## For and while loops

- For and while loops are two types of control structures that allow a program to execute a block of code repeatedly until a certain condition is met.
- For loops are used when the number of iterations is known in advance, or when the loop needs to iterate over a sequence of elements, such as a list, a tuple, a string, or a range object.
- While loops are used when the number of iterations is not known in advance, or when the loop needs to check a condition before each iteration, such as a user input, a random number, or a boolean expression.
- The syntax of a for loop is:

```python
for variable in sequence:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
```

- Both for and while loops can use the `break` statement to exit the loop prematurely, or the `continue` statement to skip the current iteration and move on to the next one.
- Both for and while loops can also have an optional `else` clause that executes after the loop ends normally, but not when the loop is terminated by a `break` statement.

## Handling divided by zero exception

- Divided by zero exception is a type of runtime error that occurs when a program tries to divide a number by zero, which is mathematically undefined and invalid.
- In Python, dividing by zero will raise a `ZeroDivisionError` exception, which will stop the program execution and display an error message, unless the exception is handled by a `try-except` block.
- A `try-except` block is a way of handling exceptions by enclosing the code that may cause an exception in a `try` clause, and specifying what to do in case of an exception in an `except` clause.
- The syntax of a `try-except` block is:

```python
try:
    # do something that may cause an exception
except ExceptionType as e:
    # do something to handle the exception
```

- The `ExceptionType` is the name of the specific exception that the program wants to handle, such as `ZeroDivisionError`, `ValueError`, `TypeError`, etc. The `e` is a variable that holds the exception object, which contains information about the error, such as the error message, the line number, the stack trace, etc.
- The `try-except` block can have multiple `except` clauses to handle different types of exceptions, or a single `except` clause without specifying the `ExceptionType` to handle any exception. It can also have an optional `else` clause that executes if no exception occurs, and a `finally` clause that executes regardless of whether an exception occurs or not.
- To handle the divided by zero exception, the program can use a `try-except` block to catch the `ZeroDivisionError` exception, and either display a custom error message, or perform an alternative calculation, or ask the user to enter a valid input, or terminate the program gracefully.

## Printing current time for 10 times with an interval of 1 second

- To print the current time, the program can use the `datetime` module, which provides various functions and classes to manipulate dates and times.
- The `datetime` module has a `datetime` class, which represents a date and time object with attributes such as year, month, day, hour, minute, second, microsecond, etc.
- The `datetime` class has a `now` method, which returns the current local date and time as a `datetime` object.
- The `datetime` class also has a `strftime` method, which converts a `datetime` object into a formatted string according to a given format specifier, such as `%Y` for year, `%m` for month, `%d` for day, `%H` for hour, `%M` for minute, `%S` for second, etc.
- To print the current time for 10 times with an interval of 1 second, the program can use a for loop to iterate 10 times, and use the `datetime` module to get and format the current time, and use the `print` function to display it.
- To create an interval of 1 second between each iteration, the program can use the `time` module, which provides various functions and classes to deal with time-related tasks.
- The `time` module has a `sleep` function, which pauses the program execution for a given number of seconds.
- The program can call the `sleep` function with an argument of