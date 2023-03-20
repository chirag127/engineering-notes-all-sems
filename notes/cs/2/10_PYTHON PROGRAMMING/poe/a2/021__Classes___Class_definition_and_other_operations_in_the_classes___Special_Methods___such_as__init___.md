 Here are the notes for the given topics:

### Classes :

- Class definition: Defining a class using `class` keyword followed by the class name.
- Class attributes: Attributes defined inside the class. Shared by all instances of the class.
- Instance attributes: Attributes defined inside the `__init__()` method. Unique to each instance.
- Methods: Functions defined inside the class. Used to expose the behavior of the class.

### Special Methods:

- `__init__()`: Used to initialize the instance attributes. Called when an object is created.
- `__str__()`: Called when the object is converted to a string. Used to customize the string representation of the object.
- Comparison methods: `__eq__()`, `__ne__()`, `__lt__()`, `__le__()`, `__gt__()`, `__ge__()`. Used to compare objects.
- Arithmetic methods: `__add__()`, `__sub__()`, `__mul__()`, `__truediv__()`, etc. Used to perform arithmetic operations on objects.

### Class Example:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person {self.name}, {self.age} years old.'

p = Person('Jack', 20)
print(p)  # Person Jack, 20 years old.
```

### Inheritance:

- Used to derive a new class from an existing class. The derived class inherits all the attributes and methods from the base class.
- Allows code reuse and promotes DRY (Don't Repeat Yourself) principle.
- The derived class can also override the methods from the base class.

### Inheritance and OOP:

- Object-Oriented Programming (OOP) is a paradigm based on objects and their interactions.
- Encapsulation: Hiding the internal details and showing only the necessary interface.
- Inheritance: Deriving new classes from existing ones.
- Polymorphism: Providing a uniform interface for interacting with objects of different classes.

### Sieve of Eratosthenes:

- Generate prime numbers up to a given number `n`.
- Algorithm:
    1. Take a list of numbers from 2 to n.
    2. Repeatedly find the smallest unmarked number in the list. This is the next prime.
    3. Mark all multiples of the prime number as non-prime.
- Time complexity: O(n log(log n)).
- Sample code:

```python
n = 30
primes = [True] * n
primes[0] = primes[1] = False

for (i, is_prime) in enumerate(primes):
    if is_prime:
        for n in range(i*i, n, i):
            primes[n] = False

print([i for i in range(n) if primes[i]])  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```