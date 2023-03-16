# Using for and while loops, handling divided by zero exception, and printing current time for 10 times with an interval of 1 second

## For and while loops
- For and while loops are two types of control structures that allow a program to execute a block of code repeatedly based on a condition.
- A for loop has a fixed number of iterations, determined by a range, a list, or a string. It uses the syntax `for variable in iterable:`
- A while loop has an indefinite number of iterations, determined by a boolean expression. It uses the syntax `while condition:`
- Both for and while loops can use the keywords `break` and `continue` to alter the flow of the loop. `break` exits the loop immediately, while `continue` skips the rest of the current iteration and moves to the next one.
- Example of a for loop that prints the numbers from 1 to 10:

```python
for i in range(1, 11):
  print(i)
```

- Example of a while loop that prints the numbers from 1 to 10:

```python
i = 1
while i <= 10:
  print(i)
  i = i + 1
```

## Handling divided by zero exception
- An exception is an error that occurs during the execution of a program, which disrupts the normal flow of the program.
- A divided by zero exception is a specific type of exception that occurs when a number is divided by zero, which is mathematically undefined.
- In Python, a divided by zero exception is represented by the `ZeroDivisionError` class, which inherits from the `ArithmeticError` class, which in turn inherits from the `Exception` class.
- To handle an exception, a program can use the `try-except` statement, which allows the program to try a block of code and catch any exception that occurs in that block.
- The syntax of the `try-except` statement is:

```python
try:
  # block of code that may raise an exception
except ExceptionType as e:
  # block of code that handles the exception
```

- The `ExceptionType` is the name of the exception class that the program wants to catch. The `e` is a variable that holds the exception object, which contains information about the error.
- If the `ExceptionType` is omitted, the program will catch any exception that occurs in the `try` block. However, it is recommended to specify the exception type to avoid catching unrelated errors.
- Example of handling a divided by zero exception:

```python
try:
  x = 10 / 0 # this will raise a ZeroDivisionError
except ZeroDivisionError as e:
  print("Cannot divide by zero") # this will handle the exception
  print(e) # this will print the exception object
```

## Printing current time for 10 times with an interval of 1 second
- To print the current time, a program can use the `datetime` module, which provides various classes and functions for working with dates and times.
- The `datetime` module has a `datetime` class, which represents a date and time object. The `datetime` class has a `now` method, which returns the current date and time as a `datetime` object.
- To format the `datetime` object as a string, the program can use the `strftime` method, which takes a format string as an argument and returns a formatted string according to the format.
- The format string can contain various placeholders that represent different components of the date and time, such as `%Y` for year, `%m` for month, `%d` for day, `%H` for hour, `%M` for minute, and `%S` for second.
- Example of printing the current date and time in the format `YYYY-MM-DD HH:MM:SS`:

```python
from datetime import datetime # import the datetime module
now = datetime.now() # get the current date and time as a datetime object
print(now.strftime("%Y-%m-%d %H:%M:%S")) # format and print the datetime object as a string
```

- To print the current time for 10 times with an interval of 1 second, a program can use a for loop or a while loop, and use the `time` module, which provides various functions for working with time.
- The `time` module has a `sleep` function, which takes a number of seconds as an argument and pauses the execution of the program for that amount of time.
- Example of printing the current time for 10 times with an interval of 1 second using a for loop:

```python
from datetime import datetime # import