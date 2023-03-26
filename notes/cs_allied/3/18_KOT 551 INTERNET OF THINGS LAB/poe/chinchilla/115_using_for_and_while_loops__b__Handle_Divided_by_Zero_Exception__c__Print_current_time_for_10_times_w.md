# Using For and While Loops

## Introduction
Loops are used in programming to execute a block of code multiple times. In this tutorial, we will learn about two types of loops: for and while loops. We will also learn how to handle the divided by zero exception and print the current time for 10 times with an.

## For Loops
A for loop is used to iterate over a sequence of values. The basic syntax of a for loop is as follows:

```python
for variable in sequence:
    # code block
```

Here, `variable` is a variable that takes on the value of each element in the `sequence` one at a time, and the `code block` is the code that is executed for each value of `variable`.

Example:

```python
for i in range(5):
    print(i)
```

Output:
```
0
1
2
3
4
```

## While Loops
A while loop is used to execute a block of code repeatedly as long as a condition is true. The basic syntax of a while loop is as follows:

```python
while condition:
    # code block
```

Here, `condition` is a boolean expression that is checked at the beginning of each iteration of the loop. If the condition is true, the `code block` is executed; otherwise, the loop terminates.

Example:

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
Dividing a number by zero is not allowed in mathematics and will result in an error if attempted in programming. To handle this error, we can use a try-except block. The basic syntax of a try-except block is as follows:

```python
try:
    # code block
except ExceptionType:
    # code block
```

Here, `ExceptionType` is the type of exception that we want to catch. If an exception of that type occurs in the `try` block, the `except` block is executed.

Example:

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:
```
Cannot divide by zero
```

## Printing Current Time for 10 Times with An
To print the current time for 10 times with an, we can use the datetime module, which provides classes for working with dates and times. The basic syntax for getting the current time is as follows:

```python
import datetime

now = datetime.datetime.now()
```

Here, `now` is a datetime object that represents the current date and time. We can then format this object using the `strftime()` method to print it in a specific format.

Example:

```python
import datetime

for i in range(10):
    now = datetime.datetime.now()
    print(f"At {now.strftime('%H:%M:%S')}, I am doing something")
```

Output:
```
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
At 10:30:45, I am doing something
```

## Conclusion
In this tutorial, we have learned about for and while loops, how to handle the divided by zero exception, and how to print the current time for 10 times with an. These concepts are fundamental to programming and are used frequently in various applications.