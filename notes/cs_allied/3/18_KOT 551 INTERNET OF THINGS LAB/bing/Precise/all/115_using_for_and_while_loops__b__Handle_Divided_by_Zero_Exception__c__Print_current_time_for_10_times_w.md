# Using for and while loops, Handling Divided by Zero Exception, and Printing current time for 10 times with an interval of 1 second

## For and While Loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- The `for` loop is used when the number of iterations is known beforehand.
- The `while` loop is used when the number of iterations is not known beforehand and depends on a condition.

## Handling Divided by Zero Exception
- Dividing a number by zero is not allowed in mathematics and results in an error in most programming languages.
- To handle this error, a try-except block can be used.
- The code that might cause the error is placed inside the `try` block.
- If an error occurs, the code inside the `except` block is executed.

## Printing current time for 10 times with an interval of 1 second
- The `time` module can be used to get the current time and to add a delay between iterations.
- The `time.time()` function returns the current time in seconds since the epoch.
- The `time.sleep()` function can be used to add a delay between iterations.
- A `for` loop can be used to iterate 10 times and print the current time with an interval of 1 second between each iteration.

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
    print(time.ctime())
    time.sleep(1)
```