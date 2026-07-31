### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, only the behavior and interface of the data type .
- An ADT can have multiple concrete data types (CDTs) that implement the ADT using different data structures and algorithms .
- Examples of ADTs are stack, queue, list, map, set, tree, etc. Each of these ADTs can have different CDTs, such as array-based, linked-list-based, hash-based, etc.

### ADT Interface in Python

- Python does not have a built-in way to define ADTs, but it provides some features that can be used to create and use ADTs .
- One way to create an ADT in Python is to use a class that defines the methods for the ADT operations, but leaves them unimplemented or raises a `NotImplementedError` exception .
- Another way to create an ADT in Python is to use an abstract base class (ABC) from the `abc` module, which allows defining abstract methods that must be overridden by subclasses that inherit from the ABC.
- To use an ADT in Python, one can create a subclass that inherits from the ADT class or ABC, and implements the abstract methods using a specific data structure and algorithm .
- Alternatively, one can use an existing CDT that implements the ADT interface, such as the built-in types `list`, `dict`, `set`, etc, or the types from the `collections` module, such as `deque`, `OrderedDict`, `Counter`, etc .

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm works by creating a list of numbers from 2 to the limit, and marking the multiples of each number starting from 2 as composite (not prime).
- The algorithm stops when the square of the current number is greater than the limit, and returns the unmarked numbers as primes.
- The algorithm can be implemented in Python using a list as a CDT for the ADT of a sequence.
- The following is a possible Python code for the sieve of Eratosthenes:

```python
def sieve_of_eratosthenes(limit):
  # create a list of numbers from 2 to limit
  numbers = list(range(2, limit + 1))
  # loop through the numbers from 2 to the square root of limit
  for i in range(2, int(limit ** 0.5) + 1):
    # if the number is not marked as composite
    if numbers[i - 2] != 0:
      # mark the multiples of the number as composite
      for j in range(i * i, limit + 1, i):
        numbers[j - 2] = 0
  # return the unmarked numbers as primes
  return [n for n in numbers if n != 0]
```