# Loops: Purpose and working of loops

- Loops are a way of repeating a block of code multiple times until a certain condition is met.
- Loops are useful for performing tasks that require iteration, such as processing a list of items, generating a sequence of numbers, or displaying a pattern on the screen.
- There are two types of loops in Python: for loops and while loops.

## For loops

- A for loop executes a block of code for each element in an iterable object, such as a list, a tuple, a string, or a range.
- The syntax of a for loop is:

```python
for variable in iterable:
    # block of code
```

- The variable takes the value of each element in the iterable in each iteration.
- The block of code is indented under the for statement and is executed once for each element.
- The loop ends when the iterable is exhausted or when a break statement is encountered.

- For example, the following for loop prints the numbers from 1 to 10:

```python
for i in range(1, 11):
    print(i)
```

## While loops

- A while loop executes a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # block of code
```

- The condition is a boolean expression that is evaluated before each iteration.
- The block of code is indented under the while statement and is executed as long as the condition is true.
- The loop ends when the condition becomes false or when a break statement is encountered.

- For example, the following while loop prints the numbers from 1 to 10:

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

- Note that the loop variable i must be initialized before the loop and updated inside the loop to avoid an infinite loop.