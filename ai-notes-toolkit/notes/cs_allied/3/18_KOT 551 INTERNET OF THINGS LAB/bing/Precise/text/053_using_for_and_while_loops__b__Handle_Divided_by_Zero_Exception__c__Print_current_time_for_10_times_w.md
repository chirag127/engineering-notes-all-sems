# Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and the loop should continue until a certain condition is met.

# Handling Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and most programming languages.
- To handle a divided by zero exception, you can use a `try` and `except` block.
- In the `try` block, you can attempt to perform the division.
- In the `except` block, you can catch the `ZeroDivisionError` and handle it appropriately, such as by printing an error message or returning a default value.

# Printing current time for 10 times with an interval
- To print the current time, you can use the `datetime` module in Python.
- You can use the `datetime.now()` function to get the current date and time.
- To print the current time for 10 times with an interval, you can use a `for` loop and the `time.sleep()` function to introduce a delay between each iteration.
- Here is an example code snippet that prints the current time for 10 times with an interval of 1 second:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```