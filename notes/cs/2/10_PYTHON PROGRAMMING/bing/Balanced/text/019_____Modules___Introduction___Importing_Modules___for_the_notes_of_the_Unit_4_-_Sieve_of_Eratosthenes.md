### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, and variables.
- Modules can be used to organize and reuse code, as well as to avoid name conflicts between different parts of a program.
- To use a module in another Python file, we need to import it using the `import` statement.
- The `import` statement can take different forms, such as:

  - `import module_name`: This imports the entire module and makes its contents available under the module name. For example, `import math` allows us to access the `math` module and use its functions like `math.sqrt()`.
  - `from module_name import name1, name2, ...`: This imports specific names from a module and makes them available without the module name prefix. For example, `from math import pi, sin` allows us to use `pi` and `sin` directly, without writing `math.pi` or `math.sin`.
  - `from module_name import *`: This imports all names from a module and makes them available without the module name prefix. This is not recommended, as it can cause name conflicts and make the code less readable.
  - `import module_name as alias`: This imports a module and gives it an alias, which can be used instead of the module name. For example, `import numpy as np` allows us to use `np` instead of `numpy` to access the `numpy` module.

- Modules can also be nested, meaning that a module can contain other modules. To access a nested module, we need to use the dot notation, such as `module1.module2.name`.

### Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, 19, etc. are prime numbers.
- The sieve of Eratosthenes is a method for finding all prime numbers up to a given limit. It works by creating a list of all natural numbers from 2 to the limit, and then marking the multiples of each prime number as composite (not prime), starting from the first prime number, 2.
- The algorithm can be implemented in Python as follows:

  - Create a list of boolean values, where the index represents the number and the value represents whether it is prime or not. Initially, all values are set to True, except for 0 and 1, which are set to False.
  - Loop over the list from 2 to the square root of the limit, and check if the current number is prime (i.e., its value is True). If it is, then mark all its multiples (starting from its square) as False, as they are composite.
  - Return the list of prime numbers, which are the indices of the True values in the list.

- Here is an example of the code in Python:

```python
def sieve_of_eratosthenes(limit):
  # Create a list of boolean values, where the index represents the number and the value represents whether it is prime or not
  is_prime = [False, False] + [True] * (limit - 1)

  # Loop over the list from 2 to the square root of the limit
  for i in range(2, int(limit**0.5) + 1):
    # Check if the current number is prime
    if is_prime[i]:
      # Mark all its multiples (starting from its square) as False
      for j in range(i * i, limit + 1, i):
        is_prime[j] = False

  # Return the list of prime numbers, which are the indices of the True values in the list
  return [i for i, prime in enumerate(is_prime) if prime]
```