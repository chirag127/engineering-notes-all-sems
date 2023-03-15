### Classes in Python

Classes are a fundamental concept in object-oriented programming (OOP). A class is a blueprint for creating objects, which are instances of the class. A class defines a set of attributes and methods that are common to all objects of that class.

#### Class Definition

A class is defined using the `class` keyword, followed by the name of the class and a colon. The body of the class is indented and contains the class's attributes and methods.

```python
class MyClass:
    # class attributes and methods
```

#### Special Methods

Special methods are methods that have double underscores before and after their names. These methods are called automatically by Python when certain operations are performed on objects of the class.

Some common special methods include:

- `__init__(self, ...)`: This method is called when an object is created from the class. It is used to initialize the object's attributes.
- `__str__(self)`: This method is called by the `str()` built-in function and by the `print()` function to get a string representation of the object.
- `__eq__(self, other)`: This method is called to compare two objects for equality using the `==` operator.
- `__ne__(self, other)`: This method is called to compare two objects for inequality using the `!=` operator.
- `__lt__(self, other)`: This method is called to compare two objects using the `<` operator.
- `__le__(self, other)`: This method is called to compare two objects using the `<=` operator.
- `__gt__(self, other)`: This method is called to compare two objects using the `>` operator.
- `__ge__(self, other)`: This method is called to compare two objects using the `>=` operator.
- `__add__(self, other)`: This method is called to add two objects using the `+` operator.
- `__sub__(self, other)`: This method is called to subtract two objects using the `-` operator.
- `__mul__(self, other)`: This method is called to multiply two objects using the `*` operator.
- `__truediv__(self, other)`: This method is called to divide two objects using the `/` operator.

#### Class Example

Here is an example of a simple class that represents a point in 2D space:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f"({self.x}, {self.y})"
```

This class has an `__init__` method that takes two arguments, `x` and `y`, and initializes the `x` and `y` attributes of the object. It also has a `distance_from_origin` method that calculates the distance of the point from the origin (0, 0), and a `__str__` method that returns a string representation of the point.

#### Inheritance

Inheritance is a mechanism that allows a new class to be defined based on an existing class. The new class inherits the attributes and methods of the existing class, and can also add new attributes and methods or override the inherited ones.

Inheritance is specified by including the name of the base class in parentheses after the name of the new class:

```python
class MySubclass(MyClass):
    # class attributes and methods
```

In this example, `MySubclass` is a subclass of `MyClass` and inherits all of its attributes and methods.

#### Inheritance and OOP

Inheritance is a powerful feature of OOP that allows for code reuse and modularity. By defining a base class with common attributes and methods, and then creating subclasses that inherit from the base class and add or override specific attributes and methods, a complex hierarchy of classes can be created that share common behavior but also have their own specialized behavior.

### Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm for generating prime numbers. It was created by the Greek mathematician Eratosthenes.

The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the multiples of 2. The algorithm can be implemented in Python as follows:

```python
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n **