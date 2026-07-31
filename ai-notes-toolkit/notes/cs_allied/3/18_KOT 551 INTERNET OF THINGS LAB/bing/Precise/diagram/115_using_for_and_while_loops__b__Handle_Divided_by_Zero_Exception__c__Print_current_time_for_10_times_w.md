# Using for and while loops, Handling Divided by Zero Exception, and Printing current time for 10 times with an interval of 1 second

## For and While Loops
- `for` and `while` loops are used to iterate over a block of code multiple times.
- `for` loop is used when the number of iterations is known beforehand.
- `while` loop is used when the number of iterations is not known beforehand and depends on a condition.
- Syntax of `for` loop:
```
for variable in sequence:
    # code block to be executed
```
- Syntax of `while` loop:
```
while condition:
    # code block to be executed
```

## Handling Divided by Zero Exception
- Dividing a number by zero results in an error called `ZeroDivisionError`.
- This error can be handled using the `try-except` block.
- Syntax:
```
try:
    # code block that may raise ZeroDivisionError
except ZeroDivisionError:
    # code block to handle the error
```

## Printing current time for 10 times with an interval of 1 second
- The `time` module can be used to get the current time and to add a delay between iterations.
- The `time` module has a function called `sleep` which can be used to add a delay.
- The `time` module also has a function called `ctime` which returns the current time as a string.
- Example code:
```
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1)
```
This code prints the current time for 10 times with an interval of 1 second between each iteration.