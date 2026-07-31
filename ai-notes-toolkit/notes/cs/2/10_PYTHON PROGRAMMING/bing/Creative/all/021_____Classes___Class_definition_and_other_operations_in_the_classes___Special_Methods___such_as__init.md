# Classes

## Class definition and other operations in the classes

- A class is a blueprint for creating objects that have certain attributes and behaviors.
- A class is defined using the `class` keyword followed by the class name and a colon.
- The class name should follow the naming convention of capitalizing the first letter of each word.
- The class body contains the attributes and methods of the class, indented under the class definition.
- An attribute is a variable that belongs to the class or an instance of the class.
- A method is a function that belongs to the class or an instance of the class and can access the attributes and other methods of the class or the instance.
- The `self` parameter is used to refer to the current instance of the class within a method.
- The `__init__` method is a special method that is automatically called when a new instance of the class is created. It is used to initialize the attributes of the instance.
- The `__str__` method is a special method that returns a string representation of the instance. It is called when the `print` function or the `str` function is applied to the instance.
- The `__eq__`, `__lt__`, `__gt__`, `__le__`, and `__ge__` methods are special methods that define how instances of the class can be compared using the `==`, `<`, `>`, `<=`, and `>=` operators respectively.
- The `__add__`, `__sub__`, `__mul__`, `__truediv__`, `__floordiv__`, `__mod__`, `__pow__`, and `__neg__` methods are special methods that define how instances of the class can be operated on using the `+`, `-`, `*`, `/`, `//`, `%`, `**`, and unary `-` operators respectively.

## Class Example

- Here is an example of a class that represents a point in a two-dimensional plane.

```python
class Point:
    # class attribute that counts the number of points created
    count = 0

    # __init__ method that initializes the x and y coordinates of the point
    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1 # increment the class attribute by 1

    # __str__ method that returns a string representation of the point
    def __str__(self):
        return f"({self.x}, {self.y})"

    # method that calculates the distance between two points
    def distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    # __eq__ method that checks if two points have the same coordinates
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # __add__ method that returns a new point that is the sum of two points
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # __neg__ method that returns a new point that is the negation of the point
    def __neg__(self):
        return Point(-self.x, -self.y)
```

- Here are some examples of how to use the class and its methods.

```python
# create two points
p1 = Point(3, 4)
p2 = Point(1, 2)

# print the points
print(p1) # (3, 4)
print(p2) # (1, 2)

# print the number of points created
print(Point.count) # 2

# calculate the distance between the points
print(p1.distance(p2)) # 2.8284271247461903

# compare the points
print(p1 == p2) # False
print(p1 == Point(3, 4)) # True

# add the points
print(p1 + p2) # (4, 6)

# negate the points
print(-p1) # (-3, -4)
print(-p2) # (-1, -2)
```

## Inheritance

- Inheritance is a mechanism that allows a class to inherit the attributes and methods from another class.
- The class that inherits from another class is called the subclass or the child class.
- The class that is inherited from is called the superclass or the parent class.
- A subclass can