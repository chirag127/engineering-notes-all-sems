# Python Data Structure : Tuples , Unpacking Sequences , Lists , Mutable Sequences , List Comprehension , Sets , Dictionaries

## Tuples
- A tuple is a collection type data structure that is **immutable** by design and holds a sequence of **heterogeneous** elements.
- A tuple can be defined by using a pair of parentheses `()` and its elements are separated by commas.
- For example: `tuple_1 = (1, 2, 3, 2)`
- Tuples can be accessed via **unpacking** or **indexing**.
- Unpacking means assigning the elements of a tuple to individual variables, such as `a, b, c = tuple_1`.
- Indexing means accessing the elements of a tuple by their position, such as `tuple_1[0]` or `tuple_1[-1]`.
- Tuples can be used as **keys** for dictionaries or as **elements** of sets.
- Tuples have some methods, such as `count()` and `index()`, but not as many as lists.

## Lists
- A list is a collection type data structure that is **mutable** and holds a sequence of **homogeneous** or **heterogeneous** elements.
- A list can be defined by using a pair of square brackets `[]` and its elements are separated by commas.
- For example: `list_1 = [1, 2, 3, 4]` or `list_2 = ["a", "b", 1, 2]`
- Lists can be accessed via **iterating** or **indexing**.
- Iterating means looping over the elements of a list, such as `for x in list_1: print(x)`.
- Indexing means accessing the elements of a list by their position, such as `list_1[0]` or `list_1[-1]`.
- Lists can be **modified** by adding, removing, or changing elements.
- Lists have many methods, such as `append()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, and `copy()`.

## Mutable Sequences
- A mutable sequence is a collection type data structure that can be **changed** after it is created.
- Lists are examples of mutable sequences, as they can be modified by adding, removing, or changing elements.
- Other examples of mutable sequences are **byte arrays** and **memory views**.
- Byte arrays are sequences of bytes that can be manipulated at the binary level.
- Memory views are objects that allow shared access to data without copying it.

## List Comprehension
- A list comprehension is a concise way of creating a list from another iterable object.
- A list comprehension consists of a pair of square brackets `[]` containing an **expression** followed by a **for** clause, and optionally one or more **if** clauses.
- For example: `list_3 = [x**2 for x in range(10) if x % 2 == 0]`
- This creates a list of the squares of the even numbers from 0 to 9.
- List comprehensions can be nested, meaning that one list comprehension can contain another list comprehension.
- For example: `list_4 = [[x, y] for x in range(3) for y in range(2)]`
- This creates a list of lists containing the pairs of numbers from 0 to 2 and from 0 to 1.

## Sets
- A set is a collection type data structure that is **unordered** and **mutable** and does not allow any **duplicate** elements .
- A set can be defined by using a pair of curly braces `{}` and its elements are separated by commas.
- For example: `set_1 = {1, 2, 3, 4}`
- Sets can also be created by using the `set()` function on an iterable object, such as `set_2 = set("hello")`
- Sets can be used for **membership testing** and **eliminating duplicate entries**.
- Sets have many methods, such as `add()`, `remove()`, `discard()