# Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- A module can be imported by another Python program to use its code.
- To import a module, use the `import` statement followed by the module name, for example: `import math`
- To access the code in a module, use the dot notation, for example: `math.sqrt(25)`
- To import only specific names from a module, use the `from` ... `import` statement, for example: `from math import pi, sin`
- To import all names from a module, use the `from` ... `import *` statement, for example: `from math import *`
- To rename a module or a name imported from a module, use the `as` keyword, for example: `import math as m`, `from math import pi as p`

# Sieve of Eratosthenes: Generate Prime Numbers with the Help of an Algorithm Given by the Greek Mathematician Named Eratosthenes, Whose Algorithm is Known as Sieve of Eratosthenes

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The sieve of Eratosthenes is a method for finding all prime numbers up to a given limit.
- The algorithm works as follows:
  - Create a list of consecutive numbers from 2 to the limit, and mark them all as prime.
  - Start from the first prime number, 2, and mark all its multiples (except itself) as composite (not prime).
  - Move to the next unmarked number, which is the next prime number, and repeat the previous step.
  - Continue this process until all the numbers are either marked as prime or composite.
  - The remaining unmarked numbers are the prime numbers.

- Here is an example of the sieve of Eratosthenes for finding all prime numbers up to 20:

| Number | Mark | Reason |
| --- | --- | --- |
| 2 | Prime | The first prime number |
| 3 | Prime | The next unmarked number |
| 4 | Composite | A multiple of 2 |
| 5 | Prime | The next unmarked number |
| 6 | Composite | A multiple of 2 and 3 |
| 7 | Prime | The next unmarked number |
| 8 | Composite | A multiple of 2 |
| 9 | Composite | A multiple of 3 |
| 10 | Composite | A multiple of 2 and 5 |
| 11 | Prime | The next unmarked number |
| 12 | Composite | A multiple of 2 and 3 |
| 13 | Prime | The next unmarked number |
| 14 | Composite | A multiple of 2 and 7 |
| 15 | Composite | A multiple of 3 and 5 |
| 16 | Composite | A multiple of 2 |
| 17 | Prime | The next unmarked number |
| 18 | Composite | A multiple of 2 and 3 |
| 19 | Prime | The next unmarked number |
| 20 | Composite | A multiple of 2 and 5 |

- Here is a Python program that implements the sieve of Eratosthenes for finding all prime numbers up to a given limit:

```python
# Define a function that takes a limit as a parameter
def sieve_of_eratosthenes(limit):
  # Create a list of consecutive numbers from 2 to the limit, and mark them all as True (prime)
  numbers = [True] * (limit + 1)
  # Start from the first prime number, 2
  p = 2
  # Loop until the square of p is greater than the limit
  while p * p <= limit:
    # If p is marked as True (prime), then mark all its multiples (except itself) as False (composite)
    if numbers[p]:
      for i in range(p * p, limit + 1, p):
        numbers[i] = False
    # Move to the next number
    p += 1
  # Create an empty list to store the prime numbers
  primes = []
  # Loop through the numbers list
  for i in range(2, limit + 1):
    # If the number is marked as True (prime), then append it to the primes list
    if numbers[i]:
      primes.append(i)
  # Return the primes