### Abstract Data Types : Abstract data types and ADT interface in Python Programming.

- An abstract data type (ADT) is a mathematical model of a data structure that specifies the type of data stored, the operations supported on them, and the behaviour of those operations.
- An ADT does not specify how the data structure is implemented, only the interface that it provides to the user or the programmer.
- An ADT interface is a set of methods or functions that define the operations of an ADT. For example, a stack ADT interface may include methods like push, pop, peek, and is_empty.
- An ADT can have multiple implementations, as long as they conform to the same interface. For example, a stack ADT can be implemented using an array, a linked list, or a dynamic array.
- Python does not have a built-in ADT mechanism, but it supports the concept of ADT through classes and objects. A class defines the data attributes and methods of an ADT, and an object is an instance of a class that stores the data and can invoke the methods.
- Python also provides some built-in data types that can be used as ADTs, such as lists, tuples, sets, and dictionaries. These data types have predefined methods that define their operations and behaviour.
- To use an ADT in Python, we need to import the module that contains the class definition of the ADT, create an object of the class, and use the object's methods to perform the operations. For example, to use a stack ADT, we can do the following:

```python
# import the stack module
from stack import Stack

# create a stack object
s = Stack()

# use the stack methods
s.push(10) # push 10 to the top of the stack
s.push(20) # push 20 to the top of the stack
s.pop() # pop and return the top element of the stack, which is 20
s.peek() # return the top element of the stack without removing it, which is 10
s.is_empty() # return True if the stack is empty, False otherwise
```

- The advantages of using ADTs are:

  - They provide a clear and concise way of defining the data and operations of a data structure.
  - They hide the implementation details and complexity from the user or the programmer, and allow them to focus on the functionality and logic of the data structure.
  - They promote modularity, reusability, and maintainability of the code, as different implementations of the same ADT can be easily interchanged without affecting the rest of the program.
  - They enable abstraction, encapsulation, and data hiding, which are important principles of object-oriented programming.

- The disadvantages of using ADTs are:

  - They may introduce some overhead in terms of memory and performance, as the ADT methods may involve additional checks and operations that are not necessary for the underlying data structure.
  - They may not provide the optimal solution for a specific problem or application, as the ADT interface may not match the exact requirements or constraints of the problem or application.
  - They may not support some operations or features that are available for the underlying data structure, such as indexing, slicing, or sorting for lists.

### Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors, 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, etc. are prime numbers.
- The Sieve of Eratosthenes is an ancient algorithm for finding all the prime numbers up to a given limit. It was devised by Eratosthenes, a Greek mathematician and astronomer, in the 3rd century BC.
- The algorithm works as follows:

  - Create a list of consecutive natural numbers from 2 to the limit, and mark them all as prime.
  - Start from the first prime number, 2, and mark all its multiples (except itself) as composite, i.e., not prime. For example, 4, 6, 8, 10, etc.
  - Move to the next prime number, 3, and mark all its multiples (except itself) as composite. For example, 6, 9

- One possible mnemonic for remembering the prime numbers up to 100 is:

  - **P**lease **R**emember **T**o **F**ind **A**ll **P**rime **N**umbers **U**nder **H**undred
  - The first letter of each word corresponds to the first digit of a prime number, and the number of letters in each word corresponds to the second digit of a prime number. For example, P (2 letters) R (1 letter) corresponds to 21, which is not a prime number, so it is skipped. T (1 letter) F (1 letter) corresponds to 11, which is a prime number, so it is included. The mnemonic covers all the prime numbers from 11 to 97.

- Another possible mnemonic for remembering the prime numbers up to 100 is:

  - **P**rime **N**umbers **A**re **T**he **B**est **F**or **M**ultiplication **P**roblems
  - The number of letters in each word corresponds to a prime number. For example, P (1 letter) corresponds to 1, which is not a prime number, so it is skipped. N (1 letter) A (1 letter) corresponds to 11, which is a prime number, so it is included. The mnemonic covers all the prime numbers from 11 to 31.

- A possible learning trick for understanding the Sieve of Eratosthenes is to use a grid of squares to represent the numbers from 2 to the limit, and use different colors to mark the prime and composite numbers. For example, for the limit of 100, we can use a 10 by 10 grid, and use green for prime numbers and red for composite numbers. The algorithm can be visualized as follows:

  - Start with all the squares in green, except for 1, which is neither prime nor composite.

  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|
  | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
  | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
  | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
  | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
  | 51 | 52 | 53 | 54 | 55 | 56 | 57 | 58 | 59 | 60 |
  | 61 | 62 | 63 | 64 | 65 | 66 | 67 | 68 | 69 | 70 |
  | 71 | 72 | 73 | 74 | 75 | 76 | 77 | 78 | 79 | 80 |
  | 81 | 82 | 83 | 84 | 85 | 86 | 87 | 88 | 89 | 90 |
  | 91 | 92 | 93 | 94 | 95 | 96 | 97 | 98 | 99 | 100 |

  - Start from the first prime number, 2, and mark all its multiples (except itself) in red. For example, 4, 6, 8, 10, etc.

  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|
  | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
  | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 |
  | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 |
  | 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 |
  | 51 |