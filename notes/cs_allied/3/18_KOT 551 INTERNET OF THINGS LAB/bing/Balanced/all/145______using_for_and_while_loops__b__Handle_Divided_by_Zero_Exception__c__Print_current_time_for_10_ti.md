# Using for and while loops, handling divided by zero exception, and printing current time for 10 times with an interval of 5 seconds.

- For and while loops are two types of control structures that allow a program to execute a block of code repeatedly based on a condition.
- A for loop has a fixed number of iterations, determined by a range or a sequence. A while loop has an indefinite number of iterations, determined by a boolean expression.
- A for loop has the following syntax:

```python
for variable in range_or_sequence:
    # do something
```

- A while loop has the following syntax:

```python
while boolean_expression:
    # do something
```

- A divided by zero exception is an error that occurs when a program tries to perform a division operation with zero as the divisor. This is an invalid mathematical operation and results in an undefined value.
- To handle a divided by zero exception, a program can use a try-except block, which allows it to catch and handle the error gracefully, instead of crashing or terminating.
- A try-except block has the following syntax:

```python
try:
    # do something that might cause an error
except ZeroDivisionError:
    # do something to handle the error
```

- To print the current time for 10 times with an interval of 5 seconds, a program can use the datetime module to get the current time, and the time module to create a delay between each iteration.
- The datetime module has a function called datetime.now() that returns the current date and time as a datetime object. The time module has a function called time.sleep() that takes a number of seconds as an argument and pauses the program for that duration.
- To print the current time for 10 times with an interval of 5 seconds, a program can use a for loop or a while loop, and call the datetime.now() and time.sleep() functions inside the loop body. For example:

```python
# using a for loop
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(5)

# using a while loop
import datetime
import time

i = 0
while i < 10:
    print(datetime.datetime.now())
    time.sleep(5)
    i += 1
```