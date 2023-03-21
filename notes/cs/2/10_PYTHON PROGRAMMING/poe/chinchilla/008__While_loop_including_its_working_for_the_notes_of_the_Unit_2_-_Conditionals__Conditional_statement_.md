### While Loop in Python

A while loop in Python is a type of loop that executes a set of statements repeatedly as long as a condition is true. The syntax for a while loop in Python is as follows:

```python
while condition:
    # code block
```

The condition is a boolean expression that is evaluated before each iteration of the loop. If the condition is true, the code block is executed. The loop continues to execute as long as the condition remains true.

#### Working of While Loop

1. The condition is evaluated before the loop starts.
2. If the condition is true, the code block is executed.
3. After the code block is executed, the condition is evaluated again.
4. If the condition is still true, the code block is executed again.
5. This process continues until the condition becomes false.
6. Once the condition becomes false, the loop terminates and the program continues with the next statement after the loop.

#### Example

```python
count = 0
while count < 5:
    print("Count is:", count)
    count += 1
print("Done")
```

In this example, the while loop is executed as long as the value of the variable `count` is less than 5. The code block inside the loop prints the value of `count` and increments its value by 1. Once the value of `count` becomes 5, the condition becomes false and the loop terminates. The program then continues with the next statement after the loop, which prints "Done".

#### Nested If-else Statement

A nested if-else statement is an if-else statement that is nested inside another if-else statement. This allows for more complex conditions to be evaluated.

```python
if condition1:
    # code block
    if condition2:
        # code block
    else:
        # code block
else:
    # code block
```

In this example, if `condition1` is true, the code block inside the first if statement is executed. If `condition2` is true, the code block inside the nested if statement is executed. If `condition2` is false, the code block inside the else statement is executed. If `condition1` is false, the code block inside the else statement is executed.

#### Elif Statement

The elif statement is short for "else if". It allows for multiple conditions to be evaluated in sequence. The syntax for an elif statement is as follows:

```python
if condition1:
    # code block
elif condition2:
    # code block
else:
    # code block
```

In this example, if `condition1` is true, the code block inside the first if statement is executed. If `condition1` is false and `condition2` is true, the code block inside the elif statement is executed. If both `condition1` and `condition2` are false, the code block inside the else statement is executed.

#### Expression Evaluation & Float Representation

In Python, expressions are evaluated using a set of rules called operator precedence. This determines the order in which operators are evaluated in an expression. For example, multiplication and division have a higher precedence than addition and subtraction. 

In addition, Python uses a floating-point representation to represent decimal numbers. This means that some decimal numbers cannot be represented exactly in binary, which can lead to rounding errors. To avoid these errors, it is important to use the `round()` function when working with floating-point numbers. 

In conclusion, the while loop is a powerful tool in Python that allows for repeated execution of code as long as a condition is true. Nested if-else statements and elif statements allow for more complex conditions to be evaluated, while expression evaluation and float representation are important concepts to keep in mind when working with Python.