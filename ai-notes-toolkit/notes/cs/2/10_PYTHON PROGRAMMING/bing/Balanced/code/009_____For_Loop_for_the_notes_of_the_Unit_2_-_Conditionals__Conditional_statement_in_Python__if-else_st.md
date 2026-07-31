### For Loop

- A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.
- Syntax:

```python
for variable in sequence:
    # loop body
    # statements to be executed
```

- The sequence can be any iterable object, such as a list, a tuple, a string, or a range object.
- The variable is assigned the value of each element in the sequence in each iteration, and the loop body is executed.
- The loop body must be indented, and the indentation level determines the scope of the loop.
- The loop ends when the sequence is exhausted or when a break statement is encountered.

- Example:

```python
# print the numbers from 1 to 10
for i in range(1, 11):
    print(i)
```

- Output:

```text
1
2
3
4
5
6
7
8
9
10
```

- The range function returns a range object that represents a sequence of numbers. It can take one, two, or three arguments: start, stop, and step.
- The range object is lazy, meaning it only generates the numbers when needed, not all at once.
- The range object is iterable, meaning it can be used in a for loop or converted to a list.
- The range function follows the half-open interval convention, meaning the start value is included, but the stop value is excluded.
- If only one argument is given, it is assumed to be the stop value, and the start value is 0 by default.
- If two arguments are given, they are the start and stop values, and the step value is 1 by default.
- If three arguments are given, they are the start, stop, and step values, and the step value can be positive or negative, but not zero.
- Examples:

```python
# range with one argument
range(5) # equivalent to range(0, 5, 1)
# represents the sequence 0, 1, 2, 3, 4

# range with two arguments
range(1, 5) # equivalent to range(1, 5, 1)
# represents the sequence 1, 2, 3, 4

# range with three arguments
range(1, 10, 2) # start = 1, stop = 10, step = 2
# represents the sequence 1, 3, 5, 7, 9

range(10, 1, -2) # start = 10, stop = 1, step = -2
# represents the sequence 10, 8, 6, 4, 2
```

- The for loop can also be used to iterate over other iterable objects, such as lists, tuples, strings, etc.
- Examples:

```python
# iterate over a list of fruits
fruits = ["apple", "banana", "orange", "grape"]
for fruit in fruits:
    print(fruit)

# iterate over a tuple of colors
colors = ("red", "green", "blue", "yellow")
for color in colors:
    print(color)

# iterate over a string of characters
name = "Sydney"
for char in name:
    print(char)
```