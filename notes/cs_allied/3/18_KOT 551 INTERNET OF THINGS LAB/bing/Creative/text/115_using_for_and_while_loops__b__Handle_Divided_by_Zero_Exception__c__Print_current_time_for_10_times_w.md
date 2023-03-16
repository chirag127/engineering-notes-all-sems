# Using for and while loops

- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- A while loop is a control structure that allows you to repeat a block of code as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in iterable:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
```

- An iterable is an object that can be iterated over, such as a list, a string, a range, etc.
- A condition is an expression that evaluates to a boolean value (True or False).
- You can use the break statement to exit a loop prematurely, and the continue statement to skip the current iteration and move to the next one.

# Handling Divided by Zero Exception

- An exception is an error that occurs during the execution of a program, and interrupts the normal flow of control.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is mathematically undefined.
- In Python, a divided by zero exception is represented by the ZeroDivisionError class, which inherits from the ArithmeticError class, which in turn inherits from the Exception class.
- You can handle exceptions using the try-except-finally construct, which has the following syntax:

```python
try:
    # try to execute some code that may raise an exception
except ExceptionType as e:
    # handle the exception of type ExceptionType
    # e is the exception object that contains information about the error
finally:
    # execute some code that will always run, regardless of whether an exception occurred or not
```

- You can have multiple except clauses to handle different types of exceptions, or use a generic except clause to catch any exception.
- The finally clause is optional, but useful for performing cleanup actions or releasing resources.
- To handle a divided by zero exception, you can use the following code:

```python
try:
    # try to divide two numbers
    result = num1 / num2
except ZeroDivisionError as e:
    # handle the divided by zero exception
    print("Cannot divide by zero")
    print(e)
finally:
    # execute some code that will always run
    print("End of program")
```

# Printing current time for 10 times with an interval of 1 second

- To print the current time, you can use the datetime module, which provides various classes and functions for working with dates and times.
- To import the datetime module, you can use the following statement:

```python
import datetime
```

- To get the current date and time as a datetime object, you can use the datetime.now() function, which returns a datetime object with the current local date and time.
- To format a datetime object as a string, you can use the strftime() method, which takes a format string as an argument and returns a formatted string according to the given format.
- To pause the execution of a program for a certain amount of time, you can use the time module, which provides various functions for working with time.
- To import the time module, you can use the following statement:

```python
import time
```

- To sleep for a specified number of seconds, you can use the time.sleep() function, which takes a number of seconds as an argument and suspends the execution of the current thread for that duration.
- To print the current time for 10 times with an interval of 1 second, you can use the following code:

```python
import datetime
import time

# use a for loop to repeat 10 times
for i in range(10):
    # get the current date and time as a datetime object
    now = datetime.datetime.now()
    # format the datetime object as a string
    formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
    # print the formatted string
    print(formatted_now)
    # sleep for 1 second
    time.sleep(1)
```