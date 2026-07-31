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

# Handle Divided by Zero Exception

- A divided by zero exception is an error that occurs when you try to divide a number by zero, which is not allowed in mathematics.
- To handle a divided by zero exception in Python, you can use a try-except block, which allows you to catch and handle errors that may occur during the execution of your code.
- The syntax of a try-except block is:

```python
try:
    # do something that may cause an error
except ExceptionType as e:
    # handle the error
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

# Print current time for 10 times with an interval of 1 second

- To print the current time in Python, you can use the datetime module, which provides various functions and classes to deal with dates and times.
- To import the datetime module, you can write:

```python
import datetime
```

- To get the current time, you can use the datetime.now() function, which returns a datetime object that represents the current date and time.
- To print the current time, you can use the print() function, which displays the value of its argument to the standard output.
- To print the current time for 10 times, you can use a for loop or a while loop, as explained above.
- To print the current time with an interval of 1 second, you can use the time module, which provides various functions and classes to deal with time-related tasks.
- To import the time module, you can write:

```python
import time
```

- To pause the execution of your code for 1 second, you can use the time.sleep() function, which takes a number of seconds as an argument and suspends the current thread for that amount of time.
- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```python
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```