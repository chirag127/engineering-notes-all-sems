### Loops: Purpose and working of loops

- A loop is a programming construct that allows a block of code to be executed repeatedly until a certain condition is met.
- The purpose of loops is to automate repetitive tasks, such as processing a list of items, performing calculations, or generating output.
- There are two types of loops in Python: for loops and while loops.
- A for loop iterates over a sequence of values, such as a list, a tuple, a string, or a range object, and executes the block of code for each value in the sequence.
- A while loop executes the block of code as long as a given condition is true, and stops when the condition becomes false.
- The syntax of a for loop is:

```python
for variable in sequence:
    # block of code
```

- The syntax of a while loop is:

```python
while condition:
    # block of code
```

- The block of code inside a loop is indented by four spaces or a tab, and is also called the loop body.
- The loop variable in a for loop takes the value of each element in the sequence, and can be used inside the loop body.
- The condition in a while loop is a boolean expression that evaluates to either True or False, and can use any comparison or logical operators.
- To exit a loop prematurely, the break statement can be used. This will stop the loop execution and jump to the next statement after the loop.
- To skip the current iteration of a loop and continue with the next one, the continue statement can be used. This will skip the loop body and go back to the loop condition.
- To loop through a sequence of values in reverse order, the reversed() function can be used. This will return an iterator that yields the values in reverse order.
- To loop through two or more sequences of values in parallel, the zip() function can be used. This will return an iterator that yields tuples of corresponding values from each sequence.
- To loop through a sequence of values with their indices, the enumerate() function can be used. This will return an iterator that yields pairs of index and value from the sequence.