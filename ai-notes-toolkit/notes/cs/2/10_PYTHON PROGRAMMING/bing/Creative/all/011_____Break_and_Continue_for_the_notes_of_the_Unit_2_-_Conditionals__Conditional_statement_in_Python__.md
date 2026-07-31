# Break and Continue

- Break and continue are two keywords that can be used to alter the flow of a loop in Python.
- Break is used to exit the loop prematurely, while continue is used to skip the current iteration and move to the next one.
- Break and continue can be used with both for and while loops.

## Break

- The break statement terminates the loop containing it and transfers the control to the statement immediately following the loop.
- The break statement can be used to end an infinite loop or to stop the loop when a certain condition is met.
- The break statement can also be used with nested loops. In this case, the break statement will only exit the innermost loop that contains it.

### Syntax of break

```python
for i in iterable:
    # some code
    if condition:
        break # exit the loop
    # some more code
# code after the loop
```

### Example of break

```python
# print the numbers from 1 to 10, but stop when 5 is reached
for i in range(1, 11):
    if i == 5:
        break # exit the loop
    print(i)
# output: 1 2 3 4
```

## Continue

- The continue statement skips the current iteration of the loop and jumps to the next one.
- The continue statement can be used to avoid executing some statements in the loop body or to skip some values in the iterable.
- The continue statement can also be used with nested loops. In this case, the continue statement will only skip the current iteration of the innermost loop that contains it.

### Syntax of continue

```python
for i in iterable:
    # some code
    if condition:
        continue # skip the current iteration
    # some more code
# code after the loop
```

### Example of continue

```python
# print the odd numbers from 1 to 10, but skip 7
for i in range(1, 11):
    if i == 7:
        continue # skip this iteration
    if i % 2 == 0:
        continue # skip even numbers
    print(i)
# output: 1 3 5 9
```