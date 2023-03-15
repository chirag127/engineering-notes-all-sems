Modularization in software design is the process of breaking down a complex system into smaller, independent, and reusable components, called modules. Modules can be organized in a hierarchical structure, where each module has a well-defined interface and a specific functionality. Modularization can improve the readability, maintainability, testability, and reusability of software code.

Here is an example of modularization in Python:

```python
# main.py
# This is the main module that uses other modules

# Import the modules
import math
import greetings

# Use the math module to calculate the area of a circle
radius = 5
area = math.pi * radius ** 2
print(f"The area of the circle is {area:.2f}")

# Use the greetings module to say hello
name = "Alice"
greetings.say_hello(name)
```

```python
# greetings.py
# This is a module that defines some greeting functions

def say_hello(name):
    # This function prints a hello message with the name
    print(f"Hello, {name}!")

def say_goodbye(name):
    # This function prints a goodbye message with the name
    print(f"Goodbye, {name}!")
```

Output:

```
The area of the circle is 78.54
Hello, Alice!
```