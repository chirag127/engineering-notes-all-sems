### Python Data Structure : Tuples , Unpacking Sequences , Lists , Mutable Sequences , List Comprehension , Sets , Dictionaries

- A data structure is a way of organizing and storing data in a computer memory.
- Python provides several built-in data structures, such as tuples, lists, sets, and dictionaries.
- Each data structure has its own characteristics and operations.

#### Tuples
- A tuple is an ordered and immutable sequence of values, separated by commas and enclosed in parentheses.
- A tuple can store any type of data, such as numbers, strings, booleans, or other tuples.
- A tuple can be indexed and sliced using square brackets, similar to strings.
- A tuple can be iterated over using a for loop or a while loop.
- A tuple can be compared, concatenated, and repeated using operators, such as ==, +, and *.
- A tuple can be converted to a list using the list() function, or to a set using the set() function.
- A tuple can be created with or without parentheses, or with a single element and a trailing comma.
- Example:

```python
# Creating a tuple
t = (1, 2, 3, 4, 5)
t = 1, 2, 3, 4, 5 # without parentheses
t = (1,) # with a single element and a trailing comma

# Accessing a tuple element
t[0] # returns 1
t[-1] # returns 5
t[1:3] # returns (2, 3)

# Iterating over a tuple
for x in t:
  print(x)

i = 0
while i < len(t):
  print(t[i])
  i += 1

# Comparing tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t1 == t2 # returns False
t1 < t2 # returns True

# Concatenating and repeating tuples
t3 = t1 + t2 # returns (1, 2, 3, 4, 5, 6)
t4 = t1 * 2 # returns (1, 2, 3, 1, 2, 3)

# Converting a tuple to a list or a set
l = list(t) # returns [1, 2, 3, 4, 5]
s = set(t) # returns {1, 2, 3, 4, 5}
```

#### Unpacking Sequences
- Unpacking sequences is a way of assigning multiple values from a sequence, such as a tuple or a list, to multiple variables in one line of code.
- The number of variables must match the number of elements in the sequence, otherwise a ValueError will be raised.
- The variables can be enclosed in parentheses or not, depending on the style preference.
- The unpacking can also be done with nested sequences, such as tuples of tuples or lists of lists.
- Example:

```python
# Unpacking a tuple
t = (1, 2, 3)
a, b, c = t # a = 1, b = 2, c = 3
(a, b, c) = t # same as above

# Unpacking a list
l = [4, 5, 6]
x, y, z = l # x = 4, y = 5, z = 6
[x, y, z] = l # same as above

# Unpacking a nested sequence
t = ((1, 2), (3, 4))
(a, b), (c, d) = t # a = 1, b = 2, c = 3, d = 4
```

#### Lists
- A list is an ordered and mutable sequence of values, separated by commas and enclosed in square brackets.
- A list can store any type of data, such as numbers, strings, booleans, or other lists.
- A list can be indexed and sliced using square brackets, similar to strings and tuples.
- A list can be iterated over using a for loop or a while loop.
- A list can be compared, concatenated, and repeated using operators, such as ==, +, and *.
- A list can be converted to a tuple using the tuple() function, or to a set using the set() function.
- A list can be modified using methods, such as append(), insert(), remove(), pop(), sort(), reverse(), and clear().
- A list can be created with or without square brackets, or with a single element and a trailing