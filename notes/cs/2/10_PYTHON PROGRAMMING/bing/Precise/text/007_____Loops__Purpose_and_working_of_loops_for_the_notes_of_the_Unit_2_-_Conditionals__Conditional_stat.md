### Loops: Purpose and working of loops

Loops are an essential part of programming, allowing for the repetition of a block of code a specified number of times or until a certain condition is met. In Python, there are two main types of loops: `for` and `while`.

The `for` loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object. The code block within the loop is executed once for each item in the sequence. Here is an example of a `for` loop in Python:

```python
for i in range(5):
    print(i)
```

This loop will print the numbers 0 to 4, as the `range` function generates a sequence of numbers from 0 to the specified end value (not inclusive).

The `while` loop, on the other hand, is used to repeatedly execute a block of code as long as a certain condition is `True`. Here is an example of a `while` loop in Python:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

This loop will also print the numbers 0 to 4. The condition `i < 5` is checked at the beginning of each iteration. If the condition is `True`, the code block within the loop is executed. If the condition is `False`, the loop is exited.

Loops can be nested, meaning that one loop can be placed inside another loop. This can be useful for iterating over multiple dimensions of data, such as a two-dimensional list (a list of lists). Here is an example of nested loops in Python:

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

This code will print the following pairs of numbers: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1).

In summary, loops are a powerful tool in programming, allowing for the efficient repetition of a block of code. Python provides two main types of loops, `for` and `while`, which can be used to iterate over sequences or repeat a block of code while a condition is `True`, respectively. Loops can also be nested to iterate over multiple dimensions of data.