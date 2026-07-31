# Modules: Introduction, Importing Modules

In Python, a module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` added. For example, if you have a file named `example.py`, you can use it as a module named `example`.

You can use any Python source file as a module by executing an import statement in some other Python source file. The `import` statement combines two operations: it searches for the named module, then it binds the results of that search to a name in the local scope.

For example, to import the `example` module, you can use the following statement:

```python
import example
```

After importing the module, you can use its functions and variables by prefixing them with the module name and a dot. For example, if the `example` module has a function named `my_function`, you can call it like this:

```python
example.my_function()
```

You can also import specific functions or variables from a module using the `from` keyword. For example, to import only the `my_function` function from the `example` module, you can use the following statement:

```python
from example import my_function
```

After importing the function, you can call it directly, without prefixing it with the module name:

```python
my_function()
```

In the context of the Sieve of Eratosthenes, you can use modules to organize your code and make it easier to reuse. For example, you can create a module named `sieve` that contains the implementation of the Sieve of Eratosthenes algorithm, and then import it in other programs that need to generate prime numbers.