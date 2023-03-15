# Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, and variables.
- Modules can be imported by other Python programs to reuse the code and avoid duplication.
- Modules can also provide access to external libraries and frameworks that extend the functionality of Python.
- To import a module, use the `import` statement followed by the name of the module. For example, `import math` imports the math module that provides mathematical functions and constants.
- To access the attributes of a module, use the dot notation. For example, `math.pi` returns the value of pi from the math module.
- To import only specific attributes from a module, use the `from` ... `import` statement. For example, `from math import pi` imports only the pi constant from the math module.
- To import all attributes from a module, use the `from` ... `import *` statement. For example, `from math import *` imports everything from the math module. However, this is not recommended as it may cause name conflicts and reduce readability.
- To rename a module or an attribute when importing, use the `as` keyword. For example, `import math as m` imports the math module and assigns it the alias m. Similarly, `from math import pi as p` imports the pi constant and assigns it the alias p.

# Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11, 13, 17, etc. are prime numbers.
- The Sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit n. It works by marking the multiples of each prime number as composite (not prime), starting from the first prime number 2.
- The algorithm can be implemented in Python as follows:

```python
# Define a function to perform the sieve
def sieve_of_eratosthenes(n):
  # Create a list of boolean values from 0 to n, initially all True
  is_prime = [True] * (n + 1)
  # Set the values for 0 and 1 to False, as they are not prime
  is_prime[0] = is_prime[1] = False
  # Loop from 2 to the square root of n
  for i in range(2, int(n ** 0.5) + 1):
    # If i is marked as prime
    if is_prime[i]:
      # Mark all the multiples of i as composite, starting from i * i
      for j in range(i * i, n + 1, i):
        is_prime[j] = False
  # Return the list of prime numbers
  return [i for i in range(n + 1) if is_prime[i]]

# Test the function
print(sieve_of_eratosthenes(100))
# Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```