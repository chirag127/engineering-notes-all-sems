# Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- The `for` loop is used when the number of iterations is known beforehand.
- The `while` loop is used when the number of iterations is not known beforehand.

# Handling Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming.
- In Python, attempting to divide by zero will raise a `ZeroDivisionError` exception.
- This exception can be handled using a `try` and `except` block.

# Printing current time for 10 times with an interval of 1 second
- The `time` module in Python provides functions to work with time.
- The `time.time()` function returns the current time in seconds since the epoch.
- The `time.sleep()` function can be used to pause the execution of the program for a specified number of seconds.
- To print the current time for 10 times with an interval of 1 second, a `for` loop can be used in combination with the `time` module functions.

Here is an example code that demonstrates the above concepts:

```python
import time

# Using for and while loops
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1

# Handling Divided by Zero Exception
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")

# Printing current time for 10 times with an interval of 1 second
for i in range(10):
    print(time.time())
    time.sleep(1)
```