#### Using for and while loops
- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # loop body
```
- The syntax of a while loop is:

```python
while condition:
    # loop body
```
- To exit a loop prematurely, you can use the break statement.
- To skip the current iteration of a loop, you can use the continue statement.

#### Handle Divided by Zero Exception
- A divided by zero exception is a runtime error that occurs when you try to divide a number by zero.
- To handle a divided by zero exception, you can use a try-except block.
- A try-except block is a structure that allows you to catch and handle errors that may occur during the execution of a program.
- The syntax of a try-except block is:

```python
try:
    # code that may cause an error
except ExceptionType as e:
    # code that handles the error
```
- To handle a divided by zero exception, you can use the ZeroDivisionError exception type.
- An example of a try-except block that handles a divided by zero exception is:

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("The result is", z)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
    print("The error message is:", e)
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module.
- The datetime module provides various classes and functions to manipulate dates and times.
- To get the current date and time, you can use the datetime.now() function.
- To format the date and time, you can use the strftime() method.
- To pause the execution of a program for a certain amount of time, you can use the time module.
- The time module provides various functions to deal with time-related tasks.
- To pause the execution of a program for a certain amount of time, you can use the time.sleep() function.
- An example of a program that prints the current time for 10 times with an interval of 1 second is:

```python
import datetime
import time

for i in range(10):
    # get the current date and time
    now = datetime.datetime.now()
    # format the date and time
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    # print the date and time
    print(formatted)
    # pause the execution for 1 second
    time.sleep(1)
```