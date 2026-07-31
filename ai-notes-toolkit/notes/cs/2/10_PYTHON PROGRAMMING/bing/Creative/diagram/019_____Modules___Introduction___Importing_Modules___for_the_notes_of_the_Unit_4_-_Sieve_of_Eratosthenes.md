### Modules: Introduction, Importing Modules

- A module is a file that contains Python code, such as definitions of functions, classes, variables, etc.
- Modules can be used to organize and reuse code, as well as to avoid name conflicts between different parts of a program.
- Modules can be imported into other modules or scripts using the `import` statement, which makes the module's contents available in the current namespace.
- The syntax for importing a module is `import module_name`, where `module_name` is the name of the file without the `.py` extension.
- Alternatively, specific names from a module can be imported using the syntax `from module_name import name1, name2, ...`, where `name1, name2, ...` are the names of the functions, classes, variables, etc. that are defined in the module.
- Another way to import a module is to use the syntax `import module_name as alias`, where `alias` is a short name that can be used to refer to the module instead of the full module name.
- Modules can also be imported inside functions or classes, which limits their scope to the local namespace of the function or class.

### Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

- The Sieve of Eratosthenes is a simple and efficient algorithm to find all the prime numbers up to a given limit `n`.
- The algorithm works by creating a list of numbers from `2` to `n`, and marking the multiples of each prime number as composite (not prime), starting from the first prime number `2`.
- The numbers that are not marked as composite are the prime numbers, and they can be returned as a list or a set.
- The pseudocode for the algorithm is as follows:

```
# Create a list of numbers from 2 to n, and mark them all as prime
prime = [True for i in range(n + 1)]
# Loop from 2 to the square root of n
for p in range(2, int(sqrt(n)) + 1):
  # If p is marked as prime, then mark its multiples as composite
  if prime[p]:
    # Start from p * p, and increment by p
    for i in range(p * p, n + 1, p):
      prime[i] = False
# Return the numbers that are still marked as prime
return [p for p in range(2, n + 1) if prime[p]]
```

- The Python code for the algorithm is as follows:

```python
# Import the math module to use the sqrt function
import math

# Define a function that takes a limit n as a parameter
def sieve_of_eratosthenes(n):
  # Create a list of numbers from 2 to n, and mark them all as prime
  prime = [True for i in range(n + 1)]
  # Loop from 2 to the square root of n
  for p in range(2, int(math.sqrt(n)) + 1):
    # If p is marked as prime, then mark its multiples as composite
    if prime[p]:
      # Start from p * p, and increment by p
      for i in range(p * p, n + 1, p):
        prime[i] = False
  # Return the numbers that are still marked as prime
  return [p for p in range(2, n + 1) if prime[p]]

# Test the function with some examples
print(sieve_of_eratosthenes(10)) # [2, 3, 5, 7]
print(sieve_of_eratosthenes(20)) # [2, 3, 5, 7, 11, 13, 17, 19]
print(sieve_of_eratosthenes(100)) # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
```