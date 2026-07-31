### While Loop

A while loop is a control flow statement that allows code to be executed repeatedly based on a given Boolean condition. The while loop can be thought of as a repeating if statement. The basic structure of a while loop is:

```
while condition:
    # code block to be executed
```

The `condition` is evaluated, and if the condition is true, the code block within the loop is executed. This repeats until the condition becomes false. Here are some key points to remember about while loops:

1. The condition is evaluated before the loop is executed. If the condition is false at the start, the loop will not be executed at all.
2. The code block within the loop must change the value of the condition, or the loop will run indefinitely.
3. While loops are useful when the number of iterations is not known beforehand.

Here is an example of a while loop that counts down from 5:

```python
count = 5
while count > 0:
    print(count)
    count -= 1
```

This while loop will print the numbers 5, 4, 3, 2, and 1. The condition `count > 0` is true at the start, so the loop is executed. The code block within the loop prints the value of `count` and then decrements it by 1. This continues until `count` is no longer greater than 0, at which point the loop exits.

While loops are a powerful tool in Python programming, and are commonly used in a wide range of applications. It is important to use them correctly to avoid infinite loops and other potential issues.