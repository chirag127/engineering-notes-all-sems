### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, only the behavior and interface of the data type .
- An ADT can have multiple concrete data types (CDTs) that implement the ADT using different data structures and algorithms .
- Examples of ADTs are stack, queue, list, map, set, tree, etc. Each of these ADTs can have different CDTs, such as array-based stack, linked-list stack, hash map, binary tree, etc .

### ADT Interface in Python

- Python does not have a built-in way to define ADTs, but it provides some features that can help create and use ADTs .
- One way to define an ADT in Python is to use a class that specifies the methods and attributes of the ADT, but leaves them unimplemented or raises a `NotImplementedError` exception .
- Another way to define an ADT in Python is to use an abstract base class (ABC) from the `abc` module, which allows marking methods and properties as abstract using the `@abstractmethod` and `@abstractproperty` decorators.
- An ABC can also register concrete subclasses that implement the ADT using the `register` method or the `@register` decorator.
- An example of an ABC that defines the ADT of a stack is:

```python
from abc import ABC, abstractmethod

class Stack(ABC):
    """An abstract base class for a stack ADT."""

    @abstractmethod
    def push(self, item):
        """Add an item to the top of the stack."""
        pass

    @abstractmethod
    def pop(self):
        """Remove and return the item from the top of the stack."""
        pass

    @abstractmethod
    def peek(self):
        """Return the item from the top of the stack without removing it."""
        pass

    @abstractmethod
    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        pass

    @abstractmethod
    def size(self):
        """Return the number of items in the stack."""
        pass
```

- A concrete subclass that implements the stack ADT using a list is:

```python
class ListStack(Stack):
    """A concrete class for a stack ADT using a list."""

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Remove and return the item from the top of the stack."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the item from the top of the stack without removing it."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Return True if the stack is empty, False otherwise."""
        return len(self._items) == 0

    def size(self):
        """Return the number of items in the stack."""
        return len(self._items)
```

- An example of using the stack ADT is:

```python
s = ListStack() # create a stack object
s.push(1) # push 1 to the stack
s.push(2) # push 2 to the stack
s.peek() # return 2
s.pop() # return and remove 2
s.size() # return 1
s.is_empty() # return False
s.pop() # return and remove 1
s.is_empty() # return True
s.pop() # raise IndexError
```

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all prime numbers up to a given limit.
- The algorithm works by creating a list of numbers from 2 to the limit, and marking the multiples of each number, starting from 2, as composite (not prime).
- The numbers that are not marked as composite are prime, and can be returned