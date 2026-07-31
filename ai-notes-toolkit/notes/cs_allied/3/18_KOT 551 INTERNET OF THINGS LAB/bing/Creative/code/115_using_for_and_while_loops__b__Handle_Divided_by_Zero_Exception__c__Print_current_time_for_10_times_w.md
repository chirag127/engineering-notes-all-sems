# Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # loop body
```
- The syntax of a while loop is:

```python
while condition:
    # loop body
```
- To handle a divided by zero exception, you can use a try-except block that catches the ZeroDivisionError and handles it gracefully.
- The syntax of a try-except block is:

```python
try:
    # code that may raise an exception
except ZeroDivisionError:
    # code that handles the exception
```
- To print the current time for 10 times with an interval of 1 second, you can use the datetime module and the time module in Python.
- The datetime module provides functions to work with date and time objects, such as datetime.now() which returns the current local date and time.
- The time module provides functions to work with time values, such as time.sleep() which pauses the execution for a given number of seconds.
- The code to print the current time for 10 times with an interval of 1 second is:

```python
import datetime
import time

# use a for loop to repeat 10 times
for i in range(10):
    # get the current time and print it
    now = datetime.datetime.now()
    print(now)
    # wait for 1 second
    time.sleep(1)
```