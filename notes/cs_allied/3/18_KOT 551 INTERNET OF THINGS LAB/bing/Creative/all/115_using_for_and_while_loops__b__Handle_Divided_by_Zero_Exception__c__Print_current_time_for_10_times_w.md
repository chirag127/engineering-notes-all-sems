# Using for and while loops, handling divided by zero exception, and printing current time for 10 times with an interval of 5 seconds.

## For and while loops
- For and while loops are two types of control structures that allow a program to execute a block of code repeatedly based on a condition.
- For loops are used when the number of iterations is known in advance, or when the loop needs to iterate over a sequence of elements, such as a list, a tuple, a string, or a range.
- While loops are used when the number of iterations is not known in advance, or when the loop needs to repeat until a certain condition is met or changed.
- The syntax of a for loop is:

```python
for variable in sequence:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
    # update condition if needed
```

- Both for and while loops can use the `break` statement to exit the loop prematurely, or the `continue` statement to skip the current iteration and move to the next one.
- Both for and while loops can also have an optional `else` clause that executes after the loop ends normally, but not when the loop is terminated by a `break` statement.

## Handling divided by zero exception
- Divided by zero exception is a type of runtime error that occurs when a program tries to divide a number by zero, which is mathematically undefined.
- In Python, dividing by zero will raise a `ZeroDivisionError` exception, which will stop the program execution unless it is handled by a `try-except` block.
- A `try-except` block is a way of handling exceptions by enclosing the code that may cause an exception in a `try` clause, and specifying what to do in case of an exception in an `except` clause.
- The syntax of a `try-except` block is:

```python
try:
    # do something that may cause an exception
except ExceptionType as error:
    # do something to handle the exception
    # error is a variable that holds the exception object
```

- The `ExceptionType` can be a specific type of exception, such as `ZeroDivisionError`, or a generic type, such as `Exception`, which can catch any kind of exception.
- The `error` variable can be used to access the attributes and methods of the exception object, such as `error.args` or `error.__str__()`.
- A `try-except` block can have multiple `except` clauses to handle different types of exceptions, or a `finally` clause that executes regardless of whether an exception occurs or not.

## Printing current time for 10 times with an interval of 5 seconds
- To print the current time, we can use the `datetime` module, which provides various classes and functions to manipulate dates and times.
- To import the `datetime` module, we can use the `import` statement:

```python
import datetime
```

- To get the current date and time as a `datetime` object, we can use the `datetime.now()` function:

```python
current_time = datetime.datetime.now()
```

- To format the `datetime` object as a string, we can use the `strftime()` method, which takes a format string as an argument and returns a formatted string according to the specified format.
- The format string can contain various placeholders that represent different components of the date and time, such as `%Y` for year, `%m` for month, `%d` for day, `%H` for hour, `%M` for minute, and `%S` for second.
- For example, to format the current time as `YYYY-MM-DD HH:MM:SS`, we can use:

```python
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
```

- To print the formatted time, we can use the `print()` function:

```python
print(formatted_time)
```

- To print the current time for 10 times with an interval of 5 seconds, we can use a for loop that iterates over a range of 10, and a `time` module that provides various functions to deal with time.
- To import the `time` module, we can use the `import` statement:

```python
import time
```

- To pause the program execution for a certain number of seconds, we can use the `time.sleep()` function, which takes a number of seconds as an argument and blocks the program until the specified time elapses.
- For example, to pause the program for 5 seconds, we can use:

```python
time.sleep(5)