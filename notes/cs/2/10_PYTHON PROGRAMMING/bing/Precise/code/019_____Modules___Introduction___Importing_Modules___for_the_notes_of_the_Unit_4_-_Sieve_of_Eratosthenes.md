### Modules: Introduction, Importing Modules

In Python, a module is a file containing Python definitions and statements. Modules allow us to organize our code into reusable components, which can be imported and used in other programs.

To use a module in a Python program, we need to import it using the `import` statement. For example, to import the `math` module, we would write `import math`. Once a module is imported, we can use its functions and variables by prefixing them with the module name and a dot. For example, to use the `sqrt` function from the `math` module, we would write `math.sqrt(4)`.

Unit 4 - Sieve of Eratosthenes: generate prime numbers with the help of an algorithm given by the Greek Mathematician named Eratosthenes, whose algorithm is known as Sieve of Eratosthenes.

The Sieve of Eratosthenes is an algorithm for finding all prime numbers up to a specified integer. It works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2. The algorithm can be implemented in Python using a list to represent the numbers from 2 to the maximum integer, and a loop to iterate over the list and mark the multiples of each prime.

Here is an example implementation of the Sieve of Eratosthenes in Python:

```python
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return [p for p in range(n + 1) if primes[p]]
```

This function takes as input an integer `n` and returns a list of all prime numbers up to `n`. It uses a list of boolean values to represent the numbers from 2 to `n`, with `True` indicating that the number is prime and `False` indicating that it is composite. The function then iterates over the list, marking the multiples of each prime as composite. Finally, it returns a list of all the prime numbers by filtering the list of boolean values.
