#### Using for and while loops
- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- A while loop is a control structure that allows you to repeat a block of code as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in iterable:
    # do something with variable
```

- The syntax of a while loop is:

```python
while condition:
    # do something
```

- For example, to print the numbers from 1 to 10 using a for loop, you can write:

```python
for i in range(1, 11):
    print(i)
```

- To print the numbers from 1 to 10 using a while loop, you can write:

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

#### Handle Divided by Zero Exception
- An exception is an error that occurs during the execution of a program.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is mathematically undefined.
- To handle an exception, you can use a try-except block, which allows you to catch and handle the error gracefully, instead of crashing the program.
- The syntax of a try-except block is:

```python
try:
    # try to do something that may cause an exception
except ExceptionType as e:
    # handle the exception of type ExceptionType
```

- For example, to handle a divided by zero exception, you can write:

```python
try:
    x = 10 / 0 # this will cause a ZeroDivisionError
except ZeroDivisionError as e:
    print("Cannot divide by zero:", e)
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module, which provides various functions and classes to work with dates and times.
- To print the current time for 10 times with an interval of 1 second, you can use a for loop and the time module, which provides various functions to work with time.
- The syntax to print the current time is:

```python
from datetime import datetime
print(datetime.now())
```

- The syntax to wait for 1 second is:

```python
import time
time.sleep(1)
```

- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```python
from datetime import datetime
import time
for i in range(10):
    print(datetime.now())
    time.sleep(1)
```