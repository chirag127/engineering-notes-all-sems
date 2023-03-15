### While loop

- A while loop is a type of loop that repeatedly executes a block of code as long as a given condition is true.
- The syntax of a while loop is:

```python
while condition:
    # code block
```

- The condition is a boolean expression that evaluates to either True or False. If the condition is True, the code block is executed and the condition is checked again. If the condition is False, the loop is terminated and the program moves to the next statement after the loop.
- A while loop can be used to implement various tasks that require repetition, such as counting, iterating, accumulating, etc.
- A while loop can also be used to create an infinite loop, which is a loop that never ends. This can be useful for some applications that need to run continuously, such as servers, games, etc. However, an infinite loop can also cause problems if there is no way to exit the loop or stop the program. To create an infinite loop, the condition can be set to True or a value that always evaluates to True, such as 1, "hello", etc.
- A while loop can be controlled by using break and continue statements. A break statement can be used to exit the loop prematurely, while a continue statement can be used to skip the current iteration and move to the next one. For example:

```python
# A while loop that prints the numbers from 1 to 10, except 5
n = 1
while n <= 10:
    if n == 5:
        n += 1
        continue # skip the rest of the code block and move to the next iteration
    print(n)
    n += 1
```

- The output of this loop is:

```output
1
2
3
4
6
7
8
9
10
```