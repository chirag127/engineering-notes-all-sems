#### Using for and while loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loops are used when the number of iterations is known beforehand.
- `while` loops are used when the number of iterations is not known beforehand and depends on a condition.
- Syntax for `for` loop: `for variable in sequence:`
- Syntax for `while` loop: `while condition:`

#### Handle Divided by Zero Exception
- Dividing by zero is not allowed in mathematics and will result in an error in most programming languages.
- To handle this exception, you can use a `try` and `except` block.
- Syntax: 
```
try:
    # code that may raise an exception
except ZeroDivisionError:
    # code to handle the exception
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the `datetime` module in Python.
- To pause the execution of the program for 1 second, you can use the `time` module in Python.
- Example code:
```
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```