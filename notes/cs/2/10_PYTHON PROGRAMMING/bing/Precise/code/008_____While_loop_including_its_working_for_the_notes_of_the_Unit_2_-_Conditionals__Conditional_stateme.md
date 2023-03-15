### While Loop

The `while` loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The `while` loop can be thought of as a repeating `if` statement.

Here is the basic structure of a `while` loop in Python:

```
while condition:
    # code block to be executed
```

The `condition` is evaluated, and if the `condition` is `True`, the code block within the loop is executed. This process is repeated as long as the `condition` remains `True`. Once the `condition` becomes `False`, the loop is exited and the program continues with the next statement after the loop.

Here are some key points to remember about `while` loops:

- The `condition` is evaluated before each iteration. If the `condition` is `False` at the start, the code block within the loop will not be executed at all.
- The code block within the loop must change the value of the `condition` or the loop will run indefinitely, resulting in an infinite loop.
- `while` loops are useful when the number of iterations is not known beforehand.

Here is an example of a `while` loop that counts down from 5:

```
count = 5
while count > 0:
    print(count)
    count -= 1
```

This `while` loop will print the numbers 5, 4, 3, 2, and 1. The `condition` is `count > 0`, which is `True` at the start. The code block within the loop is executed, printing the value of `count` and decrementing it by 1. This process is repeated until `count` is no longer greater than 0, at which point the loop is exited.
