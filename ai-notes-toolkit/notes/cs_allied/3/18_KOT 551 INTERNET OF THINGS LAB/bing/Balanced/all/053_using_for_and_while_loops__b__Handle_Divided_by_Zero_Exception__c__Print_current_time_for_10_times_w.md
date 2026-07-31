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

- Both for and while loops can use the `break` statement to exit the loop prematurely, or the `continue` statement to skip the current iteration and move to the next one.
- Both for and while loops can also use an optional `else` clause that executes after the loop ends normally, but not if the loop is terminated by a `break` statement.

## Handling divided by zero exception
- Dividing by zero is an invalid mathematical operation that causes a `ZeroDivisionError` exception in Python.
- An exception is an error that occurs during the execution of a program and disrupts the normal flow of control.
- To handle an exception, a program can use a `try-except` block that encloses the code that may cause the exception, and specifies what to do in case the exception occurs.
- The syntax of a `try-except` block is:

```python
try:
    # do something that may cause an exception
except ExceptionType as error:
    # do something to handle the exception
```

- The `ExceptionType` is the name of the specific exception that the program wants to catch, such as `ZeroDivisionError`, `ValueError`, `IndexError`, etc. The `error` variable is an optional name that can be used to access the exception object and its attributes, such as `error.args`, `error.message`, etc.
- A `try-except` block can have multiple `except` clauses to handle different types of exceptions, or a single `except` clause without specifying the exception type to catch any exception. It can also have an optional `else` clause that executes if no exception occurs, and a `finally` clause that executes regardless of whether an exception occurs or not.
- To handle a divided by zero exception, a program can use a `try-except` block that catches the `ZeroDivisionError` exception and performs an alternative action, such as printing a message, returning a default value, or raising another exception.

## Printing current time for 10 times with an interval of 1 second
- To print the current time, a program can use the `datetime` module that provides various functions and classes to manipulate dates and times.
- The `datetime.datetime.now()` function returns a `datetime` object that represents the current date and time in the local timezone.
- The `datetime.datetime.strftime()` method converts a `datetime` object into a string according to a given format.
- To print the current time for 10 times with an interval of 1 second, a program can use a for loop that iterates over a range of 10, and prints the formatted current time using the `datetime` module. It can also use the `time` module that provides various functions to deal with time-related tasks.
- The `time.sleep()` function pauses the execution of the program for a given number of seconds.
- The following code snippet demonstrates how to print the current time for 10 times with an interval of 1 second:

```python
import datetime
import time

for i in range(10):
    # get the current time as a datetime object
    now = datetime.datetime.now()
    # format the datetime object as a string
    time_string = now.strftime("%H:%M:%S")
    # print the time string
    print(time_string)
    # wait for 1 second
    time.sleep(1)
```