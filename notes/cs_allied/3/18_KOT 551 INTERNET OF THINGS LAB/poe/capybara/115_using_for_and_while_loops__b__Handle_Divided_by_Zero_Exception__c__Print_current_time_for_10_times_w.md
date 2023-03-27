# Using for and while loops, handling divided by zero exception, and printing current time

In programming, loops are a fundamental concept that allows us to repeat a certain block of code multiple times. Two common types of loops are the `for` loop and the `while` loop. 

## For Loops

A `for` loop is used when we know how many times we want to execute a block of code. The syntax for a `for` loop is as follows:

```
for <variable> in <sequence>:
    <block of code>
```

Here, `<variable>` is a variable that takes on the value of each element of the `<sequence>` in turn, and `<block of code>` is the code that is executed for each value of `<variable>`. 

For example, suppose we want to print the numbers from 1 to 10. We can use a `for` loop as follows:

```
for i in range(1, 11):
    print(i)
```

Here, `range(1, 11)` generates a sequence of numbers from 1 to 10, which is then used to iterate over the `for` loop. The output of this program will be:

```
1
2
3
4
5
6
7
8
9
10
```

## While Loops

A `while` loop is used when we don't know how many times we want to execute a block of code. The syntax for a `while` loop is as follows:

```
while <condition>:
    <block of code>
```

Here, `<condition>` is a boolean expression that is tested before each iteration of the loop, and `<block of code>` is the code that is executed for each iteration of the loop as long as the `<condition>` is true. 

For example, suppose we want to print the numbers from 1 to 10 using a `while` loop. We can use the following code:

```
i = 1
while i <= 10:
    print(i)
    i += 1
```

Here, `i` is initialized to 1, and the `while` loop continues as long as `i` is less than or equal to 10. The output of this program will be the same as the `for` loop example above:

```
1
2
3
4
5
6
7
8
9
10
```

## Handling Divided by Zero Exception

In programming, it is important to handle errors that may occur during the execution of a program. One common error is the "divided by zero" exception, which occurs when we try to divide a number by zero. To handle this exception, we can use a `try`-`except` block. 

The syntax for a `try`-`except` block is as follows:

```
try:
    <block of code>
except <exception>:
    <block of code>
```

Here, `<block of code>` is the code that may raise an exception, and `<exception>` is the type of exception that we want to handle. If an exception of type `<exception>` is raised in the `<block of code>`, then the code in the `<except>` block is executed. 

For example, suppose we want to divide two numbers and handle the "divided by zero" exception. We can use the following code:

```
a = 10
b = 0

try:
    c = a / b
    print(c)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

Here, we try to divide `a` by `b`, but since `b` is zero, a `ZeroDivisionError` exception is raised. We handle this exception by printing a message instead of trying to print the result of the division. The output of this program will be:

```
Cannot divide by zero
```

## Printing Current Time

In programming, we often need to work with dates and times. Python has a built-in module called `datetime` that allows us to work with dates and times. 

To print the current time, we can use the following code:

```
import datetime

current_time = datetime.datetime.now()

print(current_time)
```

Here, we import the `datetime` module, create a variable called `current_time` that contains the current date and time, and print the value of `current_time`. The output of this program will be something like:

```
2023-03-27 12:34:56.789012
```

## Putting it All Together

Now that we know how to use `for` and `while` loops, handle the "divided by zero" exception, and print the current time, let's put it all together. 

Suppose we want to print the current time for 10 times, with a delay of 1 second between each print. We can use