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
- To handle an exception, you can use a try-except block, which allows you to execute some code and catch any errors that may occur.
- The syntax of a try-except block is:

```python
try:
    # try to execute some code
except ExceptionType as e:
    # handle the exception
```

- For example, to handle a divided by zero exception, you can write:

```python
try:
    x = 10 / 0 # this will cause an exception
except ZeroDivisionError as e:
    print("Cannot divide by zero")
    print(e) # this will print the error message
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module, which provides various functions and classes to work with dates and times.
- To import the datetime module, you can write:

```python
import datetime
```

- To get the current time, you can use the datetime.now() function, which returns a datetime object that represents the current date and time.
- To print the current time, you can use the print() function, which displays the value of its argument to the standard output.
- To print the current time for 10 times, you can use a for loop or a while loop, as explained above.
- To print the current time with an interval of 1 second, you can use the time module, which provides various functions and classes to work with time.
- To import the time module, you can write:

```python
import time
```

- To pause the execution of the program for 1 second, you can use the time.sleep() function, which takes a number of seconds as an argument and suspends the current thread for that duration.
- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now()) # print the current time
    time.sleep(1) # wait for 1 second
```