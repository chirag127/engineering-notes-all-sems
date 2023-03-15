Hello, I am Sydney, your AI assistant. I can help you with your study material for Python programming. Here is the content for the topic of for loop in markdown format:

### For Loop

- A for loop is a type of loop that iterates over a sequence of items, such as a list, a tuple, a string, or a range object.
- The syntax of a for loop is:

```python
for item in sequence:
    # do something with item
```

- The item variable can be any valid identifier, and it takes the value of each element in the sequence in each iteration.
- The sequence can be any iterable object that supports the `__iter__()` and `__next__()` methods, such as a list, a tuple, a string, or a range object.
- The body of the loop is indented under the for statement, and it can contain any valid Python statements, including other loops, conditionals, expressions, etc.
- The loop terminates when the sequence is exhausted, or when a `break` statement is encountered inside the loop body.
- A `continue` statement can be used inside the loop body to skip the current iteration and move to the next one.
- An optional `else` clause can be added after the loop body, which is executed only if the loop terminates normally (without a `break` statement).

- Here is an example of a for loop that prints the elements of a list:

```python
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)
```

- The output of this loop is:

```
apple
banana
orange
grape
```

- Here is another example of a for loop that iterates over a range object and prints the square of each number:

```python
for i in range(1, 11):
    print(i ** 2)
```

- The output of this loop is:

```
1
4
9
16
25
36
49
64
81
100
```