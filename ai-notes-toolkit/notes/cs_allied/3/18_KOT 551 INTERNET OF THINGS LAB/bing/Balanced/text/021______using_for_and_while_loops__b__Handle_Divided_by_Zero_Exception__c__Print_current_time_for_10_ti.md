#### Using for and while loops
- A for loop is a control structure that allows you to repeat a block of code a fixed number of times.
- A while loop is a control structure that allows you to repeat a block of code as long as a condition is true.
- The syntax of a for loop is:

```
for variable in sequence:
    # do something
```

- The syntax of a while loop is:

```
while condition:
    # do something
```

- For example, to print the numbers from 1 to 10 using a for loop, you can write:

```
for i in range(1, 11):
    print(i)
```

- To print the numbers from 1 to 10 using a while loop, you can write:

```
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

```
try:
    # try to do something that may cause an exception
except ExceptionType:
    # handle the exception
```

- For example, to handle a divided by zero exception, you can write:

```
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    print("The result is", z)
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

#### Print current time for 10 times with an interval of 1 second
- To print the current time, you can use the datetime module, which provides various functions and classes to manipulate dates and times.
- To import the datetime module, you can write:

```
import datetime
```

- To get the current time, you can use the datetime.now() function, which returns a datetime object with the current date and time.
- To print the current time, you can use the print() function, which displays the value of its argument to the standard output.
- To print the current time for 10 times, you can use a for loop, which allows you to repeat a block of code a fixed number of times.
- To create an interval of 1 second between each print, you can use the time module, which provides various functions and classes to manipulate time.
- To import the time module, you can write:

```
import time
```

- To create a delay of 1 second, you can use the time.sleep() function, which pauses the execution of the program for the specified number of seconds.
- For example, to print the current time for 10 times with an interval of 1 second, you can write:

```
import datetime
import time

for i in range(10):
    print(datetime.datetime.now())
    time.sleep(1)
```