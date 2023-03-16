#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and depends on a condition.

#### Handle Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming.
- In most programming languages, attempting to divide by zero will result in an error or exception.
- To handle this exception, you can use a `try-except` block to catch the exception and handle it gracefully.

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the `datetime` module in Python.
- To print the current time for 10 times with an interval of 1 second, you can use a `for` loop and the `sleep` function from the `time` module.
- Here is an example code snippet:
```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```