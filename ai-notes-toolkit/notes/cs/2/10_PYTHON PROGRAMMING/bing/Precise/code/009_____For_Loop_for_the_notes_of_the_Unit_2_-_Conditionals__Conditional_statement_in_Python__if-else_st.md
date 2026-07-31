### For Loop

A for loop is a control flow statement in Python that allows code to be executed repeatedly. It is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object, executing the code block for each element in the sequence.

Here are some key points to remember when using for loops in Python:

1. The syntax for a for loop is `for variable in sequence:`, where `variable` is the name of the variable that will take on the value of each element in the sequence, and `sequence` is the sequence to be iterated over.

2. The code block to be executed for each iteration is indented under the for loop statement.

3. The `range()` function can be used to generate a sequence of numbers to iterate over. For example, `for i in range(5):` will iterate over the values 0, 1, 2, 3, and 4.

4. The `break` statement can be used to exit a for loop prematurely, while the `continue` statement can be used to skip the rest of the current iteration and move on to the next one.

5. For loops can be nested inside other for loops or conditional statements.

6. The `else` clause can be used with a for loop to specify code that should be executed after the loop has finished executing, but only if the loop completed normally (i.e., if it was not exited prematurely by a `break` statement).

For example, here is a simple for loop that prints the numbers 1 to 5:

```python
for i in range(1, 6):
    print(i)
```

This for loop uses the `range()` function to generate a sequence of numbers from 1 to 5. The variable `i` takes on the value of each number in the sequence, and the `print()` function is called to print the value of `i` for each iteration of the loop. The output of this code would be:

```
1
2
3
4
5
```

For loops are a powerful tool in Python that allow you to automate repetitive tasks and process data in a structured manner. They are an essential part of any Python programmer's toolkit.