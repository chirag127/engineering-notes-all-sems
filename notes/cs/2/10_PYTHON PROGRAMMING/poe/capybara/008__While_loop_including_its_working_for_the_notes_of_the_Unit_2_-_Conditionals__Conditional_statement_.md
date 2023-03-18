### While Loop

A while loop is a type of loop in Python that keeps repeating a block of code until a certain condition becomes false. The syntax of a while loop is as follows:

```python
while (condition):
    # code block
```

The condition is a Boolean expression that is evaluated before each iteration of the loop. If the condition is true, the code block is executed. If the condition is false, the loop is exited and the program continues.

Here's an example of a while loop that prints the numbers from 1 to 5:

```python
i = 1
while (i <= 5):
    print(i)
    i += 1
```

In this example, the variable `i` is initialized to 1. The while loop checks if `i` is less than or equal to 5. If it is, the value of `i` is printed and then incremented by 1. This process continues until `i` is no longer less than or equal to 5.

### If-Else Statement

An if-else statement is a conditional statement in Python that allows you to execute different code blocks depending on whether a condition is true or false. The syntax of an if-else statement is as follows:

```python
if (condition):
    # code block if condition is true
else:
    # code block if condition is false
```

The condition is a Boolean expression that is evaluated. If the condition is true, the code block after the `if` statement is executed. If the condition is false, the code block after the `else` statement is executed.

Here's an example of an if-else statement that checks if a number is positive or negative:

```python
num = -5
if (num >= 0):
    print("The number is positive")
else:
    print("The number is negative")
```

In this example, the variable `num` is assigned a value of -5. The if-else statement checks if `num` is greater than or equal to 0. Since `num` is negative, the code block after the `else` statement is executed and "The number is negative" is printed.

### Nested-If Statement

A nested-if statement is a conditional statement in Python that allows you to execute different code blocks depending on multiple conditions. The syntax of a nested-if statement is as follows:

```python
if (condition1):
    # code block if condition1 is true
    if (condition2):
        # code block if condition1 and condition2 are true
    else:
        # code block if condition1 is true and condition2 is false
else:
    # code block if condition1 is false
```

The nested-if statement checks if a series of conditions are true or false. If the first condition is true, the code block after the first `if` statement is executed. If the second condition is true, the code block after the second `if` statement is executed. If the first condition is true but the second condition is false, the code block after the `else` statement is executed.

Here's an example of a nested-if statement that checks if a number is positive, negative, or zero:

```python
num = 0
if (num > 0):
    print("The number is positive")
elif (num < 0):
    print("The number is negative")
else:
    print("The number is zero")
```

In this example, the variable `num` is assigned a value of 0. The nested-if statement first checks if `num` is greater than 0. Since `num` is not greater than 0, the next condition is checked. This condition checks if `num` is less than 0. Since `num` is not less than 0, the code block after the `else` statement is executed and "The number is zero" is printed.

### Elif Statement

An elif statement is a conditional statement in Python that allows you to check for multiple conditions in a single if statement. The syntax of an elif statement is as follows:

```python
if (condition1):
    # code block if condition1 is true
elif (condition2):
    # code block if condition1 is false and condition2 is true
else:
    # code block if condition1 and condition2 are false
```

The elif statement is used in conjunction with the if statement to check for additional conditions. If the first condition is false, the elif statement checks if the second condition is true. If the second condition is true, the code block after the elif statement is executed. If both conditions are false, the code block after the `else` statement is executed.

Here's an example of an elif statement that checks if a number is positive, negative, or zero:

```python
num = 0
if (num > 0):
    print("The number is positive")
elif (num < 0):
    print("