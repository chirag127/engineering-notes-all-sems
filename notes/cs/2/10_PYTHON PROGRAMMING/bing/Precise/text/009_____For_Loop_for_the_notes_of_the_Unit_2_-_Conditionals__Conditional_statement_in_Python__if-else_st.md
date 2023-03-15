### For Loop

A for loop is a control flow statement in Python that allows code to be executed repeatedly. It is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object, executing the code block for each element in the sequence.

Here are some key points to remember when using for loops in Python:

1. The syntax for a for loop is: `for variable in sequence:`
2. The code block within the for loop is indented and will be executed for each element in the sequence.
3. The loop variable takes on the value of the current element in the sequence for each iteration of the loop.
4. The `range()` function can be used to generate a sequence of numbers to iterate over.
5. The `break` statement can be used to exit a for loop prematurely.
6. The `continue` statement can be used to skip the rest of the code block for the current iteration and move on to the next iteration.

Here is an example of a for loop that prints the numbers 1 to 5:

```python
for i in range(1, 6):
    print(i)
```

This for loop uses the `range()` function to generate a sequence of numbers from 1 to 5. The loop variable `i` takes on the value of each number in the sequence for each iteration of the loop. The code block within the for loop is executed for each iteration, printing the value of `i` to the screen.
