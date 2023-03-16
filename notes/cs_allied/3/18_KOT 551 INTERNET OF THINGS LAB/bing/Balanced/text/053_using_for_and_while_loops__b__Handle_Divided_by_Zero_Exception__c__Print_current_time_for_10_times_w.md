# Using for and while loops

- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- A while loop is a repetition control structure that allows you to write a loop that will repeat as long as a condition is true.
- The syntax of a for loop is:

```python
for variable in range(start, end, step):
    # do something
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

# Handling Divided by Zero Exception

- An exception is an error that occurs during the execution of a program.
- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is not allowed in mathematics.
- To handle an exception, you can use a try-except block, which allows you to catch and handle the error gracefully, without terminating the program.
- The syntax of a try-except block is:

```python
try:
    # do something that might cause an exception
except ExceptionType as e:
    # handle the exception
```

- For example, to handle a divided by zero exception, you can write:

```python
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("The result is", z)
except ZeroDivisionError as e:
    print("You cannot divide by zero!")
```

# Printing Current Time for 10 Times with an Interval of 1 Second

- To print the current time, you can use the datetime module, which provides various functions and classes to deal with dates and times.
- To import the datetime module, you can write:

```python
import datetime
```

- To get the current time, you can use the datetime.now() function, which returns a datetime object that represents the current date and time.
- To print the current time, you can use the strftime() method, which converts a datetime object into a formatted string according to a given format specifier.
- For example, to print the current time in the format of hour:minute:second, you can write:

```python
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))
```

- To print the current time for 10 times with an interval of 1 second, you can use a for loop and the time module, which provides various functions to deal with time-related tasks.
- To import the time module, you can write:

```python
import time
```

- To pause the execution of the program for a given number of seconds, you can use the time.sleep() function, which takes a number as an argument and suspends the program for that amount of time.
- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```python
import datetime
import time

for i in range(10):
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    time.sleep(1)
```