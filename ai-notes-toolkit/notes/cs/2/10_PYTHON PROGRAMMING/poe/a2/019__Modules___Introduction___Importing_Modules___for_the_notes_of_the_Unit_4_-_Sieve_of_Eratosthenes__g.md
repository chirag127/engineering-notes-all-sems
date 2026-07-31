 Here is the content in markdown format without any emojis or external links:

### Modules : Introduction

- A module is a file containing Python definitions and statements.
- The file name is the module name with the suffix .py appended.
- Within a module, the module's name (as a string) is available as the value of the global variable __name__.
- Modules are imported from other modules using the import statement.

### Importing Modules

- There are three ways to import a module:

1. import module_name: Imports the module and allows access to the module's contents with the qualified name - for example, module_name.function_name.
2. from module_name import func_name: Imports just the function 'func_name' from the module 'module_name' allowing to call the function directly as 'func_name()'.
3. from module_name import *: Imports all the names except those beginning with an underscore (_). This form is not recommended because it can cause namespace conflicts.

- The import statement first checks the module cache to see if the module has already been imported. If it has, the module is not reloaded; otherwise, the module's code is executed and the module is added to the cache.

### Sieve of Eratosthenes: generate prime numbers

- The Sieve of Eratosthenes is an algorithm for finding all prime numbers up to any given limit.
- The algorithm:

1. Create a list of consecutive integers from 2 to n: (2, 3, 4, ..., n).
2. Starting from 2, mark as composite (not prime) all multiples of 2.
3. Then starting from 3, mark as composite all multiples of 3.
4. Proceed till the square root of n.
5. The unmarked integers that are left are prime.

- The time complexity of this algorithm is O(n log(log n)).
- An example implementation in Python:

def sieve_of_eratosthenes(n):
    prime_list = []
    composites = set()

    for number in range(2, n + 1):
        if number not in composites:
            prime_list.append(number)
            for multiple in range(number * number, n + 1, number):
                composites.add(multiple)

    return prime_list