### For Loop

A for loop is a control flow statement that allows code to be executed repeatedly. It is used to iterate over a sequence, such as a list, tuple, or string, or other iterable objects.

Here are the key points to remember about for loops in Python:

1. The for loop is used to iterate over a sequence or other iterable object.
2. The syntax of a for loop is: `for variable in sequence: statements`
3. The `variable` takes on the value of the next element in the sequence each time through the loop.
4. The `statements` are executed once for each element in the sequence.
5. The `range()` function can be used to generate a sequence of numbers to iterate over.
6. The `break` statement can be used to exit a for loop before the sequence is exhausted.
7. The `continue` statement can be used to skip the rest of the statements in the current iteration and move on to the next iteration.

For example, here is a simple for loop that prints the numbers 1 to 5:

```python
for i in range(1, 6):
    print(i)
```

This for loop uses the `range()` function to generate a sequence of numbers from 1 to 5. The variable `i` takes on the value of each number in the sequence, and the `print()` function is called to print the value of `i` each time through the loop.
