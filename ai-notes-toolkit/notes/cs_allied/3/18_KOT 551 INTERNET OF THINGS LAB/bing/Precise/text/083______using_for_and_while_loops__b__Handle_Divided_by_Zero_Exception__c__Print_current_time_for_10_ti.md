#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- The `for` loop is used when the number of iterations is known beforehand. It is commonly used to iterate over a sequence (such as a list or string) or a range of numbers.
- The `while` loop is used when the number of iterations is not known beforehand. It continues to execute the block of code as long as the condition specified in the loop remains `True`.

#### Handle Divided by Zero Exception
- Dividing a number by zero is not allowed in mathematics and will result in an error in most programming languages.
- To handle this exception, you can use a `try` and `except` block. The code that may cause the exception is placed in the `try` block, and the code to handle the exception is placed in the `except` block.
- For example, in Python, you can handle a divided by zero exception like this:
```python
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the `datetime` module in Python.
- To print the current time for 10 times with an interval of 1 second, you can use a `for` loop and the `sleep` function from the `time` module.
- Here is an example in Python:
```python
from datetime import datetime
from time import sleep

for i in range(10):
    print(datetime.now())
    sleep(1)
```