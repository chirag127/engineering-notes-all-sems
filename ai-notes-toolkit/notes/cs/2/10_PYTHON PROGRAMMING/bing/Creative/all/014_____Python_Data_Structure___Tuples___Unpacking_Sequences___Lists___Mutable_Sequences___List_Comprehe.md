# Python Data Structure : Tuples , Unpacking Sequences , Lists , Mutable Sequences , List Comprehension , Sets , Dictionaries

## Tuples
- A tuple is a collection type data structure that is **immutable** by design and holds a sequence of **heterogeneous** elements.
- A tuple is defined by using a pair of parentheses `( )` and its elements are separated by commas.
- For example: `tuple_1 = (1, 2, 3, 2)`
- Tuples can be accessed by **indexing** or **unpacking**.
- Indexing is using square brackets `[ ]` to get the element at a specific position in the tuple.
- For example: `tuple_1[0]` returns `1`
- Unpacking is assigning the elements of a tuple to individual variables in one line of code.
- For example: `a, b, c, d = tuple_1` assigns `a = 1`, `b = 2`, `c = 3`, and `d = 2`
- Tuples are useful for storing **fixed** and **ordered** data that do not need to be changed.

## Lists
- A list is a collection type data structure that is **mutable** by design and holds a sequence of **homogeneous** or **heterogeneous** elements.
- A list is defined by using square brackets `[ ]` and its elements are separated by commas.
- For example: `list_1 = [1, 2, 3, 4]` or `list_2 = ["apple", "banana", "orange"]`
- Lists can be accessed by **indexing** or **iterating**.
- Indexing is using square brackets `[ ]` to get the element at a specific position in the list.
- For example: `list_1[0]` returns `1`
- Iterating is using a loop to go through each element in the list.
- For example: `for item in list_2: print(item)` prints `"apple"`, `"banana"`, and `"orange"`
- Lists are useful for storing **dynamic** and **ordered** data that need to be changed or manipulated.

## Mutable Sequences
- A mutable sequence is a data structure that can be **modified** after it is created.
- Lists are an example of mutable sequences, as they can be changed by adding, removing, or updating elements.
- Some common operations on mutable sequences are:
  - `append(x)`: adds an element `x` to the end of the sequence
  - `extend(iterable)`: adds all the elements of an iterable (such as another list or tuple) to the end of the sequence
  - `insert(i, x)`: inserts an element `x` at a given position `i` in the sequence
  - `remove(x)`: removes the first occurrence of an element `x` from the sequence
  - `pop(i)`: removes and returns the element at position `i` from the sequence
  - `clear()`: removes all the elements from the sequence
  - `reverse()`: reverses the order of the elements in the sequence
  - `sort(key=None, reverse=False)`: sorts the elements of the sequence according to a given key function or a reverse flag
- For example: `list_1.append(5)` adds `5` to the end of `list_1`, making it `[1, 2, 3, 4, 5]`

## List Comprehension
- A list comprehension is a concise way of creating a new list from an existing iterable (such as another list or tuple) by applying a certain condition or transformation to each element.
- A list comprehension is defined by using square brackets `[ ]` and has the following syntax:
  - `[expression for item in iterable if condition]`
  - The `expression` is the transformation to be applied to each `item` in the `iterable` if the `condition` is true.
- For example: `[x**2 for x in list_1 if x % 2 == 0]` creates a new list of the squares of the even numbers in `list_1`, which is `[4, 16]`
- List comprehensions are useful for creating **efficient** and **readable** code that can manipulate lists.

##