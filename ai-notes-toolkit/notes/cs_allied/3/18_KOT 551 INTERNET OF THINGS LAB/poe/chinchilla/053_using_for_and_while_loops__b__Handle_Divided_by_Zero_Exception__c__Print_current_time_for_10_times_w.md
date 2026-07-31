# Using For and While Loops

## Introduction

In programming, loops provide a way to execute a set of instructions repeatedly. For loops and while loops are two types of loops that allow us to repeat a block of code multiple times. In this study material, we will learn about using for and while loops in Python.

## For Loops

A for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a block of code for each item in the sequence. The basic syntax of a for loop in Python is:

```python
for item in sequence:
    # do something with item
```

The `item` variable represents the current item in the sequence, and the block of code below the `for` statement is executed for each item in the sequence.

For example, the following code uses a for loop to print each item in a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Output:

```
apple
banana
cherry
```

## While Loops

A while loop is used to repeatedly execute a block of code as long as a certain condition is true. The basic syntax of a while loop in Python is:

```python
while condition:
    # do something
```

The `condition` is a Boolean expression that is evaluated before each iteration of the loop. If the condition is true, the block of code below the `while` statement is executed. This process repeats until the condition becomes false.

For example, the following code uses a while loop to print the numbers from 0 to 4:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

Output:

```
0
1
2
3
4
```

## Handling Divided by Zero Exception

When dividing a number by zero, Python raises a ZeroDivisionError exception. To handle this exception, we can use a try-except block. The basic syntax of a try-except block in Python is:

```python
try:
    # do something that might raise an exception
except ExceptionType:
    # handle the exception
```

In the `try` block, we write the code that might raise an exception. If an exception of type `ExceptionType` is raised, the code in the `except` block is executed.

For example, the following code divides two numbers and handles the ZeroDivisionError exception:

```python
a = 5
b = 0
try:
    c = a / b
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```
Cannot divide by zero
```

## Printing Current Time

To print the current time, we can use the datetime module in Python. The `datetime.now()` method returns a datetime object representing the current date and time. We can then use the `strftime()` method to format the datetime object as a string.

The following code prints the current time in the format "HH:MM:SS" for 10 times using a for loop:

```python
import datetime

for i in range(10):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(current_time)
```

Output:

```
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
22:30:45
```

Conclusion:

In this study material, we learned about using for and while loops in Python. We also learned how to handle the ZeroDivisionError exception and how to print the current time using the datetime module. With this knowledge, we can write more efficient and error-free programs.