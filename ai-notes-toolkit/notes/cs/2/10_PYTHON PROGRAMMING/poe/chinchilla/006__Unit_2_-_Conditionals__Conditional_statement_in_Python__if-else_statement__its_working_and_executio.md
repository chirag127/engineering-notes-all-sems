## Unit 2 - Conditionals: Conditional statement in Python

Conditionals are an essential part of programming, allowing your code to make decisions based on certain conditions. In this unit, we will focus on conditional statements in Python, including if-else statements, nested if statements, and elif statements. We will also cover expression evaluation and float representation.

### If-Else Statements

The if-else statement is used to execute a block of code if a particular condition is true. If the condition is false, another block of code will be executed. The syntax for an if-else statement in Python is as follows:

```
if condition:
    # code to be executed if condition is true
else:
    # code to be executed if condition is false
```

### Working and Execution of If-Else Statements

The if-else statement works by first evaluating the condition specified in the if statement. If the condition is true, the code inside the if block is executed. If the condition is false, the code inside the else block is executed.

### Nested If Statements

A nested if statement is an if statement inside another if statement. This allows for more complex conditions to be evaluated. The syntax for a nested if statement in Python is as follows:

```
if condition1:
    # code to be executed if condition1 is true
    if condition2:
        # code to be executed if both condition1 and condition2 are true
    else:
        # code to be executed if condition1 is true but condition2 is false
else:
    # code to be executed if condition1 is false
```

### Elif Statements

The elif statement is used to evaluate multiple conditions in a single if-else block. It is a shorthand for writing multiple if statements. The syntax for an elif statement in Python is as follows:

```
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition1 is false and condition2 is true
else:
    # code to be executed if both condition1 and condition2 are false
```

### Expression Evaluation

Expression evaluation is the process of calculating the value of an expression. In Python, expressions can be evaluated using arithmetic operators (+, -, *, /) and comparison operators (==, <, >, <=, >=). Parentheses can be used to group parts of an expression together.

### Float Representation

Floating-point numbers (or floats for short) are a type of number with a decimal point. In Python, floats can be represented using the float() function. However, due to the way computers store floating-point numbers, there can be issues with precision and accuracy. It is important to be aware of these issues when working with floats.

Overall, understanding conditional statements and expression evaluation is essential for writing effective Python code. By mastering these concepts, you will be able to write more complex and powerful programs.