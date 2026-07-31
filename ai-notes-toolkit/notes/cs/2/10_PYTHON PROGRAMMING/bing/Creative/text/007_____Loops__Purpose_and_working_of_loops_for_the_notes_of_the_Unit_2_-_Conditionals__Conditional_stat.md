### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or validating user input.
- There are two types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the loop body for each element in the sequence.
- A while loop executes the loop body as long as a given boolean expression evaluates to True, and stops when the expression becomes False or a break statement is encountered.
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

- Both types of loops can have an optional else clause, which is executed when the loop terminates normally, i.e. without a break statement.
- The syntax of a for loop with an else clause is:

```python
for variable in sequence:
    # loop body
    # statements to be executed for each element in the sequence
else:
    # else clause
    # statements to be executed when the loop ends normally
```

- The syntax of a while loop with an else clause is:

```python
while expression:
    # loop body
    # statements to be executed as long as the expression is True
else:
    # else clause
    # statements to be executed when the loop ends normally
```

- Loops can be nested inside other loops, creating a loop within a loop. This is useful for iterating over multidimensional data structures, such as matrices or nested lists.
- The syntax of a nested loop is:

```python
for variable1 in sequence1:
    # outer loop body
    for variable2 in sequence2:
        # inner loop body
        # statements to be executed for each pair of elements from sequence1 and sequence2
```

- The same syntax applies for nested while loops, except that the expression for the inner loop must be evaluated separately from the expression for the outer loop.
- Loops can be controlled using the break, continue, and pass statements.
- The break statement terminates the current loop and skips the else clause, if any. It is used to exit the loop prematurely when a certain condition is met or an error occurs.
- The continue statement skips the rest of the current iteration and moves to the next one. It is used to skip some elements in the sequence or some cases in the expression that are not relevant or valid.
- The pass statement does nothing and is used as a placeholder when a statement is required syntactically but no action is needed. It is used to create empty loops or loop bodies that will be filled later.