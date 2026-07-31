### For Loop

A `for` loop in Python is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects (such as range or dictionary) and execute a block of code for each item in the sequence.

The general syntax for a `for` loop is:

```python
for variable in sequence:
    # code to be executed
```

- The `variable` is assigned the value of each item in the `sequence` one by one.
- The code inside the for loop is executed for each value of the `variable`.

#### Example:

```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

Output:

```
apple
banana
cherry
```

#### Range Function:

The `range()` function is commonly used with `for` loop to generate a sequence of numbers. 

- The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.

```python
for x in range(6):
    print(x)
```

Output:

```
0
1
2
3
4
5
```

#### Nested for loop:

A nested `for` loop is a loop inside a loop. The inner loop will be executed one time for each iteration of the outer loop.

```python
for x in range(1, 4):
    for y in range(1, 3):
        print(x, y)
```

Output:

```
1 1
1 2
2 1
2 2
3 1
3 2
```

Note: The inner loop runs to completion for each value of the outer loop.

### Conditional statement in Python:

Conditional statements in Python are used to execute different statements based on different conditions. There are three different types of conditional statements in Python:

#### 1. if statement:

The `if` statement is used to execute a block of code if a condition is true.

```python
if condition:
    # code to be executed
```

- The `condition` is evaluated to a boolean value.
- If the `condition` is true, the code inside the `if` statement will be executed.

#### 2. if-else statement:

The `if-else` statement is used to execute a block of code if a condition is true, and another block of code if the condition is false.

```python
if condition:
    # code to be executed if the condition is true
else:
    # code to be executed if the condition is false
```

- The `condition` is evaluated to a boolean value.
- If the `condition` is true, the code inside the `if` statement will be executed.
- If the `condition` is false, the code inside the `else` statement will be executed.

#### 3. elif statement:

The `elif` statement is short for "else if". It allows you to check multiple conditions and execute a specific block of code based on which condition is true.

```python
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition2 is true
else:
    # code to be executed if all conditions are false
```

- The `condition1` is evaluated to a boolean value.
- If the `condition1` is true, the code inside the first `if` statement will be executed.
- If the `condition1` is false, the `condition2` is evaluated to a boolean value.
- If the `condition2` is true, the code inside the `elif` statement will be executed.
- If all conditions are false, the code inside the `else` statement will be executed.

### Expression Evaluation:

Python uses the Order of Operations (PEMDAS) to evaluate expressions.

1. Parentheses - evaluate expressions inside parentheses first.
2. Exponents - evaluate exponential expressions (e.g., 2^3) next.
3. Multiplication and Division - evaluate multiplication and division expressions from left to right.
4. Addition and Subtraction - evaluate addition and subtraction expressions from left to right.

#### Example:

```python
result = (2 + 3) * 4 / 2 ** 2 - 1
print(result)
```

Output:

```
4.0
```

Explanation:

```
(2 + 3) * 4 / 2 ** 2 - 1
    5    * 4 / 4     - 1
         20 / 4     - 1
             5     - 1
                 4.0
```

### Float Representation:

In Python, float numbers are represented with finite precision. This means that some decimal numbers cannot be represented exactly with a finite number of bits. This can lead to unexpected results when performing arithmetic