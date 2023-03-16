#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and depends on a condition.

#### Handle Divided by Zero Exception
- Dividing by zero is an illegal operation in mathematics and programming.
- In most programming languages, attempting to divide by zero will result in an error or exception.
- This exception can be handled using a `try-except` block in Python or a `try-catch` block in Java and C++.

#### Print current time for 10 times with an interval of 1 second
- The current time can be obtained using the `time` module in Python or the `java.time` package in Java.
- The `time.sleep()` function in Python or the `Thread.sleep()` method in Java can be used to introduce a delay of 1 second between each iteration.
- A `for` loop can be used to iterate 10 times and print the current time at each iteration.

Here is an example in Python:
```python
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1)
```