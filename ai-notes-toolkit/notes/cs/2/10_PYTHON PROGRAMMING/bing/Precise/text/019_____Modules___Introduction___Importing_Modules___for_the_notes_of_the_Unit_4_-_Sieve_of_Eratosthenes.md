### Modules: Introduction, Importing Modules

In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added. For example, if you have a file named `example.py`, you can use it as a module named `example`.

Modules can define functions, classes, and variables that you can reference in other Python programs. To use the definitions from a module, you need to import the module using the `import` statement.

For example, to import the `example` module, you would use the following code:

```python
import example
```

Once the module is imported, you can use its definitions by referencing them with the module name followed by a dot (`.`) and the name of the definition. For example, to use a function named `my_function` from the `example` module, you would use the following code:

```python
example.my_function()
```

You can also use the `from` keyword to import specific definitions from a module directly into the current namespace. For example, to import only the `my_function` definition from the `example` module, you would use the following code:

```python
from example import my_function
```

Once the definition is imported, you can use it directly without having to reference the module name. For example, to call the `my_function` definition, you would use the following code:

```python
my_function()
```

It is important to note that the Sieve of Eratosthenes is an algorithm for generating prime numbers. It is not directly related to the topic of modules in Python. However, you could write a Python program that implements the Sieve of Eratosthenes algorithm and save it as a module that can be imported and used in other Python programs.