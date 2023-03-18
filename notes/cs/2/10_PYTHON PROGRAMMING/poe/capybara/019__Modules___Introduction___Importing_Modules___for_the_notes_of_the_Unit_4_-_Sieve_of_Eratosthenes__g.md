### Modules

In Python, a module is a file that contains Python definitions and statements. The file name is the module name with the suffix `.py` added. Modules can be imported and used in other Python files.

#### Introduction

- A module is a collection of functions, variables, and classes.
- Modules allow code to be reused across multiple files or projects.
- Python has a lot of built-in modules that can be used without installing anything extra.

#### Importing Modules

- To use a module in a Python file, you need to import it first.
- There are several ways to import a module:
  - `import module_name`: Import the entire module.
  - `from module_name import function_name`: Import a specific function from the module.
  - `from module_name import *`: Import all functions from the module.
- Once a module is imported, you can use its functions and variables in your code.

#### Sieve of Eratosthenes

- The Sieve of Eratosthenes is an algorithm for generating prime numbers.
- It was developed by the Greek mathematician Eratosthenes.
- The algorithm works by creating a list of numbers from 2 to a given limit.
- It then iterates over the list, removing all multiples of each number.
- The resulting list contains only prime numbers.
- The Sieve of Eratosthenes can be implemented in Python using a module.