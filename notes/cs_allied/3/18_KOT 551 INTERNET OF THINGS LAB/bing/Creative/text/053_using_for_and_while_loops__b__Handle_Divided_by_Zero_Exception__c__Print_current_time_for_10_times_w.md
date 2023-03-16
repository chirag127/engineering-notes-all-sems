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

- To print the current time for 10 times with an interval of 5 seconds, you can use the datetime module to get the current time and the time module to pause the execution.
- The code for this task is:

```python
import datetime
import time

# loop 10 times
for i in range(10):
    # get the current time
    now = datetime.datetime.now()
    # print the time in a formatted way
    print(now.strftime("%H:%M:%S"))
    # pause for 5 seconds
    time.sleep(5)
```