#### using for and while loops. b) Handle Divided by Zero Exception. c) Print current time for 10 times with an

Sure!

a) For and while loops are two of the most common control structures used in programming. They are used to repeat a block of code until a certain condition is met.

The `for` loop is used to repeat a block of code a specific number of times. The loop is initialized with a starting value, and the loop continues to run until the ending value is reached. The loop increments the value by a specified amount on each iteration.

The `while` loop, on the other hand, is used to repeat a block of code while a certain condition is true. The loop continues to run as long as the condition remains true, and it stops running when the condition becomes false.

Here is an example of a `for` loop in Python:

```
for i in range(10):
    print(i)
```

This code will print the numbers 0 through 9, and then the loop will stop.

Here is an example of a `while` loop in Python:

```
count = 0
while count < 10:
    print(count)
    count = count + 1
```

This code will print the numbers 0 through 9, and then the loop will stop.

b) Handling a divided by zero exception is important in programming because dividing by zero is undefined and can result in an error. To handle this exception, you can use a try-except block in Python. The try-except block allows you to catch the exception and handle it gracefully, rather than having the program terminate with an error.

Here is an example of a try-except block in Python:

```
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

This code will catch the ZeroDivisionError exception and print a message indicating that the division by zero is not allowed.

c) To print the current time in Python, you can use the `datetime` module. The `datetime` module provides a `datetime` object that represents the current date and time. You can use the `strftime` method of the `datetime` object to format the date and time as a string.

Here is an example of how to print the current time in Python:

```
import datetime

for i in range(10):
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
```

This code will print the current date and time 10 times, using the format `YYYY-MM-DD HH:MM:SS`.
