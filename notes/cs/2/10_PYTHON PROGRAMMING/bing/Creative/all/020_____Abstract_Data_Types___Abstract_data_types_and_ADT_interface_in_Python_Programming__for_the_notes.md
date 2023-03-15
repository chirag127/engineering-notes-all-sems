# Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, but only the interface or behavior of the data type .
- An ADT can have multiple concrete data types (CDTs) that implement the ADT using different data structures and algorithms .
- Examples of ADTs are list, stack, queue, set, map, tree, etc. Each of these ADTs can have different CDTs, such as array, linked list, hash table, binary tree, etc .
- In Python, an ADT can be defined using abstract base classes (ABCs) from the `abc` module.
- An ABC is a class that has at least one abstract method, which is a method that is declared but not implemented.
- An ABC can also have concrete methods, which are methods that have an implementation and can be inherited by subclasses.
- An ABC can be used as a base class for other classes that implement the ADT.
- A subclass of an ABC must override all the abstract methods of the ABC, otherwise it will also be abstract and cannot be instantiated.
- A subclass of an ABC can also override the concrete methods of the ABC, or use them as they are.
- An ABC can be registered as a virtual subclass of another ABC, which means that it will be considered a subclass of that ABC even if it does not inherit from it directly.
- An ABC can also define abstract properties, which are properties that have a getter method but no setter method.
- An ABC can also define abstract class methods and abstract static methods, which are class methods and static methods that are declared but not implemented.
- An ABC can also define abstract slots, which are attributes that are reserved for subclasses to define.
- An ABC can also define a `__subclasshook__` method, which is a class method that can customize the subclass checking for the ABC.

# ADT Interface in Python

- An ADT interface in Python is a set of methods that define the behavior of the ADT.
- An ADT interface can be defined using an ABC, as explained above.
- An ADT interface can also be defined using a protocol, which is an informal interface that is not enforced by the language, but by convention and documentation.
- A protocol can be defined using a regular class, a mixin class, or a metaclass.
- A protocol can also be defined using a structural subtyping system, such as the `typing` module.
- A protocol can also be defined using a duck typing system, which is a dynamic typing system that relies on the presence of certain methods or attributes, rather than the type of the object.
- An example of an ADT interface in Python is the `collections.abc` module, which defines ABCs for various common ADTs, such as `Iterable`, `Sequence`, `Mapping`, `MutableMapping`, `Set`, `MutableSet`, etc.
- Another example of an ADT interface in Python is the `numbers` module, which defines ABCs for various numeric ADTs, such as `Number`, `Complex`, `Real`, `Rational`, `Integral`, etc.

# Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for finding all the prime numbers up to a given limit.
- The algorithm is named after the Greek mathematician Eratosthenes, who lived in the 3rd century BC.
- The algorithm works by creating a list of consecutive integers from 2 to the limit, and marking the multiples of each prime number, starting from 2, as composite.
- The unmarked numbers in the list are the prime numbers.
- The algorithm can be implemented in Python using the following steps:

  1. Create a boolean list of size limit + 1, and initialize all the elements to True, except the first two, which are False (0 and 1 are not prime).
  2. Loop from 2 to the square root