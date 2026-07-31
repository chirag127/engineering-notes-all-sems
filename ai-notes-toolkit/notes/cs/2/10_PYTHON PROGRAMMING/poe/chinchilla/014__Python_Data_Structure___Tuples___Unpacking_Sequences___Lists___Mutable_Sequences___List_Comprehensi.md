### Python Data Structures

Python provides several built-in data structures to store and manipulate data efficiently. Understanding these data structures is crucial for writing efficient and effective code.

#### Tuples

- Tuples are ordered, immutable collections of objects.
- They are similar to lists, but once created, their contents cannot be changed.
- Tuples are created using parentheses and commas.

```python
tuple_1 = (1, 2, 3)
tuple_2 = ('a', 'b', 'c')
```

- Tuples can be accessed using indexing or slicing.

```python
tuple_1[0]  # 1
tuple_2[1:]  # ('b', 'c')
```

#### Unpacking Sequences

- Python allows unpacking sequences into variables.

```python
x, y, z = (1, 2, 3)
```

- This assigns the values 1, 2, and 3 to the variables x, y, and z respectively.

#### Lists

- Lists are ordered, mutable collections of objects.
- They are created using square brackets and commas.

```python
list_1 = [1, 2, 3]
list_2 = ['a', 'b', 'c']
```

- Lists can be accessed using indexing or slicing.

```python
list_1[0]  # 1
list_2[1:]  # ['b', 'c']
```

- Lists can be modified by adding, removing or changing elements.

```python
list_1.append(4)
list_2[0] = 'd'
```

#### Mutable Sequences

- In addition to lists, Python provides other mutable sequences such as bytearrays and memoryviews.

```python
byte_array = bytearray(b'hello')
memory_view = memoryview(byte_array)
```

- Bytearrays are like mutable strings, while memoryviews are used for efficient memory access.

#### List Comprehension

- List comprehension is a concise way to create lists in Python.

```python
squares = [x**2 for x in range(1, 6)]
```

- This creates a list of squares of numbers from 1 to 5.

#### Sets

- Sets are unordered collections of unique elements.
- They are created using curly braces or the set() function.

```python
set_1 = {1, 2, 3}
set_2 = set(['a', 'b', 'c'])
```

- Sets support mathematical operations such as union, intersection, and difference.

```python
set_1.union(set_2)
set_1.intersection(set_2)
set_1.difference(set_2)
```

#### Dictionaries

- Dictionaries are unordered collections of key-value pairs.
- They are created using curly braces and colons.

```python
dict_1 = {'a': 1, 'b': 2, 'c': 3}
```

- Dictionaries can be accessed using keys.

```python
dict_1['a']  # 1
```

- Dictionaries can be modified by adding, removing or changing key-value pairs.

```python
dict_1['d'] = 4
del dict_1['a']
```

### Parts of A Function

- A function is a reusable block of code that performs a specific task.
- Functions are defined using the def keyword.

```python
def greet(name):
    print('Hello, ' + name + '!')
```

- The function above takes a parameter name and prints a greeting.

### Execution of A Function

- A function is executed by calling it with arguments.

```python
greet('John')
```

- This will print "Hello, John!".

### Keyword and Default Arguments

- Functions can accept keyword arguments and default arguments.

```python
def greet(name, greeting='Hello'):
    print(greeting + ', ' + name + '!')
```

- The function above takes a parameter greeting with a default value of "Hello".
- The greeting can also be specified using a keyword argument.

```python
greet('John', greeting='Hi')
```

- This will print "Hi, John!".

### Scope Rules

- The scope of a variable refers to the region of the program where it is accessible.
- Python has a set of rules that govern the scope of variables.

```python
def greet():
    message = 'Hello'

print(message)
```

- This will result in a NameError because message is not defined in the global scope.
- Variables defined inside a function have local scope and are not accessible outside the function.
- Variables defined outside a function have global scope and are accessible everywhere in the program.