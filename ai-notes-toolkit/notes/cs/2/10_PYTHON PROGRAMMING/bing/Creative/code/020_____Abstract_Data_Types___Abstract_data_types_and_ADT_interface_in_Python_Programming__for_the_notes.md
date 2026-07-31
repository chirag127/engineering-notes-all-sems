### Abstract Data Types

- An abstract data type (ADT) is a mathematical model for data types that defines the logical form of the data and the operations that can be performed on the data .
- An ADT does not specify how the data is stored or implemented, but only the interface or behavior of the data type .
- An ADT can be implemented using different concrete data types (CDTs), such as arrays, lists, maps, queues, sets, stacks, tables, trees, vectors, etc .
- An ADT can be viewed as a concept or a specification rather than a data type .
- In Python, an ADT can be defined using abstract base classes (ABCs) from the `abc` module.
- An ABC is a class that has at least one abstract method, which is a method that is declared but not implemented.
- An ABC can also have concrete methods, which are methods that have an implementation.
- An ABC can be subclassed by a CDT that provides implementations for all the abstract methods of the ABC.
- An ABC can also be registered as a virtual subclass of another ABC, which means that it inherits the interface of the other ABC without actually subclassing it.
- An ABC can be used to check if an object is an instance of the ADT, using the `isinstance` function.

### ADT Interface in Python

- An ADT interface in Python is a set of abstract methods that define the behavior of the ADT.
- An ADT interface can be declared using the `@abstractmethod` decorator from the `abc` module.
- An ADT interface can also include concrete methods that provide default or common implementations for some operations .
- An ADT interface can be inherited or registered by a CDT that provides concrete implementations for the abstract methods .
- An ADT interface can be used to enforce a consistent and coherent design for the ADT and its CDTs .

### Example: Stack ADT

- A stack is an ADT that represents a sequence of objects in which only the most recently added object is accessible.
- A stack follows the last-in, first-out (LIFO) principle, meaning that the last object added to the stack is the first one to be removed.
- A stack ADT can be defined using an ABC with the following abstract methods:
  - `push`: add an object to the top of the stack
  - `pop`: remove and return the object at the top of the stack
  - `peek`: return the object at the top of the stack without removing it
  - `is_empty`: return True if the stack is empty, False otherwise
  - `size`: return the number of objects in the stack
- A stack ADT can also have a concrete method that implements the `__str__` magic method, which returns a string representation of the stack.
- A stack ADT can be implemented using different CDTs, such as a list, an array, a linked list, etc.
- A stack ADT can be used for various applications, such as reversing a sequence, evaluating expressions, backtracking, etc.

### Sieve of Eratosthenes

- The sieve of Eratosthenes is an algorithm for generating prime numbers, which are numbers that are only divisible by 1 and themselves.
- The algorithm was devised by the Greek mathematician Eratosthenes in the 3rd century BC.
- The algorithm works as follows:
  - Create a list of consecutive integers from 2 to n, where n is the upper limit of the prime numbers to be generated
  - Mark 2 as a prime number and cross out all its multiples from the list
  - Find the next unmarked number in the list, which is the next prime number, and cross out all its multiples from the list
  - Repeat the previous step until there are no more unmarked numbers in the list
  - The remaining unmarked numbers in the list are the prime numbers from 2 to n
- The sieve of Eratosthenes can be implemented in Python using a list or