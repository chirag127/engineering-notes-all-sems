# Using for and while loops, handling divided by zero exception, and printing current time for 10 times with an interval of 1 second.

- For and while loops are two types of iteration statements in Python that allow a block of code to be executed repeatedly until a certain condition is met.
- A for loop iterates over a sequence of items, such as a list, a tuple, a string, or a range object, and executes the block of code for each item in the sequence.
- A while loop executes the block of code as long as a given boolean expression evaluates to True. The expression is checked before each iteration, and the loop terminates when the expression becomes False.
- A common use case for while loops is to implement indefinite loops that run until the user decides to quit or some external event occurs.
- A divided by zero exception is a type of runtime error that occurs when an attempt is made to divide a number by zero, which is mathematically undefined. In Python, this exception is represented by the ZeroDivisionError class, which inherits from the ArithmeticError class.
- To handle a divided by zero exception, the try-except statement can be used. The try block contains the code that may cause the exception, and the except block contains the code that handles the exception if it occurs. The except block can specify the type of exception to catch, or use a generic except clause to catch any exception.
- The current time can be obtained in Python using the datetime module, which provides various classes and functions for manipulating dates and times. The datetime.now() function returns a datetime object that represents the current local date and time.
- To print the current time for 10 times with an interval of 1 second, a for loop or a while loop can be used, along with the time module, which provides various functions for working with time. The time.sleep() function pauses the execution of the program for a given number of seconds.
- Here is an example of using a for loop to print the current time for 10 times with an interval of 1 second:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```

- Here is an example of using a while loop to print the current time for 10 times with an interval of 1 second:

```python
import datetime
import time

count = 0
while count < 10:
    print(datetime.datetime.now())
    time.sleep(1)
    count += 1
```

- Here is an example of handling a divided by zero exception:

```python
try:
    x = 10
    y = 0
    z = x / y
    print(z)
except ZeroDivisionError:
    print("Cannot divide by zero")
```