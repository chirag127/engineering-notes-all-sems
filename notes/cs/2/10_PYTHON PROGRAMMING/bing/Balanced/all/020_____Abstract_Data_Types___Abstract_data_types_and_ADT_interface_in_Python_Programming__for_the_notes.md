# Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data  .
- An ADT does not specify how the data is stored or implemented, only the behavior and interface of the data type .
- An ADT can be implemented using different concrete data types (CDTs), such as arrays, lists, maps, queues, sets, stacks, tables, trees, vectors, etc .
- An ADT can also be defined using abstract base classes (ABCs) in Python, which are classes that provide a common interface and behavior for subclasses, but cannot be instantiated directly.
- An example of an ADT is the stack, which is a sequence of objects in which only the most recently added object is accessible.
- The stack ADT has two main operations: push, which adds an object to the top of the stack, and pop, which removes and returns the object at the top of the stack.
- The stack ADT can be implemented using different CDTs, such as lists, arrays, or linked lists.
- The stack ADT can also be defined using an ABC in Python, which provides the methods push and pop, and raises a NotImplementedError if they are not overridden by subclasses.

# ADT Interface in Python

- An ADT interface in Python is a way of defining the behavior and interface of an ADT using an ABC.
- An ABC is a class that inherits from the abc.ABC class, which is a metaclass that provides the infrastructure for defining ABCs in Python.
- An ABC can use the @abstractmethod decorator to mark methods that must be implemented by subclasses.
- An ABC can also use the @abstractproperty decorator to mark properties that must be implemented by subclasses.
- An ABC can also use the @classmethod, @staticmethod, and @abstractclassmethod decorators to mark class methods, static methods, and abstract class methods respectively.
- An ABC can also use the @abstractmethod and @abstractproperty decorators to mark special methods, such as __len__, __getitem__, __iter__, etc.
- An ABC cannot be instantiated directly, but can be subclassed by CDTs that provide the implementation of the abstract methods and properties.
- An example of an ADT interface in Python is the collections.abc.Sequence ABC, which defines the behavior and interface of a sequence ADT.
- The collections.abc.Sequence ABC inherits from the collections.abc.Reversible and collections.abc.Collection ABCs, which provide some common methods and properties for reversible and collection ADTs respectively.
- The collections.abc.Sequence ABC has two abstract methods: __getitem__, which returns the element at a given index, and __len__, which returns the number of elements in the sequence.
- The collections.abc.Sequence ABC also has some concrete methods, such as index, count, __contains__, __reversed__, etc, that are based on the abstract methods.
- The collections.abc.Sequence ABC can be subclassed by CDTs that provide the implementation of the __getitem__ and __len__ methods, such as lists, tuples, strings, etc.

# Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for generating prime numbers, which are numbers that are only divisible by 1 and themselves.
- The algorithm was given by the Greek mathematician Eratosthenes, who lived in the 3rd century BC.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to n, where n is the upper limit of the prime numbers to be generated.
  - Mark 2 as a prime number, and mark all the multiples of 2 as composite numbers (not prime).
  - Find the next unmarked number, which is 3, and mark it as a prime number, and mark all the multiples of 3 as composite numbers.
  - Repeat the previous step until there are no more unmarked numbers, or until the square of the current number is greater than n.
  - The remaining unmarked numbers are the prime numbers up to n.
- The sieve of Eratosthenes can be implemented