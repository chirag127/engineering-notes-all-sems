#### Using for and while loops, handling divided by zero exception, and printing current time for 10 times

When programming, it is often necessary to repeat a particular set of instructions multiple times. This can be achieved using loops, which allow us to execute a block of code repeatedly. In this article, we will cover how to use both for and while loops, as well as how to handle divided by zero exceptions and how to print the current time for 10 times.

##### Using for and while loops

Loops are a fundamental part of programming, and there are two main types of loops in Python: for loops and while loops.

- For loops: For loops allow us to iterate over a sequence of values, such as a list or a tuple. The basic syntax for a for loop is:

```python
for variable in sequence:
    # code to execute
```

- While loops: While loops allow us to execute a block of code repeatedly as long as a certain condition is true. The basic syntax for a while loop is:

```python
while condition:
    # code to execute
```

##### Handling divided by zero exceptions

When dividing by zero, Python will raise a ZeroDivisionError. To handle this exception, we can use a try-except block. The basic syntax for a try-except block is:

```python
try:
    # code that may raise an exception
except ExceptionType:
    # code to execute if the exception is raised
```

To handle a divided by zero exception specifically, we can use the ZeroDivisionError exception type:

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

##### Printing current time for 10 times

To print the current time for 10 times, we can use the datetime module in Python, which provides various classes for working with dates and times. The basic syntax for getting the current time is:

```python
import datetime

current_time = datetime.datetime.now()
print(current_time)
```

To print the current time for 10 times, we can use a for loop:

```python
import datetime

for i in range(10):
    current_time = datetime.datetime.now()
    print(current_time)
```

Alternatively, we can use a while loop:

```python
import datetime

i = 0
while i < 10:
    current_time = datetime.datetime.now()
    print(current_time)
    i += 1
```

In conclusion, for and while loops are essential tools in programming that allow us to repeat a particular set of instructions multiple times. We can also handle exceptions such as divided by zero errors using try-except blocks. Finally, the datetime module in Python provides a convenient way to work with dates and times, allowing us to print the current time for any number of iterations.