### Loops: Purpose and working of loops for the notes of the Unit 2 - Conditionals: Conditional statement in Python (if-else statement, its working and execution), Nested-if statement and Elif statement in Python, Expression Evaluation & Float Representation.

When writing programs, it is often necessary to repeat a block of code multiple times. Loops in Python provide a way to repeat a block of code a certain number of times or until a certain condition is met. There are two types of loops in Python: `for` and `while` loops.

#### For Loop

A `for` loop is used to iterate over a sequence (such as a list, tuple, or string) and perform a certain action for each item in the sequence. The basic syntax for a `for` loop is as follows:

```python
for variable in sequence:
    # Code to be executed for each item in sequence
```

The `variable` is assigned the value of each item in the `sequence` in turn, and the code inside the loop is executed for each value of `variable`. For example, the following code prints each item in a list:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

The output of the above code would be:

```
apple
banana
cherry
```

#### While Loop

A `while` loop is used to repeat a block of code as long as a certain condition is true. The basic syntax for a `while` loop is as follows:

```python
while condition:
    # Code to be executed while condition is true
```

The `condition` is checked at the beginning of each iteration of the loop, and the code inside the loop is executed only if the condition is true. For example, the following code prints the numbers from 1 to 5 using a `while` loop:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

The output of the above code would be:

```
1
2
3
4
5
```

#### Nested If Statement

Sometimes it is necessary to use an `if` statement inside another `if` statement. This is called a nested `if` statement. The basic syntax for a nested `if` statement is as follows:

```python
if condition1:
    # Code to be executed if condition1 is true
    if condition2:
        # Code to be executed if condition1 and condition2 are true
```

The code inside the nested `if` statement is only executed if both the outer and inner conditions are true. For example, the following code checks if a number is positive, negative, or zero using a nested `if` statement:

```python
num = -5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    # num < 0
    print("Negative number")
```

The output of the above code would be:

```
Negative number
```

#### Elif Statement

An `elif` statement is used to add additional conditions to an `if` statement. The `elif` statement is only checked if the previous `if` statement(s) are false. The basic syntax for an `if` statement with `elif` statements is as follows:

```python
if condition1:
    # Code to be executed if condition1 is true
elif condition2:
    # Code to be executed if condition1 is false and condition2 is true
elif condition3:
    # Code to be executed if condition1 and condition2 are false and condition3 is true
else:
    # Code to be executed if all conditions are false
```

The `elif` statements are checked in order, and the first `elif` statement with a true condition is executed. If none of the conditions are true, the `else` statement is executed (if present). For example, the following code checks if a number is positive, negative, or zero using an `if` statement with `elif` statements:

```python
num = 0
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    # num == 0
    print("Zero")
```

The output of the above code would be:

```
Zero
```

#### Expression Evaluation & Float Representation

Python uses a certain order of operations when evaluating expressions. The order of operations is as follows:

1. Parentheses
2. Exponents
3. Multiplication and Division (from left to right)
4. Addition and Subtraction (from left to right)

It is important to use parentheses to group expressions in the order that you want them to be evaluated. For example, the following code evaluates the expression `2 + 3 * 4`:

```python
result = 2 +

```
