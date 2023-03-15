# Classes in Python

## Class Definition and Operations

- A class is a blueprint for creating objects, providing initial values for state and implementations of behavior.
- Classes are defined using the `class` keyword, followed by the class name and a colon.
- The body of the class is indented and contains the class's methods and attributes.
- Attributes are defined by assigning values to variables within the class body.
- Methods are functions defined within the class body and have access to the instance and its attributes.
- The `self` parameter refers to the instance of the class and is used to access its attributes.

## Special Methods

- Special methods are methods with double underscores before and after their names, such as `__init__` and `__str__`.
- The `__init__` method is called when an instance of the class is created and is used to initialize the instance's attributes.
- The `__str__` method is called by the `str` built-in function and by the `print` function to get a string representation of the object.
- Comparison methods such as `__eq__`, `__ne__`, `__lt__`, `__le__`, `__gt__`, and `__ge__` are used to define how instances of the class are compared to each other.
- Arithmetic methods such as `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, and `__neg__` are used to define how instances of the class can be used in arithmetic operations.

## Class Example

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"
```

## Inheritance

- Inheritance allows a new class to be defined based on an existing class, inheriting its attributes and methods.
- The new class is called a subclass and the existing class is called the superclass.
- The subclass can add new attributes and methods, and can override the methods of the superclass.
- Inheritance is defined by placing the name of the superclass in parentheses after the name of the subclass.

## Inheritance and OOP

- Inheritance is a fundamental concept in object-oriented programming (OOP).
- It allows for the creation of hierarchies of classes, with more specific classes inheriting from more general classes.
- This allows for code reuse and makes it easier to maintain and extend the code.

## Sieve of Eratosthenes

- The Sieve of Eratosthenes is an algorithm for generating prime numbers.
- It was created by the Greek mathematician Eratosthenes.
- The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2.
- The algorithm can be implemented in Python using a list to represent the numbers and a loop to iterate over the multiples of each prime.

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]
```