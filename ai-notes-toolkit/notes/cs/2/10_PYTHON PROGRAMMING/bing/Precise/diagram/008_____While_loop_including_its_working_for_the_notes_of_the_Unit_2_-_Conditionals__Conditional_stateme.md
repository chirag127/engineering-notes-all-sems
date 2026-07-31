### While Loop

A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement.

The basic structure of a while loop is:

```
while condition:
    # code block to be executed
```

The `condition` is evaluated, and if the condition is true, the code within the block is executed. This repeats until the condition becomes false. If the condition is false at the start, the code block will not be executed at all.

Here are some key points to remember about while loops:

- The condition is evaluated before each iteration. If the condition is false, the loop will not be executed.
- The code block can contain any number of statements, including other control structures like if-else statements, nested-if statements, and elif statements.
- It is important to make sure that the condition eventually becomes false, otherwise the loop will run indefinitely, creating an infinite loop.
- The loop variable, if any, must be initialized before the loop and changed within the loop.

Here is an example of a while loop that prints the numbers from 1 to 5:

```python
i = 1
while i <= 5:
    print(i)
    i += 1
```

In this example, the loop variable `i` is initialized to 1 before the loop. The condition `i <= 5` is true, so the code block is executed, printing the value of `i`. The loop variable is then incremented by 1. This process repeats until the condition becomes false, at which point the loop exits.

While loops are useful when you need to repeat a set of statements an unknown number of times, until a specific condition is met. For example, you could use a while loop to read data from a file until the end of the file is reached, or to validate user input until the user enters a valid value.