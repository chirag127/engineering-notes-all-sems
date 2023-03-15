# Modules: Introduction, Importing Modules

## Introduction

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- Modules can be used to organize and reuse code, as well as to avoid name conflicts between different parts of a program.
- Modules can be imported by other modules or scripts using the `import` statement, which makes the module's contents available in the current namespace.
- Modules can also be executed as scripts by running them directly from the command line or an IDE, in which case the module's name is set to `__main__`.

## Importing Modules

- There are different ways to import modules in Python, depending on how much of the module's contents are needed and how they are accessed.
- The simplest way is to use the `import` statement followed by the module name, which imports the whole module and creates a reference to it in the current namespace. For example:

```python
import math
print(math.pi) # prints 3.141592653589793
```

- Another way is to use the `from` statement followed by the module name and the names of the specific items to import, which imports only those items and makes them directly available in the current namespace. For example:

```python
from math import pi, sqrt
print(pi) # prints 3.141592653589793
print(sqrt(2)) # prints 1.4142135623730951
```

- A third way is to use the `from` statement followed by the module name and the `*` symbol, which imports all the items from the module and makes them directly available in the current namespace. This is not recommended, as it can cause name conflicts and make the code less readable. For example:

```python
from math import *
print(pi) # prints 3.141592653589793
print(sin(0)) # prints 0.0
```

- A fourth way is to use the `as` keyword followed by an alias for the module or the item to import, which creates a new name for the reference in the current namespace. This can be useful to avoid name conflicts or to shorten long names. For example:

```python
import math as m
print(m.pi) # prints 3.141592653589793

from math import sqrt as s
print(s(2)) # prints 1.4142135623730951
```

# Unit 4 - Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

## Sieve of Eratosthenes

- The sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit n.
- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, etc. are prime numbers, while 4, 6, 8, 9, 10, etc. are not.
- The algorithm works by creating a list of all the natural numbers from 2 to n, and then marking as composite (not prime) the multiples of each prime number, starting from 2. The remaining unmarked numbers are prime.
- The algorithm can be implemented in Python as follows:

```python
def sieve_of_eratosthenes(n):
    # create a list of booleans, initially all True, to represent the numbers from 2 to n
    is_prime = [True] * (n + 1)
    # loop from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # if i is prime, mark its multiples as composite
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    # return the list of prime numbers
    return [i for i in range(2, n + 1) if is_prime[i]]
```

- The algorithm has a time complexity of O(n log log n), which is asymptotically faster than checking each number for primality individually.