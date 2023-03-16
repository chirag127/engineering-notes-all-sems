#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and depends on a condition.

#### Handle Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming languages.
- In most programming languages, attempting to divide by zero results in a runtime error.
- This error can be handled using exception handling mechanisms.
- In Python, for example, the `try` and `except` statements can be used to catch and handle the `ZeroDivisionError` exception.

#### Print current time for 10 times with an interval
- The current time can be obtained using the `datetime` module in Python.
- The `time` module can be used to introduce a delay between iterations.
- A `for` loop can be used to iterate 10 times and print the current time at each iteration.
- The `sleep` function from the `time` module can be used to introduce a delay between iterations.

Here is an example code snippet in Python that demonstrates the above concepts:

```python
import datetime
import time

for i in range(10):
    current_time = datetime.datetime.now()
    print(current_time)
    time.sleep(1)
```