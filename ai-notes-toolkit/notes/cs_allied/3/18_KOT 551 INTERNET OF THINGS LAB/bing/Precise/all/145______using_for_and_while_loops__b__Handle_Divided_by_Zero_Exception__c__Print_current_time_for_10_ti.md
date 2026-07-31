#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and the loop continues until a certain condition is met.

#### Handle Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming languages.
- In Python, attempting to divide by zero raises a `ZeroDivisionError` exception.
- This exception can be handled using a `try`-`except` block to prevent the program from crashing.

#### Print current time for 10 times with an interval of 1 second
- The `time` module in Python provides functions to work with time-related tasks.
- The `time.time()` function returns the current time in seconds since the epoch.
- The `time.sleep()` function can be used to pause the execution of the program for a specified number of seconds.
- To print the current time for 10 times with an interval of 1 second, a `for` loop can be used in combination with the `time` module functions.

Here is an example code snippet that demonstrates this:

```python
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1)
```