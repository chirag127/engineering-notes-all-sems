### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or validating user input.
- There are two types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the loop body for each element in the sequence.
- A while loop executes the loop body as long as a given condition is true, and stops when the condition becomes false or a break statement is encountered.
- The syntax of a for loop is:

```python
for variable in sequence:
    # loop body
    # statements to be executed for each element in the sequence
```

- The syntax of a while loop is:

```python
while condition:
    # loop body
    # statements to be executed as long as the condition is true
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
while condition:
    # loop body
    # statements to be executed as long as the condition is true
else:
    # else clause
    # statements to be executed when the loop ends normally
```

- Loops can be nested, i.e. a loop can contain another loop inside its body. This is useful for iterating over multidimensional data structures, such as matrices or nested lists.
- The syntax of a nested loop is:

```python
for variable1 in sequence1:
    # outer loop body
    # statements to be executed for each element in the outer sequence
    for variable2 in sequence2:
        # inner loop body
        # statements to be executed for each element in the inner sequence
```

- Loops can be controlled by using some keywords, such as break, continue, and pass.
- The break keyword exits the current loop and skips the else clause, if any.
- The continue keyword skips the rest of the current iteration and moves to the next one.
- The pass keyword does nothing and is used as a placeholder when a statement is required syntactically but no action is needed.