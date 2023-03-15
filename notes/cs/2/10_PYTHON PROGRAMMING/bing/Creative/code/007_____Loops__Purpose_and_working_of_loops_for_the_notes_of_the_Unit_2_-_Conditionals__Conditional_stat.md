### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or generating output.
- There are two main types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the loop body for each element in the sequence.
- A while loop executes the loop body as long as a given boolean expression evaluates to True, and stops when the expression becomes False.
- The syntax of a for loop is:

```python
for variable in sequence:
    # loop body
    # statements to be executed for each element in the sequence
```

- The syntax of a while loop is:

```python
while expression:
    # loop body
    # statements to be executed as long as the expression is True
```

- Both types of loops can be controlled by using break, continue, and else statements.
- A break statement terminates the loop and jumps to the next statement after the loop.
- A continue statement skips the current iteration of the loop and continues with the next one.
- An else statement executes a block of code after the loop ends, but only if the loop was not terminated by a break statement.