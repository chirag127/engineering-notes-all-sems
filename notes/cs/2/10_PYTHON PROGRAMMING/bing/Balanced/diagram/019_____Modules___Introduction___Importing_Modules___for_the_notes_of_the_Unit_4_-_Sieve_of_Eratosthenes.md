### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- A module can be imported by another Python program to use its code.
- To import a module, use the `import` statement followed by the module name, e.g., `import math`.
- To access the code of a module, use the dot notation, e.g., `math.sqrt(25)` to call the `sqrt` function from the `math` module.
- To import only specific names from a module, use the `from` ... `import` statement, e.g., `from math import pi, sin`.
- To import all names from a module, use the `from` ... `import *` statement, e.g., `from math import *`.
- To rename a module or a name from a module, use the `as` keyword, e.g., `import math as m`, `from math import pi as p`.

### Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself.
- The Sieve of Eratosthenes is an algorithm that finds all the prime numbers up to a given limit, n.
- The algorithm works as follows:
  - Create a list of consecutive numbers from 2 to n: (2, 3, 4, ..., n).
  - Start with the first number, 2, and mark it as prime.
  - Find the next unmarked number, 3, and mark it as prime.
  - For each multiple of 3, starting from 3 * 3, mark it as composite (not prime).
  - Repeat the previous two steps for the next unmarked number, 5, and so on, until the square of the current number is greater than n.
  - The remaining unmarked numbers are all prime.
- The algorithm can be implemented in Python as follows:

```python
# Define a function to perform the sieve
def sieve_of_eratosthenes(n):
  # Create a list of booleans to represent the numbers from 2 to n
  # Initially, all are set to True, meaning they are prime
  is_prime = [True] * (n + 1)
  # Loop from 2 to the square root of n
  for i in range(2, int(n ** 0.5) + 1):
    # If i is prime, mark its multiples as composite
    if is_prime[i]:
      for j in range(i * i, n + 1, i):
        is_prime[j] = False
  # Return the list of prime numbers
  return [i for i in range(2, n + 1) if is_prime[i]]

# Test the function
print(sieve_of_eratosthenes(100))
```

- The output of the function is:

```python
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```