# Using For and While Loops

Programming languages provide us with different types of loops to execute a block of code multiple times. Two of the most commonly used loops are the `for` and `while` loops. Here's what you need to know about them:

## For Loops

A `for` loop is used to execute a block of code a fixed number of times. The syntax of a `for` loop is as follows:

```
for variable in range(start, stop, step):
    # code to be executed
```

- `variable` is the name of the variable that will be used to iterate through the loop.
- `start` is the starting value of the variable (default is 0).
- `stop` is the ending value of the variable (not inclusive).
- `step` is the amount by which the variable will be incremented (default is 1).

For example, the following code will print the numbers from 1 to 10:

```
for i in range(1, 11):
    print(i)
```

## While Loops

A `while` loop is used to execute a block of code as long as the specified condition is true. The syntax of a `while` loop is as follows:

```
while condition:
    # code to be executed
```

The `condition` is checked at the beginning of each iteration. If the condition is `True`, the code inside the loop will be executed. This will continue until the condition becomes `False`. 

For example, the following code will print the numbers from 1 to 10 using a `while` loop:

```
i = 1
while i <= 10:
    print(i)
    i += 1
```

## Handling Divided by Zero Exception

Sometimes, our code might encounter an error if we try to divide a number by zero. This is known as a "divided by zero" exception. We can handle this exception using a `try`-`except` block. 

```
try:
    # code that might raise an exception
except ZeroDivisionError:
    # code to handle the exception
```

For example, the following code will handle the "divided by zero" exception:

```
numerator = 10
denominator = 0

try:
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## Printing Current Time for 10 Times with an

We can use the `datetime` module in Python to get the current date and time. To print the current time for 10 times with an "AM" or "PM" suffix, we can use a `for` loop and the `strftime()` method. 

```
import datetime

for i in range(10):
    now = datetime.datetime.now()
    print(now.strftime("%I:%M:%S %p"))
```

This will print the current time in the format of `hh:mm:ss AM/PM`. 

Remember to practice using loops and exception handling to become proficient in programming. Good luck with your exams!