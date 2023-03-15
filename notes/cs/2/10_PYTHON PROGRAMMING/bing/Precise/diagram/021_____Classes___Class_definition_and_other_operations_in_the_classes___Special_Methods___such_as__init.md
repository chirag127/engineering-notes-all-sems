### Classes

A class is a blueprint for creating objects. It defines the attributes and methods that an object of that class will have.

#### Class Definition and Other Operations in the Classes

To define a class in Python, use the `class` keyword followed by the name of the class. The body of the class is indented and contains the attributes and methods of the class.

```python
class MyClass:
    # class attributes and methods
```

To create an object of a class, call the class name as if it were a function.

```python
my_object = MyClass()
```

#### Special Methods

Special methods are methods that have double underscores before and after their names. They are also known as "dunder" methods. These methods are used to define how objects of a class behave with respect to certain operations.

- `__init__`: This method is called when an object is created. It is used to initialize the attributes of the object.
- `__str__`: This method is called when the `str()` function is called on an object. It should return a string representation of the object.
- Comparison methods: These methods are used to define how objects of a class are compared. Some examples are `__eq__` (equal to), `__ne__` (not equal to), `__lt__` (less than), and `__le__` (less than or equal to).
- Arithmetic methods: These methods are used to define how objects of a class behave with respect to arithmetic operations. Some examples are `__add__` (addition), `__sub__` (subtraction), `__mul__` (multiplication), and `__truediv__` (true division).

#### Class Example

Here is an example of a class that represents a point in two-dimensional space.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
```

#### Inheritance

Inheritance is a mechanism that allows a new class to be defined based on an existing class. The new class inherits the attributes and methods of the existing class and can add or override them.

To define a new class based on an existing class, include the name of the existing class in parentheses after the name of the new class.

```python
class MySubclass(MyClass):
    # additional attributes and methods
```

#### Inheritance and OOP

Inheritance is one of the key concepts of object-oriented programming (OOP). It allows for the creation of hierarchies of classes, where more specific classes are based on more general classes. This can make the code more modular and reusable.

### Sieve of Eratosthenes

The Sieve of Eratosthenes is an algorithm for generating prime numbers. It was created by the Greek mathematician Eratosthenes.

The algorithm works by iteratively marking as composite (i.e., not prime) the multiples of each prime, starting with the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime.

Here is an example of how the Sieve of Eratosthenes can be implemented in Python.

```python
def sieve_of_eratosthenes(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    primes[0] = False
    primes[1] = False
    return [p for p in range(n + 1) if primes[p]]
```