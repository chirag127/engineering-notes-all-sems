# Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand.

# Handling Divided by Zero Exception
- Dividing by zero is not allowed in mathematics and will result in an error in most programming languages.
- To handle this exception, you can use a conditional statement to check if the denominator is zero before performing the division.
- If the denominator is zero, you can handle the exception by displaying an error message or performing an alternative calculation.

# Printing current time for 10 times with an interval
- To print the current time for 10 times with an interval, you can use a `for` loop and the `time` module.
- Inside the `for` loop, use the `time` module's `ctime` function to get the current time and print it.
- Use the `time` module's `sleep` function to pause the execution of the program for the desired interval before the next iteration of the loop.

Here is an example code snippet in Python:

```python
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1)
```