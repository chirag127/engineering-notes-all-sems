# For Loop

- A for loop is a type of loop that iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- The syntax of a for loop is:

```python
for item in sequence:
    # do something with item
```

- The item variable can be any valid identifier, and it takes the value of each element in the sequence in each iteration.
- The sequence can be any iterable object that supports the `__iter__` and `__next__` methods, such as a list, a tuple, a string, or a range object.
- The body of the loop is indented under the for statement, and it can contain any valid Python statements, including other loops, conditionals, or function calls.
- The loop terminates when the sequence is exhausted, or when a `break` or `return` statement is encountered inside the loop body.
- A for loop can also have an optional `else` clause, which is executed when the loop ends normally, i.e., without a `break` or `return` statement. The syntax of a for loop with an else clause is:

```python
for item in sequence:
    # do something with item
else:
    # do something else
```

- A for loop can be used for various purposes, such as iterating over the elements of a list, a tuple, a string, or a range object, performing a task for a fixed number of times, traversing the keys or values of a dictionary, or generating a list comprehension.