### Modules: Introduction, Importing Modules

#### Introduction

In Python programming, a module is a file that contains Python definitions and statements. Modules are used to organize and reuse code, making it easier to maintain and understand. 

A module can contain functions, classes, and variables, which can be used by other Python programs. Python comes with a vast library of modules that can be used for various purposes, such as math, random, and time.

#### Importing Modules

To use a module in Python, you need to import it first. You can import a module using the `import` statement, followed by the name of the module. For example, to import the math module, you can use the following statement:

```python
import math
```

After importing the module, you can use its functions and variables by prefixing them with the module name, like this:

```python
import math

print(math.pi)
```

This will print the value of pi, which is defined in the math module.

You can also import specific functions or variables from a module using the `from` keyword. For example, to import the `sqrt` function from the math module, you can use the following statement:

```python
from math import sqrt
```

After importing the function, you can use it directly in your code, like this:

```python
from math import sqrt

x = sqrt(4)
print(x)
```

This will print the square root of 4, which is 2.

#### Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm used to generate prime numbers. It was developed by the Greek mathematician Eratosthenes, and is one of the most efficient algorithms for finding all prime numbers up to a given limit.

The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2. It then moves on to the next unmarked number and repeats the process until all numbers have been processed.

To implement the Sieve of Eratosthenes in Python, you can use a list to keep track of the prime numbers. Initially, all numbers are assumed to be prime. You can then iterate over the list, starting with the first prime number (i.e., 2), and mark all of its multiples as composite. Then, you move on to the next unmarked number and repeat the process until all numbers have been processed.

Here is an example implementation of the Sieve of Eratosthenes in Python:

```python
def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(2, n+1) if primes[i]]
```

This implementation takes an integer `n` as input and returns a list of all prime numbers up to `n`. The algorithm uses the `primes` list to keep track of which numbers are prime, and iteratively marks the multiples of each prime as composite.

To use this implementation, you can simply call the `sieve` function with the desired value of `n`, like this:

```python
primes = sieve(100)
print(primes)
```

This will print a list of all prime numbers up to 100, which are [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97].