# Using For and While Loops

For and while loops are used to iterate over a block of code multiple times. The difference between the two is that a for loop is used when the number of iterations is known, while a while loop is used when the number of iterations is unknown.

## For Loop
A for loop has the following syntax:
```
for variable in sequence:
    # code block
```
The `variable` takes on the value of each element in the `sequence` one by one, and the code block is executed for each value.

## While Loop
A while loop has the following syntax:
```
while condition:
    # code block
```
The code block is executed repeatedly as long as the `condition` is `True`. The `condition` is checked before each iteration.

# Handling Divide by Zero Exception

In Python, dividing by zero raises a `ZeroDivisionError`. This can be handled using a try-except block. Here is an example:
```
try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```
In the above code, if `y` is zero, a `ZeroDivisionError` is raised and caught by the except block. The error message is then printed.

# Printing Current Time for 10 Times with an Interval

To print the current time for 10 times with an interval, we can use the `time` module. Here is an example:
```
import time

for i in range(10):
    print(time.ctime())
    time.sleep(1)
```
In the above code, the `time.ctime()` function returns the current time as a string. The `time.sleep(1)` function causes the program to pause for 1 second before the next iteration. This results in the current time being printed 10 times with an interval of 1 second between each print.