### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- A module can be imported by another Python program to use its code.
- To import a module, use the `import` statement followed by the module name, for example: `import math`
- To access the code of a module, use the dot (`.`) operator followed by the name of the function, class, variable, etc., for example: `math.sqrt(25)`
- To import only specific names from a module, use the `from` ... `import` statement, for example: `from math import pi, sin`
- To import all names from a module, use the `from` ... `import *` statement, for example: `from math import *`
- To rename a module or a name from a module, use the `as` keyword, for example: `import math as m`, `from math import pi as p`

### Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The sieve of Eratosthenes is a method for finding all prime numbers up to a given limit, n.
- The algorithm works as follows:
  - Create a list of consecutive numbers from 2 to n: (2, 3, 4, ..., n).
  - Start with the first number, 2, and mark it as prime.
  - Find the next unmarked number, 3, and mark it as prime.
  - For each prime number p, mark all its multiples from 2p to n as composite (not prime), for example: 4, 6, 8, ..., n for p = 2; 6, 9, 12, ..., n for p = 3; etc.
  - Repeat the previous step until there are no more unmarked numbers.
  - The remaining unmarked numbers are all prime.
- The sieve of Eratosthenes is an efficient way to find small prime numbers, but it requires a lot of memory to store the list of numbers and their marks.
- Here is an example of a Python program that implements the sieve of Eratosthenes:

```python
# Define a function that takes a limit n and returns a list of prime numbers up to n
def sieve_of_eratosthenes(n):
  # Create a list of consecutive numbers from 2 to n: (2, 3, 4, ..., n)
  numbers = list(range(2, n + 1))
  # Create a list of boolean values to mark the numbers as prime or composite
  # Initially, all numbers are marked as prime (True)
  marks = [True] * (n - 1)
  # Loop through the numbers from 2 to the square root of n
  for i in range(2, int(n ** 0.5) + 1):
    # If the number is marked as prime
    if marks[i - 2]:
      # Mark all its multiples from 2i to n as composite (False)
      for j in range(2 * i, n + 1, i):
        marks[j - 2] = False
  # Create an empty list to store the prime numbers
  primes = []
  # Loop through the numbers from 2 to n
  for i in range(2, n + 1):
    # If the number is marked as prime
    if marks[i - 2]:
      # Append it to the list of prime numbers
      primes.append(i)
  # Return the list of prime numbers
  return primes

# Test the function with some examples
print(sieve_of_eratosthenes(10)) # [2, 3, 5, 7]
print(sieve_of_eratosthenes(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(sieve_of_eratosthenes(100)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,