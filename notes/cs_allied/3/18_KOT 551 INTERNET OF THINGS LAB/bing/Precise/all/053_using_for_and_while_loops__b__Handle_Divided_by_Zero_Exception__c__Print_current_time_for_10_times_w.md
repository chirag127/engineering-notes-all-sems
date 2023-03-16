# Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- The `for` loop is used when the number of iterations is known beforehand.
- The `while` loop is used when the number of iterations is not known beforehand and depends on a condition.

# Handling Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming.
- In most programming languages, attempting to divide by zero results in a runtime error.
- To handle this error, you can use exception handling techniques such as `try` and `except` blocks in Python.

# Printing current time for 10 times with an interval
- To print the current time, you can use the `datetime` module in Python.
- To print the current time for 10 times with an interval, you can use a `for` loop and the `sleep` function from the `time` module.
- Here is an example code snippet that prints the current time for 10 times with an interval of 1 second:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```