# For Loop

A for loop is a control flow statement in Python that allows code to be executed repeatedly. It is used to iterate over a sequence (such as a list, tuple, or string) or other iterable object, executing the code block for each element in the sequence.

Here are some key points to remember when using for loops in Python:

1. The syntax for a for loop is `for variable in sequence:`, where `variable` is the name of the variable that will take on the value of each element in the sequence, and `sequence` is the sequence to iterate over.

2. The code block to be executed for each iteration is indented under the for loop statement.

3. The `range()` function can be used to generate a sequence of numbers to iterate over. For example, `for i in range(5):` will iterate over the values 0, 1, 2, 3, and 4.

4. The `break` statement can be used to exit a for loop prematurely.

5. The `continue` statement can be used to skip the rest of the code block for the current iteration and move on to the next iteration.

6. The `else` clause can be used with a for loop to specify code to be executed when the loop has finished iterating over the sequence. The code in the `else` clause is only executed if the loop completes normally (i.e., if it is not exited prematurely by a `break` statement).

For example, here is a simple for loop that prints the numbers 0 to 4:

```python
for i in range(5):
    print(i)
```

This for loop uses the `range()` function to generate a sequence of numbers from 0 to 4, and the variable `i` takes on the value of each number in the sequence during each iteration of the loop. The code block under the for loop statement simply prints the value of `i` during each iteration. The output of this for loop would be:

```
0
1
2
3
4
```

For loops are a powerful tool in Python and are commonly used for tasks such as iterating over the elements in a list or string, or for performing a specific action a certain number of times. It is important to understand the syntax and behavior of for loops in order to use them effectively in your Python programs.