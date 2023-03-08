### Modules: Introduction

- A module is a piece of software that has a specific functionality. A Python module is a file that contains Python code. For example, when building a shopping cart application, you can have one module for calculating prices and another module for managing items in the cart.
- A module can define variables, functions, classes, and objects that can be imported and used in another Python program. This allows you to reuse code and avoid duplication. For example, you can use the built-in math module to perform mathematical operations without writing your own functions.
- A module is identified by its name, which is the same as the filename without the .py extension. For example, a module named pricing.py can be imported as pricing. To import a module, you use the import statement, which tells the Python interpreter to load the module and make its contents available in the current namespace.

### Importing Modules

- To import a module, you use the import statement followed by the module name. For example, to import the math module, you write:

```python
import math
```

- After importing a module, you can access its variables, functions, classes, and objects by using the dot (.) operator. For example, to access the pi constant and the sqrt function from the math module, you write:

```python
print(math.pi) # 3.141592653589793
print(math.sqrt(25)) # 5.0
```

- You can also import specific names from a module without importing the whole module. This can save memory and avoid name conflicts. To do this, you use the from ... import ... statement. For example, to import only the pi constant and the sqrt function from the math module, you write:

```python
from math import pi, sqrt
```

- After importing specific names from a module, you can use them directly without the dot (.) operator. For example, to use the pi constant and the sqrt function from the math module, you write:

```python
print(pi) # 3.141592653589793
print(sqrt(25)) # 5.0
```

- You can also import all names from a module by using the asterisk (*) symbol. However, this is not recommended as it can cause name conflicts and make the code less readable. For example, to import all names from the math module, you write:

```python
from math import *
```

- After importing all names from a module, you can use them directly without the dot (.) operator. For example, to use the pi constant and the sqrt function from the math module, you write:

```python
print(pi) # 3.141592653589793
print(sqrt(25)) # 5.0
```

- You can also rename a module or a name from a module by using the as keyword. This can make the code more concise and avoid name conflicts. For example, to import the math module as m, you write:

```python
import math as m
```

- After renaming a module, you can use the new name with the dot (.) operator. For example, to use the pi constant and the sqrt function from the math module, you write:

```python
print(m.pi) # 3.141592653589793
print(m.sqrt(25)) # 5.0
```

- Similarly, to import the pi constant and the sqrt function from the math module as p and s, you write:

```python
from math import pi as p, sqrt as s
```

- After renaming names from a module, you can use the new names directly without the dot (.) operator. For example, to use the pi constant and the sqrt function from the math module, you write:

```python
print(p) # 3.141592653589793
print(s(25)) # 5.0
```

- You can also import modules from subdirectories by using the dot (.) operator. For example, if you have a directory named mypackage that contains a module named mymodule, you can import it as:

```python
import mypackage.mymodule
```

- Alternatively, you can use the from ... import ... statement to import the module or specific names from the module. For example, to import the mymodule module or the myfunction function from the mypackage directory, you write:

```python
from mypackage import mymodule
from mypackage.mymodule import myfunction
```

- After importing modules from subdirectories, you can

Some possible mnemonics and learning tricks for the topic are:

- To remember the syntax of the import statement, you can use the acronym IMPS: Import Module or Particular Stuff.
- To remember the difference between importing a whole module and importing specific names from a module, you can use the analogy of a book: importing a whole module is like getting the whole book, while importing specific names from a module is like getting only the pages or chapters you need.
- To remember the difference between using the dot (.) operator and not using it, you can use the analogy of a phone: using the dot (.) operator is like dialing the area code before the number, while not using it is like dialing the number directly.
- To remember the syntax of the as keyword, you can use the acronym ASK: As Something else Known.
- To remember the syntax of importing modules from subdirectories, you can use the analogy of a file path: using the dot (.) operator is like using the slash (/) symbol to separate the directories, while using the from ... import ... statement is like using the colon (:) symbol to separate the directories.