### Modules: Introduction, Importing Modules

In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added. For example, if you have a file named `sieve.py`, it can be imported as a module named `sieve`.

To import a module, you can use the `import` statement. For example, to import the `sieve` module, you can write `import sieve`. After importing the module, you can use its functions and variables by prefixing them with the module name and a dot. For example, if the `sieve` module has a function named `generate_primes`, you can call it like this: `sieve.generate_primes()`.

The Sieve of Eratosthenes is an algorithm for generating prime numbers. It was created by the Greek mathematician Eratosthenes. The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2. The algorithm can be implemented in Python using a module.

Here is an example of how the Sieve of Eratosthenes can be implemented in a Python module named `sieve`:

```python
def generate_primes(n):
    """Generate all primes up to n using the Sieve of Eratosthenes."""
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    return primes
```

This module defines a function named `generate_primes` that takes an integer `n` as an argument and returns a list of all prime numbers up to `n`. The function uses the Sieve of Eratosthenes algorithm to generate the primes.

To use this module, you can save the code to a file named `sieve.py` and then import it in your Python script. Here is an example of how to use the `sieve` module to generate the prime numbers up to 100:

```python
import sieve

primes = sieve.generate_primes(100)
print(primes)
```

This code imports the `sieve` module and then calls its `generate_primes` function to generate the prime numbers up to 100. The resulting list of prime numbers is then printed to the screen.