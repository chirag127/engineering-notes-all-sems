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

## Break and continue statements

- The break statement terminates the current loop and resumes execution at the next statement after the loop.
- The continue statement skips the rest of the current iteration and jumps to the next iteration of the loop.
- These statements can be used to control the flow of the loop and to exit the loop when a certain condition is met.

- For example, the following for loop prints the numbers from 1 to 10, but breaks when it reaches 5:

```python
for i in range(1, 11):
    if i == 5:
        break
    print(i)
```

- The output is:

```python
1
2
3
4
```

- For example, the following for loop prints the numbers from 1 to 10, but skips the even numbers:

```python
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
```

- The output is:

```python
1
3
5
7
9
```